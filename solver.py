import re
from data import ROOT_SECTIONS


# ================== ЧИСЛА + ЕДИНИЦЫ ==================
_NUM_UNIT_RE = re.compile(
    r'(-?\d+(?:[.,]\d+)?)\s*'
    r'(км/ч|м/с|km/h|m/s'
    r'|км|см|мм|м'
    r'|мин|ч|сек|с|часа|часов|час'
    r'|кг|г|т'
    r'|дж|вт|па|н|а|в|ом'
    r'|°c|°с|°'
    r'|л|м³|см³|м²|см²)?',
    re.IGNORECASE
)


_UNIT_NORM = {
    'км/ч': 'speed', 'м/с': 'speed', 'km/h': 'speed', 'm/s': 'speed',
    'км': 'distance', 'м': 'distance', 'см': 'distance_cm', 'мм': 'distance_mm',
    'ч': 'time_h', 'час': 'time_h', 'часа': 'time_h', 'часов': 'time_h',
    'мин': 'time_min',
    'с': 'time_s', 'сек': 'time_s',
    'кг': 'mass_kg', 'г': 'mass_g', 'т': 'mass_t',
    'н': 'force', 'дж': 'energy', 'вт': 'power', 'па': 'pressure',
    'а': 'current', 'в': 'voltage', 'ом': 'resistance',
    '°c': 'temp', '°с': 'temp', '°': 'temp',
    'л': 'volume_l', 'м³': 'volume', 'см³': 'volume_cm3',
    'м²': 'area', 'см²': 'area_cm2',
}


def extract_values(text: str) -> list[dict]:
    out = []
    for m in _NUM_UNIT_RE.finditer(text):
        try:
            num = float(m.group(1).replace(',', '.'))
        except ValueError:
            continue
        unit_raw = (m.group(2) or '').strip().lower()
        out.append({
            'value': num,
            'unit': _UNIT_NORM.get(unit_raw, ''),
        })
    return out


# ================== МЕТАДАННЫЕ ТЕМ ==================
# Ключ: (root_key, name_темы)
TOPIC_META = {
    # ---------- ФИЗИКА ----------
    ("phys", "Скорость (равномерное движение)"): {
        "keywords": ["скорость", "едет", "движется", "летит", "плывёт", "плывет",
                     "проехал", "прошёл", "прошел", "прошла",
                     "какое расстояние", "какой путь"],
        "units": {"v": ["speed"], "s": ["distance"], "t": ["time_h", "time_s", "time_min"]},
        "question_hints": {
            "v": ["скорость", "быстро"],
            "s": ["путь", "расстояние", "сколько проедет", "сколько пройдёт", "сколько пройдет"],
            "t": ["время", "за сколько"],
        },
    },
    ("phys", "Путь при равномерном движении"): {
        "keywords": ["путь", "расстояние"],
        "units": {"v": ["speed"], "t": ["time_h", "time_s", "time_min"], "s": ["distance"]},
    },
    ("phys", "Плотность вещества"): {
        "keywords": ["плотность", "вещество"],
        "units": {"m": ["mass_kg", "mass_g", "mass_t"],
                  "V": ["volume", "volume_l", "volume_cm3"],
                  "ρ": ["density"]},
    },
    ("phys", "Сила тяжести"): {
        "keywords": ["сила тяжести", "вес тела"],
        "units": {"m": ["mass_kg"], "F": ["force"]},
    },
    ("phys", "Закон Гука (сила упругости)"): {
        "keywords": ["пружина", "жёсткость", "жесткость", "удлинение", "растянул", "сжал"],
        "units": {"k": ["stiffness"], "x": ["distance"], "F": ["force"]},
    },
    ("phys", "Давление твёрдого тела"): {
        "keywords": ["давление", "давит"],
        "units": {"F": ["force"], "S": ["area"], "p": ["pressure"]},
    },
    ("phys", "Давление жидкости"): {
        "keywords": ["глубина", "жидкость", "вода", "керосин", "нефть"],
        "units": {"ρ": ["density"], "h": ["distance"], "p": ["pressure"]},
    },
    ("phys", "Сила Архимеда"): {
        "keywords": ["архимед", "выталкивающая", "плавает", "погружён", "погружен"],
        "units": {"ρ": ["density"], "V": ["volume"], "F": ["force"]},
    },
    ("phys", "Механическая работа"): {
        "keywords": ["работа", "совершил"],
        "units": {"F": ["force"], "s": ["distance"], "A": ["energy"]},
    },
    ("phys", "Мощность"): {
        "keywords": ["мощность", "ватт"],
        "units": {"A": ["energy"], "t": ["time_h", "time_s", "time_min"], "N": ["power"]},
    },
    ("phys", "Кинетическая энергия"): {
        "keywords": ["кинетическая", "энергия движения"],
        "units": {"m": ["mass_kg"], "v": ["speed"], "Ek": ["energy"]},
    },
    ("phys", "Потенциальная энергия"): {
        "keywords": ["потенциальная", "подняли", "на высоте"],
        "units": {"m": ["mass_kg"], "h": ["distance"], "Ep": ["energy"]},
    },
    ("phys", "Количество теплоты при нагревании"): {
        "keywords": ["нагрели", "нагревание", "теплоёмкость", "теплоемкость", "температура"],
        "units": {"c": ["specific_heat"], "m": ["mass_kg"], "dt": ["temp"], "Q": ["energy"]},
    },
    ("phys", "Теплота плавления"): {
        "keywords": ["плавление", "расплавили", "лёд", "лед"],
        "units": {"lam": ["specific_latent"], "m": ["mass_kg"], "Q": ["energy"]},
    },
    ("phys", "Закон Ома для участка цепи"): {
        "keywords": ["ток", "напряжение", "сопротивление", "ом"],
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
        "keywords": ["мощность тока", "мощность лампы"],
        "units": {"U": ["voltage"], "I": ["current"], "P": ["power"]},
    },
    ("phys", "Работа электрического тока"): {
        "keywords": ["работа тока"],
        "units": {"U": ["voltage"], "I": ["current"], "t": ["time_h", "time_s"], "A": ["energy"]},
    },
    ("phys", "Закон Джоуля-Ленца"): {
        "keywords": ["джоуль", "ленц", "проводник"],
        "units": {"I": ["current"], "R": ["resistance"], "t": ["time_s", "time_h"], "Q": ["energy"]},
    },
    ("phys", "Скорость при равноускоренном движении"): {
        "keywords": ["ускорение", "равноускоренное", "начальная скорость"],
        "units": {"v0": ["speed"], "a": ["accel"], "t": ["time_s", "time_h"], "v": ["speed"]},
    },
    ("phys", "Второй закон Ньютона"): {
        "keywords": ["ньютон", "второй закон"],
        "units": {"m": ["mass_kg"], "a": ["accel"], "F": ["force"]},
    },
    ("phys", "Импульс тела"): {
        "keywords": ["импульс"],
        "units": {"m": ["mass_kg"], "v": ["speed"], "p": ["impulse"]},
    },
    ("phys", "Свободное падение"): {
        "keywords": ["свободное падение", "упало", "падает с высоты"],
        "units": {"t": ["time_s"], "h": ["distance"]},
    },
    ("phys", "Центростремительное ускорение"): {
        "keywords": ["центростремительное", "по окружности"],
        "units": {"v": ["speed"], "R": ["distance"], "a": ["accel"]},
    },
    ("phys", "Период и частота вращения"): {
        "keywords": ["период", "частота", "оборот"],
        "units": {"nu": ["frequency"], "T": ["time_s"]},
    },
    ("phys", "Длина волны"): {
        "keywords": ["длина волны", "волна"],
        "units": {"v": ["speed"], "T": ["time_s"], "lam": ["distance"]},
    },
    ("phys", "Закон всемирного тяготения"): {
        "keywords": ["тяготение", "гравитация", "притяжение"],
        "units": {"m1": ["mass_kg"], "m2": ["mass_kg"], "r": ["distance"], "F": ["force"]},
    },

    # ---------- ГЕОМЕТРИЯ ----------
    ("geom", "Площадь треугольника"): {
        "keywords": ["площадь треугольника", "треугольник", "основание"],
        "field_hints": {"a": ["основание", "основанию", "основанием"],
                        "h": ["высота", "высот"]},
        "question_hints": {"S": ["площадь", "площади"]},
    },
    ("geom", "Формула Герона"): {
        "keywords": ["герон", "три стороны"],
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


# ================== ЛОГИКА ==================
def _score(meta: dict, text: str) -> int:
    return sum(len(kw) for kw in meta.get("keywords", []) if kw in text)


def _assign(meta: dict, topic: dict, values: list[dict], text: str) -> dict | None:
    calc = topic.get("calc")
    if not calc:
        return None
    var_names = [v[0] for v in calc["vars"]]
    units_map = meta.get("units", {})
    hints_map = meta.get("field_hints", {})

    assignment, used = {}, set()

    # 1. По единицам
    for i, val in enumerate(values):
        if i in used or not val["unit"]:
            continue
        for var in var_names:
            if var in assignment:
                continue
            if val["unit"] in units_map.get(var, []):
                assignment[var] = val["value"]
                used.add(i)
                break

    # 2. По подсказкам ("основание 4")
    for var, hints in hints_map.items():
        if var in assignment:
            continue
        for hint in hints:
            m = re.search(re.escape(hint) + r'[а-я]*\s+(-?\d+(?:[.,]\d+)?)', text, re.IGNORECASE)
            if m:
                try:
                    assignment[var] = float(m.group(1).replace(',', '.'))
                    break
                except ValueError:
                    pass

    # 3. По позиции (если не хватает одной переменной — она цель)
    unused = [values[i]["value"] for i in range(len(values)) if i not in used]
    remaining = [v for v in var_names if v not in assignment]
    if len(unused) == len(remaining) - 1 and len(unused) > 0:
        for i, var in enumerate(remaining[:-1]):
            assignment[var] = unused[i]

    return assignment or None


def _target(meta: dict, topic: dict, text: str, assignment: dict) -> str | None:
    calc = topic["calc"]
    var_names = [v[0] for v in calc["vars"]]
    solvers = calc["solvers"]

    for var, hints in meta.get("question_hints", {}).items():
        if var in solvers and var not in assignment:
            for h in hints:
                if h in text:
                    return var

    candidates = [v for v in var_names if v not in assignment and v in solvers]
    return candidates[0] if len(candidates) == 1 else None


def solve_problem(text: str) -> dict | None:
    if not text or len(text.strip()) < 5:
        return None

    text_lower = text.lower()
    values = extract_values(text_lower)
    if not values:
        return None

    candidates = []
    for root_key, data in ROOT_SECTIONS.items():
        for idx, topic in enumerate(data["topics"]):
            meta = TOPIC_META.get((root_key, topic["name"]))
            if not meta or not topic.get("calc"):
                continue
            score = _score(meta, text_lower)
            if score > 0:
                candidates.append((score, root_key, idx, topic, meta))

    candidates.sort(key=lambda x: -x[0])

    for _score_val, root_key, idx, topic, meta in candidates:
        assignment = _assign(meta, topic, values, text_lower)
        if not assignment:
            continue
        target = _target(meta, topic, text_lower, assignment)
        if not target:
            continue
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
        }
    return None
