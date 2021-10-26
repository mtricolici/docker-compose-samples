FROM python:3.9-alpine

ADD sources/requirements.txt /tmp/

RUN apk add --no-cache bash libldap && \
    apk add --no-cache --virtual build-deps gcc musl-dev openldap-dev python3-dev && \
    pip install -r /tmp/requirements.txt && \
    apk del build-deps

    
#apk add --no-cache --virtual build-deps gcc musl-dev openldap-dev && \
#apk add --no-cache --virtual build-deps build-base openldap-dev python2-dev python3-dev && \
