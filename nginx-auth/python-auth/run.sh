#!/bin/bash

sdir="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

TAG=python-sample1

#worker-class: sync, gevent, gthread

docker run -it --rm \
  -e APP_CONFIG_FILE=/application-config.yaml \
  -e GUNICORN_WORKERS=3 \
  -e GUNICORN_THREADS=5 \
  -e GUNICORN_WORKER_CLASS=gevent \
  -p 8081:8080 \
  -e LOG_LEVEL=DEBUG \
  -v $sdir/sources:/app \
  -v $sdir/sample-config.yaml:/application-config.yaml \
  --tmpfs /my-tmp-dir \
  --name debug_python_sample1 \
  --network=nginx-auth_my-network \
  $TAG
