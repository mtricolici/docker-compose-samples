#!/bin/sh
set -ex

pip freeze

echo "Starting application"

exec python /app/main.py
