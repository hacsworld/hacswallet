# core/Dockerfile
FROM python:3.11-slim

# Оптимизация Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl &&     rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем код приложения
COPY . /app

# Открываем порт
EXPOSE 8000

# Запуск FastAPI через Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
