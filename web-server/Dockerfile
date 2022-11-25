FROM python:3.10

WORKDIR /app
COPY requeriment.txt /app/requeriment.txt

RUN pip install --no-cache-dir --upgrade -r /app/requeriment.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]