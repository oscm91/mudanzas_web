#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput

touch /logs/gunicorn.log
touch /logs/error.log
touch /logs/access.log

/usr/local/bin/gunicorn ecommerce.wsgi:application -w 2 -b :8000 --reload
