#The Dockerfile was written by referring to 
#https://github.com/ruddra/docker-django to deploy Django 
#using Nginx, Celery, Redis, and Postgresql with Docker.
FROM ubuntu:latest
# FROM python:3.6-alpine

ENV LANG=C.UTF-8
ENV TZ=Asia/Seoul
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata g++ git curl

# installing java jdk and java jre
RUN apt-get install -y default-jdk default-jre

# installing python3 and pip3
RUN apt-get install -y python3-pip python3-dev

# install postgres module
RUN apt-get install -y python3-psycopg2

RUN cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    ln -s /usr/bin/pip3 pip && \
    pip3 install --upgrade pip

# apt cleanse
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# timezone
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# make workspace
RUN mkdir -p /workspace
WORKDIR /workspace

# install konlpy dependencies: jpype, konlpy, with mecab module
RUN pip install jpype1-py3 konlpy
RUN cd /workspace && curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh


ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /src
RUN mkdir /static
RUN mkdir /config

WORKDIR /src
ADD ./src /src

RUN apt-get update
RUN apt-get install -y  \
    postgresql \
    libxml2-dev \
    libxslt-dev \
    zlib1g-dev \
    libjpeg-dev \
    gcc \
    musl-dev \
    cmake 
# postgresql-contrib 
# zlib \  
# jpeg \
# openblas \ 
# libstdc++ 

# RUN apt-get install build-deps \
#     libxml2-dev \
#     libxslt-dev \
#     gcc \  
# python3-dev \ 
# musl-dev \
# postgresql-dev\
# zlib-dev \
# jpeg-dev \ 
# openblas-dev \
# cmake \
# && ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip3 install --upgrade pip
COPY ./config/requirements.txt /config/
RUN pip install -r /config/requirements.txt

# removing temporary packages from docker and removing cache 
# RUN apt del build-deps && \
#     find -type d -name __pycache__ -prune -exec rm -rf {} \;

# CMD will run when this dockerfile is running
# CMD ["sh", "-c", "python3 manage.py collectstatic --no-input; python3 manage.py migrate; gunicorn web.wsgi -b 0.0.0.0:8000 & celery --app decider.tasks worker --loglevel=INFO"]
# CMD ["sh", "-c", "python3 manage.py collectstatic --no-input; python3 manage.py migrate; gunicorn web.wsgi -b 0.0.0.0:8000"]