#The Dockerfile was written by referring to 
#https://github.com/ruddra/docker-django to deploy Django 
#using Nginx, Celery, Redis, and Postgresql with Docker.
FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
RUN mkdir /static
RUN mkdir /config

WORKDIR /src
ADD ./src /src

RUN apt-get update && apt-get install -y openjdk-11-jre-headless && apt-get clean

RUN apt-get update && apt-get install -y \
    postgresql \
    libxml2-dev  \  
    libxslt-dev \
    cmake \
    musl-dev 

RUN pip3 install --upgrade pip
COPY ./config/requirements.txt /config/
RUN pip install --no-cache-dir -r /config/requirements.txt && pip3 install tensorflow-aarch64 -f https://cf.tf.kmtea.eu/whl/stable.html

# removing temporary packages from docker and removing cache 
# RUN apt-get del build-deps && find -type d -name __pycache__ -prune -exec rm -rf {} \

# CMD will run when this dockerfile is running
# CMD ["sh", "-c", "python3 manage.py collectstatic --no-input; python3 manage.py migrate; gunicorn web.wsgi -b 0.0.0.0:8000 & celery --app decider.tasks worker --loglevel=INFO"]
CMD ["sh", "-c", "python3 manage.py collectstatic --no-input; python3 manage.py migrate; gunicorn web.wsgi -b 0.0.0.0:8000"]