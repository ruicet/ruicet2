import tkinter as tk
from tkinter import font as tkfont
import math


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧮 Калькулятор")
        self.geometry("380x560")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")

        # Состояние
        self.expression = ""      # строка выражения
        self.memory = 0.0         # память
        self.history = []         # история вычислений

        # Шрифты
        self.font_display = tkfont.Font(family="Segoe UI", size=28, weight="bold")
        self.font_small = tkfont.Font(family="Segoe UI", size=11)
        self.font_btn = tkfont.Font(family="Segoe UI", size=15, weight="bold")

        self._build_ui()
        self._bind_keys()

    # ================== ИНТЕРФЕЙС ==================
    def _build_ui(self):
        # --- История (мелким шрифтом сверху) ---
        self.history_var = tk.StringVar(value="")
        history_label = tk.Label(
            self, textvariable=self.history_var,
            font=self.font_small, bg="#1e1e1e", fg="#888",
            anchor="e", padx=15
        )
        history_label.pack(fill="x", pady=(10, 0))

        # --- Основной дисплей ---
        self.display_var = tk.StringVar(value="0")
        display = tk.Label(
            self, textvariable=self.display_var,
            font=self.font_display, bg="#1e1e1e", fg="white",
            anchor="e", padx=15, pady=10
        )
        display.pack(fill="x")

        # Индикатор памяти
        self.mem_var = tk.StringVar(value="")
        tk.Label(
            self, textvariable=self.mem_var, font=self.font_small,
            bg="#1e1e1e", fg="#ffb74d", anchor="w", padx=15
        ).pack(fill="x")

        # --- Сетка кнопок ---
        grid = tk.Frame(self, bg="#1e1e1e")
        grid.pack(fill="both", expand=True, padx=10, pady=10)

        # (текст, row, col, rowspan, colspan, тип)
        # тип: 'num', 'op', 'func', 'eq', 'clear', 'mem'
        buttons = [
            ("MC", 0, 0, "mem"), ("MR", 0, 1, "mem"), ("M+", 0, 2, "mem"), ("M-", 0, 3, "mem"),
            ("C",  1, 0, "clear"), ("⌫", 1, 1, "clear"), ("%", 1, 2, "func"), ("÷", 1, 3, "op"),
            ("7",  2, 0, "num"), ("8", 2, 1, "num"), ("9", 2, 2, "num"), ("×", 2, 3, "op"),
            ("4",  3, 0, "num"), ("5", 3, 1, "num"), ("6", 3, 2, "num"), ("-", 3, 3, "op"),
            ("1",  4, 0, "num"), ("2", 4, 1, "num"), ("3", 4, 2, "num"), ("+", 4, 3, "op"),
            ("±",  5, 0, "func"), ("0", 5, 1, "num"), (".", 5, 2, "num"), ("=", 5, 3, "eq"),
            ("√",  6, 0, "func"), ("x²", 6, 1, "func"), ("xʸ", 6, 2, "func"), ("1/x", 6, 3, "func"),
        ]

        colors = {
            "num":   ("#2d2d2d", "#ffffff"),
            "op":    ("#ff9800", "#ffffff"),
            "func":  ("#424242", "#ffffff"),
            "eq":    ("#4caf50", "#ffffff"),
            "clear": ("#d32f2f", "#ffffff"),
            "mem":   ("#37474f", "#b0bec5"),
        }

        for i in range(7):
            grid.rowconfigure(i, weight=1)
        for i in range(4):
            grid.columnconfigure(i, weight=1)

        for text, row, col, kind in buttons:
            bg, fg = colors[kind]
            btn = tk.Button(
                grid, text=text, font=self.font_btn,
                bg=bg, fg=fg, activebackground=bg, activeforeground=fg,
                bd=0, relief="flat",
                command=lambda t=text: self.on_button(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    # ================== КЛАВИАТУРА ==================
    def _bind_keys(self):
        self.bind("<Key>", self.on_key)

    def on_key(self, event):
        key = event.char
        if key.isdigit() or key == ".":
            self.on_button(key)
        elif key == "+":
            self.on_button("+")
        elif key == "-":
            self.on_button("-")
        elif key == "*":
            self.on_button("×")
        elif key == "/":
            self.on_button("÷")
        elif key == "%":
            self.on_button("%")
        elif key in ("\r", "="):     # Enter
            self.on_button("=")
        elif key == "\x08":          # Backspace
            self.on_button("⌫")
        elif key == "\x1b":          # Escape
            self.on_button("C")
        elif key == "r":
            self.on_button("√")
        elif key == "s":
            self.on_button("x²")

    # ================== ЛОГИКА ==================
    def on_button(self, text):
        if text.isdigit() or text == ".":
            self._input_digit(text)
        elif text in ("+", "-", "×", "÷"):
            self._input_operator(text)
        elif text == "=":
            self._calculate()
        elif text == "C":
            self.expression = ""
            self.display_var.set("0")
            self.history_var.set("")
        elif text == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression or "0")
        elif text == "%":
            self._apply_percent()
        elif text == "±":
            self._toggle_sign()
        elif text == "√":
            self._apply_unary(math.sqrt)
        elif text == "x²":
            self._apply_unary(lambda x: x ** 2)
        elif text == "1/x":
            self._apply_unary(lambda x: 1 / x)
        elif text == "xʸ":
            self._input_operator("**")
        elif text == "MC":
            self.memory = 0.0
            self._update_memory_indicator()
        elif text == "MR":
            self._input_digit(str(self.memory))
        elif text == "M+":
            self._memory_add(1)
        elif text == "M-":
            self._memory_add(-1)

    # ---------- Ввод цифр ----------
    def _input_digit(self, digit):
        # защита от двух точек в одном числе
        last_number = self.expression.replace("+", " ").replace("-", " ") \
                                      .replace("×", " ").replace("÷", " ").replace("**", " ").split()[-1:]
        if digit == "." and last_number and "." in last_number[0]:
            return
        self.expression += digit
        self.display_var.set(self.expression)

    # ---------- Ввод оператора ----------
    def _input_operator(self, op):
        if not self.expression:
            return
        # заменяем последний оператор, если он уже есть
        if self.expression[-1] in "+-×÷*":
            self.expression = self.expression[:-1]
        self.expression += op
        self.display_var.set(self.expression)

    # ---------- Процент ----------
    def _apply_percent(self):
        try:
            value = self._safe_eval(self.expression)
            result = value / 100
            self.expression = self._format(result)
            self.display_var.set(self.expression)
        except Exception:
            self._show_error()

    # ---------- Смена знака ----------
    def _toggle_sign(self):
        try:
            value = self._safe_eval(self.expression)
            result = -value
            self.expression = self._format(result)
            self.display_var.set(self.expression)
        except Exception:
            self._show_error()

    # ---------- Унарные операции ----------
    def _apply_unary(self, func):
        try:
            value = self._safe_eval(self.expression)
            result = func(value)
            self.expression = self._format(result)
            self.display_var.set(self.expression)
        except Exception:
            self._show_error()

    # ---------- Память ----------
    def _memory_add(self, sign):
        try:
            value = self._safe_eval(self.expression)
            self.memory += sign * value
            self._update_memory_indicator()
        except Exception:
            self._show_error()

    def _update_memory_indicator(self):
        self.mem_var.set(f"📌 M = {self.memory}" if self.memory else "")

    # ---------- Основное вычисление ----------
    def _calculate(self):
        if not self.expression:
            return
        try:
            result = self._safe_eval(self.expression)
            formatted = self._format(result)
            self.history_var.set(f"{self.expression} =")
            self.history.append(f"{self.expression} = {formatted}")
            self.expression = formatted
            self.display_var.set(formatted)
        except ZeroDivisionError:
            self._show_error("Деление на ноль!")
        except Exception:
            self._show_error("Ошибка")

    # ---------- Безопасное вычисление ----------
    def _safe_eval(self, expr: str) -> float:
        """Заменяем символы и считаем через eval с ограниченным словарём."""
        # Заменяем визуальные операторы на Python-синтаксис
        expr = expr.replace("×", "*").replace("÷", "/")

        # Разрешаем только цифры, операторы, точку и пробелы
        allowed = set("0123456789.+-*/() ")
        if not set(expr).issubset(allowed):
            raise ValueError("Недопустимые символы")

        # eval без доступа к встроенным функциям
        return eval(expr, {"__builtins__": {}}, {})

    # ---------- Форматирование ----------
    def _format(self, value: float) -> str:
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        # убираем плавающую точность
        return f"{value:.12g}"

    # ---------- Ошибка ----------
    def _show_error(self, msg="Ошибка"):
        self.display_var.set(msg)
        self.expression = ""


# ================== ЗАПУСК ==================
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
