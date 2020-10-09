FROM python:3.7-slim as base

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT=5005

CMD ["python3", "main.py"]