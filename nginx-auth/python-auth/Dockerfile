FROM python:3.9-alpine

ADD sources/requirements.txt /tmp/

RUN apk add --no-cache bash && \
    apk add --no-cache --virtual build-deps gcc musl-dev openldap-dev && \
    pip install -r /tmp/requirements.txt && \
    apk del build-deps

