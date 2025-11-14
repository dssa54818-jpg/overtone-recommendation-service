# Dockerfile (обновлено)
FROM python:3.11-slim

WORKDIR /app

# Шаг 1: Установка системных сертификатов для SSL/TLS-подключения к MongoDB Atlas
# Это требование задания для решения проблем с TLS/SSL 
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем директорию приложения после установки зависимостей
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]