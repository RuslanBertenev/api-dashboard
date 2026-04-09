# Базовый образ Python 3.14 (slim версия оптимальна по размеру)
FROM python:3.14-slim

# Переменная среды: отключает буферизацию вывода (удобно для логов)
ENV PYTHONUNBUFFERED=1

# Создаём рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей ПЕРЕД остальным кодом.
# Это позволяет Docker кешировать слой установки библиотек,
# пока requirements.txt не изменится.
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# (Опционально) Создаём непривилегированного пользователя для безопасности
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Команда запуска проекта. Замените main.py на ваш файл/скрипт
CMD ["python", "main.py"]