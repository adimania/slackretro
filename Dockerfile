FROM python:3.7-slim
MAINTAINER Aditya Patawari <aditya@devopsnexus.com>

RUN apt-get update && apt-get install -y gcc curl gnupg && echo 'deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main' > /etc/apt/sources.list.d/pgdg.list && curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && apt-get -y update && apt-get install -y libpq-dev
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD gunicorn --bind :8082 --workers 1 --threads 4 --timeout 0 slackretro:app
