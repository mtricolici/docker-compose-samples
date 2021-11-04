FROM python:3.9-alpine

ADD sources /app

RUN echo "---> Adding python user/group" && \
    addgroup python && \
    adduser -s /bin/sh -G python -D -H python && \
    echo "---> Install additional tools (bash etc)..." && \
    apk add --no-cache bash libldap && \
    echo "---> Install temporary dependencies ..." && \
    DEPS="gcc g++ make musl-dev python3-dev libffi-dev openldap-dev" && \
    apk add --no-cache --virtual build-deps $DEPS && \
    echo "---> install PIP requirements" && \
    pip install -r /app/requirements.txt && \
    echo "---> cleanup" && \
    apk del build-deps

USER python:python

ENTRYPOINT ["/bin/sh"]
CMD ["/app/entrypoint.sh"]
