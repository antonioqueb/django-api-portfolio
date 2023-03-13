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
    && pip install -r requirements.txt 
