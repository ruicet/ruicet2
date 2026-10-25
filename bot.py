import asyncio
import logging
import os
import phonenumbers
from phonenumbers import carrier, geocoder
import requests
from bs4 import BeautifulSoup
import aiohttp

from aiohttp import web
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BufferedInputFile, InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder

import cairosvg

from data import ROOT_SECTIONS, get_subsections, get_topic, search_all
from solver import solve_problem

# ================== НАСТРОЙКИ ==================
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PORT = int(os.environ.get("PORT", 10000))

if not BOT_TOKEN:
    raise RuntimeError("Переменная окружения BOT_TOKEN не задана!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# ================== СОСТОЯНИЯ ==================
class St(StatesGroup):
    calc = State()
    osint_phone = State()
    osint_tg = State()

# ================== КЛАВИАТУРЫ ==================
def kb_main():
    kb = InlineKeyboardBuilder()
    kb.button(text="📐  ГЕОМЕТРИЯ", callback_data="root:geom")
    kb.button(text="⚛️  ФИЗИКА", callback_data="root:phys")
    kb.button(text="🧠  РЕШИТЬ ЗАДАЧУ", callback_data="solve:start")
    kb.button(text="⭐", callback_data="osint_menu")  # Секретная кнопка
    kb.button(text="ℹ️  СПРАВКА", callback_data="help")
    kb.adjust(1)
    return kb.as_markup()

def kb_osint_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="📱 По номеру телефона", callback_data="osint:phone")
    kb.button(text="✈️ По Telegram (юзернейм)", callback_data="osint:tg")
    kb.button(text="⬅️  НАЗАД", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()

def kb_subs(root_key: str):
    kb = InlineKeyboardBuilder()
    for section in get_subsections(root_key):
        kb.button(text=section.upper(), callback_data=f"sec:{root_key}:{section}")
    kb.button(text="⬅️  НАЗАД", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()

def kb_section(root_key: str, section: str):
    kb = InlineKeyboardBuilder()
    for idx, name in get_subsections(root_key).get(section, []):
        kb.button(text=name, callback_data=f"topic:{root_key}:{idx}")
    kb.button(text="⬅️  НАЗАД", callback_data=f"root:{root_key}")
    kb.adjust(1)
    return kb.as_markup()

def kb_topic(root_key: str, idx: int):
    t = get_topic(root_key, idx)
    kb = InlineKeyboardBuilder()
    if t.get("calc"):
        kb.button(text="🧮  РЕШИТЬ ПО ФОРМУЛЕ", callback_data=f"solve:{root_key}:{idx}")
    kb.button(text="⬅️  НАЗАД", callback_data=f"sec:{root_key}:{t['section']}")
    kb.adjust(1)
    return kb.as_markup()

def kb_targets(root_key: str, idx: int):
    calc = get_topic(root_key, idx)["calc"]
    kb = InlineKeyboardBuilder()
    for name, _ in calc["vars"]:
        if name in calc["solvers"]:
            kb.button(text=f"Найти {name}", callback_data=f"pick:{root_key}:{idx}:{name}")
    kb.button(text="⬅️  НАЗАД", callback_data=f"topic:{root_key}:{idx}")
    kb.adjust(2)
    return kb.as_markup()

# ================== SVG → PNG ==================
def svg_to_png(svg_str: str) -> bytes:
    return cairosvg.svg2png(
        bytestring=svg_str.encode("utf-8"),
        output_width=900, output_height=675, background_color="#0f1729",
    )

# ================== ФОРМАТ ==================
def fmt_number(x) -> str:
    if isinstance(x, float) and abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{x:.6g}"

_UNIT_FOR_TARGET = {
    "s": "м", "S": "", "v": "м/с", "t": "с", "m": "кг", "V": "м³", "ρ": "кг/м³",
    "F": "Н", "F1": "Н", "F2": "Н", "MT": "Н", "p": "Па", "A": "Дж", "Q": "Дж",
    "Ek": "Дж", "Ep": "Дж", "N": "Вт", "P": "Вт", "U": "В", "I": "А", "R": "Ом",
    "a": "м/с²", "v0": "м/с", "x": "м", "x0": "м", "h": "м", "l": "м", "d": "м",
    "f": "м", "lam": "м", "T": "с", "nu": "Гц", "w": "рад/с", "D": "дптр",
    "n": "", "B": "Тл", "Phi": "Вб", "e": "В", "C": "", "R1": "Ом", "R2": "Ом",
    "k": "Н/м", "x_": "",
}

# ================== ПОКАЗ СООБЩЕНИЯ ==================
async def show_message(callback: types.CallbackQuery, *, text: str = None, kb=None, photo_bytes: bytes = None):
    msg = callback.message
    wants_photo = photo_bytes is not None
    is_photo = bool(msg.photo)

    if wants_photo and is_photo:
        try:
            await msg.edit_media(media=InputMediaPhoto(media=BufferedInputFile(photo_bytes, filename="f.png"), caption=text, parse_mode="HTML"), reply_markup=kb)
            return
        except Exception: logging.exception("edit_media failed")
    elif not wants_photo and not is_photo:
        try:
            await msg.edit_text(text, parse_mode="HTML", reply_markup=kb)
            return
        except Exception: logging.exception("edit_text failed")

    try: await msg.delete()
    except Exception: pass

    try:
        if wants_photo:
            await bot.send_photo(msg.chat.id, BufferedInputFile(photo_bytes, filename="f.png"), caption=text, parse_mode="HTML", reply_markup=kb)
        else:
            await bot.send_message(msg.chat.id, text, parse_mode="HTML", reply_markup=kb)
    except Exception: logging.exception("send failed")

# ================== КАРТОЧКА ТЕМЫ ==================
async def show_topic(callback: types.CallbackQuery, root_key: str, idx: int):
    t = get_topic(root_key, idx)
    section_title = ROOT_SECTIONS[root_key]["title"].replace("📐 ", "").replace("⚛️ ", "")
    caption = f"<b>{t['name'].upper()}</b>\n<i>{section_title} · {t['section']}</i>\n━━━━━━━━━━━━━━━━━━━━━\n\n<b>ФОРМУЛА</b>\n<code>{t['formula']}</code>"
    variants = t.get("variants") or []
    if variants:
        caption += "\n\n<b>КАК НАЙТИ</b>"
        for symbol, name, f in variants:
            caption += f"\n• <b>{name}</b>: <code>{f}</code>"
    caption += f"\n\n<b>ТЕОРЕМА</b>\n{t['theorem']}"
    if t.get("example"):
        caption += f"\n\n<b>ПРИМЕР</b>\n{t['example']}"
    if len(caption) > 1000: caption = caption[:1000] + "…"
    photo_bytes = None
    if t.get("svg"):
        try: photo_bytes = svg_to_png(t["svg"]())
        except Exception: pass
    await show_message(callback, text=caption, kb=kb_topic(root_key, idx), photo_bytes=photo_bytes)

# ================== КОМАНДЫ ==================
@dp.message(Command("start"))
async def cmd_start(m: types.Message, state: FSMContext):
    await state.clear()
    await m.answer("<b>СУПЕР-БОТ: ФИЗИКА & ГЕОМЕТРИЯ</b>\n━━━━━━━━━━━━━━━━━━━━━\nВыберите раздел:", parse_mode="HTML", reply_markup=kb_main())

@dp.message(Command("cancel"))
async def cmd_cancel(m: types.Message, state: FSMContext):
    if await state.get_state() is None:
        await m.answer("Нет активного действия.")
        return
    await state.clear()
    await m.answer("Отменено.", reply_markup=kb_main())

# ================== НАВИГАЦИЯ ==================
@dp.callback_query(F.data == "back:main")
async def cb_main(cb: types.CallbackQuery):
    await show_message(cb, text="<b>ГЛАВНОЕ МЕНЮ</b>\n━━━━━━━━━━━━━━━━━━━━━", kb=kb_main())
    await cb.answer()

@dp.callback_query(F.data.startswith("root:"))
async def cb_root(cb: types.CallbackQuery):
    root_key = cb.data.split(":", 1)[1]
    title = ROOT_SECTIONS[root_key]["title"]
    await show_message(cb, text=f"<b>{title}</b>\n━━━━━━━━━━━━━━━━━━━━━\nПодраздел:", kb=kb_subs(root_key))
    await cb.answer()

@dp.callback_query(F.data.startswith("sec:"))
async def cb_section(cb: types.CallbackQuery):
    _, root_key, section = cb.data.split(":", 2)
    await show_message(cb, text=f"<b>{section.upper()}</b>\n━━━━━━━━━━━━━━━━━━━━━\nТема:", kb=kb_section(root_key, section))
    await cb.answer()

@dp.callback_query(F.data.startswith("topic:"))
async def cb_topic(cb: types.CallbackQuery, state: FSMContext):
    _, root_key, idx_s = cb.data.split(":", 2)
    await state.clear()
    await cb.answer()
    await show_topic(cb, root_key, int(idx_s))

# ================== КАЛЬКУЛЯТОР ==================
@dp.callback_query(F.data.startswith("solve:"))
async def cb_solve(cb: types.CallbackQuery):
    parts = cb.data.split(":", 2)
    if len(parts) == 2 and parts[1] == "start":
        await cb.message.answer("Опишите задачу одним сообщением.")
        await cb.answer(); return
    _, root_key, idx_s = parts
    idx = int(idx_s)
    t = get_topic(root_key, idx)
    if not t.get("calc"): await cb.answer("Нет калькулятора", show_alert=True); return
    await cb.message.answer(f"<b>{t['name'].upper()}</b>\n<code>{t['formula']}</code>\n\nЧто найти?", parse_mode="HTML", reply_markup=kb_targets(root_key, idx))
    await cb.answer()

@dp.callback_query(F.data.startswith("pick:"))
async def cb_pick(cb: types.CallbackQuery, state: FSMContext):
    _, root_key, idx_s, target = cb.data.split(":", 3)
    idx = int(idx_s)
    calc = get_topic(root_key, idx)["calc"]
    needed = [n for n, _ in calc["vars"] if n != target]
    labels = {n: lbl for n, lbl in calc["vars"]}
    if not needed: await cb.answer("Нечего вводить", show_alert=True); return
    await state.update_data(root_key=root_key, topic_idx=idx, target=target, needed=needed, labels=labels, values={}, current=0)
    await state.set_state(St.calc)
    await cb.answer()
    await cb.message.answer(f"<b>Найти: {target}</b>\nВведите <b>{labels[needed[0]]}</b> (1 из {len(needed)}):", parse_mode="HTML")

@dp.message(St.calc, F.text)
async def calc_input(m: types.Message, state: FSMContext):
    try: value = float(m.text.strip().replace(",", "."))
    except ValueError: await m.answer("Нужно число. Попробуйте ещё раз или /cancel."); return
    data = await state.get_data()
    needed, labels, values, current = data["needed"], data["labels"], data["values"], data["current"]
    values[needed[current]] = value
    current += 1
    if current < len(needed):
        await state.update_data(values=values, current=current)
        await m.answer(f"Введите <b>{labels[needed[current]]}</b> ({current + 1} из {len(needed)}):", parse_mode="HTML")
        return
    root_key, idx, target = data["root_key"], data["topic_idx"], data["target"]
    t = get_topic(root_key, idx)
    try: result = t["calc"]["solvers"][target](**values)
    except Exception as e: await m.answer(f"Ошибка: {e}"); await state.clear(); return
    given = "\n".join(f"  {k} = {fmt_number(v)}" for k, v in values.items())
    unit = _UNIT_FOR_TARGET.get(target, "")
    unit_str = f" {unit}" if unit else ""
    await m.answer(f"<b>РЕЗУЛЬТАТ</b>\n━━━━━━━━━━━━━━━━━━━━━\n<b>Формула</b>  <code>{t['formula']}</code>\n\n<b>Дано</b>\n{given}\n\n<b>{target} = {fmt_number(result)}{unit_str}</b>", parse_mode="HTML", reply_markup=kb_topic(root_key, idx))
    await state.clear()

# ================== OSINT МОДУЛЬ ==================
@dp.callback_query(F.data == "osint_menu")
async def cb_osint_menu(cb: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await show_message(cb, text="<b>🕵️‍♂️ OSINT МОДУЛЬ</b>\n━━━━━━━━━━━━━━━━━━━━━\nВыберите тип данных для поиска:", kb=kb_osint_menu())
    await cb.answer()

@dp.callback_query(F.data == "osint:phone")
async def cb_osint_phone(cb: types.CallbackQuery, state: FSMContext):
    await state.set_state(St.osint_phone)
    await cb.message.edit_text("📱 <b>Введите номер телефона</b> (в формате +79...):\n\nДля отмены: /cancel", parse_mode="HTML")
    await cb.answer()

@dp.message(St.osint_phone, F.text)
async def process_osint_phone(m: types.Message, state: FSMContext):
    text = m.text.strip()
    try:
        parsed = phonenumbers.parse(text, "RU")
        if not phonenumbers.is_valid_number(parsed):
            await m.answer("❌ Неверный формат. Введите с кодом страны (+79512041698).")
            return
        op = carrier.name_for_number(parsed, "ru") or "Неизвестен / MVNO"
        reg = geocoder.description_for_number(parsed, "ru") or "Не определен"
        clean_num = text.replace("+", "").replace(" ", "")
        
        kb = InlineKeyboardBuilder()
        kb.button(text="Искать в ВК", url=f"https://vk.com/search?c%5Bsection%5D=people")
        kb.button(text="Искать на Авито", url=f"https://yandex.ru/search/?text=%22{clean_num}%22+site%3Aavito.ru")
        kb.button(text="Спам-база", url=f"https://zvonili.com/phone/{clean_num}")
        kb.adjust(1)
        
        await m.answer(f"📱 <b>РЕЗУЛЬТАТ ПО НОМЕРУ:</b> <code>{text}</code>\n━━━━━━━━━━━━━━━━━━━━━\n📡 <b>Оператор:</b> {op}\n🗺 <b>Регион:</b> {reg}\n\n👇 Используй кнопки ниже:", parse_mode="HTML", reply_markup=kb.as_markup())
        await state.clear()
    except Exception as e:
        await m.answer(f"❌ Ошибка: {e}"); await state.clear()

@dp.callback_query(F.data == "osint:tg")
async def cb_osint_tg(cb: types.CallbackQuery, state: FSMContext):
    await state.set_state(St.osint_tg)
    await cb.message.edit_text("✈️ <b>Введите Telegram юзернейм</b> (например, @durov):\n\nДля отмены: /cancel", parse_mode="HTML")
    await cb.answer()

@dp.message(St.osint_tg, F.text)
async def process_osint_tg(m: types.Message, state: FSMContext):
    clean_user = m.text.replace("@", "").strip()
    msg = await m.answer("🔍 Сканирую Telegram и генерирую ссылки...")
    
    url = f"https://t.me/{clean_user}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    try:
        # Асинхронный запрос, чтобы не вешать бота
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as response:
                
                if response.status != 200:
                    await msg.edit_text(f"❌ Telegram заблокировал запрос (Код: {response.status}). Возможно, IP сервера в бане. Попробуйте позже.")
                    await state.clear()
                    return
                
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                title_tag = soup.find("div", class_="tgme_page_title")
                
                if title_tag:
                    name = title_tag.text.strip()
                    bio_tag = soup.find("div", class_="tgme_page_description")
                    bio_text = bio_tag.text.strip() if bio_tag else "Нет описания"
                    img_tag = soup.find("img", class_="tgme_page_photo_image")
                    avatar = img_tag["src"] if img_tag else None
                    
                    # Создаем кнопки для дальнейшего поиска
                    kb = InlineKeyboardBuilder()
                    kb.button(text="Искать в ВК", url=f"https://vk.com/{clean_user}")
                    kb.button(text="Искать в Яндексе", url=f"https://yandex.ru/search/?text=%22{clean_user}%22")
                    kb.button(text="Поиск по форумам", url=f"https://yandex.ru/search/?text=%22{clean_user}%22+forum")
                    kb.adjust(1)
                    
                    caption = (
                        f"✈️ <b>ПРОФИЛЬ:</b> @{clean_user}\n"
                        "━━━━━━━━━━━━━━━━━━━━━\n"
                        f"👤 <b>Имя:</b> {name}\n"
                        f"📝 <b>Bio:</b> {bio_text}\n\n"
                        f"👇 <i>Дополнительный поиск:</i>"
                    )
                    
                    if avatar:
                        await bot.send_photo(chat_id=m.chat.id, photo=avatar, caption=caption, parse_mode="HTML", reply_markup=kb.as_markup())
                        await msg.delete()
                    else:
                        await msg.edit_text(caption, parse_mode="HTML", reply_markup=kb.as_markup())
                else:
                    await msg.edit_text(f"❌ Профиль <b>@{clean_user}</b> не найден или скрыт настройками приватности.", parse_mode="HTML")
                    
    except asyncio.TimeoutError:
        await msg.edit_text("❌ Таймаут. Сервер Render не смог достучаться до Telegram за 10 секунд.")
    except Exception as e:
        await msg.edit_text(f"❌ Ошибка соединения: {str(e)[:100]}")
    finally:
        await state.clear()

# ================== ПОИСК (ТЕКСТ) ==================
@dp.message(F.text & ~F.text.startswith("/"))
async def search_handler(m: types.Message, state: FSMContext):
    if await state.get_state() in [St.calc, St.osint_phone, St.osint_tg]:
        return

    text = m.text.strip()
    if len(text) >= 6 and any(c.isdigit() for c in text):
        result = solve_problem(text)
        if result:
            t = result["topic"]
            values = result["values"]
            target = result["target"]
            answer = result["result"]
            root_key = result["root_key"]
            idx = result["idx"]
            has_kmh = result.get("has_kmh", False)
            root_title = ROOT_SECTIONS[root_key]["title"].replace("📐 ", "").replace("⚛️ ", "")
            given = "\n".join(f"  {k} = {fmt_number(v)}" for k, v in values.items())
            unit = _UNIT_FOR_TARGET.get(target, "")
            if has_kmh:
                if target in ["S", "s"]: unit = "км"
                elif target == "v": unit = "км/ч"
                elif target == "t": unit = "ч"
            unit_str = f" {unit}" if unit else ""
            await m.answer(f"<b>РЕШЕНИЕ</b>\n━━━━━━━━━━━━━━━━━━━━━\n<i>{t['section']} · {root_title}</i>\n\n<b>Формула</b>  <code>{t['formula']}</code>\n\n<b>Дано</b>\n{given}\n\n<b>Ответ</b>\n{target} = {fmt_number(answer)}{unit_str}", parse_mode="HTML", reply_markup=kb_topic(root_key, idx))
            return

    if len(text) < 2:
        await m.answer("Введите хотя бы 2 символа.")
        return

    results = search_all(text)
    if not results:
        await m.answer("<b>НЕ УДАЛОСЬ РАСПОЗНАТЬ</b>\n━━━━━━━━━━━━━━━━━━━━━\nПопробуйте описать подробнее или откройте меню.", parse_mode="HTML", reply_markup=kb_main())
        return

    kb = InlineKeyboardBuilder()
    for root_key, idx in results[:20]:
        t = get_topic(root_key, idx)
        kb.button(text=t["name"], callback_data=f"topic:{root_key}:{idx}")
    kb.button(text="⬅️  НАЗАД", callback_data="back:main")
    kb.adjust(1)

    await m.answer(f"<b>НАЙДЕНО: {len(results)}</b>", parse_mode="HTML", reply_markup=kb.as_markup())

# ================== HEALTH & ЗАПУСК ==================
async def health(request):
    return web.Response(text="ok")

async def start_web():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", PORT).start()

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
    await start_web()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Stopped")
