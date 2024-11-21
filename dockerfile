# Базовый образ Python
FROM python:3.10-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Указываем команду для запуска API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
