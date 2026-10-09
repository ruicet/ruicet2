import math
import re
from data import ROOT_SECTIONS


# ================== ПРЕДОБРАБОТКА ТЕКСТА ==================
def preprocess(text: str) -> str:
    """Приводим текст к удобному виду: 'пол часа' → '0.5 ч', 'километров в час' → 'км/ч' и т.п."""
    t = text.lower()

    # ----- составные выражения (числа словами) -----
    compound = [
        (r'\bпол\s*[-]?\s*часа?\b', ' 0.5 ч '),
        (r'\bпол\s*[-]?\s*минуты?\b', ' 0.5 мин '),
        (r'\bпол\s*[-]?\s*секунды?\b', ' 0.5 сек '),
        (r'\bполтора\s+часа?\b', ' 1.5 ч '),
        (r'\bполтора\s+минуты?\b', ' 1.5 мин '),
        (r'\bчетверть\s+часа?\b', ' 0.25 ч '),
        (r'\bполовина\s+часа?\b', ' 0.5 ч '),
        (r'\bтри\s+четверти\s+часа\b', ' 0.75 ч '),
        (r'\bдва\s+часа\b', ' 2 ч '),
        (r'\bтри\s+часа\b', ' 3 ч '),
    ]
    for pat, repl in compound:
        t = re.sub(pat, repl, t)

    # ----- скорости: разные варианты написания -----
    speeds = [
        (r'километров\s+в\s+час[ау]?', 'км/ч'),
        (r'километр\s+в\s+час', 'км/ч'),
        (r'км\s*/\s*час[ау]?', 'км/ч'),
        (r'км\s*/\s*ч\b', 'км/ч'),
        (r'км\s+в\s+час[ау]?', 'км/ч'),
        (r'км\s+час', 'км/ч'),
        (r'метров\s+в\s+секунду', 'м/с'),
        (r'метр\s+в\s+секунду', 'м/с'),
        (r'м\s*/\s*сек[унды]*', 'м/с'),
        (r'м\s*/\s*с(?![а-яё])', 'м/с'),
        (r'м\s+в\s+с(?![а-яё])', 'м/с'),
        (r'km/h', 'км/ч'),
        (r'm/s', 'м/с'),
    ]
    for pat, repl in speeds:
        t = re.sub(pat, repl, t)

    # ----- единицы времени и других величин -----
    units = [
        (r'\bминут[аыуеой]*\b', 'мин'),
        (r'\bсекунд[аыуеой]*\b', 'сек'),
        (r'\bчасов\b', 'ч'),
        (r'\bчаса\b', 'ч'),
        (r'\bчасу\b', 'ч'),
        (r'\bчас\b', 'ч'),
        (r'\bкилограмм[аов]*\b', 'кг'),
        (r'\bграмм[аов]*\b', 'г'),
        (r'\bтонн[аыуе]*\b', 'т'),
        (r'\bлитр[аов]*\b', 'л'),
        (r'\bградус[аов]*\b', '°c'),
        (r'\bджоул[ьяи]*\b', 'дж'),
        (r'\bватт[аов]*\b', 'вт'),
        (r'\bпаскал[ьяи]*\b', 'па'),
        (r'\bньютон[аов]*\b', 'н'),
        (r'\bампер[аов]*\b', 'а'),
        (r'\bвольт[аов]*\b', 'в'),
        (r'\bом[аов]*\b', 'ом'),
        (r'\bкилометр[аов]*\b', 'км'),
        (r'\bсантиметр[аов]*\b', 'см'),
        (r'\bмиллиметр[аов]*\b', 'мм'),
        (r'\bметр[аов]*\b', 'м'),  # ставим после "метров в секунду" и "сантиметр"/"миллиметр"
    ]
    for pat, repl in units:
        t = re.sub(pat, repl, t)

    return t


# ================== ИЗВЛЕЧЕНИЕ ЧИСЕЛ С ЕДИНИЦАМИ ==================
_NUM_UNIT_RE = re.compile(
    r'(-?\d+(?:[.,]\d+)?)\s*'
    r'(км/ч|м/с'
    r'|°c'
    r'|мин|сек|ч'
    r'|кг|г|т'
    r'|дж|вт|па|н|ом'
    r'|л|м³|см³|м²|см²'
    r'|км|см|мм|м'
    r')?',
    re.IGNORECASE
)

_UNIT_NORM = {
    'км/ч': 'speed_kmh', 'м/с': 'speed_ms',
    'км': 'distance_km', 'см': 'distance_cm', 'мм': 'distance_mm', 'м': 'distance_m',
    'ч': 'time_h', 'мин': 'time_min', 'сек': 'time_s',
    'кг': 'mass_kg', 'г': 'mass_g', 'т': 'mass_t',
    'н': 'force', 'дж': 'energy', 'вт': 'power', 'па': 'pressure',
    'ом': 'resistance', 'а': 'current', 'в': 'voltage',
    '°c': 'temp',
    'л': 'volume_l', 'м³': 'volume_m3', 'см³': 'volume_cm3',
    'м²': 'area_m2', 'см²': 'area_cm2',
}


def extract_values(text: str):
    out = []
    for m in _NUM_UNIT_RE.finditer(text):
        try:
            num = float(m.group(1).replace(',', '.'))
        except ValueError:
            continue
        unit_raw = (m.group(2) or '').strip().lower()
        out.append({'value': num, 'unit': _UNIT_NORM.get(unit_raw, '')})
    return out


# ================== МЕТАДАННЫЕ ТЕМ ==================
TOPIC_META = {
    # ---------- ФИЗИКА ----------
    ("phys", "Скорость (равномерное движение)"): {
        "keywords": ["скорость", "едет", "ехал", "движется", "летит", "плыв",
                     "проехал", "прошёл", "прошел", "прошла", "прошло",
                     "какой путь", "какое расстояние", "сколько проедет", "сколько пройдет"],
        "units": {"v": ["speed_kmh", "speed_ms"],
                  "s": ["distance_km", "distance_m", "distance_cm", "distance_mm"],
                  "t": ["time_h", "time_min", "time_s"]},
        "question_hints": {
            "v": ["скорость", "быстро"],
            "s": ["путь", "расстояние", "проедет", "пройдёт", "пройдет", "пройдёт"],
            "t": ["время", "за сколько", "сколько времени"],
        },
    },
    ("phys", "Путь при равномерном движении"): {
        "keywords": ["путь", "расстояние"],
        "units": {"v": ["speed_kmh", "speed_ms"],
                  "s": ["distance_km", "distance_m"],
                  "t": ["time_h", "time_min", "time_s"]},
    },
    ("phys", "Плотность вещества"): {
        "keywords": ["плотность", "вещество"],
        "units": {"m": ["mass_kg", "mass_g", "mass_t"],
                  "V": ["volume_m3", "volume_l", "volume_cm3"],
                  "ρ": ["density"]},
    },
    ("phys", "Сила тяжести"): {
        "keywords": ["сила тяжести", "вес тела", "сила притяжения"],
        "units": {"m": ["mass_kg", "mass_g", "mass_t"], "F": ["force"]},
        "question_hints": {"F": ["сила", "вес"]},
    },
    ("phys", "Закон Гука (сила упругости)"): {
        "keywords": ["пружина", "пружину", "жёсткость", "жесткость", "удлинение",
                     "растянул", "сжал", "растянулась"],
        "units": {"k": ["stiffness"], "x": ["distance_m", "distance_cm", "distance_mm"], "F": ["force"]},
    },
    ("phys", "Давление твёрдого тела"): {
        "keywords": ["давление", "давит", "опора"],
        "units": {"F": ["force"], "S": ["area_m2", "area_cm2"], "p": ["pressure"]},
    },
    ("phys", "Давление жидкости"): {
        "keywords": ["глубина", "жидкость", "вода", "керосин", "нефть", "ртуть", "на глубине"],
        "units": {"ρ": ["density"], "h": ["distance_m"], "p": ["pressure"]},
    },
    ("phys", "Сила Архимеда"): {
        "keywords": ["архимед", "выталкивающая", "плавает", "погружён", "погружен", "погрузили"],
        "units": {"ρ": ["density"], "V": ["volume_m3", "volume_l"], "F": ["force"]},
    },
    ("phys", "Механическая работа"): {
        "keywords": ["работа", "совершил", "совершает"],
        "units": {"F": ["force"], "s": ["distance_m", "distance_km"], "A": ["energy"]},
    },
    ("phys", "Мощность"): {
        "keywords": ["мощность", "ватт"],
        "units": {"A": ["energy"], "t": ["time_h", "time_s", "time_min"], "N": ["power"]},
    },
    ("phys", "Кинетическая энергия"): {
        "keywords": ["кинетическая", "энергия движения"],
        "units": {"m": ["mass_kg"], "v": ["speed_ms", "speed_kmh"], "Ek": ["energy"]},
    },
    ("phys", "Потенциальная энергия"): {
        "keywords": ["потенциальная", "подняли", "на высоте", "высота"],
        "units": {"m": ["mass_kg"], "h": ["distance_m"], "Ep": ["energy"]},
    },
    ("phys", "Количество теплоты при нагревании"): {
        "keywords": ["нагрели", "нагревание", "нагреть", "теплоёмкость", "теплоемкость",
                     "температура", "градусов", "градуса"],
        "units": {"c": ["specific_heat"], "m": ["mass_kg"], "dt": ["temp"], "Q": ["energy"]},
    },
    ("phys", "Теплота плавления"): {
        "keywords": ["плавление", "расплавили", "лёд", "лед", "таял"],
        "units": {"lam": ["specific_latent"], "m": ["mass_kg"], "Q": ["energy"]},
    },
    ("phys", "Закон Ома для участка цепи"): {
        "keywords": ["ток", "напряжение", "сопротивление", "ом", "цепь"],
        "units": {"U": ["voltage"], "R": ["resistance"], "I": ["current"]},
        "question_hints": {"I": ["сила тока", "ток"], "U": ["напряжение"], "R": ["сопротивление"]},
    },
    ("phys", "Последовательное соединение"): {
        "keywords": ["последовательное", "последовательно"],
        "units": {"R1": ["resistance"], "R2": ["resistance"], "R": ["resistance"]},
    },
    ("phys", "Параллельное соединение"): {
        "keywords": ["параллельное", "параллельно"],
        "units": {"R1": ["resistance"], "R2": ["resistance"], "R": ["resistance"]},
    },
    ("phys", "Мощность электрического тока"): {
        "keywords": ["мощность тока", "мощность лампы", "мощность прибора"],
        "units": {"U": ["voltage"], "I": ["current"], "P": ["power"]},
    },
    ("phys", "Работа электрического тока"): {
        "keywords": ["работа тока", "работа электрического"],
        "units": {"U": ["voltage"], "I": ["current"], "t": ["time_h", "time_s"], "A": ["energy"]},
    },
    ("phys", "Закон Джоуля-Ленца"): {
        "keywords": ["джоуль", "ленц", "проводник", "провод"],
        "units": {"I": ["current"], "R": ["resistance"], "t": ["time_s", "time_h"], "Q": ["energy"]},
    },
    ("phys", "Скорость при равноускоренном движении"): {
        "keywords": ["ускорение", "равноускоренное", "начальная скорость", "ускорением"],
        "units": {"v0": ["speed_kmh", "speed_ms"], "a": ["accel"],
                  "t": ["time_s", "time_h"], "v": ["speed_kmh", "speed_ms"]},
    },
    ("phys", "Второй закон Ньютона"): {
        "keywords": ["ньютон", "второй закон", "ускорением", "сила действует"],
        "units": {"m": ["mass_kg"], "a": ["accel"], "F": ["force"]},
    },
    ("phys", "Импульс тела"): {
        "keywords": ["импульс"],
        "units": {"m": ["mass_kg"], "v": ["speed_kmh", "speed_ms"], "p": ["impulse"]},
    },
    ("phys", "Свободное падение"): {
        "keywords": ["свободное падение", "упало", "падает с высоты", "упал", "падает"],
        "units": {"t": ["time_s"], "h": ["distance_m"]},
    },
    ("phys", "Центростремительное ускорение"): {
        "keywords": ["центростремительное", "по окружности"],
        "units": {"v": ["speed_kmh", "speed_ms"], "R": ["distance_m"], "a": ["accel"]},
    },
    ("phys", "Период и частота вращения"): {
        "keywords": ["период", "частота", "оборот"],
        "units": {"nu": ["frequency"], "T": ["time_s"]},
    },
    ("phys", "Длина волны"): {
        "keywords": ["длина волны", "волна"],
        "units": {"v": ["speed_ms", "speed_kmh"], "T": ["time_s"], "lam": ["distance_m"]},
    },
    ("phys", "Закон всемирного тяготения"): {
        "keywords": ["тяготение", "гравитация", "притяжение"],
        "units": {"m1": ["mass_kg"], "m2": ["mass_kg"], "r": ["distance_m"], "F": ["force"]},
    },

    # ---------- ГЕОМЕТРИЯ ----------
    ("geom", "Площадь треугольника"): {
        "keywords": ["площадь треугольника", "треугольник", "основание"],
        "field_hints": {"a": ["основание", "основанию", "основанием"],
                        "h": ["высота", "высот", "высоте"]},
        "question_hints": {"S": ["площадь", "площади"]},
    },
    ("geom", "Формула Герона"): {
        "keywords": ["герон", "три стороны", "по трём сторонам"],
        "question_hints": {"S": ["площадь"]},
    },
    ("geom", "Теорема Пифагора"): {
        "keywords": ["пифагор", "прямоугольный треугольник", "катет", "гипотенуз"],
        "field_hints": {"a": ["катет"], "b": ["катет"], "c": ["гипотенуз"]},
        "question_hints": {"c": ["гипотенуз"], "a": ["катет"], "b": ["катет"]},
    },
    ("geom", "Площадь параллелограмма"): {
        "keywords": ["параллелограмм"],
        "question_hints": {"S": ["площадь"]},
    },
    ("geom", "Площадь трапеции"): {
        "keywords": ["трапеция", "трапеции"],
        "question_hints": {"S": ["площадь"]},
    },
    ("geom", "Площадь ромба"): {
        "keywords": ["ромб", "ромба"],
        "question_hints": {"S": ["площадь"]},
    },
    ("geom", "Длина окружности"): {
        "keywords": ["длина окружности", "длина круга"],
        "question_hints": {"C": ["длина", "длину"]},
    },
    ("geom", "Площадь круга"): {
        "keywords": ["круг", "окружность", "радиус"],
        "question_hints": {"S": ["площадь"], "R": ["радиус"]},
    },
    ("geom", "Объём шара"): {
        "keywords": ["шар", "шара", "сфера"],
        "question_hints": {"V": ["объём", "объем"], "R": ["радиус"]},
    },
    ("geom", "Объём цилиндра"): {
        "keywords": ["цилиндр", "цилиндра"],
        "question_hints": {"V": ["объём", "объем"]},
    },
    ("geom", "Объём конуса"): {
        "keywords": ["конус", "конуса"],
        "question_hints": {"V": ["объём", "объем"]},
    },
    ("geom", "Объём призмы"): {
        "keywords": ["призма", "призмы"],
        "question_hints": {"V": ["объём", "объем"]},
    },
    ("geom", "Объём пирамиды"): {
        "keywords": ["пирамида", "пирамиды"],
        "question_hints": {"V": ["объём", "объем"]},
    },
}


# ================== КОНВЕРТАЦИЯ ЕДИНИЦ ПЕРЕД ПОДСТАНОВКОЙ ==================
def _convert_to_solver(values_with_units: dict) -> dict:
    """values_with_units: {var: (value, unit)}  →  {var: value} в удобной системе."""
    has_kmh = any(u == 'speed_kmh' for _, u in values_with_units.values())

    result = {}
    for var, (val, unit) in values_with_units.items():
        nv = val
        if unit == 'time_h':
            nv = val if has_kmh else val * 3600
        elif unit == 'time_min':
            nv = val / 60 if has_kmh else val * 60
        elif unit == 'time_s':
            nv = val / 3600 if has_kmh else val

        elif unit == 'distance_km':
            nv = val if has_kmh else val * 1000
        elif unit == 'distance_m':
            nv = val if not has_kmh else val / 1000
        elif unit == 'distance_cm':
            nv = val / 100 if not has_kmh else val / 100000
        elif unit == 'distance_mm':
            nv = val / 1000 if not has_kmh else val / 1_000_000

        elif unit == 'mass_g':
            nv = val / 1000
        elif unit == 'mass_t':
            nv = val * 1000

        elif unit == 'volume_l':
            nv = val / 1000
        elif unit == 'volume_cm3':
            nv = val / 1_000_000

        elif unit == 'area_cm2':
            nv = val / 10000

        elif unit == 'speed_ms':
            nv = val * 3.6 if has_kmh else val
        elif unit == 'speed_kmh':
            nv = val if has_kmh else val / 3.6

        result[var] = nv
    return result


# ================== ПОДБОР ТЕМЫ И ПЕРЕМЕННЫХ ==================
def _score(meta: dict, text: str) -> int:
    return sum(len(kw) for kw in meta.get("keywords", []) if kw in text)


def _assign(meta: dict, topic: dict, values: list[dict], text: str):
    """Возвращает {var: (value, unit)} или None."""
    calc = topic.get("calc")
    if not calc:
        return None
    var_names = [v[0] for v in calc["vars"]]
    units_map = meta.get("units", {})
    hints_map = meta.get("field_hints", {})

    assignment: dict = {}
    used: set = set()

    # 1. По единицам
    for i, val in enumerate(values):
        if i in used or not val["unit"]:
            continue
        for var in var_names:
            if var in assignment:
                continue
            if val["unit"] in units_map.get(var, []):
                assignment[var] = (val["value"], val["unit"])
                used.add(i)
                break

    # 2. По подсказкам ("основание 4", "катет 3")
    for var, hints in hints_map.items():
        if var in assignment:
            continue
        for hint in hints:
            m = re.search(
                re.escape(hint) + r'[а-яё]*\s*(?:равен[а-яё]*\s*|=\s*)?(-?\d+(?:[.,]\d+)?)',
                text, re.IGNORECASE
            )
            if m:
                try:
                    assignment[var] = (float(m.group(1).replace(',', '.')), '')
                    break
                except ValueError:
                    pass

    # 3. По позиции (последняя незанятая переменная считается целью)
    unused = [(i, values[i]) for i in range(len(values)) if i not in used]
    remaining = [v for v in var_names if v not in assignment]
    # Распределяем оставшиеся числа по оставшимся переменным (кроме предполагаемой цели)
    if 0 < len(unused) == len(remaining) - 1:
        for idx_pos, var in enumerate(remaining[:-1]):
            i, val = unused[idx_pos]
            assignment[var] = (val["value"], val["unit"])
            used.add(i)

    return assignment or None


def _target(meta: dict, topic: dict, text: str, assignment: dict):
    calc = topic["calc"]
    var_names = [v[0] for v in calc["vars"]]
    solvers = calc["solvers"]

    # Сначала по подсказкам в вопросе
    for var, hints in meta.get("question_hints", {}).items():
        if var in solvers and var not in assignment:
            for h in hints:
                if h in text:
                    return var

    # Иначе — единственная незанятая переменная, которую можно решить
    candidates = [v for v in var_names if v not in assignment and v in solvers]
    return candidates[0] if len(candidates) == 1 else None


# ================== ОСНОВНАЯ ФУНКЦИЯ ==================
def solve_problem(text: str):
    if not text or len(text.strip()) < 4:
        return None

    processed = preprocess(text)
    values = extract_values(processed)
    if not values:
        return None

    candidates = []
    for root_key, data in ROOT_SECTIONS.items():
        for idx, topic in enumerate(data["topics"]):
            meta = TOPIC_META.get((root_key, topic["name"]))
            if not meta or not topic.get("calc"):
                continue
            score = _score(meta, processed)
            if score > 0:
                candidates.append((score, root_key, idx, topic, meta))

    candidates.sort(key=lambda x: -x[0])

    for _score_val, root_key, idx, topic, meta in candidates:
        assignment_with_units = _assign(meta, topic, values, processed)
        if not assignment_with_units:
            continue

        # Определяем цель до конвертации (по исходным vars)
        target = _target(meta, topic, processed, {k: v for k, v in assignment_with_units.items()})
        if not target:
            continue

        # Конвертация единиц
        assignment = _convert_to_solver(assignment_with_units)

        try:
            result = topic["calc"]["solvers"][target](**assignment)
        except Exception:
            continue

        return {
            "root_key": root_key,
            "idx": idx,
            "topic": topic,
            "values": assignment,
            "target": target,
            "result": result,
            "has_kmh": any(u == 'speed_kmh' for _, u in assignment_with_units.values()),
        }
    return None
