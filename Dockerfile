# Use official Python image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./

EXPOSE 8501

ENV OPENROUTER_API_KEY=""

CMD ["streamlit", "run", "main.py"]
