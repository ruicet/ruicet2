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

from data import (
    ROOT_SECTIONS,
    get_subsections,
    get_topic,
    search_all,
)


# ================== НАСТРОЙКИ ==================
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PORT = int(os.environ.get("PORT", 10000))

if not BOT_TOKEN:
    raise RuntimeError("Переменная окружения BOT_TOKEN не задана!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# ================== СОСТОЯНИЯ ==================
class CalcStates(StatesGroup):
    waiting_value = State()


# ================== КЛАВИАТУРЫ ==================
def root_menu_kb():
    kb = InlineKeyboardBuilder()
    for key, data in ROOT_SECTIONS.items():
        kb.button(text=data["title"], callback_data=f"root:{key}")
    kb.button(text="🔍 Как искать", callback_data="help")
    kb.adjust(1)
    return kb.as_markup()


def subsections_kb(root_key: str):
    kb = InlineKeyboardBuilder()
    subs = get_subsections(root_key)
    for section in subs:
        kb.button(text=f"📂 {section}", callback_data=f"sec:{root_key}:{section}")
    kb.button(text="🏠 Разделы", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()


def section_kb(root_key: str, section: str):
    kb = InlineKeyboardBuilder()
    subs = get_subsections(root_key)
    for idx, name in subs.get(section, []):
        kb.button(text=name, callback_data=f"topic:{root_key}:{idx}")
    kb.button(text="⬅️ Назад", callback_data=f"root:{root_key}")
    kb.button(text="🏠 Разделы", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()


def topic_kb(root_key: str, idx: int):
    t = get_topic(root_key, idx)
    kb = InlineKeyboardBuilder()
    if t.get("calc"):
        kb.button(text="🧮 Решить задачу", callback_data=f"solve:{root_key}:{idx}")
    kb.button(text="⬅️ К списку", callback_data=f"sec:{root_key}:{t['section']}")
    kb.button(text="🏠 Разделы", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()


def solve_targets_kb(root_key: str, idx: int):
    calc = get_topic(root_key, idx)["calc"]
    kb = InlineKeyboardBuilder()
    for name, label in calc["vars"]:
        if name in calc["solvers"]:
            kb.button(
                text=f"Найти {name}",
                callback_data=f"pick:{root_key}:{idx}:{name}",
            )
    kb.button(text="⬅️ Назад", callback_data=f"topic:{root_key}:{idx}")
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


# ================== ОТПРАВКА КАРТОЧКИ ТЕМЫ ==================
async def send_topic(target, root_key: str, idx: int):
    t = get_topic(root_key, idx)

    caption = (
        f"<b>{t['name']}</b>\n"
        f"<i>{t['section']}</i>\n\n"
        f"<b>📐 Формула:</b>\n<code>{t['formula']}</code>\n\n"
        f"<b>📖 Теория:</b>\n{t['theorem']}"
    )
    if t.get("example"):
        caption += f"\n\n<b>💡 Пример:</b>\n{t['example']}"

    # Telegram ограничивает подпись к фото 1024 символами
    if len(caption) > 1000:
        caption = caption[:1000] + "…"

    kb = topic_kb(root_key, idx)

    if t.get("svg"):
        try:
            png = svg_to_png(t["svg"]())
            await target.answer_photo(
                BufferedInputFile(png, filename="figure.png"),
                caption=caption,
                parse_mode="HTML",
                reply_markup=kb,
            )
            return
        except Exception:
            logging.exception("SVG render failed — отправляю только текст")

    await target.answer(caption, parse_mode="HTML", reply_markup=kb)


# ================== ХЕЛПЕР ==================
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


# ================== КОМАНДЫ ==================
@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "👋 Привет!\n\n"
        "Я — справочник по <b>геометрии</b> и <b>физике</b>.\n"
        "📐 Формулы и теоремы\n"
        "⚛️ Физика 7–9 класс\n"
        "🧮 Калькулятор для каждой формулы\n\n"
        "Выбери раздел 👇",
        parse_mode="HTML",
        reply_markup=root_menu_kb(),
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📖 <b>Как пользоваться ботом</b>\n\n"
        "• Выбери раздел (Геометрия / Физика)\n"
        "• Затем подраздел (Треугольники, 7 класс, …)\n"
        "• И тему — увидишь формулу, теорему и рисунок\n"
        "• Кнопка <b>🧮 Решить задачу</b> откроет калькулятор\n\n"
        "🔍 <b>Поиск:</b> просто отправь слово:\n"
        "<i>пифагор</i>, <i>скорость</i>, <i>шар</i>, <i>ом</i>\n\n"
        "Команды:\n"
        "/start — меню\n"
        "/cancel — отменить ввод",
        parse_mode="HTML",
        reply_markup=root_menu_kb(),
    )


@dp.message(Command("cancel"))
async def cmd_cancel(message: types.Message, state: FSMContext):
    if await state.get_state() is None:
        await message.answer("Нечего отменять 🙂")
        return
    await state.clear()
    await message.answer("✅ Отменено.", reply_markup=root_menu_kb())


# ================== НАВИГАЦИЯ ==================
@dp.callback_query(F.data == "back:main")
async def cb_main(callback: types.CallbackQuery):
    await edit_or_send(callback, "📚 Выбери раздел:", root_menu_kb())
    await callback.answer()


@dp.callback_query(F.data == "help")
async def cb_help(callback: types.CallbackQuery):
    await callback.message.answer(
        "🔍 Отправь любое слово — я найду формулу.\n"
        "Например: <i>косинус</i>, <i>плотность</i>, <i>объём шара</i>",
        parse_mode="HTML",
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("root:"))
async def cb_root(callback: types.CallbackQuery):
    root_key = callback.data.split(":", 1)[1]
    if root_key not in ROOT_SECTIONS:
        await callback.answer("Раздел не найден", show_alert=True)
        return
    title = ROOT_SECTIONS[root_key]["title"]
    await edit_or_send(callback, f"{title}\n\nВыбери подраздел:", subsections_kb(root_key))
    await callback.answer()


@dp.callback_query(F.data.startswith("sec:"))
async def cb_section(callback: types.CallbackQuery):
    parts = callback.data.split(":", 2)
    if len(parts) != 3:
        await callback.answer("Ошибка", show_alert=True)
        return
    _, root_key, section = parts
    await edit_or_send(
        callback,
        f"📂 <b>{section}</b>\n\nВыбери тему:",
        section_kb(root_key, section),
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("topic:"))
async def cb_topic(callback: types.CallbackQuery, state: FSMContext):
    parts = callback.data.split(":", 2)
    if len(parts) != 3:
        await callback.answer("Ошибка", show_alert=True)
        return
    _, root_key, idx_s = parts
    try:
        idx = int(idx_s)
    except ValueError:
        await callback.answer("Ошибка", show_alert=True)
        return
    await state.clear()
    await callback.answer()
    await send_topic(callback.message, root_key, idx)


# ================== КАЛЬКУЛЯТОР ==================
@dp.callback_query(F.data.startswith("solve:"))
async def cb_solve_start(callback: types.CallbackQuery):
    parts = callback.data.split(":", 2)
    if len(parts) != 3:
        await callback.answer("Ошибка", show_alert=True)
        return
    _, root_key, idx_s = parts
    try:
        idx = int(idx_s)
    except ValueError:
        await callback.answer("Ошибка", show_alert=True)
        return

    t = get_topic(root_key, idx)
    calc = t.get("calc")
    if not calc:
        await callback.answer("Для этой формулы нет калькулятора", show_alert=True)
        return

    await callback.message.answer(
        f"🧮 <b>{t['name']}</b>\n"
        f"Формула: <code>{t['formula']}</code>\n\n"
        f"Что нужно найти?",
        parse_mode="HTML",
        reply_markup=solve_targets_kb(root_key, idx),
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("pick:"))
async def cb_pick_target(callback: types.CallbackQuery, state: FSMContext):
    parts = callback.data.split(":", 3)
    if len(parts) != 4:
        await callback.answer("Ошибка", show_alert=True)
        return
    _, root_key, idx_s, target = parts
    try:
        idx = int(idx_s)
    except ValueError:
        await callback.answer("Ошибка", show_alert=True)
        return

    t = get_topic(root_key, idx)
    calc = t["calc"]

    needed = [n for n, _ in calc["vars"] if n != target]
    labels = {n: lbl for n, lbl in calc["vars"]}

    if not needed:
        await callback.answer("Нечего вводить", show_alert=True)
        return

    await state.update_data(
        root_key=root_key,
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
        f"Всего значений: {len(needed)}\n\n"
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

    # Все значения собраны — считаем
    root_key = data["root_key"]
    idx = data["topic_idx"]
    target = data["target"]
    t = get_topic(root_key, idx)
    calc = t["calc"]

    try:
        result = calc["solvers"][target](**values)
    except ZeroDivisionError:
        await message.answer("❌ Деление на ноль.", reply_markup=topic_kb(root_key, idx))
        await state.clear()
        return
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}", reply_markup=topic_kb(root_key, idx))
        await state.clear()
        return

    if isinstance(result, float) and abs(result - round(result)) < 1e-9:
        s = str(int(round(result)))
    else:
        s = f"{result:.6g}"

    given = "\n".join(f"  <b>{k}</b> = {v:g}" for k, v in values.items())
    await message.answer(
        f"✅ <b>{target} = {s}</b>\n\n"
        f"<b>Дано:</b>\n{given}\n\n"
        f"<b>Формула:</b> <code>{t['formula']}</code>",
        parse_mode="HTML",
        reply_markup=topic_kb(root_key, idx),
    )
    await state.clear()


# ================== ПОИСК ==================
@dp.message(F.text & ~F.text.startswith("/"))
async def search_handler(message: types.Message, state: FSMContext):
    if await state.get_state() is not None:
        return  # заняты вводом чисел

    q = message.text.strip()
    if len(q) < 2:
        await message.answer("Введи хотя бы 2 символа для поиска.")
        return

    results = search_all(q)

    if not results:
        await message.answer(
            "😕 Ничего не найдено.\n"
            "Попробуй другое слово или открой /start для меню."
        )
        return

    kb = InlineKeyboardBuilder()
    for root_key, idx in results[:20]:
        t = get_topic(root_key, idx)
        icon = "📐" if root_key == "geom" else "⚛️"
        kb.button(text=f"{icon} {t['name']}", callback_data=f"topic:{root_key}:{idx}")
    kb.button(text="🏠 Разделы", callback_data="back:main")
    kb.adjust(1)

    await message.answer(
        f"🔍 Найдено тем: <b>{len(results)}</b>",
        parse_mode="HTML",
        reply_markup=kb.as_markup(),
    )


# ================== HEALTH-СЕРВЕР ДЛЯ RENDER ==================
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

    await start_web_server()
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("🤖 Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("👋 Остановлено")
