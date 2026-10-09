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
         preserveAspectRatio="xMidYMid meet"
         style="width:100%; height:100%;">
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
    return svg_wrap('''
        <polygon points="60,240 340,240 140,60" class="l fill"/>
        <text x="45" y="260" class="t">A</text>
        <text x="345" y="260" class="t">B</text>
        <text x="130" y="50" class="t">C</text>
    ''')


def draw_right_triangle():
    return svg_wrap('''
        <polygon points="60,240 340,240 60,60" class="l fill"/>
        <rect x="60" y="220" width="20" height="20" fill="none" stroke="#e94560" stroke-width="2"/>
        <text x="45" y="260" class="t">A</text>
        <text x="345" y="260" class="t">B</text>
        <text x="40" y="55" class="t">C</text>
        <text x="180" y="265" class="t-yellow">a</text>
        <text x="25" y="155" class="t-yellow">b</text>
        <text x="180" y="140" class="t-red">c</text>
    ''')


def draw_triangle_height():
    return svg_wrap('''
        <polygon points="60,240 340,240 260,60" class="l fill"/>
        <line x1="260" y1="60" x2="260" y2="240" class="l-red"/>
        <rect x="240" y="220" width="20" height="20" fill="none" stroke="#e94560" stroke-width="1.5"/>
        <text x="45" y="260" class="t">A</text>
        <text x="345" y="260" class="t">B</text>
        <text x="265" y="50" class="t">C</text>
        <text x="235" y="260" class="t-red">H</text>
        <text x="270" y="155" class="t-red">h</text>
    ''')


def draw_triangle_circle():
    return svg_wrap('''
        <circle cx="200" cy="150" r="110" class="l-dash"/>
        <polygon points="200,40 105,205 295,205" class="l fill"/>
        <text x="200" y="30" class="t">A</text>
        <text x="85" y="220" class="t">B</text>
        <text x="300" y="220" class="t">C</text>
    ''')


def draw_parallelogram():
    return svg_wrap('''
        <polygon points="60,240 280,240 340,60 120,60" class="l fill"/>
        <line x1="120" y1="60" x2="120" y2="240" class="l-red"/>
        <text x="45" y="260" class="t">A</text>
        <text x="285" y="260" class="t">B</text>
        <text x="345" y="55" class="t">C</text>
        <text x="105" y="55" class="t">D</text>
        <text x="130" y="155" class="t-red">h</text>
    ''')


def draw_trapezoid():
    return svg_wrap('''
        <polygon points="50,240 350,240 270,60 130,60" class="l fill"/>
        <line x1="130" y1="60" x2="130" y2="240" class="l-red"/>
        <text x="35" y="260" class="t">A</text>
        <text x="355" y="260" class="t">B</text>
        <text x="275" y="55" class="t">C</text>
        <text x="115" y="55" class="t">D</text>
        <text x="140" y="155" class="t-red">h</text>
    ''')


def draw_rhombus():
    return svg_wrap('''
        <polygon points="200,40 330,150 200,260 70,150" class="l fill"/>
        <line x1="200" y1="40" x2="200" y2="260" class="l-red"/>
        <line x1="330" y1="150" x2="70" y2="150" class="l-red"/>
        <text x="190" y="30" class="t">A</text>
        <text x="340" y="155" class="t">B</text>
        <text x="190" y="280" class="t">C</text>
        <text x="40" y="155" class="t">D</text>
        <text x="210" y="90" class="t-red">d₁</text>
        <text x="230" y="170" class="t-red">d₂</text>
    ''')


def draw_polygon():
    return svg_wrap('''
        <polygon points="200,40 320,100 320,210 200,270 80,210 80,100" class="l fill"/>
    ''')


def draw_circle():
    return svg_wrap('''
        <circle cx="200" cy="150" r="105" class="l fill"/>
        <line x1="200" y1="150" x2="305" y2="150" class="l-red"/>
        <circle cx="200" cy="150" r="4" fill="#e94560"/>
        <text x="245" y="140" class="t-red">R</text>
    ''')


def draw_sector():
    return svg_wrap('''
        <path d="M200,150 L305,150 A105,105 0 0,0 252,60 Z" class="l fill"/>
        <circle cx="200" cy="150" r="105" class="l-dash"/>
        <text x="235" y="125" class="t-red">α</text>
    ''')


def draw_inscribed_angle():
    return svg_wrap('''
        <circle cx="200" cy="150" r="105" class="l"/>
        <line x1="200" y1="150" x2="95" y2="150" class="l-yellow"/>
        <line x1="200" y1="150" x2="252" y2="240" class="l-yellow"/>
        <line x1="120" y1="90" x2="95" y2="150" class="l-red"/>
        <line x1="120" y1="90" x2="252" y2="240" class="l-red"/>
        <circle cx="95" cy="150" r="4" fill="white"/>
        <circle cx="252" cy="240" r="4" fill="white"/>
        <circle cx="120" cy="90" r="4" fill="white"/>
        <circle cx="200" cy="150" r="4" fill="#facc15"/>
        <text x="75" y="145" class="t">A</text>
        <text x="260" y="255" class="t">B</text>
        <text x="110" y="80" class="t">C</text>
        <text x="205" y="140" class="t-yellow">O</text>
    ''')


def draw_secant():
    return svg_wrap('''
        <circle cx="250" cy="135" r="65" class="l"/>
        <line x1="60" y1="210" x2="200" y2="90" class="l-red"/>
        <line x1="60" y1="210" x2="185" y2="135" class="l-yellow"/>
        <line x1="185" y1="135" x2="315" y2="135" class="l-yellow"/>
        <circle cx="60" cy="210" r="5" fill="white"/>
        <circle cx="200" cy="90" r="4" fill="#e94560"/>
        <text x="40" y="225" class="t">M</text>
        <text x="205" y="85" class="t-red">T</text>
    ''')


def draw_unit_circle():
    return svg_wrap('''
        <line x1="60" y1="150" x2="340" y2="150" stroke="#4a4a6a" stroke-width="1"/>
        <line x1="200" y1="30" x2="200" y2="270" stroke="#4a4a6a" stroke-width="1"/>
        <circle cx="200" cy="150" r="105" class="l"/>
        <line x1="200" y1="150" x2="280" y2="82" class="l-red"/>
        <line x1="280" y1="82" x2="280" y2="150" class="l-yellow"/>
        <line x1="200" y1="150" x2="280" y2="150" stroke="#a78bfa" stroke-width="2.5"/>
        <text x="288" y="115" class="t-yellow">sin</text>
        <text x="230" y="168" style="fill:#a78bfa; font-family:'Cambria Math'; font-size:14px; font-weight:bold;">cos</text>
        <text x="222" y="130" class="t-red">α</text>
    ''')


def draw_prism():
    return svg_wrap('''
        <polygon points="120,90 260,90 300,130 160,130" class="l fill"/>
        <polygon points="120,170 260,170 300,210 160,210" class="l fill"/>
        <line x1="120" y1="90" x2="120" y2="170" class="l"/>
        <line x1="260" y1="90" x2="260" y2="170" class="l"/>
        <line x1="300" y1="130" x2="300" y2="210" class="l"/>
        <line x1="160" y1="130" x2="160" y2="210" class="l"/>
    ''')


def draw_pyramid():
    return svg_wrap('''
        <polygon points="80,200 220,240 330,180 190,140" class="l fill"/>
        <line x1="80" y1="200" x2="200" y2="60" class="l"/>
        <line x1="220" y1="240" x2="200" y2="60" class="l"/>
        <line x1="330" y1="180" x2="200" y2="60" class="l"/>
        <line x1="190" y1="140" x2="200" y2="60" class="l"/>
        <line x1="200" y1="60" x2="200" y2="180" class="l-red"/>
        <circle cx="200" cy="60" r="4" fill="#4ade80"/>
    ''')


def draw_cylinder():
    return svg_wrap('''
        <ellipse cx="200" cy="80" rx="70" ry="20" class="l fill"/>
        <ellipse cx="200" cy="220" rx="70" ry="20" class="l fill"/>
        <line x1="130" y1="80" x2="130" y2="220" class="l"/>
        <line x1="270" y1="80" x2="270" y2="220" class="l"/>
        <line x1="200" y1="80" x2="200" y2="220" class="l-red"/>
        <text x="210" y="155" class="t-red">h</text>
    ''')


def draw_cone():
    return svg_wrap('''
        <ellipse cx="200" cy="220" rx="80" ry="22" class="l fill"/>
        <line x1="120" y1="220" x2="200" y2="60" class="l"/>
        <line x1="280" y1="220" x2="200" y2="60" class="l"/>
        <line x1="200" y1="60" x2="200" y2="220" class="l-red"/>
        <circle cx="200" cy="60" r="4" fill="#4ade80"/>
        <text x="210" y="150" class="t-red">h</text>
    ''')


def draw_sphere():
    return svg_wrap('''
        <circle cx="200" cy="150" r="105" class="l fill"/>
        <ellipse cx="200" cy="150" rx="105" ry="30" fill="none" stroke="#7a7a9a" stroke-width="1" stroke-dasharray="4 4"/>
        <line x1="200" y1="150" x2="290" y2="100" class="l-red"/>
        <circle cx="200" cy="150" r="4" fill="#e94560"/>
        <text x="240" y="115" class="t-red">R</text>
    ''')


def draw_frustum():
    return svg_wrap('''
        <polygon points="140,90 260,90 290,120 170,120" class="l fill"/>
        <polygon points="80,170 220,220 330,180 180,140" class="l fill"/>
        <line x1="140" y1="90" x2="80" y2="170" class="l"/>
        <line x1="260" y1="90" x2="220" y2="220" class="l"/>
        <line x1="290" y1="120" x2="330" y2="180" class="l"/>
        <line x1="170" y1="120" x2="180" y2="140" class="l"/>
    ''')


# ================== ДАННЫЕ ==================
TOPICS = [
    # ---------- ТРЕУГОЛЬНИКИ ----------
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

    # ---------- ЧЕТЫРЁХУГОЛЬНИКИ ----------
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

    # ---------- ОКРУЖНОСТЬ ----------
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

    # ---------- ТРИГОНОМЕТРИЯ ----------
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

    # ---------- СТЕРЕОМЕТРИЯ ----------
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
