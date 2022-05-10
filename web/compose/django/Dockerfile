#The Dockerfile was written by referring to 
#https://github.com/ruddra/docker-django to deploy Django 
#using Nginx, Celery, Redis, and Postgresql with Docker.
FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /src
RUN mkdir /static
RUN mkdir /config

WORKDIR /src
ADD ./src /src
RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg \
    openblas \ 
    libstdc++ 

RUN apk add --no-cache --virtual build-deps \
    gcc \  
    python3-dev \ 
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev \ 
    openblas-dev \
    cmake \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install --upgrade pip

COPY ./config/requirements.txt /config/
RUN pip install --no-cache-dir -r /config/requirements.txt

# removing temporary packages from docker and removing cache 
RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; 

# CMD will run when this dockerfile is running
# CMD ["sh", "-c", "python3 manage.py collectstatic --no-input; python3 manage.py migrate; gunicorn web.wsgi -b 0.0.0.0:8000 & celery --app decider.tasks worker --loglevel=INFO"]
CMD ["sh", "-c", "python3 manage.py collectstatic --no-input; python3 manage.py migrate; gunicorn web.wsgi -b 0.0.0.0:8000"]