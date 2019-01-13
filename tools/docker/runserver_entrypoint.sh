#!/bin/sh

set -e

python manage.py makemigrations
celery -A sample worker -l  debug --detach
gunicorn --workers=2 \
--bind=0.0.0.0:8000 \
--log-level=info \
--access-logfile=- \
--error-logfile =- \
sample.wsgi
