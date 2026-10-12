import math


# ================== УГЛЫ ==================
def sin_d(x): return math.sin(math.radians(x))
def cos_d(x): return math.cos(math.radians(x))
def asin_d(x): return math.degrees(math.asin(x))
def acos_d(x): return math.degrees(math.acos(x))


# ================== SVG ==================
def svg_wrap(inner):
    return f'''<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg"
        preserveAspectRatio="xMidYMid meet" style="width:100%;height:100%;">
        <style>
        .l{{stroke:#4ade80;stroke-width:2.5;fill:none;stroke-linejoin:round}}
        .l-red{{stroke:#e94560;stroke-width:2.5;fill:none}}
        .l-yellow{{stroke:#facc15;stroke-width:2.5;fill:none}}
        .l-dash{{stroke:#7a7a9a;stroke-width:1.5;fill:none;stroke-dasharray:5 5}}
        .fill{{fill:#0f3460}}
        .t{{fill:#c8c8d8;font-family:'Cambria Math',serif;font-size:16px;font-weight:bold}}
        .t-red{{fill:#e94560;font-family:'Cambria Math',serif;font-size:14px;font-weight:bold}}
        .t-yellow{{fill:#facc15;font-family:'Cambria Math',serif;font-size:14px;font-weight:bold}}
        </style>{inner}</svg>'''

def draw_triangle():
    return svg_wrap('<polygon points="60,240 340,240 140,60" class="l fill"/>'
                    '<text x="45" y="260" class="t">A</text><text x="345" y="260" class="t">B</text>'
                    '<text x="130" y="50" class="t">C</text>')

def draw_right_triangle():
    return svg_wrap('<polygon points="60,240 340,240 60,60" class="l fill"/>'
                    '<rect x="60" y="220" width="20" height="20" fill="none" stroke="#e94560" stroke-width="2"/>'
                    '<text x="45" y="260" class="t">A</text><text x="345" y="260" class="t">B</text>'
                    '<text x="40" y="55" class="t">C</text>'
                    '<text x="180" y="265" class="t-yellow">a</text>'
                    '<text x="25" y="155" class="t-yellow">b</text>'
                    '<text x="180" y="140" class="t-red">c</text>')

def draw_triangle_height():
    return svg_wrap('<polygon points="60,240 340,240 260,60" class="l fill"/>'
                    '<line x1="260" y1="60" x2="260" y2="240" class="l-red"/>'
                    '<text x="45" y="260" class="t">A</text><text x="345" y="260" class="t">B</text>'
                    '<text x="265" y="50" class="t">C</text>'
                    '<text x="270" y="155" class="t-red">h</text>')

def draw_triangle_circle():
    return svg_wrap('<circle cx="200" cy="150" r="110" class="l-dash"/>'
                    '<polygon points="200,40 105,205 295,205" class="l fill"/>'
                    '<text x="200" y="30" class="t">A</text><text x="85" y="220" class="t">B</text>'
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
                    '<line x1="120" y1="90" x2="252" y2="240" class="l-red"/>')

def draw_secant():
    return svg_wrap('<circle cx="250" cy="135" r="65" class="l"/>'
                    '<line x1="60" y1="210" x2="200" y2="90" class="l-red"/>'
                    '<line x1="60" y1="210" x2="315" y2="135" class="l-yellow"/>')

def draw_unit_circle():
    return svg_wrap('<line x1="60" y1="150" x2="340" y2="150" stroke="#4a4a6a"/>'
                    '<line x1="200" y1="30" x2="200" y2="270" stroke="#4a4a6a"/>'
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
                    '<circle cx="240" cy="200" r="15" fill="none" stroke="#e94560" stroke-width="2"/>')

def draw_heat():
    return svg_wrap('<rect x="140" y="140" width="120" height="100" class="fill l"/>'
                    '<path d="M160,130 Q170,100 180,130 Q190,100 200,130 Q210,100 220,130" class="l-red"/>'
                    '<text x="190" y="270" class="t-yellow">Q</text>')

def draw_pendulum():
    return svg_wrap('<line x1="200" y1="30" x2="200" y2="60" class="l"/>'
                    '<line x1="200" y1="60" x2="260" y2="200" class="l"/>'
                    '<circle cx="260" cy="205" r="18" class="fill l"/>'
                    '<line x1="200" y1="60" x2="200" y2="205" class="l-dash"/>'
                    '<text x="215" y="135" class="t-yellow">l</text>')

def draw_spring():
    return svg_wrap('<line x1="200" y1="30" x2="200" y2="60" class="l"/>'
                    '<path d="M200,60 L180,75 L220,90 L180,105 L220,120 L180,135 L220,150 L200,165" class="l"/>'
                    '<rect x="175" y="165" width="50" height="40" class="fill l"/>'
                    '<text x="235" y="130" class="t-yellow">k</text>')

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
                    '<circle cx="120" cy="150" r="4" fill="#facc15"/>')

def draw_magnet():
    return svg_wrap('<rect x="130" y="100" width="140" height="40" fill="#e94560" stroke="#4ade80" stroke-width="2"/>'
                    '<rect x="130" y="140" width="140" height="40" fill="#4a90e2" stroke="#4ade80" stroke-width="2"/>'
                    '<text x="90" y="125" class="t">N</text>'
                    '<text x="90" y="165" class="t">S</text>')

def draw_circle_motion():
    return svg_wrap('<circle cx="200" cy="150" r="90" class="l-dash"/>'
                    '<circle cx="290" cy="150" r="10" fill="#4ade80"/>'
                    '<line x1="200" y1="150" x2="290" y2="150" class="l-red"/>'
                    '<text x="235" y="140" class="t-red">R</text>')

def draw_two_blocks():
    return svg_wrap('<rect x="80" y="140" width="80" height="60" class="fill l"/>'
                    '<rect x="240" y="140" width="80" height="60" class="fill l"/>'
                    '<line x1="160" y1="170" x2="240" y2="170" class="l-red"/>')

def draw_slope():
    return svg_wrap('<polygon points="60,240 340,240 340,100" class="fill l"/>'
                    '<rect x="140" y="180" width="50" height="30" fill="#e94560" stroke="#4ade80" stroke-width="2"/>')

def draw_coordinate():
    return svg_wrap('<line x1="40" y1="240" x2="370" y2="240" stroke="#4ade80" stroke-width="2"/>'
                    '<polygon points="370,232 380,240 370,248" fill="#4ade80"/>'
                    '<circle cx="100" cy="240" r="5" fill="#e94560"/>'
                    '<circle cx="280" cy="240" r="5" fill="#e94560"/>'
                    '<text x="85" y="260" class="t-red">x₀</text>'
                    '<text x="265" y="260" class="t-red">x</text>')


# ================== ГЕОМЕТРИЯ ==================
GEOMETRY_TOPICS = [
    {"section": "Треугольники", "name": "Площадь треугольника",
     "formula": "S = ½ · a · h",
     "theorem": "Площадь треугольника равна половине произведения основания на высоту.",
     "example": "a = 6, h = 4 → S = 12.",
     "keywords": ["площадь треугольника", "треугольник"],
     "variants": [
         ("S", "Площадь", "S = ½ · a · h"),
         ("a", "Основание", "a = 2S / h"),
         ("h", "Высота", "h = 2S / a"),
     ],
     "svg": draw_triangle_height,
     "calc": {"vars": [("a", "Основание a"), ("h", "Высота h"), ("S", "Площадь S")],
              "solvers": {"S": lambda a, h: 0.5*a*h, "a": lambda S, h: 2*S/h, "h": lambda S, a: 2*S/a}}},

    {"section": "Треугольники", "name": "Формула Герона",
     "formula": "S = √(p(p−a)(p−b)(p−c))",
     "theorem": "Площадь через три стороны. p — полупериметр.",
     "example": "a=3, b=4, c=5 → S = 6.",
     "keywords": ["герон", "полупериметр"],
     "variants": [
         ("S", "Площадь", "S = √(p(p−a)(p−b)(p−c))"),
         ("p", "Полупериметр", "p = (a + b + c) / 2"),
     ],
     "svg": draw_triangle,
     "calc": {"vars": [("a", "a"), ("b", "b"), ("c", "c"), ("S", "S")],
              "solvers": {"S": lambda a, b, c: math.sqrt((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))}}},

    {"section": "Треугольники", "name": "Теорема косинусов",
     "formula": "c² = a² + b² − 2ab·cos(C)",
     "theorem": "Квадрат стороны через две другие и угол между ними.",
     "example": "a=3, b=4, C=90° → c = 5.",
     "keywords": ["косинусов", "теорема косинусов"],
     "variants": [
         ("c", "Сторона c", "c = √(a² + b² − 2ab·cos C)"),
         ("C", "Угол C", "C = arccos((a² + b² − c²) / (2ab))"),
         ("cos C", "Косинус", "cos C = (a² + b² − c²) / (2ab)"),
     ],
     "svg": draw_triangle,
     "calc": {"vars": [("a", "a"), ("b", "b"), ("C", "Угол C (°)"), ("c", "c")],
              "solvers": {"c": lambda a, b, C: math.sqrt(a**2 + b**2 - 2*a*b*cos_d(C)),
                          "C": lambda a, b, c: acos_d((a**2 + b**2 - c**2)/(2*a*b))}}},

    {"section": "Треугольники", "name": "Теорема синусов",
     "formula": "a / sin A = b / sin B = c / sin C = 2R",
     "theorem": "Стороны пропорциональны синусам противолежащих углов.",
     "example": "a=5, A=30° → R = 5.",
     "keywords": ["синусов", "теорема синусов"],
     "variants": [
         ("a", "Сторона a", "a = 2R · sin A"),
         ("R", "Радиус R", "R = a / (2 sin A)"),
         ("A", "Угол A", "A = arcsin(a / 2R)"),
     ],
     "svg": draw_triangle_circle,
     "calc": {"vars": [("a", "a"), ("A", "Угол A (°)"), ("R", "Радиус R")],
              "solvers": {"a": lambda A, R: 2*R*sin_d(A),
                          "R": lambda a, A: a/(2*sin_d(A)),
                          "A": lambda a, R: asin_d(a/(2*R))}}},

    {"section": "Треугольники", "name": "Теорема Пифагора",
     "formula": "a² + b² = c²",
     "theorem": "В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов.",
     "example": "a=3, b=4 → c = 5.",
     "keywords": ["пифагор", "катет", "гипотенуза"],
     "variants": [
         ("c", "Гипотенуза", "c = √(a² + b²)"),
         ("a", "Катет a", "a = √(c² − b²)"),
         ("b", "Катет b", "b = √(c² − a²)"),
     ],
     "svg": draw_right_triangle,
     "calc": {"vars": [("a", "Катет a"), ("b", "Катет b"), ("c", "Гипотенуза c")],
              "solvers": {"c": lambda a, b: math.sqrt(a**2 + b**2),
                          "a": lambda b, c: math.sqrt(c**2 - b**2),
                          "b": lambda a, c: math.sqrt(c**2 - a**2)}}},

    {"section": "Треугольники", "name": "Сумма углов треугольника",
     "formula": "A + B + C = 180°",
     "theorem": "Сумма внутренних углов любого треугольника равна 180°.",
     "example": "A=60, B=70 → C = 50°.",
     "keywords": ["сумма углов треугольника"],
     "variants": [
         ("C", "Угол C", "C = 180° − A − B"),
         ("A", "Угол A", "A = 180° − B − C"),
         ("B", "Угол B", "B = 180° − A − C"),
     ],
     "svg": draw_triangle,
     "calc": {"vars": [("A", "A"), ("B", "B"), ("C", "C")],
              "solvers": {"C": lambda A, B: 180-A-B, "A": lambda B, C: 180-B-C, "B": lambda A, C: 180-A-C}}},

    {"section": "Четырёхугольники", "name": "Площадь параллелограмма",
     "formula": "S = a · h",
     "theorem": "Площадь параллелограмма равна произведению основания на высоту.",
     "example": "a=5, h=3 → S = 15.",
     "keywords": ["параллелограмм"],
     "variants": [
         ("S", "Площадь", "S = a · h"),
         ("a", "Основание", "a = S / h"),
         ("h", "Высота", "h = S / a"),
     ],
     "svg": draw_parallelogram,
     "calc": {"vars": [("a", "Основание a"), ("h", "Высота h"), ("S", "S")],
              "solvers": {"S": lambda a, h: a*h, "a": lambda S, h: S/h, "h": lambda S, a: S/a}}},

    {"section": "Четырёхугольники", "name": "Площадь трапеции",
     "formula": "S = ½ · (a + b) · h",
     "theorem": "Площадь трапеции — полусумма оснований на высоту.",
     "example": "a=4, b=6, h=3 → S = 15.",
     "keywords": ["трапеция"],
     "variants": [
         ("S", "Площадь", "S = ½(a + b) · h"),
         ("h", "Высота", "h = 2S / (a + b)"),
         ("a", "Основание a", "a = 2S/h − b"),
         ("b", "Основание b", "b = 2S/h − a"),
     ],
     "svg": draw_trapezoid,
     "calc": {"vars": [("a", "a"), ("b", "b"), ("h", "h"), ("S", "S")],
              "solvers": {"S": lambda a, b, h: 0.5*(a+b)*h, "h": lambda a, b, S: 2*S/(a+b),
                          "a": lambda b, h, S: 2*S/h - b, "b": lambda a, h, S: 2*S/h - a}}},

    {"section": "Четырёхугольники", "name": "Площадь ромба",
     "formula": "S = ½ · d₁ · d₂",
     "theorem": "Площадь ромба — половина произведения диагоналей.",
     "example": "d₁=4, d₂=6 → S = 12.",
     "keywords": ["ромб"],
     "variants": [
         ("S", "Площадь", "S = ½ · d₁ · d₂"),
         ("d₁", "Диагональ d₁", "d₁ = 2S / d₂"),
         ("d₂", "Диагональ d₂", "d₂ = 2S / d₁"),
     ],
     "svg": draw_rhombus,
     "calc": {"vars": [("d1", "d₁"), ("d2", "d₂"), ("S", "S")],
              "solvers": {"S": lambda d1, d2: 0.5*d1*d2, "d1": lambda S, d2: 2*S/d2, "d2": lambda S, d1: 2*S/d1}}},

    {"section": "Четырёхугольники", "name": "Сумма углов n-угольника",
     "formula": "Σ = (n − 2) · 180°",
     "theorem": "Сумма внутренних углов выпуклого n-угольника.",
     "example": "n=5 → Σ = 540°.",
     "keywords": ["сумма углов", "n-угольник"],
     "variants": [
         ("S", "Сумма углов", "S = (n − 2) · 180°"),
         ("n", "Число сторон", "n = S/180° + 2"),
     ],
     "svg": draw_polygon,
     "calc": {"vars": [("n", "n"), ("S", "Сумма")],
              "solvers": {"S": lambda n: (n-2)*180, "n": lambda S: S/180 + 2}}},

    {"section": "Окружность", "name": "Длина окружности",
     "formula": "C = 2πR",
     "theorem": "Длина окружности прямо пропорциональна радиусу.",
     "example": "R=5 → C ≈ 31.42.",
     "keywords": ["длина окружности", "окружность"],
     "variants": [
         ("C", "Длина", "C = 2πR"),
         ("R", "Радиус", "R = C / (2π)"),
     ],
     "svg": draw_circle,
     "calc": {"vars": [("R", "R"), ("C", "C")],
              "solvers": {"C": lambda R: 2*math.pi*R, "R": lambda C: C/(2*math.pi)}}},

    {"section": "Окружность", "name": "Площадь круга",
     "formula": "S = πR²",
     "theorem": "Площадь круга равна πR².",
     "example": "R=3 → S ≈ 28.27.",
     "keywords": ["площадь круга", "круг"],
     "variants": [
         ("S", "Площадь", "S = πR²"),
         ("R", "Радиус", "R = √(S / π)"),
     ],
     "svg": draw_circle,
     "calc": {"vars": [("R", "R"), ("S", "S")],
              "solvers": {"S": lambda R: math.pi*R**2, "R": lambda S: math.sqrt(S/math.pi)}}},

    {"section": "Окружность", "name": "Площадь сектора",
     "formula": "S = (πR² · α) / 360°",
     "theorem": "Площадь сектора пропорциональна центральному углу α.",
     "example": "R=6, α=60° → S ≈ 18.85.",
     "keywords": ["сектор", "площадь сектора"],
     "variants": [
         ("S", "Площадь", "S = πR²·α/360°"),
         ("R", "Радиус", "R = √(360°S / πα)"),
         ("α", "Угол α", "α = 360°S / (πR²)"),
     ],
     "svg": draw_sector,
     "calc": {"vars": [("R", "R"), ("a", "α (°)"), ("S", "S")],
              "solvers": {"S": lambda R, a: math.pi*R**2*a/360,
                          "R": lambda S, a: math.sqrt(S*360/(math.pi*a)),
                          "a": lambda R, S: S*360/(math.pi*R**2)}}},

    {"section": "Окружность", "name": "Теорема о вписанном угле",
     "formula": "∠впис = ½ · ∠центр",
     "theorem": "Вписанный угол равен половине центрального.",
     "example": "∠центр=80° → ∠впис = 40°.",
     "keywords": ["вписанный угол", "центральный угол"],
     "variants": [
         ("i", "Вписанный", "∠впис = ½ · ∠центр"),
         ("c", "Центральный", "∠центр = 2 · ∠впис"),
     ],
     "svg": draw_inscribed_angle,
     "calc": {"vars": [("c", "Центральный"), ("i", "Вписанный")],
              "solvers": {"i": lambda c: c/2, "c": lambda i: i*2}}},

    {"section": "Окружность", "name": "Теорема о касательной",
     "formula": "MT² = MA · MB",
     "theorem": "Квадрат касательной равен произведению отрезков секущей.",
     "example": "MA=2, MB=8 → MT = 4.",
     "keywords": ["касательная", "секущая"],
     "variants": [
         ("MT", "Касательная", "MT = √(MA · MB)"),
         ("MA", "Отрезок MA", "MA = MT² / MB"),
         ("MB", "Отрезок MB", "MB = MT² / MA"),
     ],
     "svg": draw_secant,
     "calc": {"vars": [("MT", "MT"), ("MA", "MA"), ("MB", "MB")],
              "solvers": {"MT": lambda MA, MB: math.sqrt(MA*MB),
                          "MA": lambda MT, MB: MT**2/MB,
                          "MB": lambda MT, MA: MT**2/MA}}},

    {"section": "Тригонометрия", "name": "Основное тождество",
     "formula": "sin²α + cos²α = 1",
     "theorem": "Сумма квадратов синуса и косинуса равна 1.",
     "example": "α=30° → sin α = 0.5, cos α ≈ 0.866.",
     "keywords": ["основное тождество", "синус косинус"],
     "variants": [
         ("sin", "sin α", "sin α = √(1 − cos²α)"),
         ("cos", "cos α", "cos α = √(1 − sin²α)"),
     ],
     "svg": draw_unit_circle,
     "calc": {"vars": [("a", "α (°)"), ("sin", "sin α"), ("cos", "cos α")],
              "solvers": {"sin": lambda a: sin_d(a), "cos": lambda a: cos_d(a)}}},

    {"section": "Тригонометрия", "name": "Площадь через синус",
     "formula": "S = ½ · a · b · sin C",
     "theorem": "Площадь через две стороны и угол между ними.",
     "example": "a=3, b=4, C=30° → S = 3.",
     "keywords": ["площадь через синус"],
     "variants": [
         ("S", "Площадь", "S = ½ · a · b · sin C"),
         ("a", "Сторона a", "a = 2S / (b sin C)"),
         ("b", "Сторона b", "b = 2S / (a sin C)"),
         ("C", "Угол C", "C = arcsin(2S / ab)"),
     ],
     "svg": draw_triangle,
     "calc": {"vars": [("a", "a"), ("b", "b"), ("C", "C"), ("S", "S")],
              "solvers": {"S": lambda a, b, C: 0.5*a*b*sin_d(C),
                          "a": lambda b, C, S: 2*S/(b*sin_d(C)),
                          "b": lambda a, C, S: 2*S/(a*sin_d(C)),
                          "C": lambda a, b, S: asin_d(2*S/(a*b))}}},

    {"section": "Стереометрия", "name": "Объём призмы",
     "formula": "V = Sосн · h",
     "theorem": "Объём призмы — площадь основания на высоту.",
     "example": "S=10, h=5 → V = 50.",
     "keywords": ["призма"],
     "variants": [
         ("V", "Объём", "V = Sосн · h"),
         ("S0", "Основание", "Sосн = V / h"),
         ("h", "Высота", "h = V / Sосн"),
     ],
     "svg": draw_prism,
     "calc": {"vars": [("S0", "Sосн"), ("h", "h"), ("V", "V")],
              "solvers": {"V": lambda S0, h: S0*h, "S0": lambda V, h: V/h, "h": lambda S0, V: V/S0}}},

    {"section": "Стереометрия", "name": "Объём пирамиды",
     "formula": "V = ⅓ · Sосн · h",
     "theorem": "Объём пирамиды — треть площади основания на высоту.",
     "example": "S=9, h=4 → V = 12.",
     "keywords": ["пирамида"],
     "variants": [
         ("V", "Объём", "V = ⅓ · Sосн · h"),
         ("S0", "Основание", "Sосн = 3V / h"),
         ("h", "Высота", "h = 3V / Sосн"),
     ],
     "svg": draw_pyramid,
     "calc": {"vars": [("S0", "Sосн"), ("h", "h"), ("V", "V")],
              "solvers": {"V": lambda S0, h: S0*h/3, "S0": lambda V, h: 3*V/h, "h": lambda S0, V: 3*V/S0}}},

    {"section": "Стереометрия", "name": "Объём цилиндра",
     "formula": "V = πR² · h",
     "theorem": "Объём цилиндра — площадь основания на высоту.",
     "example": "R=2, h=5 → V ≈ 62.83.",
     "keywords": ["цилиндр"],
     "variants": [
         ("V", "Объём", "V = πR² · h"),
         ("R", "Радиус", "R = √(V / πh)"),
         ("h", "Высота", "h = V / (πR²)"),
     ],
     "svg": draw_cylinder,
     "calc": {"vars": [("R", "R"), ("h", "h"), ("V", "V")],
              "solvers": {"V": lambda R, h: math.pi*R**2*h,
                          "R": lambda V, h: math.sqrt(V/(math.pi*h)),
                          "h": lambda R, V: V/(math.pi*R**2)}}},

    {"section": "Стереометрия", "name": "Объём конуса",
     "formula": "V = ⅓ · πR² · h",
     "theorem": "Объём конуса — треть площади основания на высоту.",
     "example": "R=3, h=4 → V ≈ 37.7.",
     "keywords": ["конус"],
     "variants": [
         ("V", "Объём", "V = ⅓ · πR² · h"),
         ("R", "Радиус", "R = √(3V / πh)"),
         ("h", "Высота", "h = 3V / (πR²)"),
     ],
     "svg": draw_cone,
     "calc": {"vars": [("R", "R"), ("h", "h"), ("V", "V")],
              "solvers": {"V": lambda R, h: math.pi*R**2*h/3,
                          "R": lambda V, h: math.sqrt(3*V/(math.pi*h)),
                          "h": lambda R, V: 3*V/(math.pi*R**2)}}},

    {"section": "Стереометрия", "name": "Объём шара",
     "formula": "V = 4/3 · πR³",
     "theorem": "Объём шара радиуса R.",
     "example": "R=3 → V ≈ 113.1.",
     "keywords": ["шар", "сфера"],
     "variants": [
         ("V", "Объём", "V = 4/3 · πR³"),
         ("R", "Радиус", "R = ∛(3V / 4π)"),
     ],
     "svg": draw_sphere,
     "calc": {"vars": [("R", "R"), ("V", "V")],
              "solvers": {"V": lambda R: 4/3*math.pi*R**3,
                          "R": lambda V: (3*V/(4*math.pi))**(1/3)}}},

    {"section": "Стереометрия", "name": "Объём усечённой пирамиды",
     "formula": "V = ⅓ · h · (S₁ + √(S₁S₂) + S₂)",
     "theorem": "Объём усечённой пирамиды через площади оснований.",
     "example": "S1=4, S2=9, h=5 → V ≈ 31.67.",
     "keywords": ["усечённая пирамида"],
     "variants": [
         ("V", "Объём", "V = ⅓ · h · (S₁ + √(S₁S₂) + S₂)"),
         ("h", "Высота", "h = 3V / (S₁ + √(S₁S₂) + S₂)"),
     ],
     "svg": draw_frustum,
     "calc": {"vars": [("S1", "S₁"), ("S2", "S₂"), ("h", "h"), ("V", "V")],
              "solvers": {"V": lambda S1, S2, h: h/3*(S1 + math.sqrt(S1*S2) + S2),
                          "h": lambda S1, S2, V: 3*V/(S1 + math.sqrt(S1*S2) + S2)}}},
]


# ================== ФИЗИКА ==================
G = 10

PHYSICS_TOPICS = [
    # ============ 7 КЛАСС ============
    {"section": "7 класс", "name": "Скорость (равномерное движение)",
     "formula": "v = S / t",
     "theorem": "Скорость — путь, пройденный телом за единицу времени.",
     "example": "S = 150 км, t = 2 ч → v = 75 км/ч.",
     "keywords": ["скорость", "равномерное"],
     "variants": [
         ("v", "Скорость", "v = S / t"),
         ("S", "Путь", "S = v · t"),
         ("t", "Время", "t = S / v"),
     ],
     "svg": draw_motion,
     "calc": {"vars": [("S", "Путь S"), ("t", "Время t"), ("v", "Скорость v")],
              "solvers": {"v": lambda S, t: S/t, "S": lambda v, t: v*t, "t": lambda S, v: S/v}}},

    {"section": "7 класс", "name": "Путь при равномерном движении",
     "formula": "S = v · t",
     "theorem": "Путь равен произведению скорости на время.",
     "example": "v = 60 км/ч, t = 3 ч → S = 180 км.",
     "keywords": ["путь", "расстояние"],
     "variants": [
         ("S", "Путь", "S = v · t"),
         ("v", "Скорость", "v = S / t"),
         ("t", "Время", "t = S / v"),
     ],
     "svg": draw_motion,
     "calc": {"vars": [("v", "v"), ("t", "t"), ("S", "S")],
              "solvers": {"S": lambda v, t: v*t, "v": lambda S, t: S/t, "t": lambda S, v: S/v}}},

    {"section": "7 класс", "name": "Плотность вещества",
     "formula": "ρ = m / V",
     "theorem": "Плотность — масса единицы объёма.",
     "example": "m = 2 кг, V = 0.001 м³ → ρ = 2000 кг/м³.",
     "keywords": ["плотность", "масса", "объём"],
     "variants": [
         ("ρ", "Плотность", "ρ = m / V"),
         ("m", "Масса", "m = ρ · V"),
         ("V", "Объём", "V = m / ρ"),
     ],
     "svg": None,
     "calc": {"vars": [("m", "m"), ("V", "V"), ("ρ", "ρ")],
              "solvers": {"ρ": lambda m, V: m/V, "m": lambda ρ, V: ρ*V, "V": lambda m, ρ: m/ρ}}},

    {"section": "7 класс", "name": "Сила тяжести",
     "formula": "F = m · g",
     "theorem": "Сила, с которой Земля притягивает тело. g ≈ 10 Н/кг.",
     "example": "m = 5 кг → F = 50 Н.",
     "keywords": ["сила тяжести", "вес"],
     "variants": [
         ("F", "Сила", "F = m · g"),
         ("m", "Масса", "m = F / g"),
     ],
     "svg": draw_force,
     "calc": {"vars": [("m", "m"), ("F", "F")],
              "solvers": {"F": lambda m: m*G, "m": lambda F: F/G}}},

    {"section": "7 класс", "name": "Закон Гука",
     "formula": "F = k · x",
     "theorem": "Сила упругости пропорциональна удлинению пружины.",
     "example": "k = 200 Н/м, x = 0.05 м → F = 10 Н.",
     "keywords": ["гук", "пружина", "упругость"],
     "variants": [
         ("F", "Сила", "F = k · x"),
         ("k", "Жёсткость", "k = F / x"),
         ("x", "Удлинение", "x = F / k"),
     ],
     "svg": None,
     "calc": {"vars": [("k", "k"), ("x", "x"), ("F", "F")],
              "solvers": {"F": lambda k, x: k*x, "k": lambda F, x: F/x, "x": lambda F, k: F/k}}},

    {"section": "7 класс", "name": "Давление твёрдого тела",
     "formula": "p = F / S",
     "theorem": "Давление — сила на единицу площади.",
     "example": "F = 100 Н, S = 0.5 м² → p = 200 Па.",
     "keywords": ["давление"],
     "variants": [
         ("p", "Давление", "p = F / S"),
         ("F", "Сила", "F = p · S"),
         ("S", "Площадь", "S = F / p"),
     ],
     "svg": draw_force,
     "calc": {"vars": [("F", "F"), ("S", "S"), ("p", "p")],
              "solvers": {"p": lambda F, S: F/S, "F": lambda p, S: p*S, "S": lambda F, p: F/p}}},

    {"section": "7 класс", "name": "Давление жидкости",
     "formula": "p = ρ · g · h",
     "theorem": "Давление на глубине h в жидкости плотностью ρ.",
     "example": "ρ = 1000, h = 5 → p = 50 000 Па.",
     "keywords": ["давление жидкости", "глубина"],
     "variants": [
         ("p", "Давление", "p = ρ · g · h"),
         ("h", "Глубина", "h = p / (ρg)"),
         ("ρ", "Плотность", "ρ = p / (gh)"),
     ],
     "svg": None,
     "calc": {"vars": [("ρ", "ρ"), ("h", "h"), ("p", "p")],
              "solvers": {"p": lambda ρ, h: ρ*G*h, "h": lambda ρ, p: p/(ρ*G), "ρ": lambda h, p: p/(G*h)}}},

    {"section": "7 класс", "name": "Сила Архимеда",
     "formula": "F = ρ · g · V",
     "theorem": "Выталкивающая сила равна весу вытесненной жидкости.",
     "example": "ρ = 1000, V = 0.002 → F = 20 Н.",
     "keywords": ["архимед", "выталкивающая"],
     "variants": [
         ("F", "Сила", "F = ρ · g · V"),
         ("V", "Объём", "V = F / (ρg)"),
         ("ρ", "Плотность", "ρ = F / (gV)"),
     ],
     "svg": None,
     "calc": {"vars": [("ρ", "ρ"), ("V", "V"), ("F", "F")],
              "solvers": {"F": lambda ρ, V: ρ*G*V, "V": lambda ρ, F: F/(ρ*G), "ρ": lambda V, F: F/(G*V)}}},

    {"section": "7 класс", "name": "Механическая работа",
     "formula": "A = F · S",
     "theorem": "Работа совершается при перемещении тела под действием силы.",
     "example": "F = 20, S = 5 → A = 100 Дж.",
     "keywords": ["работа"],
     "variants": [
         ("A", "Работа", "A = F · S"),
         ("F", "Сила", "F = A / S"),
         ("S", "Путь", "S = A / F"),
     ],
     "svg": None,
     "calc": {"vars": [("F", "F"), ("S", "S"), ("A", "A")],
              "solvers": {"A": lambda F, S: F*S, "F": lambda A, S: A/S, "S": lambda F, A: A/F}}},

    {"section": "7 класс", "name": "Мощность",
     "formula": "N = A / t",
     "theorem": "Мощность — работа за единицу времени.",
     "example": "A = 500, t = 10 → N = 50 Вт.",
     "keywords": ["мощность"],
     "variants": [
         ("N", "Мощность", "N = A / t"),
         ("A", "Работа", "A = N · t"),
         ("t", "Время", "t = A / N"),
     ],
     "svg": None,
     "calc": {"vars": [("A", "A"), ("t", "t"), ("N", "N")],
              "solvers": {"N": lambda A, t: A/t, "A": lambda N, t: N*t, "t": lambda A, N: A/N}}},

    {"section": "7 класс", "name": "КПД механизма",
     "formula": "η = (Aполез / Aзатр) · 100%",
     "theorem": "КПД показывает, какая часть работы пошла на пользу.",
     "example": "80/100 → η = 80%.",
     "keywords": ["кпд"],
     "variants": [
         ("η", "КПД", "η = (Aполез / Aзатр) · 100%"),
         ("Ap", "Полезная работа", "Aполез = Aзатр · η/100"),
         ("Az", "Затраченная", "Aзатр = Aполез · 100/η"),
     ],
     "svg": None,
     "calc": {"vars": [("Ap", "Aполез"), ("Az", "Aзатр"), ("η", "КПД (%)")],
              "solvers": {"η": lambda Ap, Az: Ap/Az*100, "Ap": lambda Az, η: Az*η/100}}},

    {"section": "7 класс", "name": "Кинетическая энергия",
     "formula": "Ek = m·v² / 2",
     "theorem": "Энергия движения тела.",
     "example": "m = 2, v = 3 → Ek = 9 Дж.",
     "keywords": ["кинетическая", "энергия движения"],
     "variants": [
         ("Ek", "Энергия", "Ek = m·v² / 2"),
         ("m", "Масса", "m = 2Ek / v²"),
         ("v", "Скорость", "v = √(2Ek / m)"),
     ],
     "svg": None,
     "calc": {"vars": [("m", "m"), ("v", "v"), ("Ek", "Ek")],
              "solvers": {"Ek": lambda m, v: m*v*v/2, "m": lambda Ek, v: 2*Ek/(v*v), "v": lambda m, Ek: math.sqrt(2*Ek/m)}}},

    {"section": "7 класс", "name": "Потенциальная энергия",
     "formula": "Ep = m · g · h",
     "theorem": "Энергия тела, поднятого над Землёй.",
     "example": "m = 3, h = 4 → Ep = 120 Дж.",
     "keywords": ["потенциальная"],
     "variants": [
         ("Ep", "Энергия", "Ep = m · g · h"),
         ("m", "Масса", "m = Ep / (gh)"),
         ("h", "Высота", "h = Ep / (mg)"),
     ],
     "svg": None,
     "calc": {"vars": [("m", "m"), ("h", "h"), ("Ep", "Ep")],
              "solvers": {"Ep": lambda m, h: m*G*h, "m": lambda Ep, h: Ep/(G*h), "h": lambda m, Ep: Ep/(m*G)}}},

    {"section": "7 класс", "name": "Момент силы (правило рычага)",
     "formula": "F₁ · l₁ = F₂ · l₂",
     "theorem": "Рычаг в равновесии при равенстве моментов.",
     "example": "F₁=10, l₁=0.3, l₂=0.1 → F₂ = 30 Н.",
     "keywords": ["рычаг", "момент силы"],
     "variants": [
         ("F₂", "Сила F₂", "F₂ = F₁ · l₁ / l₂"),
         ("F₁", "Сила F₁", "F₁ = F₂ · l₂ / l₁"),
         ("l₁", "Плечо l₁", "l₁ = F₂ · l₂ / F₁"),
         ("l₂", "Плечо l₂", "l₂ = F₁ · l₁ / F₂"),
     ],
     "svg": None,
     "calc": {"vars": [("F1", "F₁"), ("l1", "l₁"), ("F2", "F₂"), ("l2", "l₂")],
              "solvers": {"F2": lambda F1, l1, l2: F1*l1/l2, "F1": lambda F2, l2, l1: F2*l2/l1,
                          "l1": lambda F2, l2, F1: F2*l2/F1, "l2": lambda F1, l1, F2: F1*l1/F2}}},

    # ============ 8 КЛАСС ============
    {"section": "8 класс", "name": "Количество теплоты при нагревании",
     "formula": "Q = c · m · Δt",
     "theorem": "Теплота для нагрева тела массой m на Δt градусов.",
     "example": "c=4200, m=2, Δt=50 → Q = 420 000 Дж.",
     "keywords": ["нагревание", "теплота", "теплоёмкость"],
     "variants": [
         ("Q", "Теплота", "Q = c · m · Δt"),
         ("m", "Масса", "m = Q / (c·Δt)"),
         ("dt", "Δ t", "Δt = Q / (c·m)"),
         ("c", "Теплоёмкость", "c = Q / (m·Δt)"),
     ],
     "svg": draw_heat,
     "calc": {"vars": [("c", "c"), ("m", "m"), ("dt", "Δt"), ("Q", "Q")],
              "solvers": {"Q": lambda c, m, dt: c*m*dt, "m": lambda c, dt, Q: Q/(c*dt),
                          "dt": lambda c, m, Q: Q/(c*m), "c": lambda m, dt, Q: Q/(m*dt)}}},

    {"section": "8 класс", "name": "Теплота плавления",
     "formula": "Q = λ · m",
     "theorem": "Теплота для плавления тела массой m.",
     "example": "λ=340000, m=0.5 → Q = 170 000 Дж.",
     "keywords": ["плавление", "лёд"],
     "variants": [
         ("Q", "Теплота", "Q = λ · m"),
         ("m", "Масса", "m = Q / λ"),
         ("λ", "λ", "λ = Q / m"),
     ],
     "svg": None,
     "calc": {"vars": [("lam", "λ"), ("m", "m"), ("Q", "Q")],
              "solvers": {"Q": lambda lam, m: lam*m, "m": lambda lam, Q: Q/lam, "lam": lambda m, Q: Q/m}}},

    {"section": "8 класс", "name": "Теплота парообразования",
     "formula": "Q = L · m",
     "theorem": "Теплота для превращения жидкости в пар.",
     "example": "L=2.3e6, m=0.2 → Q = 460 000 Дж.",
     "keywords": ["парообразование", "испарение"],
     "variants": [
         ("Q", "Теплота", "Q = L · m"),
         ("m", "Масса", "m = Q / L"),
         ("L", "L", "L = Q / m"),
     ],
     "svg": None,
     "calc": {"vars": [("L", "L"), ("m", "m"), ("Q", "Q")],
              "solvers": {"Q": lambda L, m: L*m, "m": lambda L, Q: Q/L, "L": lambda m, Q: Q/m}}},

    {"section": "8 класс", "name": "Теплота сгорания топлива",
     "formula": "Q = q · m",
     "theorem": "Теплота при сгорании топлива.",
     "example": "q=4.6e7, m=3 → Q = 1.38e8 Дж.",
     "keywords": ["сгорание", "топливо"],
     "variants": [
         ("Q", "Теплота", "Q = q · m"),
         ("m", "Масса", "m = Q / q"),
         ("q", "q", "q = Q / m"),
     ],
     "svg": draw_heat,
     "calc": {"vars": [("q", "q"), ("m", "m"), ("Q", "Q")],
              "solvers": {"Q": lambda q, m: q*m, "m": lambda q, Q: Q/q, "q": lambda m, Q: Q/m}}},

    {"section": "8 класс", "name": "Закон Ома для участка цепи",
     "formula": "I = U / R",
     "theorem": "Сила тока прямо пропорциональна напряжению.",
     "example": "U=12, R=4 → I = 3 А.",
     "keywords": ["ом", "ток", "напряжение", "сопротивление"],
     "variants": [
         ("I", "Сила тока", "I = U / R"),
         ("U", "Напряжение", "U = I · R"),
         ("R", "Сопротивление", "R = U / I"),
     ],
     "svg": draw_circuit,
     "calc": {"vars": [("U", "U"), ("R", "R"), ("I", "I")],
              "solvers": {"I": lambda U, R: U/R, "U": lambda I, R: I*R, "R": lambda U, I: U/I}}},

    {"section": "8 класс", "name": "Сопротивление проводника",
     "formula": "R = ρ · l / S",
     "theorem": "Сопротивление зависит от ρ, длины и площади.",
     "example": "ρ=0.017, l=100, S=2 → R = 0.85 Ом.",
     "keywords": ["сопротивление проводника", "удельное"],
     "variants": [
         ("R", "Сопротивление", "R = ρ · l / S"),
         ("l", "Длина", "l = R · S / ρ"),
         ("S", "Площадь", "S = ρ · l / R"),
     ],
     "svg": None,
     "calc": {"vars": [("rho", "ρ"), ("l", "l"), ("S", "S"), ("R", "R")],
              "solvers": {"R": lambda rho, l, S: rho*l/S, "l": lambda rho, S, R: R*S/rho,
                          "S": lambda rho, l, R: rho*l/R}}},

    {"section": "8 класс", "name": "Последовательное соединение",
     "formula": "R = R₁ + R₂",
     "theorem": "Сопротивления складываются.",
     "example": "R1=2, R2=3 → R = 5 Ом.",
     "keywords": ["последовательное"],
     "variants": [
         ("R", "R общее", "R = R₁ + R₂"),
         ("R1", "R₁", "R₁ = R − R₂"),
         ("R2", "R₂", "R₂ = R − R₁"),
     ],
     "svg": draw_circuit,
     "calc": {"vars": [("R1", "R₁"), ("R2", "R₂"), ("R", "R")],
              "solvers": {"R": lambda R1, R2: R1+R2, "R1": lambda R, R2: R-R2, "R2": lambda R, R1: R-R1}}},

    {"section": "8 класс", "name": "Параллельное соединение",
     "formula": "1/R = 1/R₁ + 1/R₂",
     "theorem": "Обратные сопротивления складываются.",
     "example": "R1=2, R2=4 → R ≈ 1.33 Ом.",
     "keywords": ["параллельное"],
     "variants": [
         ("R", "R общее", "R = R₁R₂ / (R₁ + R₂)"),
     ],
     "svg": draw_circuit,
     "calc": {"vars": [("R1", "R₁"), ("R2", "R₂"), ("R", "R")],
              "solvers": {"R": lambda R1, R2: (R1*R2)/(R1+R2)}}},

    {"section": "8 класс", "name": "Мощность электрического тока",
     "formula": "P = U · I",
     "theorem": "Мощность тока через напряжение и ток.",
     "example": "U=220, I=2 → P = 440 Вт.",
     "keywords": ["мощность тока"],
     "variants": [
         ("P", "Мощность", "P = U · I"),
         ("U", "Напряжение", "U = P / I"),
         ("I", "Сила тока", "I = P / U"),
     ],
     "svg": draw_circuit,
     "calc": {"vars": [("U", "U"), ("I", "I"), ("P", "P")],
              "solvers": {"P": lambda U, I: U*I, "U": lambda P, I: P/I, "I": lambda U, P: P/U}}},

    {"section": "8 класс", "name": "Работа электрического тока",
     "formula": "A = U · I · t",
     "theorem": "Работа тока за время t.",
     "example": "U=220, I=0.5, t=3600 → A = 396000 Дж.",
     "keywords": ["работа тока"],
     "variants": [
         ("A", "Работа", "A = U · I · t"),
         ("t", "Время", "t = A / (U·I)"),
     ],
     "svg": draw_circuit,
     "calc": {"vars": [("U", "U"), ("I", "I"), ("t", "t"), ("A", "A")],
              "solvers": {"A": lambda U, I, t: U*I*t, "t": lambda U, I, A: A/(U*I)}}},

    {"section": "8 класс", "name": "Закон Джоуля-Ленца",
     "formula": "Q = I² · R · t",
     "theorem": "Теплота, выделяемая проводником с током.",
     "example": "I=3, R=5, t=10 → Q = 450 Дж.",
     "keywords": ["джоуль", "ленц"],
     "variants": [
         ("Q", "Теплота", "Q = I² · R · t"),
         ("R", "Сопротивление", "R = Q / (I²t)"),
         ("t", "Время", "t = Q / (I²R)"),
     ],
     "svg": draw_heat,
     "calc": {"vars": [("I", "I"), ("R", "R"), ("t", "t"), ("Q", "Q")],
              "solvers": {"Q": lambda I, R, t: I*I*R*t, "R": lambda I, t, Q: Q/(I*I*t),
                          "t": lambda I, R, Q: Q/(I*I*R)}}},

    # ============ 9 КЛАСС · КИНЕМАТИКА ============
    {"section": "9 класс · Кинематика", "name": "Ускорение",
     "formula": "a = (v − v₀) / t",
     "theorem": "Ускорение — изменение скорости за единицу времени.",
     "example": "v₀=2, v=14, t=4 → a = 3 м/с².",
     "keywords": ["ускорение", "затормозил", "разогнался"],
     "variants": [
         ("a", "Ускорение", "a = (v − v₀) / t"),
         ("v", "Конечная скорость", "v = v₀ + a · t"),
         ("v0", "Начальная скорость", "v₀ = v − a · t"),
         ("t", "Время", "t = (v − v₀) / a"),
     ],
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("v", "v"), ("t", "t"), ("a", "a")],
              "solvers": {"a": lambda v0, v, t: (v-v0)/t, "v": lambda v0, a, t: v0+a*t,
                          "t": lambda v0, v, a: (v-v0)/a, "v0": lambda v, a, t: v - a*t}}},

    {"section": "9 класс · Кинематика", "name": "Скорость при равноускоренном движении",
     "formula": "v = v₀ + a · t",
     "theorem": "Конечная скорость через время t при начальной v₀ и ускорении a.",
     "example": "v₀=2, a=3, t=4 → v = 14 м/с.",
     "keywords": ["конечная скорость", "разогнался до", "v = v0 + at"],
     "variants": [
         ("v", "Конечная скорость", "v = v₀ + a · t"),
         ("v0", "Начальная скорость", "v₀ = v − a · t"),
         ("a", "Ускорение", "a = (v − v₀) / t"),
         ("t", "Время", "t = (v − v₀) / a"),
     ],
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("a", "a"), ("t", "t"), ("v", "v")],
              "solvers": {"v": lambda v0, a, t: v0 + a*t, "a": lambda v0, t, v: (v-v0)/t,
                          "t": lambda v0, a, v: (v-v0)/a, "v0": lambda a, t, v: v - a*t}}},

    {"section": "9 класс · Кинематика", "name": "Перемещение при равноускоренном движении",
     "formula": "S = v₀ · t + a · t² / 2",
     "theorem": "Перемещение при равноускоренном движении с начальной скоростью v₀.",
     "example": "v₀=0, a=2, t=5 → S = 25 м.",
     "keywords": ["перемещение равноускоренное", "путь равноускоренное", "S = v0t + at²/2"],
     "variants": [
         ("S", "Перемещение", "S = v₀ · t + a · t² / 2"),
         ("a", "Ускорение", "a = 2(S − v₀t) / t²"),
         ("v0", "Начальная скорость", "v₀ = (S − a·t²/2) / t"),
         ("t", "Время", "t = (−v₀ + √(v₀² + 2aS)) / a"),
     ],
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("a", "a"), ("t", "t"), ("S", "S")],
              "solvers": {"S": lambda v0, a, t: v0*t + a*t*t/2,
                          "a": lambda v0, t, S: 2*(S - v0*t)/(t*t),
                          "v0": lambda a, t, S: (S - a*t*t/2)/t}}},

    {"section": "9 класс · Кинематика", "name": "Уравнение координаты (равномерное)",
     "formula": "x = x₀ + v · t",
     "theorem": "Координата тела при равномерном движении.",
     "example": "x₀=5, v=3, t=4 → x = 17 м.",
     "keywords": ["уравнение координаты", "координата"],
     "variants": [
         ("x", "Координата x", "x = x₀ + v · t"),
         ("x0", "Начальная координата", "x₀ = x − v · t"),
         ("v", "Скорость", "v = (x − x₀) / t"),
         ("t", "Время", "t = (x − x₀) / v"),
     ],
     "svg": draw_coordinate,
     "calc": {"vars": [("x0", "x₀"), ("v", "v"), ("t", "t"), ("x", "x")],
              "solvers": {"x": lambda x0, v, t: x0 + v*t, "x0": lambda v, t, x: x - v*t,
                          "v": lambda x0, t, x: (x - x0)/t, "t": lambda x0, v, x: (x - x0)/v}}},

    {"section": "9 класс · Кинематика", "name": "Перемещение без времени",
     "formula": "S = (v² − v₀²) / (2a)",
     "theorem": "Перемещение, если время неизвестно.",
     "example": "v₀=0, v=10, a=2 → S = 25 м.",
     "keywords": ["без времени", "перемещение без времени"],
     "variants": [
         ("S", "Перемещение", "S = (v² − v₀²) / (2a)"),
         ("a", "Ускорение", "a = (v² − v₀²) / (2S)"),
         ("v", "Конечная скорость", "v = √(v₀² + 2aS)"),
         ("v0", "Начальная скорость", "v₀ = √(v² − 2aS)"),
     ],
     "svg": draw_motion,
     "calc": {"vars": [("v0", "v₀"), ("v", "v"), ("a", "a"), ("S", "S")],
              "solvers": {"S": lambda v0, v, a: (v*v - v0*v0)/(2*a),
                          "a": lambda v0, v, S: (v*v - v0*v0)/(2*S),
                          "v": lambda v0, a, S: math.sqrt(v0*v0 + 2*a*S),
                          "v0": lambda v, a, S: math.sqrt(abs(v*v - 2*a*S))}}},

    {"section": "9 класс · Кинематика", "name": "Средняя скорость",
     "formula": "vср = S_весь / t_весь",
     "theorem": "Средняя скорость — весь путь на всё время.",
     "example": "S=100, t=2 → vср = 50.",
     "keywords": ["средняя скорость", "vср"],
     "variants": [
         ("v", "Средняя скорость", "vср = S / t"),
         ("S", "Весь путь", "S = vср · t"),
         ("t", "Всё время", "t = S / vср"),
     ],
     "svg": draw_motion,
     "calc": {"vars": [("S", "S"), ("t", "t"), ("v", "vср")],
              "solvers": {"v": lambda S, t: S/t, "S": lambda v, t: v*t, "t": lambda S, v: S/v}}},

    {"section": "9 класс · Кинематика", "name": "Свободное падение",
     "formula": "h = g·t² / 2,  v = g·t",
     "theorem": "Высота и скорость при свободном падении. g ≈ 10.",
     "example": "t = 3 с → h = 45 м, v = 30 м/с.",
     "keywords": ["свободное падение", "падает", "упало"],
     "variants": [
         ("h", "Высота", "h = g·t² / 2"),
         ("t", "Время", "t = √(2h / g)"),
         ("v", "Скорость падения", "v = g · t"),
     ],
     "svg": None,
     "calc": {"vars": [("t", "t"), ("h", "h")],
              "solvers": {"h": lambda t: G*t*t/2, "t": lambda h: math.sqrt(2*h/G)}}},

    # ============ 9 КЛАСС · ДИНАМИКА ============
    {"section": "9 класс · Динамика", "name": "Второй закон Ньютона",
     "formula": "F = m · a",
     "theorem": "Сила равна произведению массы на ускорение.",
     "example": "m=4, a=3 → F = 12 Н.",
     "keywords": ["второй закон ньютона", "ньютон", "под действием силы"],
     "variants": [
         ("F", "Сила", "F = m · a"),
         ("m", "Масса", "m = F / a"),
         ("a", "Ускорение", "a = F / m"),
     ],
     "svg": draw_force,
     "calc": {"vars": [("m", "m"), ("a", "a"), ("F", "F")],
              "solvers": {"F": lambda m, a: m*a, "m": lambda F, a: F/a, "a": lambda m, F: F/m}}},

    {"section": "9 класс · Динамика", "name": "Третий закон Ньютона",
     "formula": "F₁ = − F₂",
     "theorem": "Силы взаимодействия равны по модулю и противоположны по направлению.",
     "example": "F₁ = 50 Н → F₂ = 50 Н.",
     "keywords": ["третий закон ньютона", "взаимодействие"],
     "variants": [
         ("F1", "Сила F₁", "F₁ = − F₂"),
         ("F2", "Сила F₂", "F₂ = − F₁"),
     ],
     "svg": draw_two_blocks,
     "calc": {"vars": [("F1", "F₁"), ("F2", "F₂")],
              "solvers": {"F1": lambda F2: -F2, "F2": lambda F1: -F1}}},

    {"section": "9 класс · Динамика", "name": "Импульс тела",
     "formula": "p = m · v",
     "theorem": "Импульс — произведение массы на скорость.",
     "example": "m=2, v=5 → p = 10 кг·м/с.",
     "keywords": ["импульс"],
     "variants": [
         ("p", "Импульс", "p = m · v"),
         ("m", "Масса", "m = p / v"),
         ("v", "Скорость", "v = p / m"),
     ],
     "svg": None,
     "calc": {"vars": [("m", "m"), ("v", "v"), ("p", "p")],
              "solvers": {"p": lambda m, v: m*v, "m": lambda p, v: p/v, "v": lambda m, p: p/m}}},

    {"section": "9 класс · Динамика", "name": "Закон сохранения импульса",
     "formula": "m₁v₁ + m₂v₂ = (m₁ + m₂)·v'",
     "theorem": "Импульс замкнутой системы сохраняется.",
     "example": "m1=2, v1=3, m2=1, v2=1 → v' = 7/3 ≈ 2.33.",
     "keywords": ["сохранение импульса", "сцепились", "ударились"],
     "variants": [
         ("v", "Общая скорость", "v' = (m₁v₁ + m₂v₂) / (m₁ + m₂)"),
     ],
     "svg": draw_two_blocks,
     "calc": {"vars": [("m1", "m₁"), ("v1", "v₁"), ("m2", "m₂"), ("v2", "v₂"), ("v", "v'")],
              "solvers": {"v": lambda m1, v1, m2, v2: (m1*v1 + m2*v2)/(m1+m2)}}},

    {"section": "9 класс · Динамика", "name": "Сила трения",
     "formula": "F = μ · m · g",
     "theorem": "Сила трения пропорциональна силе нормального давления.",
     "example": "μ=0.3, m=5 → F = 15 Н.",
     "keywords": ["сила трения", "трение"],
     "variants": [
         ("F", "Сила трения", "F = μ · m · g"),
         ("μ", "Коэффициент μ", "μ = F / (m·g)"),
         ("m", "Масса", "m = F / (μ·g)"),
     ],
     "svg": draw_slope,
     "calc": {"vars": [("μ", "μ"), ("m", "m"), ("F", "F")],
              "solvers": {"F": lambda μ, m: μ*m*G, "m": lambda μ, F: F/(μ*G), "μ": lambda m, F: F/(m*G)}}},

    {"section": "9 класс · Динамика", "name": "Закон всемирного тяготения",
     "formula": "F = G · m₁·m₂ / r²",
     "theorem": "Сила притяжения двух тел. G ≈ 6.67·10⁻¹¹.",
     "example": "m1=m2=1000, r=10 → F ≈ 6.67·10⁻⁷ Н.",
     "keywords": ["тяготение", "гравитация", "притяжение"],
     "variants": [
         ("F", "Сила", "F = G·m₁m₂ / r²"),
         ("r", "Расстояние", "r = √(G·m₁m₂ / F)"),
     ],
     "svg": draw_two_blocks,
     "calc": {"vars": [("m1", "m₁"), ("m2", "m₂"), ("r", "r"), ("F", "F")],
              "solvers": {"F": lambda m1, m2, r: 6.67e-11*m1*m2/(r*r)}}},

    {"section": "9 класс · Динамика", "name": "Первая космическая скорость",
     "formula": "v = √(g · R)",
     "theorem": "Скорость для выхода на круговую орбиту у поверхности.",
     "example": "g=10, R=6.4e6 → v ≈ 8000 м/с.",
     "keywords": ["космическая скорость", "орбита", "спутник"],
     "variants": [
         ("v", "Скорость", "v = √(g · R)"),
         ("R", "Радиус", "R = v² / g"),
         ("g", "g", "g = v² / R"),
     ],
     "svg": None,
     "calc": {"vars": [("g", "g"), ("R", "R"), ("v", "v")],
              "solvers": {"v": lambda g, R: math.sqrt(g*R), "R": lambda g, v: v*v/g, "g": lambda R, v: v*v/R}}},

    # ============ 9 КЛАСС · ОКРУЖНОСТЬ ============
    {"section": "9 класс · Окружность", "name": "Центростремительное ускорение",
     "formula": "a = v² / R",
     "theorem": "Ускорение тела на окружности радиусом R.",
     "example": "v=4, R=2 → a = 8 м/с².",
     "keywords": ["центростремительное", "по окружности"],
     "variants": [
         ("a", "Ускорение", "a = v² / R"),
         ("v", "Скорость", "v = √(a · R)"),
         ("R", "Радиус", "R = v² / a"),
     ],
     "svg": draw_circle_motion,
     "calc": {"vars": [("v", "v"), ("R", "R"), ("a", "a")],
              "solvers": {"a": lambda v, R: v*v/R, "v": lambda a, R: math.sqrt(a*R), "R": lambda v, a: v*v/a}}},

    {"section": "9 класс · Окружность", "name": "Период и частота вращения",
     "formula": "T = 1 / ν",
     "theorem": "Период — время одного оборота. Частота — оборотов за секунду.",
     "example": "ν=5 → T = 0.2 с.",
     "keywords": ["период", "частота", "оборот"],
     "variants": [
         ("T", "Период", "T = 1 / ν"),
         ("nu", "Частота", "ν = 1 / T"),
     ],
     "svg": draw_circle_motion,
     "calc": {"vars": [("nu", "ν (Гц)"), ("T", "T (с)")],
              "solvers": {"T": lambda nu: 1/nu, "nu": lambda T: 1/T}}},

    {"section": "9 класс · Окружность", "name": "Линейная и угловая скорость",
     "formula": "v = ω · R",
     "theorem": "Связь линейной и угловой скорости.",
     "example": "ω=3, R=2 → v = 6 м/с.",
     "keywords": ["угловая скорость", "линейная скорость"],
     "variants": [
         ("v", "Линейная скорость", "v = ω · R"),
         ("w", "Угловая скорость", "ω = v / R"),
         ("R", "Радиус", "R = v / ω"),
     ],
     "svg": draw_circle_motion,
     "calc": {"vars": [("w", "ω (рад/с)"), ("R", "R"), ("v", "v (м/с)")],
              "solvers": {"v": lambda w, R: w*R, "w": lambda v, R: v/R, "R": lambda w, v: v/w}}},

    # ============ 9 КЛАСС · КОЛЕБАНИЯ ============
    {"section": "9 класс · Колебания", "name": "Период математического маятника",
     "formula": "T = 2π · √(l / g)",
     "theorem": "Период колебаний маятника длиной l. g ≈ 10.",
     "example": "l=1 → T ≈ 1.99 с.",
     "keywords": ["математический маятник", "маятник"],
     "variants": [
         ("T", "Период", "T = 2π · √(l / g)"),
         ("l", "Длина", "l = g · T² / (4π²)"),
     ],
     "svg": draw_pendulum,
     "calc": {"vars": [("l", "l (м)"), ("T", "T (с)")],
              "solvers": {"T": lambda l: 2*math.pi*math.sqrt(l/G), "l": lambda T: T*T*G/(4*math.pi*math.pi)}}},

    {"section": "9 класс · Колебания", "name": "Период пружинного маятника",
     "formula": "T = 2π · √(m / k)",
     "theorem": "Период колебаний груза на пружине.",
     "example": "m=1, k=100 → T ≈ 0.63 с.",
     "keywords": ["пружинный маятник", "период пружины"],
     "variants": [
         ("T", "Период", "T = 2π · √(m / k)"),
         ("m", "Масса", "m = k · T² / (4π²)"),
         ("k", "Жёсткость", "k = 4π²m / T²"),
     ],
     "svg": draw_spring,
     "calc": {"vars": [("m", "m (кг)"), ("k", "k (Н/м)"), ("T", "T (с)")],
              "solvers": {"T": lambda m, k: 2*math.pi*math.sqrt(m/k),
                          "m": lambda k, T: k*T*T/(4*math.pi*math.pi),
                          "k": lambda m, T: 4*math.pi*math.pi*m/(T*T)}}},

    {"section": "9 класс · Колебания", "name": "Длина волны",
     "formula": "λ = v · T = v / ν",
     "theorem": "Длина волны — расстояние между соседними гребнями.",
     "example": "v=340, T=0.01 → λ = 3.4 м.",
     "keywords": ["длина волны", "волна", "лямбда"],
     "variants": [
         ("lam", "Длина λ", "λ = v · T"),
         ("v", "Скорость", "v = λ / T"),
         ("T", "Период", "T = λ / v"),
     ],
     "svg": draw_wave,
     "calc": {"vars": [("v", "v"), ("T", "T"), ("lam", "λ")],
              "solvers": {"lam": lambda v, T: v*T, "v": lambda lam, T: lam/T, "T": lambda v, lam: lam/v}}},

    {"section": "9 класс · Колебания", "name": "Скорость волны",
     "formula": "v = λ · ν",
     "theorem": "Скорость распространения волны через частоту.",
     "example": "λ=3.4, ν=100 → v = 340 м/с.",
     "keywords": ["скорость волны"],
     "variants": [
         ("v", "Скорость", "v = λ · ν"),
         ("lam", "Длина λ", "λ = v / ν"),
         ("nu", "Частота", "ν = v / λ"),
     ],
     "svg": draw_wave,
     "calc": {"vars": [("lam", "λ (м)"), ("nu", "ν (Гц)"), ("v", "v (м/с)")],
              "solvers": {"v": lambda lam, nu: lam*nu, "lam": lambda nu, v: v/nu, "nu": lambda lam, v: v/lam}}},

    # ============ 9 КЛАСС · МАГНЕТИЗМ ============
    {"section": "9 класс · Магнетизм", "name": "Магнитный поток",
     "formula": "Φ = B · S · cos(α)",
     "theorem": "Поток магнитной индукции через площадку S.",
     "example": "B=0.5, S=0.2, α=0° → Φ = 0.1 Вб.",
     "keywords": ["магнитный поток", "вебер", "поток"],
     "variants": [
         ("Phi", "Поток Φ", "Φ = B · S · cos α"),
         ("B", "Индукция B", "B = Φ / (S · cos α)"),
         ("S", "Площадь", "S = Φ / (B · cos α)"),
     ],
     "svg": draw_magnet,
     "calc": {"vars": [("B", "B (Тл)"), ("S", "S (м²)"), ("alpha", "α (°)"), ("Phi", "Φ (Вб)")],
              "solvers": {"Phi": lambda B, S, alpha: B*S*cos_d(alpha),
                          "B": lambda S, alpha, Phi: Phi/(S*cos_d(alpha)),
                          "S": lambda B, alpha, Phi: Phi/(B*cos_d(alpha))}}},

    {"section": "9 класс · Магнетизм", "name": "Закон электромагнитной индукции",
     "formula": "ε = ΔΦ / Δt",
     "theorem": "ЭДС индукции пропорциональна скорости изменения потока.",
     "example": "ΔΦ=0.2, Δt=0.1 → ε = 2 В.",
     "keywords": ["эдс индукции", "индукция"],
     "variants": [
         ("e", "ЭДС ε", "ε = ΔΦ / Δt"),
         ("dPhi", "Δ Φ", "ΔΦ = ε · Δt"),
         ("dt", "Δ t", "Δt = ΔΦ / ε"),
     ],
     "svg": draw_magnet,
     "calc": {"vars": [("dPhi", "ΔΦ (Вб)"), ("dt", "Δt (с)"), ("e", "ε (В)")],
              "solvers": {"e": lambda dPhi, dt: dPhi/dt, "dPhi": lambda e, dt: e*dt, "dt": lambda dPhi, e: dPhi/e}}},

    # ============ 9 КЛАСС · ОПТИКА ============
    {"section": "9 класс · Оптика", "name": "Оптическая сила линзы",
     "formula": "D = 1 / F",
     "theorem": "Оптическая сила — величина, обратная фокусному расстоянию.",
     "example": "F=0.5 → D = 2 дптр.",
     "keywords": ["оптическая сила", "линза", "диоптрия"],
     "variants": [
         ("D", "Оптическая сила", "D = 1 / F"),
         ("F", "Фокус", "F = 1 / D"),
     ],
     "svg": draw_lens,
     "calc": {"vars": [("F", "F (м)"), ("D", "D (дптр)")],
              "solvers": {"D": lambda F: 1/F, "F": lambda D: 1/D}}},

    {"section": "9 класс · Оптика", "name": "Формула тонкой линзы",
     "formula": "1/F = 1/d + 1/f",
     "theorem": "Связь фокусного расстояния и расстояний до предмета и изображения.",
     "example": "d=30, f=60 → F = 20 см.",
     "keywords": ["тонкая линза", "формула линзы"],
     "variants": [
         ("F", "Фокус", "F = d·f / (d + f)"),
         ("d", "d", "d = f·F / (f − F)"),
         ("f", "f", "f = d·F / (d − F)"),
     ],
     "svg": draw_lens,
     "calc": {"vars": [("d", "d"), ("f", "f"), ("F", "F")],
              "solvers": {"F": lambda d, f: (d*f)/(d+f),
                          "d": lambda f, F: (f*F)/(f - F),
                          "f": lambda d, F: (d*F)/(d - F)}}},

    {"section": "9 класс · Оптика", "name": "Закон преломления света",
     "formula": "sin α / sin β = n",
     "theorem": "Отношение синуса угла падения к синусу угла преломления = n.",
     "example": "α=30°, n=1.5 → β ≈ 19.5°.",
     "keywords": ["преломление", "показатель преломления"],
     "variants": [
         ("beta", "Угол β", "β = arcsin(sin α / n)"),
         ("alpha", "Угол α", "α = arcsin(n · sin β)"),
         ("n", "n", "n = sin α / sin β"),
     ],
     "svg": draw_lens,
     "calc": {"vars": [("alpha", "α (°)"), ("n", "n"), ("beta", "β (°)")],
              "solvers": {"beta": lambda alpha, n: asin_d(sin_d(alpha)/n),
                          "alpha": lambda beta, n: asin_d(n*sin_d(beta)),
                          "n": lambda alpha, beta: sin_d(alpha)/sin_d(beta)}}},
]


# ================== СТРУКТУРА ==================
ROOT_SECTIONS = {
    "geom": {"title": "📐 Геометрия", "topics": GEOMETRY_TOPICS},
    "phys": {"title": "⚛️ Физика",     "topics": PHYSICS_TOPICS},
}


def get_subsections(root_key):
    topics = ROOT_SECTIONS[root_key]["topics"]
    subs = {}
    for i, t in enumerate(topics):
        subs.setdefault(t["section"], []).append((i, t["name"]))
    return subs


def get_topic(root_key, idx):
    return ROOT_SECTIONS[root_key]["topics"][idx]


def search_all(query):
    q = query.lower().strip()
    if len(q) < 2:
        return []
    out = []
    for rk, data in ROOT_SECTIONS.items():
        for i, t in enumerate(data["topics"]):
            hay = " ".join([t.get("name", ""), t.get("formula", ""),
                            t.get("theorem", ""), t.get("example", ""),
                            t.get("section", ""), " ".join(t.get("keywords", []))]).lower()
            if q in hay:
                out.append((rk, i))
    return out
