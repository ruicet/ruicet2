FROM python:3.11-slim

# Системные библиотеки для cairosvg (рендер SVG → PNG)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libcairo2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Сначала зависимости — так Docker кэширует их и пересобирает быстрее
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Потом остальной код
COPY . .

# Порт для health-сервера (Render ждёт именно 10000)
EXPOSE 10000

# Запуск бота
CMD ["python", "bot.py"]
