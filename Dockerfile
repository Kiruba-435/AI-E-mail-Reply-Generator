# Use official Python image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY app/main.py ./main.py

EXPOSE 8501

ENV OPENROUTER_API_KEY=""
'''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'''

CMD ["streamlit", "run", "main.py"]
