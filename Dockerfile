FROM python:3.11-slim

# Системные библиотеки для cairosvg (рендер SVG → PNG)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libcairo2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Сначала зависимости — так Docker кэширует их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Затем весь код (bot.py, data.py и т.д.)
COPY . .

# Render ожидает порт 10000
EXPOSE 10000

CMD ["python", "bot.py"]
