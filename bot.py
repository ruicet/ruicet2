import asyncio
import logging
import os

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


# ================== КЛАВИАТУРЫ ==================
def kb_main():
    kb = InlineKeyboardBuilder()
    kb.button(text="📐 ГЕОМЕТРИЯ", callback_data="root:geom")
    kb.button(text="⚛️ ФИЗИКА", callback_data="root:phys")
    kb.button(text="🧠 РЕШИТЬ ЗАДАЧУ", callback_data="solve:start")
    kb.button(text="ℹ️ СПРАВКА", callback_data="help")
    kb.adjust(1)
    return kb.as_markup()


def kb_subs(root_key: str):
    kb = InlineKeyboardBuilder()
    for section in get_subsections(root_key):
        kb.button(text=section.upper(), callback_data=f"sec:{root_key}:{section}")
    kb.button(text="⬅️ НАЗАД", callback_data="back:main")
    kb.adjust(1)
    return kb.as_markup()


def kb_section(root_key: str, section: str):
    kb = InlineKeyboardBuilder()
    for idx, name in get_subsections(root_key).get(section, []):
        kb.button(text=name, callback_data=f"topic:{root_key}:{idx}")
    kb.button(text="⬅️ НАЗАД", callback_data=f"root:{root_key}")
    kb.adjust(1)
    return kb.as_markup()


def kb_topic(root_key: str, idx: int):
    t = get_topic(root_key, idx)
    kb = InlineKeyboardBuilder()
    if t.get("calc"):
        kb.button(text="🧮 РЕШИТЬ ПО ФОРМУЛЕ", callback_data=f"solve:{root_key}:{idx}")
    kb.button(text="⬅️ НАЗАД", callback_data=f"sec:{root_key}:{t['section']}")
    kb.adjust(1)
    return kb.as_markup()


def kb_targets(root_key: str, idx: int):
    calc = get_topic(root_key, idx)["calc"]
    kb = InlineKeyboardBuilder()
    for name, _ in calc["vars"]:
        if name in calc["solvers"]:
            kb.button(text=f"Найти {name}", callback_data=f"pick:{root_key}:{idx}:{name}")
    kb.button(text="⬅️ НАЗАД", callback_data=f"topic:{root_key}:{idx}")
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


# ================== ФОРМАТИРОВАНИЕ ==================
def fmt_number(x) -> str:
    if isinstance(x, float) and abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{x:.6g}"


# ================== ГЛАВНЫЙ ХЕЛПЕР: ПОКАЗ СООБЩЕНИЯ ==================
async def show_message(
    callback: types.CallbackQuery,
    *,
    text: str | None = None,
    kb=None,
    photo_bytes: bytes | None = None,
):
    """
    Гарантирует, что в чате остаётся ровно ОДНО сообщение навигации.
    - фото → фото: edit_media
    - текст → текст: edit_text
    - типы разные: удалить старое и прислать новое
    """
    msg = callback.message
    wants_photo = photo_bytes is not None
    is_photo = bool(msg.photo)

    # --- Оба фото: редактируем media ---
    if wants_photo and is_photo:
        try:
            await msg.edit_media(
                media=InputMediaPhoto(
                    media=BufferedInputFile(photo_bytes, filename="f.png"),
                    caption=text, parse_mode="HTML",
                ),
                reply_markup=kb,
            )
            return
        except Exception:
            logging.exception("edit_media failed — fallback")

    # --- Оба текст: редактируем текст ---
    elif not wants_photo and not is_photo:
        try:
            await msg.edit_text(text, parse_mode="HTML", reply_markup=kb)
            return
        except Exception:
            logging.exception("edit_text failed — fallback")

    # --- Типы разные: удаляем старое и присылаем новое ---
    try:
        await msg.delete()
    except Exception:
        logging.exception("delete failed — продолжаем")

    try:
        if wants_photo:
            await bot.send_photo(
                msg.chat.id,
                BufferedInputFile(photo_bytes, filename="f.png"),
                caption=text, parse_mode="HTML", reply_markup=kb,
            )
        else:
            await bot.send_message(
                msg.chat.id, text, parse_mode="HTML", reply_markup=kb,
            )
    except Exception:
        logging.exception("send fallback failed")


# ================== КАРТОЧКА ТЕМЫ ==================
async def show_topic(callback: types.CallbackQuery, root_key: str, idx: int):
    t = get_topic(root_key, idx)
    section_title = ROOT_SECTIONS[root_key]["title"].replace("📐 ", "").replace("⚛️ ", "")

    caption = (
        f"<b>{t['name'].upper()}</b>\n"
        f"<i>{section_title} · {t['section']}</i>\n"
        "─────────────────────\n\n"
        f"<b>ФОРМУЛА</b>\n<code>{t['formula']}</code>\n\n"
        f"<b>ТЕОРЕМА</b>\n{t['theorem']}"
    )
    if t.get("example"):
        caption += f"\n\n<b>ПРИМЕР</b>\n{t['example']}"
    if len(caption) > 1000:
        caption = caption[:1000] + "…"

    kb = kb_topic(root_key, idx)

    photo_bytes = None
    if t.get("svg"):
        try:
            photo_bytes = svg_to_png(t["svg"]())
        except Exception:
            logging.exception("SVG render failed")

    await show_message(callback, text=caption, kb=kb, photo_bytes=photo_bytes)


# ================== КОМАНДЫ ==================
@dp.message(Command("start"))
async def cmd_start(m: types.Message, state: FSMContext):
    await state.clear()
    await m.answer(
        "<b>СПРАВОЧНИК</b>\n"
        "Геометрия · Физика 7–9 класс\n"
        "─────────────────────\n"
        "Формулы, теоремы, рисунки.\n"
        "Калькуляторы и решение задач по описанию.\n\n"
        "Выберите раздел:",
        parse_mode="HTML", reply_markup=kb_main(),
    )


@dp.message(Command("help"))
async def cmd_help(m: types.Message):
    await m.answer(
        "<b>СПРАВКА</b>\n"
        "─────────────────────\n\n"
        "• <b>ГЕОМЕТРИЯ</b> / <b>ФИЗИКА</b> — справочник\n"
        "• <b>РЕШИТЬ ЗАДАЧУ</b> — опишите словами,\n"
        "  бот подберёт формулу и решит.\n\n"
        "<b>Примеры задач:</b>\n"
        "<i>Машина едет 340 км/ч пол часа. Какой путь?</i>\n"
        "<i>Тело массой 5 кг. Найди силу тяжести.</i>\n"
        "<i>Прямоугольный треугольник с катетами 3 и 4. Найди гипотенузу.</i>\n"
        "<i>Поезд прошёл 200 км за 2 часа. Найди скорость.</i>\n\n"
        "Также можно отправить слово для поиска:\n"
        "<i>пифагор</i>, <i>ускорение</i>, <i>ом</i>\n\n"
        "/start — меню\n"
        "/cancel — отмена ввода",
        parse_mode="HTML", reply_markup=kb_main(),
    )


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
    await show_message(
        cb,
        text="<b>СПРАВОЧНИК</b>\n─────────────────────\nВыберите раздел:",
        kb=kb_main(),
    )
    await cb.answer()


@dp.callback_query(F.data == "help")
async def cb_help(cb: types.CallbackQuery):
    await cb.message.answer(
        "Отправьте задачу словами или слово для поиска.\n"
        "Или нажмите РЕШИТЬ ЗАДАЧУ в меню.",
    )
    await cb.answer()


@dp.callback_query(F.data.startswith("root:"))
async def cb_root(cb: types.CallbackQuery):
    root_key = cb.data.split(":", 1)[1]
    if root_key not in ROOT_SECTIONS:
        await cb.answer("Ошибка", show_alert=True)
        return
    title = ROOT_SECTIONS[root_key]["title"]
    await show_message(
        cb,
        text=f"<b>{title}</b>\n─────────────────────\nПодраздел:",
        kb=kb_subs(root_key),
    )
    await cb.answer()


@dp.callback_query(F.data.startswith("sec:"))
async def cb_section(cb: types.CallbackQuery):
    parts = cb.data.split(":", 2)
    if len(parts) != 3:
        await cb.answer("Ошибка", show_alert=True)
        return
    _, root_key, section = parts
    await show_message(
        cb,
        text=f"<b>{section.upper()}</b>\n─────────────────────\nТема:",
        kb=kb_section(root_key, section),
    )
    await cb.answer()


@dp.callback_query(F.data.startswith("topic:"))
async def cb_topic(cb: types.CallbackQuery, state: FSMContext):
    parts = cb.data.split(":", 2)
    if len(parts) != 3:
        await cb.answer("Ошибка", show_alert=True)
        return
    _, root_key, idx_s = parts
    try:
        idx = int(idx_s)
    except ValueError:
        await cb.answer("Ошибка", show_alert=True)
        return
    await state.clear()
    await cb.answer()
    await show_topic(cb, root_key, idx)


# ================== РЕШИТЬ ПО ФОРМУЛЕ / РЕШИТЬ ЗАДАЧУ ==================
@dp.callback_query(F.data.startswith("solve:"))
async def cb_solve(cb: types.CallbackQuery):
    parts = cb.data.split(":", 2)

    # --- Кнопка "РЕШИТЬ ЗАДАЧУ" ---
    if len(parts) == 2 and parts[1] == "start":
        await cb.message.answer(
            "<b>РЕШЕНИЕ ЗАДАЧИ</b>\n"
            "─────────────────────\n"
            "Опишите задачу одним сообщением.\n\n"
            "<b>Примеры:</b>\n"
            "<i>Машина едет 340 км/ч пол часа. Какой путь?</i>\n"
            "<i>Тело массой 5 кг. Найди силу тяжести.</i>\n"
            "<i>Прямоугольный треугольник с катетами 3 и 4. Найди гипотенузу.</i>\n"
            "<i>Круг радиусом 3. Найди площадь.</i>\n"
            "<i>Нагрели 2 кг воды на 50 градусов. Найди теплоту.</i>\n"
            "<i>Поезд прошёл 200 км за 2 часа. Найди скорость.</i>",
            parse_mode="HTML",
        )
        await cb.answer()
        return

    # --- Калькулятор для темы ---
    if len(parts) != 3:
        await cb.answer("Ошибка", show_alert=True)
        return
    _, root_key, idx_s = parts
    try:
        idx = int(idx_s)
    except ValueError:
        await cb.answer("Ошибка", show_alert=True)
        return
    t = get_topic(root_key, idx)
    if not t.get("calc"):
        await cb.answer("Нет калькулятора", show_alert=True)
        return
    await cb.message.answer(
        f"<b>{t['name'].upper()}</b>\n"
        f"<code>{t['formula']}</code>\n\n"
        "Что найти?",
        parse_mode="HTML", reply_markup=kb_targets(root_key, idx),
    )
    await cb.answer()


@dp.callback_query(F.data.startswith("pick:"))
async def cb_pick(cb: types.CallbackQuery, state: FSMContext):
    parts = cb.data.split(":", 3)
    if len(parts) != 4:
        await cb.answer("Ошибка", show_alert=True)
        return
    _, root_key, idx_s, target = parts
    try:
        idx = int(idx_s)
    except ValueError:
        await cb.answer("Ошибка", show_alert=True)
        return

    calc = get_topic(root_key, idx)["calc"]
    needed = [n for n, _ in calc["vars"] if n != target]
    labels = {n: lbl for n, lbl in calc["vars"]}

    if not needed:
        await cb.answer("Нечего вводить", show_alert=True)
        return

    await state.update_data(root_key=root_key, topic_idx=idx, target=target,
                            needed=needed, labels=labels, values={}, current=0)
    await state.set_state(St.calc)
    await cb.answer()
    await cb.message.answer(
        f"Найти: <b>{target}</b>\n"
        f"Значений: {len(needed)}\n\n"
        f"Введите <b>{labels[needed[0]]}</b> (1 из {len(needed)}):",
        parse_mode="HTML",
    )


@dp.message(St.calc, F.text)
async def calc_input(m: types.Message, state: FSMContext):
    raw = m.text.strip().replace(",", ".")
    try:
        value = float(raw)
    except ValueError:
        await m.answer("Нужно число. Попробуйте ещё раз или /cancel.")
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
        await m.answer(
            f"Введите <b>{labels[needed[current]]}</b> "
            f"({current + 1} из {len(needed)}):",
            parse_mode="HTML",
        )
        return

    root_key = data["root_key"]
    idx = data["topic_idx"]
    target = data["target"]
    t = get_topic(root_key, idx)
    calc = t["calc"]

    try:
        result = calc["solvers"][target](**values)
    except ZeroDivisionError:
        await m.answer("Деление на ноль.")
        await state.clear()
        return
    except Exception as e:
        await m.answer(f"Ошибка: {e}")
        await state.clear()
        return

    given = "\n".join(f"  {k} = {fmt_number(v)}" for k, v in values.items())
    await m.answer(
        f"<b>РЕЗУЛЬТАТ</b>\n"
        "─────────────────────\n"
        f"Формула: <code>{t['formula']}</code>\n\n"
        f"<b>Дано</b>\n{given}\n\n"
        f"<b>{target} = {fmt_number(result)}</b>",
        parse_mode="HTML", reply_markup=kb_topic(root_key, idx),
    )
    await state.clear()


# ================== ПОИСК + РЕШЕНИЕ ЗАДАЧ ==================
@dp.message(F.text & ~F.text.startswith("/"))
async def search_handler(m: types.Message, state: FSMContext):
    if await state.get_state() == St.calc:
        return

    text = m.text.strip()

    # 1. Сначала пробуем решить как задачу
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

            unit_suffix = ""
            if target == "s":
                unit_suffix = " км" if has_kmh else " м"
            elif target == "v":
                unit_suffix = " км/ч" if has_kmh else " м/с"
            elif target == "t":
                unit_suffix = " ч" if has_kmh else " с"
            elif target in ("F", "F1", "F2", "MT"):
                unit_suffix = " Н"
            elif target in ("A", "Q", "Ek", "Ep"):
                unit_suffix = " Дж"
            elif target in ("N", "P"):
                unit_suffix = " Вт"
            elif target == "p":
                unit_suffix = " Па"
            elif target == "V":
                unit_suffix = " м³"
            elif target == "I":
                unit_suffix = " А"
            elif target == "U":
                unit_suffix = " В"
            elif target == "R":
                unit_suffix = " Ом"
            elif target == "a":
                unit_suffix = " м/с²"
            elif target == "lam":
                unit_suffix = " м"
            elif target == "T":
                unit_suffix = " с"

            await m.answer(
                f"<b>РЕШЕНИЕ</b>\n"
                "─────────────────────\n"
                f"<i>{t['section']} · {root_title}</i>\n\n"
                f"<b>Формула</b>\n<code>{t['formula']}</code>\n\n"
                f"<b>Дано</b>\n{given}\n\n"
                f"<b>Ответ</b>\n{target} = {fmt_number(answer)}{unit_suffix}",
                parse_mode="HTML",
                reply_markup=kb_topic(root_key, idx),
            )
            return

    # 2. Обычный поиск
    if len(text) < 2:
        await m.answer("Введите хотя бы 2 символа.")
        return

    results = search_all(text)
    if not results:
        await m.answer(
            "<b>НЕ УДАЛОСЬ РАСПОЗНАТЬ</b>\n"
            "─────────────────────\n"
            "Попробуйте описать задачу подробнее:\n"
            "• Укажите единицы: <i>км/ч, кг, минуты, градусов</i>\n"
            "• Явно напишите, что найти: <i>найди путь</i>\n\n"
            "Или откройте раздел ГЕОМЕТРИЯ / ФИЗИКА\n"
            "и найдите тему вручную.",
            parse_mode="HTML", reply_markup=kb_main(),
        )
        return

    kb = InlineKeyboardBuilder()
    for root_key, idx in results[:20]:
        t = get_topic(root_key, idx)
        kb.button(text=t["name"], callback_data=f"topic:{root_key}:{idx}")
    kb.button(text="⬅️ НАЗАД", callback_data="back:main")
    kb.adjust(1)

    await m.answer(
        f"<b>НАЙДЕНО: {len(results)}</b>",
        parse_mode="HTML", reply_markup=kb.as_markup(),
    )


# ================== HEALTH ==================
async def health(request):
    return web.Response(text="ok")


async def start_web():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", PORT).start()
    logging.info(f"Health on port {PORT}")


# ================== ЗАПУСК ==================
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    await start_web()
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Stopped")
