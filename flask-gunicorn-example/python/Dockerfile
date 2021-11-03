FROM python:3.9-alpine

ADD sources /app

RUN addgroup python && \
    adduser -s /bin/sh -G python -D -H python && \
    pip install -r /app/requirements.txt

USER python:python

ENTRYPOINT ["/bin/sh"]
CMD ["/app/entrypoint.sh"]
