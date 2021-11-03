#!/bin/sh
set -e

workers="${GUNICORN_WORKERS:-1}"
threads="${GUNICORN_THREADS:-1}"
port="${GUNICORN_PORT:-8080}"

echo "unicorn workers: $workers"
echo "gunicorn threads: $threads"

exec gunicorn --chdir /app \
  --workers $workers \
  --threads $threads \
  --bind "0.0.0.0:$port" \
  --user python \
  --group python \
  sample:exemplu
