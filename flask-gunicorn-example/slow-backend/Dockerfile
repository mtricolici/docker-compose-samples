FROM python:3.9-alpine

ADD sources /app

RUN pip install -r /app/requirements.txt

CMD ["python", "/app/slow.py"]
