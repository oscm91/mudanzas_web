FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /docker/
RUN mkdir /docker/web/
RUN mkdir /docker/srv
RUN mkdir /docker/srv/static
RUN mkdir /docker/srv/media
WORKDIR /docker/web/
ADD requirements.txt /docker/web/
RUN pip install -r requirements.txt
ADD . /docker/web/