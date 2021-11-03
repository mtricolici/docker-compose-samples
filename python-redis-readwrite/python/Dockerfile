FROM python:3.9-alpine

ADD sources/requirements.txt /tmp/
ADD sources /app
ADD entry.sh /

RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["/entry.sh"]
