FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend/

WORKDIR /backend/

COPY . /backend/

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install gunicorn \
    && pip install psycopg2 \
    && pip install -r requirements.txt \
    && python manage.py collectstatic --noinput \
    && python manage.py makemigrations \
    && python manage.py migrate

CMD gunicorn mysite.wsgi --bind 0.0.0.0:$PORT --chdir /backend --log-file - --workers 4 --timeout 120 --access-logfile - --error-logfile - --preload --max-requests 500 --max-requests-jitter 50 --log-level debug
