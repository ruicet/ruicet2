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

# ---------- Физические рисунки ----------
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

def draw_pendulum():
    return svg_wrap('<line x1="200" y1="30" x2="200" y2="60" class="l"/>'
                    '<line x1="200" y1="60" x2="260" y2="200" class="l"/>'
                    '<circle cx="260" cy="205" r="18" class="fill l"/>'
                    '<line x1="200" y1="60" x2="200" y2="205" class="l-dash"/>'
                    '<text x="215" y="135" class="t-yellow">l</text>'
                    '<text x="270" y="230" class="t">m</text>')

def draw_spring():
    return svg_wrap('<line x1="200" y1="30" x2="200" y2="60" class="l"/>'
                    '<path d="M200,60 L180,75 L220,90 L180,105 L220,120 L180,135 L220,150 L200,165" class="l"/>'
                    '<rect x="175" y="165" width="50" height="40" class="fill l"/>'
                    '<text x="235" y="130" class="t-yellow">k</text>'
                    '<text x="235" y="195" class="t">m</text>')

def draw_wave():
    return svg_wrap('<path d="M30,150 Q80,90 130,150 T230,150 T330,150 T370,150" class="l"/>'
                    '<line x1="30" y1="150" x2="370" y2="150" stroke="#4a4a6a" stroke-dasharray="4 4"/>'
                    '<line x1="130" y1="150" x2="230" y2="150" class="l-red"/>'
                    '<text x="160" y="175" class="t-red">λ</text>')

def draw_lens():
    return svg_wrap('<ellipse cx="200" cy="150" rx="15" ry="90" class="l fill"/>'
                    '<line x1="20" y1="150" x2="380" y2="150" stroke="#4a4a6a" stroke-dasharray="4 4"/>'
                    '<line x1="200" y1="40" x2="200" y2="260" stroke="#4a4a6a" stroke-dasharray="4 4"/>'
                    '<circle cx="200" cy="150" r="4" fill="#facc15"/>'
                    '<circle cx="280" cy="150" r="4" fill="#facc15"/>'
                    '<circle cx="120" cy="150" r="4" fill="#facc15"/>'
                    '<text x="275" y="135" class="t-yellow">F</text>'
                    '<text x="110" y="135" class="t-yellow">F</text>')

def draw_magnet():
    return svg_wrap('<rect x="130" y="100" width="140" height="40" fill="#e94560" stroke="#4ade80" stroke-width="2"/>'
                    '<rect x="130" y="140" width="140" height="40" fill="#4a90e2" stroke="#4ade80" stroke-width="2"/>'
                    '<text x="90" y="125" class="t">N</text>'
                    '<text x="90" y="165" class="t">S</text>'
                    '<path d="M270,120 Q330,120 330,150 Q330,180 270,180" class="l-yellow"/>'
                    '<polygon points="270,110 260,120 280,120" fill="#facc15"/>')

def draw_circle_motion():
    return svg_wrap('<circle cx="200" cy="150" r="90" class="l-dash"/>'
                    '<circle cx="290" cy="150" r="10" fill="#4ade80"/>'
                    '<line x1="200" y1="150" x2="290" y2="150" class="l-red"/>'
                    '<text x="235" y="140" class="t-red">R</text>'
                    '<polygon points="280,130 300,150 280,170" fill="#facc15"/>'
                    '<text x="305" y="145" class="t-yellow">v</text>')

def draw_two_blocks():
    return svg_wrap('<rect x="80" y="140" width="80" height="60" class="fill l"/>'
                    '<rect x="240" y="140" width="80" height="60" class="fill l"/>'
                    '<line x1="160" y1="170" x2="240" y2="170" class="l-red"/>'
                    '<polygon points="230,160 250,170 230,180" fill="#e94560"/>'
                    '<polygon points="170,160 150,170 170,180" fill="#e94560"/>'
                    '<text x="100" y="175" class="t">m₁</text>'
                    '<text x="260" y="175" class="t">m₂</text>')

def draw_slope():
    return svg_wrap('<polygon points="60,240 340,240 340,100" class="fill l"/>'
                    '<rect x="140" y="180" width="50" height="30" fill="#e94560" stroke="#4ade80" stroke-width="2" transform="rotate(-30, 165, 195)"/>'
                    '<text x="150" y="170" class="t-yellow">μ</text>')

def draw_coordinate():
    return svg_wrap('<line x1="40" y1="240" x2="370" y2="240" stroke="#4ade80" stroke-width="2"/>'
                    '<polygon points="370,232 380,240 370,248" fill="#4ade80"/>'
                    '<circle cx="100" cy="240" r="5" fill="#e94560"/>'
                    '<circle cx="280" cy="240" r="5" fill="#e94560"/>'
                    '<text x="85" y="260" class="t-red">x₀</text>'
                    '<text x="265" y="260" class="t-red">x</text>'
                    '<text x="350" y="265" class="t-yellow">x</text>')


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
    # ========== 7 КЛАСС ==========
    {"section": "7 класс", "name": "Скорость (равномерное движение)",
     "formula": "v = s / t",
     "theorem": "Скорость — путь, пройденный телом за единицу времени. При равномерном движении скорость постоянна.",
     "example": "Автомобиль проехал 150 км за 2 ч. v = 150 / 2 = 75 км/ч.",
     "keywords": ["скорость", "движение", "равномерное", "v", "s", "t"],
     "svg": draw_motion,
     "calc": {"vars": [("s", "Путь s"), ("t", "Время t"), ("v", "Скорость v")],
              "solvers": {"v": lambda s, t: s/t, "s": lambda v, t: v*t, "t": lambda s, v: s/v}}},

    {"section": "7 класс", "name": "Путь при равномерном движении",
     "formula": "s = v · t",
     "theorem": "Путь равен произведению скорости на время движения.",
     "example": "Поезд идёт 60 км/ч в течение 3 ч. s = 60 · 3 = 180 км.",
     "keywords": ["путь", "расстояние", "s", "v", "t"],
     "svg": draw_motion,
     "calc": {"vars": [("v", "Скорость v"), ("t", "Время t"), ("s", "Путь s")],
              "solvers": {"s": lambda v, t: v*t, "v": lambda s, t: s/t, "t": lambda s, v: s/v}}},

    {"section": "7 класс", "name": "Плотность вещества",
     "formula": "ρ = m / V",
     "theorem": "Плотность — масса единицы объёма вещества. Единица измерения — кг/м³.",
     "example": "m = 2 кг, V = 0.001 м³ → ρ = 2000 кг/м³.",
     "keywords": ["плотность", "масса", "объём", "ρ"],
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("V", "Объём V"), ("ρ", "Плотность ρ")],
              "solvers": {"ρ": lambda m, V: m/V, "m": lambda ρ, V: ρ*V, "V": lambda m, ρ: m/ρ}}},

    {"section": "7 класс", "name": "Сила тяжести",
     "formula": "F = m · g",
     "theorem": "Сила, с которой Земля притягивает тело. g ≈ 9.8 Н/кг (для расчётов 10).",
     "example": "m = 5 кг → F = 5 · 10 = 50 Н.",
     "keywords": ["сила тяжести", "вес", "F", "m", "g"],
     "svg": draw_force,
     "calc": {"vars": [("m", "Масса m"), ("F", "Сила F")],
              "solvers": {"F": lambda m: m*G, "m": lambda F: F/G}}},

    {"section": "7 класс", "name": "Закон Гука",
     "formula": "F = k · x",
     "theorem": "Сила упругости пропорциональна удлинению пружины. k — жёсткость (Н/м).",
     "example": "k = 200 Н/м, x = 0.05 м → F = 10 Н.",
     "keywords": ["сила упругости", "закон гука", "пружина", "жёсткость", "удлинение"],
     "svg": None,
     "calc": {"vars": [("k", "Жёсткость k"), ("x", "Удлинение x"), ("F", "Сила F")],
              "solvers": {"F": lambda k, x: k*x, "k": lambda F, x: F/x, "x": lambda F, k: F/k}}},

    {"section": "7 класс", "name": "Давление твёрдого тела",
     "formula": "p = F / S",
     "theorem": "Давление — сила, действующая на единицу площади поверхности. В паскалях (Па).",
     "example": "F = 100 Н, S = 0.5 м² → p = 200 Па.",
     "keywords": ["давление", "площадь", "p", "F", "S"],
     "svg": draw_force,
     "calc": {"vars": [("F", "Сила F"), ("S", "Площадь S"), ("p", "Давление p")],
              "solvers": {"p": lambda F, S: F/S, "F": lambda p, S: p*S, "S": lambda F, p: F/p}}},

    {"section": "7 класс", "name": "Давление жидкости (гидростатическое)",
     "formula": "p = ρ · g · h",
     "theorem": "Давление на глубине h в жидкости плотностью ρ. Зависит только от глубины и плотности.",
     "example": "ρ = 1000 кг/м³, h = 5 м → p = 50 000 Па.",
     "keywords": ["давление жидкости", "гидростатика", "глубина"],
     "svg": None,
     "calc": {"vars": [("ρ", "Плотность ρ"), ("h", "Глубина h"), ("p", "Давление p")],
              "solvers": {"p": lambda ρ, h: ρ*G*h, "h": lambda ρ, p: p/(ρ*G), "ρ": lambda h, p: p/(G*h)}}},

    {"section": "7 класс", "name": "Сила Архимеда",
     "formula": "F = ρ · g · V",
     "theorem": "Выталкивающая сила равна весу вытесненной жидкости или газа.",
     "example": "ρ = 1000 кг/м³, V = 0.002 м³ → F = 20 Н.",
     "keywords": ["архимед", "выталкивающая", "плавает", "погружен"],
     "svg": None,
     "calc": {"vars": [("ρ", "Плотность ρ"), ("V", "Объём V"), ("F", "Сила F")],
              "solvers": {"F": lambda ρ, V: ρ*G*V, "V": lambda ρ, F: F/(ρ*G), "ρ": lambda V, F: F/(G*V)}}},

    {"section": "7 класс", "name": "Механическая работа",
     "formula": "A = F · s",
     "theorem": "Работа совершается при перемещении тела под действием силы. В джоулях (Дж).",
     "example": "F = 20 Н, s = 5 м → A = 100 Дж.",
     "keywords": ["работа", "механическая", "A", "F", "s"],
     "svg": None,
     "calc": {"vars": [("F", "Сила F"), ("s", "Путь s"), ("A", "Работа A")],
              "solvers": {"A": lambda F, s: F*s, "F": lambda A, s: A/s, "s": lambda F, A: A/F}}},

    {"section": "7 класс", "name": "Мощность",
     "formula": "N = A / t",
     "theorem": "Мощность — работа за единицу времени. В ваттах (Вт).",
     "example": "A = 500 Дж, t = 10 с → N = 50 Вт.",
     "keywords": ["мощность", "ватт", "N", "A", "t"],
     "svg": None,
     "calc": {"vars": [("A", "Работа A"), ("t", "Время t"), ("N", "Мощность N")],
              "solvers": {"N": lambda A, t: A/t, "A": lambda N, t: N*t, "t": lambda A, N: A/N}}},

    {"section": "7 класс", "name": "КПД механизма",
     "formula": "η = (Aполезная / Aзатраченная) · 100%",
     "theorem": "КПД показывает, какая часть затраченной работы пошла на пользу.",
     "example": "80 Дж полезная, 100 Дж затраченная → η = 80%.",
     "keywords": ["кпд", "коэффициент полезного действия", "η"],
     "svg": None,
     "calc": {"vars": [("Ap", "Полезная работа"), ("Az", "Затраченная работа"), ("η", "КПД (%)")],
              "solvers": {"η": lambda Ap, Az: Ap/Az*100, "Ap": lambda Az, η: Az*η/100}}},

    {"section": "7 класс", "name": "Кинетическая энергия",
     "formula": "Ek = m·v² / 2",
     "theorem": "Энергия движения тела. Зависит от массы и квадрата скорости.",
     "example": "m = 2 кг, v = 3 м/с → Ek = 9 Дж.",
     "keywords": ["кинетическая энергия", "энергия движения"],
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("v", "Скорость v"), ("Ek", "Энергия Ek")],
              "solvers": {"Ek": lambda m, v: m*v*v/2, "m": lambda Ek, v: 2*Ek/(v*v), "v": lambda m, Ek: math.sqrt(2*Ek/m)}}},

    {"section": "7 класс", "name": "Потенциальная энергия",
     "formula": "Ep = m · g · h",
     "theorem": "Энергия тела, поднятого над Землёй. Зависит от массы и высоты.",
     "example": "m = 3 кг, h = 4 м → Ep = 120 Дж.",
     "keywords": ["потенциальная энергия", "высота"],
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("h", "Высота h"), ("Ep", "Энергия Ep")],
              "solvers": {"Ep": lambda m, h: m*G*h, "m": lambda Ep, h: Ep/(G*h), "h": lambda m, Ep: Ep/(m*G)}}},

    {"section": "7 класс", "name": "Момент силы (правило рычага)",
     "formula": "F₁ · l₁ = F₂ · l₂",
     "theorem": "Рычаг в равновесии, когда момент силы слева равен моменту справа.",
     "example": "F₁ = 10 Н, l₁ = 0.3 м, l₂ = 0.1 м → F₂ = 30 Н.",
     "keywords": ["рычаг", "момент силы", "плечо", "равновесие"],
     "svg": None,
     "calc": {"vars": [("F1", "F₁"), ("l1", "l₁"), ("F2", "F₂"), ("l2", "l₂")],
              "solvers": {"F2": lambda F1, l1, l2: F1*l1/l2, "F1": lambda F2, l2, l1: F2*l2/l1,
                          "l1": lambda F2, l2, F1: F2*l2/F1, "l2": lambda F1, l1, F2: F1*l1/F2}}},

    # ========== 8 КЛАСС ==========
    {"section": "8 класс", "name": "Количество теплоты при нагревании",
     "formula": "Q = c · m · Δt",
     "theorem": "Теплота для нагрева тела массой m на Δt градусов. c — удельная теплоёмкость.",
     "example": "c = 4200, m = 2, Δt = 50 → Q = 420 000 Дж.",
     "keywords": ["количество теплоты", "нагревание", "теплоёмкость", "градус"],
     "svg": draw_heat,
     "calc": {"vars": [("c", "Теплоёмкость c"), ("m", "Масса m"), ("dt", "Δ t (°C)"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda c, m, dt: c*m*dt, "m": lambda c, dt, Q: Q/(c*dt),
                          "dt": lambda c, m, Q: Q/(c*m), "c": lambda m, dt, Q: Q/(m*dt)}}},

    {"section": "8 класс", "name": "Теплота плавления",
     "formula": "Q = λ · m",
     "theorem": "Теплота для плавления тела массой m. λ — удельная теплота плавления.",
     "example": "λ = 340 000, m = 0.5 → Q = 170 000 Дж.",
     "keywords": ["плавление", "лёд", "лед", "расплавить"],
     "svg": None,
     "calc": {"vars": [("lam", "λ"), ("m", "Масса m"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda lam, m: lam*m, "m": lambda lam, Q: Q/lam, "lam": lambda m, Q: Q/m}}},

    {"section": "8 класс", "name": "Теплота парообразования",
     "formula": "Q = L · m",
     "theorem": "Теплота для превращения жидкости в пар. L — удельная теплота парообразования.",
     "example": "L = 2 300 000, m = 0.2 → Q = 460 000 Дж.",
     "keywords": ["парообразование", "испарение", "пар"],
     "svg": None,
     "calc": {"vars": [("L", "Удельная теплота L"), ("m", "Масса m"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda L, m: L*m, "m": lambda L, Q: Q/L, "L": lambda m, Q: Q/m}}},

    {"section": "8 класс", "name": "Теплота сгорания топлива",
     "formula": "Q = q · m",
     "theorem": "Теплота при сгорании топлива. q — удельная теплота сгорания.",
     "example": "q = 46 000 000, m = 3 → Q = 138 000 000 Дж.",
     "keywords": ["сгорание", "топливо", "бензин"],
     "svg": draw_heat,
     "calc": {"vars": [("q", "q топлива"), ("m", "Масса m"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda q, m: q*m, "m": lambda q, Q: Q/q, "q": lambda m, Q: Q/m}}},

    {"section": "8 класс", "name": "Закон Ома для участка цепи",
     "formula": "I = U / R",
     "theorem": "Сила тока прямо пропорциональна напряжению и обратно пропорциональна сопротивлению.",
     "example": "U = 12 В, R = 4 Ом → I = 3 А.",
     "keywords": ["закон ома", "ток", "напряжение", "сопротивление"],
     "svg": draw_circuit,
     "calc": {"vars": [("U", "Напряжение U"), ("R", "Сопротивление R"), ("I", "Сила тока I")],
              "solvers": {"I": lambda U, R: U/R, "U": lambda I, R: I*R, "R": lambda U, I: U/I}}},

    {"section": "8 класс", "name": "Сопротивление проводника",
     "formula": "R = ρ · l / S",
     "theorem": "Сопротивление зависит от удельного сопротивления, длины и площади поперечного сечения.",
     "example": "ρ = 0.017, l = 100, S = 2 → R = 0.85 Ом.",
     "keywords": ["сопротивление проводника", "удельное сопротивление"],
     "svg": None,
     "calc": {"vars": [("rho", "ρ (Ом·мм²/м)"), ("l", "Длина l"), ("S", "Площадь S"), ("R", "Сопротивление R")],
              "solvers": {"R": lambda rho, l, S: rho*l/S, "l": lambda rho, S, R: R*S/rho,
                          "S": lambda rho, l, R: rho*l/R}}},

    {"section": "8 класс", "name": "Последовательное соединение",
     "formula": "R = R₁ + R₂",
     "theorem": "Сопротивления складываются. Ток одинаков, напряжения складываются.",
     "example": "R1 = 2, R2 = 3 → R = 5 Ом.",
     "keywords": ["последовательное соединение", "цепь"],
     "svg": draw_circuit,
     "calc": {"vars": [("R1", "R₁"), ("R2", "R₂"), ("R", "R общее")],
              "solvers": {"R": lambda R1, R2: R1+R2, "R1": lambda R, R2: R-R2, "R2": lambda R, R1: R-R1}}},

    {"section": "8 класс", "name": "Параллельное соединение",
     "formula": "1/R = 1/R₁ + 1/R₂",
     "theorem": "Напряжение одинаково, токи складываются, обратные сопротивления складываются.",
     "example": "R1 = 2, R2 = 4 → R ≈ 1.33 Ом.",
     "keywords": ["параллельное соединение", "цепь"],
     "svg": draw_circuit,
     "calc": {"vars": [("R1", "R₁"), ("R2", "R₂"), ("R", "R общее")],
              "solvers": {"R": lambda R1, R2: (R1*R2)/(R1+R2)}}},

    {"section": "8 класс", "name": "Мощность электрического тока",
     "formula": "P = U · I",
     "theorem": "Мощность тока равна произведению напряжения на силу тока.",
     "example": "U = 220 В, I = 2 А → P = 440 Вт.",
     "keywords": ["мощность тока", "мощность электрического"],
     "svg": draw_circuit,
     "calc": {"vars": [("U", "Напряжение U"), ("I", "Сила тока I"), ("P", "Мощность P")],
              "solvers": {"P": lambda U, I: U*I, "U": lambda P, I: P/I, "I": lambda U, P: P/U}}},

    {"section": "8 класс", "name": "Работа электрического тока",
     "formula": "A = U · I · t",
     "theorem": "Работа тока за время t.",
     "example": "U = 220, I = 0.5, t = 3600 → A = 396 000 Дж.",
     "keywords": ["работа тока", "работа электрического"],
     "svg": draw_circuit,
     "calc": {"vars": [("U", "Напряжение U"), ("I", "Ток I"), ("t", "Время t"), ("A", "Работа A")],
              "solvers": {"A": lambda U, I, t: U*I*t, "t": lambda U, I, A: A/(U*I)}}},

    {"section": "8 класс", "name": "Закон Джоуля-Ленца",
     "formula": "Q = I² · R · t",
     "theorem": "Количество теплоты, выделяемое проводником с током.",
     "example": "I = 3, R = 5, t = 10 → Q = 450 Дж.",
     "keywords": ["джоуль", "ленц", "проводник", "теплота тока"],
     "svg": draw_heat,
     "calc": {"vars": [("I", "Ток I"), ("R", "Сопротивление R"), ("t", "Время t"), ("Q", "Теплота Q")],
              "solvers": {"Q": lambda I, R, t: I*I*R*t, "R": lambda I, t, Q: Q/(I*I*t),
                          "t": lambda I, R, Q: Q/(I*I*R)}}},

    # ========== 9 КЛАСС: КИНЕМАТИКА ==========
    {"section": "9 класс · Кинематика", "name": "Ускорение",
     "formula": "a = (v − v₀) / t",
     "theorem": "Ускорение — изменение скорости за единицу времени. Показывает, на сколько меняется скорость за 1 секунду.",
     "example": "v₀ = 2 м/с, v = 14 м/с, t = 4 с → a = (14−2)/4 = 3 м/с².",
     "keywords": ["ускорение", "a", "изменение скорости"],
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("v", "Скорость v"), ("t", "Время t"), ("a", "Ускорение a")],
              "solvers": {"a": lambda v0, v, t: (v-v0)/t, "v": lambda v0, a, t: v0+a*t,
                          "t": lambda v0, v, a: (v-v0)/a, "v0": lambda v, a, t: v - a*t}}},

    {"section": "9 класс · Кинематика", "name": "Уравнение координаты (равномерное)",
     "formula": "x = x₀ + v · t",
     "theorem": "Координата тела при равномерном движении. x₀ — начальная координата.",
     "example": "x₀ = 5 м, v = 3 м/с, t = 4 с → x = 5 + 3·4 = 17 м.",
     "keywords": ["уравнение координаты", "координата", "x", "x0"],
     "svg": draw_coordinate,
     "calc": {"vars": [("x0", "x₀"), ("v", "Скорость v"), ("t", "Время t"), ("x", "Координата x")],
              "solvers": {"x": lambda x0, v, t: x0+v*t, "x0": lambda v, t, x: x - v*t}}},

    {"section": "9 класс · Кинематика", "name": "Уравнение координаты (равноускоренное)",
     "formula": "x = x₀ + v₀·t + a·t²/2",
     "theorem": "Координата при равноускоренном движении с начальной скоростью v₀ и ускорением a.",
     "example": "x₀=0, v₀=2, a=3, t=4 → x = 0 + 8 + 24 = 32 м.",
     "keywords": ["уравнение координаты", "равноускоренное", "координата"],
     "svg": draw_coordinate,
     "calc": {"vars": [("x0", "x₀"), ("v0", "v₀"), ("a", "a"), ("t", "Время t"), ("x", "x")],
              "solvers": {"x": lambda x0, v0, a, t: x0+v0*t+a*t*t/2}}},

    {"section": "9 класс · Кинематика", "name": "Перемещение без времени",
     "formula": "s = (v² − v₀²) / (2a)",
     "theorem": "Формула перемещения при равноускоренном движении, если время неизвестно.",
     "example": "v₀=0, v=10, a=2 → s = 100/4 = 25 м.",
     "keywords": ["перемещение без времени", "s", "без времени"],
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("v", "Скорость v"), ("a", "a"), ("s", "Путь s")],
              "solvers": {"s": lambda v0, v, a: (v*v - v0*v0)/(2*a),
                          "a": lambda v0, v, s: (v*v - v0*v0)/(2*s),
                          "v": lambda v0, a, s: math.sqrt(v0*v0 + 2*a*s)}}},

    {"section": "9 класс · Кинематика", "name": "Средняя скорость",
     "formula": "vср = s_весь / t_весь",
     "theorem": "Средняя скорость — весь путь, делённый на всё время движения.",
     "example": "Путь 100 км за 2 ч → vср = 50 км/ч.",
     "keywords": ["средняя скорость", "vср"],
     "svg": draw_motion,
     "calc": {"vars": [("s", "Весь путь s"), ("t", "Всё время t"), ("v", "vср")],
              "solvers": {"v": lambda s, t: s/t, "s": lambda v, t: v*t, "t": lambda s, v: s/v}}},

    {"section": "9 класс · Кинематика", "name": "Свободное падение",
     "formula": "h = g · t² / 2,  v = g · t",
     "theorem": "Высота падения без начальной скорости за время t и скорость в момент падения. g ≈ 10.",
     "example": "t = 3 с → h = 45 м, v = 30 м/с.",
     "keywords": ["свободное падение", "падает", "высота"],
     "svg": None,
     "calc": {"vars": [("t", "Время t"), ("h", "Высота h")],
              "solvers": {"h": lambda t: G*t*t/2, "t": lambda h: math.sqrt(2*h/G)}}},

    # ========== 9 КЛАСС: ДИНАМИКА ==========
    {"section": "9 класс · Динамика", "name": "Второй закон Ньютона",
     "formula": "F = m · a",
     "theorem": "Сила равна произведению массы тела на его ускорение. Основной закон динамики.",
     "example": "m = 4 кг, a = 3 м/с² → F = 12 Н.",
     "keywords": ["второй закон ньютона", "ньютон", "сила", "ускорение"],
     "svg": draw_force,
     "calc": {"vars": [("m", "Масса m"), ("a", "Ускорение a"), ("F", "Сила F")],
              "solvers": {"F": lambda m, a: m*a, "m": lambda F, a: F/a, "a": lambda m, F: F/m}}},

    {"section": "9 класс · Динамика", "name": "Третий закон Ньютона",
     "formula": "F₁ = − F₂",
     "theorem": "Силы взаимодействия двух тел равны по модулю и противоположны по направлению.",
     "example": "Ты давишь на стол с силой 50 Н — стол давит на тебя с силой 50 Н.",
     "keywords": ["третий закон ньютона", "взаимодействие"],
     "svg": draw_two_blocks,
     "calc": None},

    {"section": "9 класс · Динамика", "name": "Импульс тела",
     "formula": "p = m · v",
     "theorem": "Импульс — произведение массы на скорость. Векторная величина, единица — кг·м/с.",
     "example": "m = 2 кг, v = 5 м/с → p = 10 кг·м/с.",
     "keywords": ["импульс", "количество движения"],
     "svg": None,
     "calc": {"vars": [("m", "Масса m"), ("v", "Скорость v"), ("p", "Импульс p")],
              "solvers": {"p": lambda m, v: m*v, "m": lambda p, v: p/v, "v": lambda m, p: p/m}}},

    {"section": "9 класс · Динамика", "name": "Закон сохранения импульса",
     "formula": "m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'",
     "theorem": "Суммарный импульс замкнутой системы сохраняется при любых взаимодействиях.",
     "example": "Тележка 2 кг (3 м/с) догоняет 1 кг (1 м/с). После сцепки v' = 7/3 ≈ 2.33 м/с.",
     "keywords": ["закон сохранения импульса", "сохранение импульса"],
     "svg": draw_two_blocks,
     "calc": {"vars": [("m1", "m₁"), ("v1", "v₁"), ("m2", "m₂"), ("v2", "v₂"), ("v", "v' общая")],
              "solvers": {"v": lambda m1, v1, m2, v2: (m1*v1 + m2*v2)/(m1+m2)}}},

    {"section": "9 класс · Динамика", "name": "Сила трения",
     "formula": "Fтр = μ · N = μ · m · g",
     "theorem": "Сила трения пропорциональна силе нормального давления. μ — коэффициент трения.",
     "example": "μ = 0.3, m = 5 кг → Fтр = 0.3·50 = 15 Н.",
     "keywords": ["сила трения", "трение", "коэффициент трения"],
     "svg": draw_slope,
     "calc": {"vars": [("μ", "Коэффициент μ"), ("m", "Масса m"), ("F", "Сила трения F")],
              "solvers": {"F": lambda μ, m: μ*m*G, "m": lambda μ, F: F/(μ*G), "μ": lambda m, F: F/(m*G)}}},

    {"section": "9 класс · Динамика", "name": "Закон всемирного тяготения",
     "formula": "F = G · m₁ · m₂ / r²",
     "theorem": "Сила притяжения двух тел. G ≈ 6.67·10⁻¹¹ Н·м²/кг².",
     "example": "m1 = m2 = 1000 кг, r = 10 м → F ≈ 6.67·10⁻⁷ Н.",
     "keywords": ["всемирное тяготение", "гравитация", "притяжение"],
     "svg": draw_two_blocks,
     "calc": {"vars": [("m1", "Масса m₁"), ("m2", "Масса m₂"), ("r", "Расстояние r"), ("F", "Сила F")],
              "solvers": {"F": lambda m1, m2, r: 6.67e-11*m1*m2/(r*r)}}},

    {"section": "9 класс · Динамика", "name": "Первая космическая скорость",
     "formula": "v = √(g · R)",
     "theorem": "Скорость для выхода на круговую орбиту у поверхности планеты.",
     "example": "g = 10, R = 6.4·10⁶ → v ≈ 8000 м/с = 8 км/с.",
     "keywords": ["космическая скорость", "орбита", "спутник"],
     "svg": None,
     "calc": {"vars": [("g", "g (м/с²)"), ("R", "Радиус R (м)"), ("v", "Скорость v (м/с)")],
              "solvers": {"v": lambda g, R: math.sqrt(g*R), "R": lambda g, v: v*v/g, "g": lambda R, v: v*v/R}}},

    # ========== 9 КЛАСС: ДВИЖЕНИЕ ПО ОКРУЖНОСТИ ==========
    {"section": "9 класс · Окружность", "name": "Центростремительное ускорение",
     "formula": "a = v² / R",
     "theorem": "Ускорение тела, движущегося по окружности радиусом R со скоростью v.",
     "example": "v = 4 м/с, R = 2 м → a = 8 м/с².",
     "keywords": ["центростремительное ускорение", "по окружности"],
     "svg": draw_circle_motion,
     "calc": {"vars": [("v", "Скорость v"), ("R", "Радиус R"), ("a", "Ускорение a")],
              "solvers": {"a": lambda v, R: v*v/R, "v": lambda a, R: math.sqrt(a*R), "R": lambda v, a: v*v/a}}},

    {"section": "9 класс · Окружность", "name": "Период и частота вращения",
     "formula": "T = 1 / ν,  ν = N / t",
     "theorem": "Период — время одного оборота. Частота — число оборотов за секунду.",
     "example": "ν = 5 Гц → T = 0.2 с.",
     "keywords": ["период", "частота", "оборот"],
     "svg": draw_circle_motion,
     "calc": {"vars": [("nu", "Частота ν (Гц)"), ("T", "Период T (с)")],
              "solvers": {"T": lambda nu: 1/nu, "nu": lambda T: 1/T}}},

    {"section": "9 класс · Окружность", "name": "Линейная и угловая скорость",
     "formula": "v = ω · R,  ω = 2π / T",
     "theorem": "Связь линейной скорости v с угловой ω и радиусом R. ω в рад/с.",
     "example": "ω = 3 рад/с, R = 2 м → v = 6 м/с.",
     "keywords": ["линейная скорость", "угловая скорость", "омега"],
     "svg": draw_circle_motion,
     "calc": {"vars": [("w", "ω (рад/с)"), ("R", "Радиус R"), ("v", "Скорость v")],
              "solvers": {"v": lambda w, R: w*R, "w": lambda v, R: v/R, "R": lambda w, v: v/w}}},

    # ========== 9 КЛАСС: КОЛЕБАНИЯ И ВОЛНЫ ==========
    {"section": "9 класс · Колебания", "name": "Период математического маятника",
     "formula": "T = 2π · √(l / g)",
     "theorem": "Период колебаний маятника длиной l. Не зависит от массы.",
     "example": "l = 1 м, g = 10 → T ≈ 1.99 с.",
     "keywords": ["математический маятник", "маятник", "период маятника"],
     "svg": draw_pendulum,
     "calc": {"vars": [("l", "Длина l (м)"), ("T", "Период T (с)")],
              "solvers": {"T": lambda l: 2*math.pi*math.sqrt(l/G), "l": lambda T: T*T*G/(4*math.pi*math.pi)}}},

    {"section": "9 класс · Колебания", "name": "Период пружинного маятника",
     "formula": "T = 2π · √(m / k)",
     "theorem": "Период колебаний груза на пружине жёсткостью k.",
     "example": "m = 1 кг, k = 100 Н/м → T ≈ 0.63 с.",
     "keywords": ["пружинный маятник", "пружина", "период пружины"],
     "svg": draw_spring,
     "calc": {"vars": [("m", "Масса m (кг)"), ("k", "Жёсткость k (Н/м)"), ("T", "Период T (с)")],
              "solvers": {"T": lambda m, k: 2*math.pi*math.sqrt(m/k),
                          "m": lambda k, T: k*T*T/(4*math.pi*math.pi),
                          "k": lambda m, T: 4*math.pi*math.pi*m/(T*T)}}},

    {"section": "9 класс · Колебания", "name": "Длина волны",
     "formula": "λ = v · T = v / ν",
     "theorem": "Длина волны — расстояние между соседними гребнями. Равна скорость × период.",
     "example": "v = 340 м/с, T = 0.01 с → λ = 3.4 м.",
     "keywords": ["длина волны", "волна", "лямбда"],
     "svg": draw_wave,
     "calc": {"vars": [("v", "Скорость v"), ("T", "Период T"), ("lam", "Длина λ")],
              "solvers": {"lam": lambda v, T: v*T, "v": lambda lam, T: lam/T, "T": lambda v, lam: lam/v}}},

    {"section": "9 класс · Колебания", "name": "Скорость волны",
     "formula": "v = λ · ν",
     "theorem": "Скорость распространения волны через длину волны и частоту.",
     "example": "λ = 3.4 м, ν = 100 Гц → v = 340 м/с.",
     "keywords": ["скорость волны", "распространение"],
     "svg": draw_wave,
     "calc": {"vars": [("lam", "Длина λ (м)"), ("nu", "Частота ν (Гц)"), ("v", "Скорость v (м/с)")],
              "solvers": {"v": lambda lam, nu: lam*nu, "lam": lambda nu, v: v/nu, "nu": lambda lam, v: v/lam}}},

    # ========== 9 КЛАСС: ЭЛЕКТРОМАГНИТНЫЕ ЯВЛЕНИЯ ==========
    {"section": "9 класс · Магнетизм", "name": "Магнитный поток",
     "formula": "Φ = B · S · cos(α)",
     "theorem": "Поток магнитной индукции через площадку S. Φ измеряется в веберах (Вб).",
     "example": "B = 0.5 Тл, S = 0.2 м², α = 0° → Φ = 0.1 Вб.",
     "keywords": ["магнитный поток", "вебер", "поток"],
     "svg": draw_magnet,
     "calc": {"vars": [("B", "Индукция B (Тл)"), ("S", "Площадь S (м²)"), ("alpha", "Угол α (°)"), ("Phi", "Поток Φ (Вб)")],
              "solvers": {"Phi": lambda B, S, alpha: B*S*cos_d(alpha),
                          "B": lambda S, alpha, Phi: Phi/(S*cos_d(alpha)),
                          "S": lambda B, alpha, Phi: Phi/(B*cos_d(alpha))}}},

    {"section": "9 класс · Магнетизм", "name": "Закон электромагнитной индукции",
     "formula": "ε = − ΔΦ / Δt",
     "theorem": "ЭДС индукции пропорциональна скорости изменения магнитного потока.",
     "example": "ΔΦ = 0.2 Вб, Δt = 0.1 с → ε = 2 В.",
     "keywords": ["эдс индукции", "электромагнитная индукция", "индукция"],
     "svg": draw_magnet,
     "calc": {"vars": [("dPhi", "ΔΦ (Вб)"), ("dt", "Δt (с)"), ("e", "ε (В)")],
              "solvers": {"e": lambda dPhi, dt: dPhi/dt, "dPhi": lambda e, dt: e*dt, "dt": lambda dPhi, e: dPhi/e}}},

    # ========== 9 КЛАСС: ОПТИКА ==========
    {"section": "9 класс · Оптика", "name": "Оптическая сила линзы",
     "formula": "D = 1 / F",
     "theorem": "Оптическая сила линзы — величина, обратная фокусному расстоянию. В диоптриях (дптр).",
     "example": "F = 0.5 м → D = 2 дптр.",
     "keywords": ["оптическая сила", "линза", "диоптрия"],
     "svg": draw_lens,
     "calc": {"vars": [("F", "Фокус F (м)"), ("D", "Оптическая сила D (дптр)")],
              "solvers": {"D": lambda F: 1/F, "F": lambda D: 1/D}}},

    {"section": "9 класс · Оптика", "name": "Формула тонкой линзы",
     "formula": "1/F = 1/d + 1/f",
     "theorem": "Связь фокусного расстояния F с расстоянием до предмета d и до изображения f.",
     "example": "d = 30 см, f = 60 см → F = 20 см.",
     "keywords": ["тонкая линза", "формула линзы", "изображение"],
     "svg": draw_lens,
     "calc": {"vars": [("d", "d (см)"), ("f", "f (см)"), ("F", "F (см)")],
              "solvers": {"F": lambda d, f: (d*f)/(d+f),
                          "d": lambda f, F: (f*F)/(f - F),
                          "f": lambda d, F: (d*F)/(d - F)}}},

    {"section": "9 класс · Оптика", "name": "Закон преломления света",
     "formula": "sin(α) / sin(β) = n",
     "theorem": "Отношение синуса угла падения к синусу угла преломления равно показателю преломления.",
     "example": "α = 30°, n = 1.5 → β ≈ 19.5°.",
     "keywords": ["преломление", "показатель преломления", "закон преломления"],
     "svg": draw_lens,
     "calc": {"vars": [("alpha", "Угол α (°)"), ("n", "n"), ("beta", "Угол β (°)")],
              "solvers": {"beta": lambda alpha, n: asin_d(sin_d(alpha)/n),
                          "alpha": lambda beta, n: asin_d(n*sin_d(beta)),
                          "n": lambda alpha, beta: sin_d(alpha)/sin_d(beta)}}},
]


# ================== СТРУКТУРА РАЗДЕЛОВ ==================
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
                " ".join(t.get("keywords", [])),
            ]).lower()
            if q in haystack:
                out.append((root_key, i))
    return out
