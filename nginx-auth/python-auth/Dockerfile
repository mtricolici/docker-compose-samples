FROM python:3.9-alpine

ADD sources/requirements.txt /tmp/
ADD sources /app

RUN apk add --no-cache bash libldap && \
    apk add --no-cache --virtual build-deps gcc musl-dev openldap-dev python3-dev && \
    pip install -r /tmp/requirements.txt && \
    apk del build-deps

ENTRYPOINT ["/app/main.py"]    
