FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 👇 this line copies .env into /app/.env
# COPY .env .env

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]