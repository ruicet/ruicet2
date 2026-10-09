import asyncio
import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import cairosvg
from data import TOPICS


# ================== НАСТРОЙКИ ==================
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PORT = int(os.environ.get("PORT", 10000))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# ================== СОСТОЯНИЯ ==================
class CalcStates(StatesGroup):
    waiting_value = State()


# ================== ИНДЕКС РАЗДЕЛОВ ==================
SECTIONS: dict[str, list[tuple[int, str]]] = {}
for _i, _t in enumerate(TOPICS):
    SECTIONS.setdefault(_t["section"], []).append((_i, _t["name"]))


# ================== КЛАВИАТУРЫ ==================
def main_menu_kb():
    kb = InlineKeyboardBuilder()
    for section in SECTIONS:
        kb.button(text=f"📂 {section}", callback_data=f"sec:{section}")
    kb.button(text="ℹ️ Помощь", callback_data="help")
    kb.adjust(1)
    return kb.as_markup()


def section_kb(section: str):
    kb = InlineKeyboardBuilder()
    for idx, name in SECTIONS[section]:
        kb.button(text=name, callback_data=f"topic:{idx}")
    kb.button(text="🏠 Меню", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()


def topic_kb(idx: int):
    kb = InlineKeyboardBuilder()
    kb.button(text="🧮 Решить задачу", callback_data=f"solve:{idx}")
    kb.button(text="⬅️ К списку", callback_data=f"sec:{TOPICS[idx]['section']}")
    kb.button(text="🏠 Меню", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()


def solve_targets_kb(idx: int):
    calc = TOPICS[idx]["calc"]
    kb = InlineKeyboardBuilder()
    for name, label in calc["vars"]:
        if name in calc["solvers"]:
            kb.button(text=f"Найти {name}", callback_data=f"pick:{idx}:{name}")
    kb.button(text="⬅️ Назад", callback_data=f"topic:{idx}")
    kb.adjust(2)
    return kb.as_markup()


# ================== SVG → PNG ==================
def svg_to_png(svg_str: str) -> bytes:
    return cairosvg.svg2png(
        bytestring=svg_str.encode("utf-8"),
        output_width=900,
        output_height=675,
        background_color="#0f1729",
    )


# ================== ОТОБРАЖЕНИЕ ТЕМЫ ==================
async def send_topic(target, idx: int):
    """Отправляет карточку темы: картинку + текст + кнопки."""
    t = TOPICS[idx]

    caption = (
        f"<b>{t['name']}</b>\n"
        f"<i>{t['section']}</i>\n\n"
        f"<b>📐 Формула:</b>\n<code>{t['formula']}</code>\n\n"
        f"<b>📖 Теорема:</b>\n{t['theorem']}"
    )

    # Обрезаем, если caption слишком длинный (лимит Telegram — 1024 символа)
    if len(caption) > 1000:
        caption = caption[:1000] + "…"

    try:
        png = svg_to_png(t["svg"]())
        photo = BufferedInputFile(png, filename="figure.png")
        await target.answer_photo(
            photo, caption=caption,
            parse_mode="HTML",
            reply_markup=topic_kb(idx),
        )
    except Exception as e:
        logging.exception("SVG render failed")
        # fallback — просто текст без картинки
        await target.answer(
            caption + f"\n\n<i>(картинка недоступна: {e})</i>",
            parse_mode="HTML",
            reply_markup=topic_kb(idx),
        )


# ================== ОБРАБОТЧИКИ: КОМАНДЫ ==================
@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "👋 Привет!\n\n"
        "Я — <b>справочник по геометрии</b>.\n"
        "Умею:\n"
        "📚 показывать формулы, теоремы и рисунки\n"
        "🧮 решать задачи по формулам\n"
        "🔍 искать темы по ключевым словам\n\n"
        "Выбери раздел 👇",
        parse_mode="HTML",
        reply_markup=main_menu_kb(),
    )


@dp.message(Command("help"))
@dp.callback_query(F.data == "help")
async def cmd_help(event, state: FSMContext = None):
    text = (
        "📖 <b>Как пользоваться</b>\n\n"
        "• Выбери раздел в меню → тему\n"
        "• В карточке темы есть кнопка <b>🧮 Решить задачу</b>\n"
        "• Введи числа по одному → получишь ответ\n\n"
        "🔍 <b>Поиск:</b> просто отправь слово, например:\n"
        "<i>пифагор</i>, <i>косинус</i>, <i>шар</i>, <i>объём</i>\n\n"
        "/start — меню\n"
        "/cancel — отменить ввод чисел"
    )
    if isinstance(event, types.CallbackQuery):
        await event.message.answer(text, parse_mode="HTML", reply_markup=main_menu_kb())
        await event.answer()
    else:
        await event.answer(text, parse_mode="HTML", reply_markup=main_menu_kb())


@dp.message(Command("cancel"))
async def cmd_cancel(message: types.Message, state: FSMContext):
    if await state.get_state() is None:
        await message.answer("Нечего отменять 🙂")
        return
    await state.clear()
    await message.answer("✅ Отменено.", reply_markup=main_menu_kb())


# ================== НАВИГАЦИЯ ==================
async def edit_or_send(callback: types.CallbackQuery, text: str, kb):
    """Аккуратно заменяет текст/подпись текущего сообщения."""
    msg = callback.message
    try:
        if msg.photo:
            await msg.edit_caption(caption=text, parse_mode="HTML", reply_markup=kb)
        else:
            await msg.edit_text(text, parse_mode="HTML", reply_markup=kb)
    except Exception:
        await msg.answer(text, parse_mode="HTML", reply_markup=kb)


@dp.callback_query(F.data == "back:main")
async def cb_main(callback: types.CallbackQuery):
    await edit_or_send(
        callback,
        "📚 Выбери раздел:",
        main_menu_kb(),
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("sec:"))
async def cb_section(callback: types.CallbackQuery):
    section = callback.data[4:]
    if section not in SECTIONS:
        await callback.answer("Раздел не найден", show_alert=True)
        return
    await edit_or_send(
        callback,
        f"📂 <b>{section}</b>\n\nВыбери тему:",
        section_kb(section),
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("topic:"))
async def cb_topic(callback: types.CallbackQuery, state: FSMContext):
    idx = int(callback.data.split(":")[1])
    await state.clear()
    await callback.answer()
    await send_topic(callback.message, idx)


# ================== КАЛЬКУЛЯТОР (FSM) ==================
@dp.callback_query(F.data.startswith("solve:"))
async def cb_solve_start(callback: types.CallbackQuery):
    idx = int(callback.data.split(":")[1])
    t = TOPICS[idx]
    calc = t.get("calc")
    if not calc:
        await callback.answer("Для этой формулы нет калькулятора", show_alert=True)
        return

    await callback.message.answer(
        f"🧮 <b>{t['name']}</b>\n"
        f"Формула: <code>{t['formula']}</code>\n\n"
        f"Что нужно найти?",
        parse_mode="HTML",
        reply_markup=solve_targets_kb(idx),
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("pick:"))
async def cb_pick_target(callback: types.CallbackQuery, state: FSMContext):
    _, idx_s, target = callback.data.split(":")
    idx = int(idx_s)
    calc = TOPICS[idx]["calc"]

    needed = [n for n, _ in calc["vars"] if n != target]
    labels = {n: lbl for n, lbl in calc["vars"]}

    await state.update_data(
        topic_idx=idx,
        target=target,
        needed=needed,
        labels=labels,
        values={},
        current=0,
    )
    await state.set_state(CalcStates.waiting_value)

    await callback.answer()
    await callback.message.answer(
        f"🔢 Ищем: <b>{target}</b>\n"
        f"Всего нужно ввести значений: {len(needed)}\n\n"
        f"Введи <b>{labels[needed[0]]}</b> (1 из {len(needed)}):",
        parse_mode="HTML",
    )


@dp.message(CalcStates.waiting_value, F.text)
async def calc_input(message: types.Message, state: FSMContext):
    raw = message.text.strip().replace(",", ".")
    try:
        value = float(raw)
    except ValueError:
        await message.answer("❌ Нужно число. Попробуй снова или /cancel.")
        return

    data = await state.get_data()
    needed = data["needed"]
    labels = data["labels"]
    values = data["values"]
    current = data["current"]

    values[needed[current]] = value
    current += 1

    if current < len(needed):
        await state.update_data(values=values, current=current)
        await message.answer(
            f"Введи <b>{labels[needed[current]]}</b> "
            f"({current + 1} из {len(needed)}):",
            parse_mode="HTML",
        )
        return

    # Все значения собраны → считаем
    idx = data["topic_idx"]
    target = data["target"]
    calc = TOPICS[idx]["calc"]

    try:
        result = calc["solvers"][target](**values)
    except ZeroDivisionError:
        await message.answer("❌ Деление на ноль.", reply_markup=topic_kb(idx))
        await state.clear()
        return
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}", reply_markup=topic_kb(idx))
        await state.clear()
        return

    if isinstance(result, float) and abs(result - round(result)) < 1e-9:
        s = str(int(round(result)))
    else:
        s = f"{result:.6g}"

    given = "\n".join(f"  {k} = {v:g}" for k, v in values.items())
    await message.answer(
        f"✅ <b>{target} = {s}</b>\n\n"
        f"<b>Дано:</b>\n{given}\n\n"
        f"<b>Формула:</b> <code>{calc and TOPICS[idx]['formula']}</code>",
        parse_mode="HTML",
        reply_markup=topic_kb(idx),
    )
    await state.clear()


# ================== ПОИСК ==================
@dp.message(F.text & ~F.text.startswith("/"))
async def search_handler(message: types.Message, state: FSMContext):
    if await state.get_state() is not None:
        return  # обрабатывается в FSM

    q = message.text.lower().strip()
    if len(q) < 2:
        await message.answer("Введи хотя бы 2 символа для поиска.")
        return

    matches = [
        i for i, t in enumerate(TOPICS)
        if q in t["name"].lower()
        or q in t["formula"].lower()
        or q in t["theorem"].lower()
        or q in t["section"].lower()
    ]

    if not matches:
        await message.answer(
            "😕 Ничего не найдено.\n"
            "Попробуй другое слово или открой /start для меню."
        )
        return

    kb = InlineKeyboardBuilder()
    for i in matches[:20]:
        kb.button(text=TOPICS[i]["name"], callback_data=f"topic:{i}")
    kb.button(text="🏠 Меню", callback_data="back:main")
    kb.adjust(1)

    await message.answer(
        f"🔍 Найдено тем: <b>{len(matches)}</b>",
        parse_mode="HTML",
        reply_markup=kb.as_markup(),
    )


# ================== HEALTH-ЭНДПОИНТ ДЛЯ RENDER ==================
async def health(request):
    return web.Response(text="Bot is alive")


async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    logging.info(f"Health server on port {PORT}")


# ================== ЗАПУСК ==================
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    if not BOT_TOKEN:
        logging.error("BOT_TOKEN не задан в переменных окружения!")
        return

    await start_web_server()
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("🤖 Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("👋 Остановлено")
