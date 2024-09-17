FROM python:3.11-slim

WORKDIR /app

COPY UI.py .
COPY requirements.txt .
COPY logo.png .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["streamlit", "run", "UI.py", "--server.port=8080", "--server.address=0.0.0.0"]
