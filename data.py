import math


# ================== УГЛЫ ==================
def sin_d(x): return math.sin(math.radians(x))
def cos_d(x): return math.cos(math.radians(x))
def asin_d(x): return math.degrees(math.asin(x))
def acos_d(x): return math.degrees(math.acos(x))


# ================== SVG РИСУНКИ ==================
def svg_wrap(inner: str) -> str:
    return f'''
    <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg"
         preserveAspectRatio="xMidYMid meet" style="width:100%; height:100%;">
        <style>
            .l {{ stroke: #4ade80; stroke-width: 2.5; fill: none; stroke-linejoin: round; }}
            .l-red {{ stroke: #e94560; stroke-width: 2.5; fill: none; }}
            .l-yellow {{ stroke: #facc15; stroke-width: 2.5; fill: none; }}
            .l-dash {{ stroke: #7a7a9a; stroke-width: 1.5; fill: none; stroke-dasharray: 5 5; }}
            .fill {{ fill: #0f3460; }}
            .t {{ fill: #c8c8d8; font-family: 'Cambria Math', serif; font-size: 16px; font-weight: bold; }}
            .t-red {{ fill: #e94560; font-family: 'Cambria Math', serif; font-size: 14px; font-weight: bold; }}
            .t-yellow {{ fill: #facc15; font-family: 'Cambria Math', serif; font-size: 14px; font-weight: bold; }}
        </style>
        {inner}
    </svg>
    '''


def draw_triangle():
    return svg_wrap('<polygon points="60,240 340,240 140,60" class="l fill"/>'
                    '<text x="45" y="260" class="t">A</text>'
                    '<text x="345" y="260" class="t">B</text>'
                    '<text x="130" y="50" class="t">C</text>')

def draw_right_triangle():
    return svg_wrap('<polygon points="60,240 340,240 60,60" class="l fill"/>'
                    '<rect x="60" y="220" width="20" height="20" fill="none" stroke="#e94560" stroke-width="2"/>'
                    '<text x="45" y="260" class="t">A</text>'
                    '<text x="345" y="260" class="t">B</text>'
                    '<text x="40" y="55" class="t">C</text>'
                    '<text x="180" y="265" class="t-yellow">a</text>'
                    '<text x="25" y="155" class="t-yellow">b</text>'
                    '<text x="180" y="140" class="t-red">c</text>')

def draw_triangle_height():
    return svg_wrap('<polygon points="60,240 340,240 260,60" class="l fill"/>'
                    '<line x1="260" y1="60" x2="260" y2="240" class="l-red"/>'
                    '<text x="45" y="260" class="t">A</text>'
                    '<text x="345" y="260" class="t">B</text>'
                    '<text x="265" y="50" class="t">C</text>'
                    '<text x="270" y="155" class="t-red">h</text>')

def draw_triangle_circle():
    return svg_wrap('<circle cx="200" cy="150" r="110" class="l-dash"/>'
                    '<polygon points="200,40 105,205 295,205" class="l fill"/>'
                    '<text x="200" y="30" class="t">A</text>'
                    '<text x="85" y="220" class="t">B</text>'
                    '<text x="300" y="220" class="t">C</text>')

def draw_parallelogram():
    return svg_wrap('<polygon points="60,240 280,240 340,60 120,60" class="l fill"/>'
                    '<line x1="120" y1="60" x2="120" y2="240" class="l-red"/>'
                    '<text x="130" y="155" class="t-red">h</text>')

def draw_trapezoid():
    return svg_wrap('<polygon points="50,240 350,240 270,60 130,60" class="l fill"/>'
                    '<line x1="130" y1="60" x2="130" y2="240" class="l-red"/>'
                    '<text x="140" y="155" class="t-red">h</text>')

def draw_rhombus():
    return svg_wrap('<polygon points="200,40 330,150 200,260 70,150" class="l fill"/>'
                    '<line x1="200" y1="40" x2="200" y2="260" class="l-red"/>'
                    '<line x1="330" y1="150" x2="70" y2="150" class="l-red"/>'
                    '<text x="210" y="90" class="t-red">d₁</text>'
                    '<text x="230" y="170" class="t-red">d₂</text>')

def draw_polygon():
    return svg_wrap('<polygon points="200,40 320,100 320,210 200,270 80,210 80,100" class="l fill"/>')

def draw_circle():
    return svg_wrap('<circle cx="200" cy="150" r="105" class="l fill"/>'
                    '<line x1="200" y1="150" x2="305" y2="150" class="l-red"/>'
                    '<circle cx="200" cy="150" r="4" fill="#e94560"/>'
                    '<text x="245" y="140" class="t-red">R</text>')

def draw_sector():
    return svg_wrap('<path d="M200,150 L305,150 A105,105 0 0,0 252,60 Z" class="l fill"/>'
                    '<circle cx="200" cy="150" r="105" class="l-dash"/>'
                    '<text x="235" y="125" class="t-red">α</text>')

def draw_inscribed_angle():
    return svg_wrap('<circle cx="200" cy="150" r="105" class="l"/>'
                    '<line x1="200" y1="150" x2="95" y2="150" class="l-yellow"/>'
                    '<line x1="200" y1="150" x2="252" y2="240" class="l-yellow"/>'
                    '<line x1="120" y1="90" x2="95" y2="150" class="l-red"/>'
                    '<line x1="120" y1="90" x2="252" y2="240" class="l-red"/>'
                    '<circle cx="200" cy="150" r="4" fill="#facc15"/>')

def draw_secant():
    return svg_wrap('<circle cx="250" cy="135" r="65" class="l"/>'
                    '<line x1="60" y1="210" x2="200" y2="90" class="l-red"/>'
                    '<line x1="60" y1="210" x2="315" y2="135" class="l-yellow"/>')

def draw_unit_circle():
    return svg_wrap('<line x1="60" y1="150" x2="340" y2="150" stroke="#4a4a6a" stroke-width="1"/>'
                    '<line x1="200" y1="30" x2="200" y2="270" stroke="#4a4a6a" stroke-width="1"/>'
                    '<circle cx="200" cy="150" r="105" class="l"/>'
                    '<line x1="200" y1="150" x2="280" y2="82" class="l-red"/>'
                    '<line x1="280" y1="82" x2="280" y2="150" class="l-yellow"/>'
                    '<line x1="200" y1="150" x2="280" y2="150" stroke="#a78bfa" stroke-width="2.5"/>')

def draw_prism():
    return svg_wrap('<polygon points="120,90 260,90 300,130 160,130" class="l fill"/>'
                    '<polygon points="120,170 260,170 300,210 160,210" class="l fill"/>'
                    '<line x1="120" y1="90" x2="120" y2="170" class="l"/>'
                    '<line x1="260" y1="90" x2="260" y2="170" class="l"/>')

def draw_pyramid():
    return svg_wrap('<polygon points="80,200 220,240 330,180 190,140" class="l fill"/>'
                    '<line x1="80" y1="200" x2="200" y2="60" class="l"/>'
                    '<line x1="220" y1="240" x2="200" y2="60" class="l"/>'
                    '<line x1="330" y1="180" x2="200" y2="60" class="l"/>'
                    '<line x1="200" y1="60" x2="200" y2="180" class="l-red"/>')

def draw_cylinder():
    return svg_wrap('<ellipse cx="200" cy="80" rx="70" ry="20" class="l fill"/>'
                    '<ellipse cx="200" cy="220" rx="70" ry="20" class="l fill"/>'
                    '<line x1="130" y1="80" x2="130" y2="220" class="l"/>'
                    '<line x1="270" y1="80" x2="270" y2="220" class="l"/>'
                    '<line x1="200" y1="80" x2="200" y2="220" class="l-red"/>')

def draw_cone():
    return svg_wrap('<ellipse cx="200" cy="220" rx="80" ry="22" class="l fill"/>'
                    '<line x1="120" y1="220" x2="200" y2="60" class="l"/>'
                    '<line x1="280" y1="220" x2="200" y2="60" class="l"/>'
                    '<line x1="200" y1="60" x2="200" y2="220" class="l-red"/>')

def draw_sphere():
    return svg_wrap('<circle cx="200" cy="150" r="105" class="l fill"/>'
                    '<ellipse cx="200" cy="150" rx="105" ry="30" fill="none" stroke="#7a7a9a" stroke-dasharray="4 4"/>'
                    '<line x1="200" y1="150" x2="290" y2="100" class="l-red"/>'
                    '<text x="240" y="115" class="t-red">R</text>')

def draw_frustum():
    return svg_wrap('<polygon points="140,90 260,90 290,120 170,120" class="l fill"/>'
                    '<polygon points="80,170 220,220 330,180 180,140" class="l fill"/>'
                    '<line x1="140" y1="90" x2="80" y2="170" class="l"/>'
                    '<line x1="260" y1="90" x2="220" y2="220" class="l"/>')

# Физические рисунки (упрощённые схемы)
def draw_motion():
    return svg_wrap('<line x1="40" y1="200" x2="360" y2="200" stroke="#4ade80" stroke-width="2"/>'
                    '<polygon points="160,170 200,200 160,230" fill="#4ade80"/>'
                    '<text x="200" y="180" class="t-yellow">v</text>'
                    '<text x="60" y="230" class="t">s, t</text>')

def draw_force():
    return svg_wrap('<rect x="150" y="120" width="100" height="60" class="fill l"/>'
                    '<line x1="250" y1="150" x2="350" y2="150" class="l-red"/>'
                    '<polygon points="350,140 370,150 350,160" fill="#e94560"/>'
                    '<text x="290" y="140" class="t-red">F</text>')

def draw_circuit():
    return svg_wrap('<line x1="80" y1="100" x2="320" y2="100" class="l"/>'
                    '<line x1="80" y1="200" x2="320" y2="200" class="l"/>'
                    '<line x1="80" y1="100" x2="80" y2="200" class="l"/>'
                    '<line x1="320" y1="100" x2="320" y2="200" class="l"/>'
                    '<rect x="150" y="90" width="60" height="20" fill="none" stroke="#facc15" stroke-width="2"/>'
                    '<circle cx="240" cy="200" r="15" fill="none" stroke="#e94560" stroke-width="2"/>'
                    '<text x="160" y="80" class="t-yellow">U</text>'
                    '<text x="230" y="235" class="t-red">R</text>')

def draw_heat():
    return svg_wrap('<rect x="140" y="140" width="120" height="100" class="fill l"/>'
                    '<path d="M160,130 Q170,100 180,130 Q190,100 200,130 Q210,100 220,130" class="l-red"/>'
                    '<text x="190" y="270" class="t-yellow">Q</text>')


# ================== ГЕОМЕТРИЯ ==================
GEOMETRY_TOPICS = [
    {"section": "Треугольники", "name": "Площадь треугольника",
     "formula": "S = ½ · a · h",
     "theorem": "Площадь треугольника равна половине произведения основания на высоту, проведённую к этому основанию.",
     "svg": draw_triangle_height,
     "calc": {"vars": [("a", "Основание a"), ("h", "Высота h"), ("S", "Площадь S")],
              "solvers": {"S": lambda a, h: 0.5*a*h, "a": lambda S, h: 2*S/h, "h": lambda S, a: 2*S/a}}},
    {"section": "Треугольники", "name": "Формула Герона",
     "formula": "S = √(p·(p−a)·(p−b)·(p−c))",
     "theorem": "Площадь треугольника через три стороны и полупериметр p = (a+b+c)/2.",
     "svg": draw_triangle,
     "calc": {"vars": [("a", "Сторона a"), ("b", "Сторона b"), ("c", "Сторона c"), ("S", "Площадь S")],
              "solvers": {"S": lambda a, b, c: math.sqrt((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))}}},
    {"section": "Треугольники", "name": "Теорема косинусов",
     "formula": "c² = a² + b² − 2ab·cos(C)",
     "theorem": "Квадрат стороны равен сумме квадратов двух других минус удвоенное произведение на косинус угла между ними.",
     "svg": draw_triangle,
     "calc": {"vars": [("a", "Сторона a"), ("b", "Сторона b"), ("C", "Угол C (°)"), ("c", "Сторона c")],
              "solvers": {"c": lambda a, b, C: math.sqrt(a**2 + b**2 - 2*a*b*cos_d(C)),
                          "C": lambda a, b, c: acos_d((a**2 + b**2 - c**2)/(2*a*b))}}},
    {"section": "Треугольники", "name": "Теорема синусов",
     "formula": "a / sin(A) = 2R",
     "theorem": "Стороны треугольника пропорциональны синусам противолежащих углов. Коэффициент = 2R.",
     "svg": draw_triangle_circle,
     "calc": {"vars": [("a", "Сторона a"), ("A", "Угол A (°)"), ("R", "Радиус R")],
              "solvers": {"a": lambda A, R: 2*R*sin_d(A),
                          "R": lambda a, A: a/(2*sin_d(A)),
                          "A": lambda a, R: asin_d(a/(2*R))}}},
    {"section": "Треугольники", "name": "Теорема Пифагора",
     "formula": "a² + b² = c²",
     "theorem": "В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов.",
     "svg": draw_right_triangle,
     "calc": {"vars": [("a", "Катет a"), ("b", "Катет b"), ("c", "Гипотенуза c")],
              "solvers": {"c": lambda a, b: math.sqrt(a**2 + b**2),
                          "a": lambda b, c: math.sqrt(c**2 - b**2),
                          "b": lambda a, c: math.sqrt(c**2 - a**2)}}},
    {"section": "Треугольники", "name": "Сумма углов треугольника",
     "formula": "A + B + C = 180°",
     "theorem": "Сумма внутренних углов любого треугольника равна 180°.",
     "svg": draw_triangle,
     "calc": {"vars": [("A", "Угол A"), ("B", "Угол B"), ("C", "Угол C")],
              "solvers": {"C": lambda A, B: 180-A-B, "A": lambda B, C: 180-B-C, "B": lambda A, C: 180-A-C}}},

    {"section": "Четырёхугольники", "name": "Площадь параллелограмма",
     "formula": "S = a · h",
     "theorem": "Площадь параллелограмма равна произведению основания на высоту.",
     "svg": draw_parallelogram,
     "calc": {"vars": [("a", "Основание a"), ("h", "Высота h"), ("S", "Площадь S")],
              "solvers": {"S": lambda a, h: a*h, "a": lambda S, h: S/h, "h": lambda S, a: S/a}}},
    {"section": "Четырёхугольники", "name": "Площадь трапеции",
     "formula": "S = ½ · (a + b) · h",
     "theorem": "Площадь трапеции равна произведению полусуммы оснований на высоту.",
     "svg": draw_trapezoid,
     "calc": {"vars": [("a", "Основание a"), ("b", "Основание b"), ("h", "Высота h"), ("S", "Площадь S")],
              "solvers": {"S": lambda a, b, h: 0.5*(a+b)*h, "h": lambda a, b, S: 2*S/(a+b),
                          "a": lambda b, h, S: 2*S/h - b, "b": lambda a, h, S: 2*S/h - a}}},
    {"section": "Четырёхугольники", "name": "Площадь ромба",
     "formula": "S = ½ · d₁ · d₂",
     "theorem": "Площадь ромба равна половине произведения его диагоналей.",
     "svg": draw_rhombus,
     "calc": {"vars": [("d1", "Диагональ d₁"), ("d2", "Диагональ d₂"), ("S", "Площадь S")],
              "solvers": {"S": lambda d1, d2: 0.5*d1*d2, "d1": lambda S, d2: 2*S/d2, "d2": lambda S, d1: 2*S/d1}}},
    {"section": "Четырёхугольники", "name": "Сумма углов n-угольника",
     "formula": "Σ = (n − 2) · 180°",
     "theorem": "Сумма внутренних углов выпуклого n-угольника.",
     "svg": draw_polygon,
     "calc": {"vars": [("n", "Число сторон n"), ("S", "Сумма углов")],
              "solvers": {"S": lambda n: (n-2)*180, "n": lambda S: S/180 + 2}}},

    {"section": "Окружность", "name": "Длина окружности",
     "formula": "C = 2πR",
     "theorem": "Длина окружности прямо пропорциональна её радиусу.",
     "svg": draw_circle,
     "calc": {"vars": [("R", "Радиус R"), ("C", "Длина C")],
              "solvers": {"C": lambda R: 2*math.pi*R, "R": lambda C: C/(2*math.pi)}}},
    {"section": "Окружность", "name": "Площадь круга",
     "formula": "S = πR²",
     "theorem": "Площадь круга равна произведению π на квадрат радиуса.",
     "svg": draw_circle,
     "calc": {"vars": [("R", "Радиус R"), ("S", "Площадь S")],
              "solvers": {"S": lambda R: math.pi*R**2, "R": lambda S: math.sqrt(S/math.pi)}}},
    {"section": "Окружность", "name": "Площадь сектора",
     "formula": "S = (πR² · α) / 360°",
     "theorem": "Площадь сектора пропорциональна его центральному углу α.",
     "svg": draw_sector,
     "calc": {"vars": [("R", "Радиус R"), ("a", "Угол α (°)"), ("S", "Площадь S")],
              "solvers": {"S": lambda R, a: math.pi*R**2*a/360,
                          "R": lambda S, a: math.sqrt(S*360/(math.pi*a)),
                          "a": lambda R, S: S*360/(math.pi*R**2)}}},
    {"section": "Окружность", "name": "Теорема о вписанном угле",
     "formula": "∠впис = ½ · ∠центр",
     "theorem": "Вписанный угол равен половине центрального, опирающегося на ту же дугу.",
     "svg": draw_inscribed_angle,
     "calc": {"vars": [("c", "Центральный угол"), ("i", "Вписанный угол")],
              "solvers": {"i": lambda c: c/2, "c": lambda i: i*2}}},
    {"section": "Окружность", "name": "Теорема о касательной",
     "formula": "MT² = MA · MB",
     "theorem": "Квадрат касательной равен произведению отрезков секущей.",
     "svg": draw_secant,
     "calc": {"vars": [("MT", "Касательная MT"), ("MA", "Отрезок MA"), ("MB", "Отрезок MB")],
              "solvers": {"MT": lambda MA, MB: math.sqrt(MA*MB),
                          "MA": lambda MT, MB: MT**2/MB,
                          "MB": lambda MT, MA: MT**2/MA}}},

    {"section": "Тригонометрия", "name": "Основное тождество",
     "formula": "sin²α + cos²α = 1",
     "theorem": "Для любого угла α сумма квадратов синуса и косинуса равна 1.",
     "svg": draw_unit_circle,
     "calc": {"vars": [("a", "Угол α (°)"), ("sin", "sin α"), ("cos", "cos α")],
              "solvers": {"sin": lambda a: sin_d(a), "cos": lambda a: cos_d(a)}}},
    {"section": "Тригонометрия", "name": "Площадь через синус",
     "formula": "S = ½ · a · b · sin(C)",
     "theorem": "Площадь треугольника через две стороны и угол между ними.",
     "svg": draw_triangle,
     "calc": {"vars": [("a", "Сторона a"), ("b", "Сторона b"), ("C", "Угол C"), ("S", "Площадь S")],
              "solvers": {"S": lambda a, b, C: 0.5*a*b*sin_d(C),
                          "a": lambda b, C, S: 2*S/(b*sin_d(C)),
                          "b": lambda a, C, S: 2*S/(a*sin_d(C)),
                          "C": lambda a, b, S: asin_d(2*S/(a*b))}}},

    {"section": "Стереометрия", "name": "Объём призмы",
     "formula": "V = Sосн · h",
     "theorem": "Объём призмы равен произведению площади основания на высоту.",
     "svg": draw_prism,
     "calc": {"vars": [("S0", "Площадь основания"), ("h", "Высота"), ("V", "Объём V")],
              "solvers": {"V": lambda S0, h: S0*h, "S0": lambda V, h: V/h, "h": lambda S0, V: V/S0}}},
    {"section": "Стереометрия", "name": "Объём пирамиды",
     "formula": "V = ⅓ · Sосн · h",
     "theorem": "Объём пирамиды — треть произведения площади основания на высоту.",
     "svg": draw_pyramid,
     "calc": {"vars": [("S0", "Площадь основания"), ("h", "Высота"), ("V", "Объём V")],
              "solvers": {"V": lambda S0, h: S0*h/3, "S0": lambda V, h: 3*V/h, "h": lambda S0, V: 3*V/S0}}},
    {"section": "Стереометрия", "name": "Объём цилиндра",
     "formula": "V = πR² · h",
     "theorem": "Объём цилиндра — произведение площади основания на высоту.",
     "svg": draw_cylinder,
     "calc": {"vars": [("R", "Радиус R"), ("h", "Высота"), ("V", "Объём V")],
              "solvers": {"V": lambda R, h: math.pi*R**2*h,
                          "R": lambda V, h: math.sqrt(V/(math.pi*h)),
                          "h": lambda R, V: V/(math.pi*R**2)}}},
    {"section": "Стереометрия", "name": "Объём конуса",
     "formula": "V = ⅓ · πR² · h",
     "theorem": "Объём конуса — треть произведения площади основания на высоту.",
     "svg": draw_cone,
     "calc": {"vars": [("R", "Радиус R"), ("h", "Высота"), ("V", "Объём V")],
              "solvers": {"V": lambda R, h: math.pi*R**2*h/3,
                          "R": lambda V, h: math.sqrt(3*V/(math.pi*h)),
                          "h": lambda R, V: 3*V/(math.pi*R**2)}}},
    {"section": "Стереометрия", "name": "Объём шара",
     "formula": "V = 4/3 · πR³",
     "theorem": "Объём шара радиуса R. Площадь сферы S = 4πR².",
     "svg": draw_sphere,
     "calc": {"vars": [("R", "Радиус R"), ("V", "Объём V")],
              "solvers": {"V": lambda R: 4/3*math.pi*R**3,
                          "R": lambda V: (3*V/(4*math.pi))**(1/3)}}},
    {"section": "Стереометрия", "name": "Объём усечённой пирамиды",
     "formula": "V = ⅓ · h · (S₁ + √(S₁·S₂) + S₂)",
     "theorem": "Объём усечённой пирамиды через площади верхнего и нижнего оснований.",
     "svg": draw_frustum,
     "calc": {"vars": [("S1", "Площадь S₁"), ("S2", "Площадь S₂"), ("h", "Высота"), ("V", "Объём V")],
              "solvers": {"V": lambda S1, S2, h: h/3*(S1 + math.sqrt(S1*S2) + S2),
                          "h": lambda S1, S2, V: 3*V/(S1 + math.sqrt(S1*S2) + S2)}}},
]


# ================== ФИЗИКА ==================
G = 10  # ускорение свободного падения (для расчётов)

PHYSICS_TOPICS = [
    # ---------- 7 КЛАСС ----------
    {"section": "7 класс", "name": "Скорость (равномерное движение)",
     "formula": "v = s / t",
     "theorem": "Скорость — путь, пройденный телом за единицу времени. При равномерном движении скорость постоянна.",
     "example": "Автомобиль проехал 150 км за 2 ч. v = 150 / 2 = 75 км/ч.",
     "svg": draw_motion,
     "calc": {"vars": [("s", "Путь s"), ("t", "Время t"), ("v", "Скорость v")],
              "solvers": {"v": lambda s, t: s/t, "s": lambda v, t: v*t, "t": lambda s, v: s/v}}},

    {"section": "7 класс", "name": "Путь при равномерном движении",
     "formula": "s = v · t",
     "theorem": "Путь равен произведению скорости на время.",
     "example": "Поезд идёт 60 км/ч в течение 3 ч. s = 60 · 3 = 180 км.",
     "svg": draw_motion,
     "calc": {"vars": [("v", "Скорость v"), ("t", "Время t"), ("s", "Путь s")],
              "solvers": {"s": lambda v, t: v*t, "v": lambda s, t: s/t, "t": lambda s, v: s/v}}},

    {"section": "7 класс", "name": "Плотность вещества",
     "formula": "ρ = m / V",
     "theorem": "Плотность — масса единицы объёма вещества.",
     "example": "m = 2 кг, V = 0.001 м³ → ρ = 2000 кг/м³.",
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("V", "Объём V"), ("ρ", "Плотность ρ")],
              "solvers": {"ρ": lambda m, V: m/V, "m": lambda ρ, V: ρ*V, "V": lambda m, ρ: m/ρ}}},

    {"section": "7 класс", "name": "Сила тяжести",
     "formula": "F = m · g",
     "theorem": "Сила, с которой Земля притягивает тело. g ≈ 10 Н/кг.",
     "example": "m = 5 кг → F = 5 · 10 = 50 Н.",
     "svg": draw_force,
     "calc": {"vars": [("m", "Масса m"), ("F", "Сила F")],
              "solvers": {"F": lambda m: m*G, "m": lambda F: F/G}}},

    {"section": "7 класс", "name": "Закон Гука (сила упругости)",
     "formula": "F = k · x",
     "theorem": "Сила упругости пропорциональна удлинению пружины. k — жёсткость (Н/м), x — удлинение (м).",
     "example": "k = 200 Н/м, x = 0.05 м → F = 200 · 0.05 = 10 Н.",
     "svg": None,
     "calc": {"vars": [("k", "Жёсткость k"), ("x", "Удлинение x"), ("F", "Сила F")],
              "solvers": {"F": lambda k, x: k*x, "k": lambda F, x: F/x, "x": lambda F, k: F/k}}},

    {"section": "7 класс", "name": "Давление твёрдого тела",
     "formula": "p = F / S",
     "theorem": "Давление — сила, действующая на единицу площади. Измеряется в паскалях (Па).",
     "example": "F = 100 Н, S = 0.5 м² → p = 200 Па.",
     "svg": draw_force,
     "calc": {"vars": [("F", "Сила F"), ("S", "Площадь S"), ("p", "Давление p")],
              "solvers": {"p": lambda F, S: F/S, "F": lambda p, S: p*S, "S": lambda F, p: F/p}}},

    {"section": "7 класс", "name": "Давление жидкости",
     "formula": "p = ρ · g · h",
     "theorem": "Давление на глубине h в жидкости плотностью ρ. g ≈ 10.",
     "example": "ρ = 1000 кг/м³, h = 5 м → p = 50 000 Па.",
     "svg": None,
     "calc": {"vars": [("ρ", "Плотность ρ"), ("h", "Глубина h"), ("p", "Давление p")],
              "solvers": {"p": lambda ρ, h: ρ*G*h, "h": lambda ρ, p: p/(ρ*G), "ρ": lambda h, p: p/(G*h)}}},

    {"section": "7 класс", "name": "Сила Архимеда",
     "formula": "F = ρ · g · V",
     "theorem": "Выталкивающая сила, равная весу вытесненной жидкости.",
     "example": "ρ = 1000 кг/м³, V = 0.002 м³ → F = 20 Н.",
     "svg": None,
     "calc": {"vars": [("ρ", "Плотность ρ"), ("V", "Объём V"), ("F", "Сила F")],
              "solvers": {"F": lambda ρ, V: ρ*G*V, "V": lambda ρ, F: F/(ρ*G), "ρ": lambda V, F: F/(G*V)}}},

    {"section": "7 класс", "name": "Механическая работа",
     "formula": "A = F · s",
     "theorem": "Работа совершается, когда тело перемещается под действием силы. В джоулях (Дж).",
     "example": "F = 20 Н, s = 5 м → A = 100 Дж.",
     "svg": None,
     "calc": {"vars": [("F", "Сила F"), ("s", "Путь s"), ("A", "Работа A")],
              "solvers": {"A": lambda F, s: F*s, "F": lambda A, s: A/s, "s": lambda F, A: A/F}}},

    {"section": "7 класс", "name": "Мощность",
     "formula": "N = A / t",
     "theorem": "Мощность — работа за единицу времени. В ваттах (Вт).",
     "example": "A = 500 Дж, t = 10 с → N = 50 Вт.",
     "svg": None,
     "calc": {"vars": [("A", "Работа A"), ("t", "Время t"), ("N", "Мощность N")],
              "solvers": {"N": lambda A, t: A/t, "A": lambda N, t: N*t, "t": lambda A, N: A/N}}},

    {"section": "7 класс", "name": "Кинетическая энергия",
     "formula": "Ek = m·v² / 2",
     "theorem": "Энергия движения тела. Зависит от массы и квадрата скорости.",
     "example": "m = 2 кг, v = 3 м/с → Ek = 9 Дж.",
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("v", "Скорость v"), ("Ek", "Энергия Ek")],
              "solvers": {"Ek": lambda m, v: m*v*v/2, "m": lambda Ek, v: 2*Ek/(v*v), "v": lambda m, Ek: math.sqrt(2*Ek/m)}}},

    {"section": "7 класс", "name": "Потенциальная энергия",
     "formula": "Ep = m · g · h",
     "theorem": "Энергия тела, поднятого над Землёй.",
     "example": "m = 3 кг, h = 4 м → Ep = 120 Дж.",
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("h", "Высота h"), ("Ep", "Энергия Ep")],
              "solvers": {"Ep": lambda m, h: m*G*h, "m": lambda Ep, h: Ep/(G*h), "h": lambda m, Ep: Ep/(m*G)}}},

    {"section": "7 класс", "name": "Момент силы (правило рычага)",
     "formula": "F₁ · l₁ = F₂ · l₂",
     "theorem": "Рычаг в равновесии, когда момент силы слева равен моменту справа.",
     "example": "F₁ = 10 Н, l₁ = 0.3 м, l₂ = 0.1 м → F₂ = 30 Н.",
     "svg": None,
     "calc": {"vars": [("F1", "F₁"), ("l1", "l₁"), ("F2", "F₂"), ("l2", "l₂")],
              "solvers": {"F2": lambda F1, l1, l2: F1*l1/l2, "F1": lambda F2, l2, l1: F2*l2/l1,
                          "l1": lambda F2, l2, F1: F2*l2/F1, "l2": lambda F1, l1, F2: F1*l1/F2}}},

    # ---------- 8 КЛАСС ----------
    {"section": "8 класс", "name": "Количество теплоты при нагревании",
     "formula": "Q = c · m · Δt",
     "theorem": "Теплота для нагрева тела массой m на Δt градусов. c — удельная теплоёмкость.",
     "example": "c = 4200, m = 2, Δt = 50 → Q = 420 000 Дж.",
     "svg": draw_heat,
     "calc": {"vars": [("c", "Теплоёмкость c"), ("m", "Масса m"), ("dt", "Δ t (°C)"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda c, m, dt: c*m*dt, "m": lambda c, dt, Q: Q/(c*dt),
                          "dt": lambda c, m, Q: Q/(c*m), "c": lambda m, dt, Q: Q/(m*dt)}}},

    {"section": "8 класс", "name": "Теплота плавления",
     "formula": "Q = λ · m",
     "theorem": "Теплота для плавления тела массой m. λ — удельная теплота плавления.",
     "example": "λ = 340 000, m = 0.5 → Q = 170 000 Дж.",
     "svg": None,
     "calc": {"vars": [("lam", "λ"), ("m", "Масса m"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda lam, m: lam*m, "m": lambda lam, Q: Q/lam, "lam": lambda m, Q: Q/m}}},

    {"section": "8 класс", "name": "Закон Ома для участка цепи",
     "formula": "I = U / R",
     "theorem": "Сила тока прямо пропорциональна напряжению и обратно пропорциональна сопротивлению.",
     "example": "U = 12 В, R = 4 Ом → I = 3 А.",
     "svg": draw_circuit,
     "calc": {"vars": [("U", "Напряжение U"), ("R", "Сопротивление R"), ("I", "Сила тока I")],
              "solvers": {"I": lambda U, R: U/R, "U": lambda I, R: I*R, "R": lambda U, I: U/I}}},

    {"section": "8 класс", "name": "Последовательное соединение",
     "formula": "R = R₁ + R₂",
     "theorem": "Сопротивления складываются. Ток одинаков, напряжения складываются.",
     "example": "R1 = 2, R2 = 3 → R = 5 Ом.",
     "svg": draw_circuit,
     "calc": {"vars": [("R1", "R₁"), ("R2", "R₂"), ("R", "R общее")],
              "solvers": {"R": lambda R1, R2: R1+R2, "R1": lambda R, R2: R-R2, "R2": lambda R, R1: R-R1}}},

    {"section": "8 класс", "name": "Параллельное соединение",
     "formula": "1/R = 1/R₁ + 1/R₂",
     "theorem": "Напряжение одинаково, токи складываются, обратные сопротивления складываются.",
     "example": "R1 = 2, R2 = 4 → R ≈ 1.33 Ом.",
     "svg": draw_circuit,
     "calc": {"vars": [("R1", "R₁"), ("R2", "R₂"), ("R", "R общее")],
              "solvers": {"R": lambda R1, R2: (R1*R2)/(R1+R2)}}},

    {"section": "8 класс", "name": "Мощность электрического тока",
     "formula": "P = U · I",
     "theorem": "Мощность тока равна произведению напряжения на силу тока.",
     "example": "U = 220 В, I = 2 А → P = 440 Вт.",
     "svg": draw_circuit,
     "calc": {"vars": [("U", "Напряжение U"), ("I", "Сила тока I"), ("P", "Мощность P")],
              "solvers": {"P": lambda U, I: U*I, "U": lambda P, I: P/I, "I": lambda U, P: P/U}}},

    {"section": "8 класс", "name": "Работа электрического тока",
     "formula": "A = U · I · t",
     "theorem": "Работа тока за время t.",
     "example": "U = 220, I = 0.5, t = 3600 → A = 396 000 Дж.",
     "svg": draw_circuit,
     "calc": {"vars": [("U", "Напряжение U"), ("I", "Ток I"), ("t", "Время t"), ("A", "Работа A")],
              "solvers": {"A": lambda U, I, t: U*I*t, "t": lambda U, I, A: A/(U*I)}}},

    {"section": "8 класс", "name": "Закон Джоуля-Ленца",
     "formula": "Q = I² · R · t",
     "theorem": "Количество теплоты, выделяемое проводником с током.",
     "example": "I = 3, R = 5, t = 10 → Q = 450 Дж.",
     "svg": draw_heat,
     "calc": {"vars": [("I", "Ток I"), ("R", "Сопротивление R"), ("t", "Время t"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda I, R, t: I*I*R*t, "R": lambda I, t, Q: Q/(I*I*t),
                          "t": lambda I, R, Q: Q/(I*I*R)}}},

    # ---------- 9 КЛАСС ----------
    {"section": "9 класс", "name": "Скорость при равноускоренном движении",
     "formula": "v = v₀ + a · t",
     "theorem": "Скорость через время t при начальной скорости v₀ и ускорении a.",
     "example": "v0 = 2, a = 3, t = 4 → v = 14 м/с.",
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("a", "Ускорение a"), ("t", "Время t"), ("v", "Скорость v")],
              "solvers": {"v": lambda v0, a, t: v0 + a*t, "a": lambda v0, t, v: (v-v0)/t,
                          "t": lambda v0, a, v: (v-v0)/a, "v0": lambda a, t, v: v - a*t}}},

    {"section": "9 класс", "name": "Перемещение при равноускоренном движении",
     "formula": "s = v₀ · t + a · t² / 2",
     "theorem": "Путь при равноускоренном движении с начальной скоростью v₀.",
     "example": "v0 = 0, a = 2, t = 5 → s = 25 м.",
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("a", "Ускорение a"), ("t", "Время t"), ("s", "Путь s")],
              "solvers": {"s": lambda v0, a, t: v0*t + a*t*t/2}}},

    {"section": "9 класс", "name": "Второй закон Ньютона",
     "formula": "F = m · a",
     "theorem": "Сила равна произведению массы тела на его ускорение. Основной закон динамики.",
     "example": "m = 4 кг, a = 3 м/с² → F = 12 Н.",
     "svg": draw_force,
     "calc": {"vars": [("m", "Масса m"), ("a", "Ускорение a"), ("F", "Сила F")],
              "solvers": {"F": lambda m, a: m*a, "m": lambda F, a: F/a, "a": lambda m, F: F/m}}},

    {"section": "9 класс", "name": "Импульс тела",
     "formula": "p = m · v",
     "theorem": "Импульс — произведение массы на скорость. Векторная величина.",
     "example": "m = 2 кг, v = 5 м/с → p = 10 кг·м/с.",
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("v", "Скорость v"), ("p", "Импульс p")],
              "solvers": {"p": lambda m, v: m*v, "m": lambda p, v: p/v, "v": lambda m, p: p/m}}},

    {"section": "9 класс", "name": "Свободное падение",
     "formula": "h = g · t² / 2",
     "theorem": "Высота падения без начальной скорости за время t. g ≈ 10.",
     "example": "t = 3 с → h = 45 м.",
     "svg": None,
     "calc": {"vars": [("t", "Время t"), ("h", "Высота h")],
              "solvers": {"h": lambda t: G*t*t/2, "t": lambda h: math.sqrt(2*h/G)}}},

    {"section": "9 класс", "name": "Центростремительное ускорение",
     "formula": "a = v² / R",
     "theorem": "Ускорение тела, движущегося по окружности радиуса R со скоростью v.",
     "example": "v = 4 м/с, R = 2 м → a = 8 м/с².",
     "svg": None,
     "calc": {"vars": [("v", "Скорость v"), ("R", "Радиус R"), ("a", "Ускорение a")],
              "solvers": {"a": lambda v, R: v*v/R, "v": lambda a, R: math.sqrt(a*R), "R": lambda v, a: v*v/a}}},

    {"section": "9 класс", "name": "Период и частота вращения",
     "formula": "T = 1 / ν",
     "theorem": "Период — время одного оборота. Частота — число оборотов за секунду.",
     "example": "ν = 5 Гц → T = 0.2 с.",
     "svg": None,
     "calc": {"vars": [("nu", "Частота ν"), ("T", "Период T")],
              "solvers": {"T": lambda nu: 1/nu, "nu": lambda T: 1/T}}},

    {"section": "9 класс", "name": "Длина волны",
     "formula": "λ = v · T",
     "theorem": "Длина волны — расстояние между соседними гребнями.",
     "example": "v = 340 м/с, T = 0.01 с → λ = 3.4 м.",
     "svg": None,
     "calc": {"vars": [("v", "Скорость v"), ("T", "Период T"), ("lam", "Длина λ")],
              "solvers": {"lam": lambda v, T: v*T, "v": lambda lam, T: lam/T, "T": lambda v, lam: lam/v}}},

    {"section": "9 класс", "name": "Закон всемирного тяготения",
     "formula": "F = G · m₁ · m₂ / r²",
     "theorem": "Сила притяжения двух тел. G ≈ 6.67·10⁻¹¹.",
     "example": "m1 = m2 = 1000 кг, r = 10 м → F ≈ 6.67·10⁻⁷ Н.",
     "svg": None,
     "calc": {"vars": [("m1", "Масса m₁"), ("m2", "Масса m₂"), ("r", "Расстояние r"), ("F", "Сила F")],
              "solvers": {"F": lambda m1, m2, r: 6.67e-11*m1*m2/(r*r)}}},
]


# ================== СТРУКТУРА РАЗДЕЛОВ ==================
# Верхний уровень: два больших раздела
ROOT_SECTIONS = {
    "geom": {"title": "📐 Геометрия", "topics": GEOMETRY_TOPICS},
    "phys": {"title": "⚛️ Физика",     "topics": PHYSICS_TOPICS},
}


def get_subsections(root_key: str) -> dict:
    """Возвращает {подраздел: [(индекс_в_списке, название), ...]}."""
    topics = ROOT_SECTIONS[root_key]["topics"]
    subs: dict[str, list[tuple[int, str]]] = {}
    for i, t in enumerate(topics):
        subs.setdefault(t["section"], []).append((i, t["name"]))
    return subs


def get_topic(root_key: str, idx: int) -> dict:
    return ROOT_SECTIONS[root_key]["topics"][idx]


def search_all(query: str):
    """Ищет во всех разделах. Возвращает [(root_key, idx), ...]."""
    q = query.lower().strip()
    if len(q) < 2:
        return []
    out = []
    for root_key, data in ROOT_SECTIONS.items():
        for i, t in enumerate(data["topics"]):
            haystack = " ".join([
                t.get("name", ""),
                t.get("formula", ""),
                t.get("theorem", ""),
                t.get("example", ""),
                t.get("section", ""),
                " ".join(t.get("keywords", [])) if "keywords" in t else "",
            ]).lower()
            if q in haystack:
                out.append((root_key, i))
    return out
