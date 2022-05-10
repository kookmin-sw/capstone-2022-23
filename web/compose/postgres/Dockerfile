#The Dockerfile was written by referring to 
#https://github.com/ruddra/docker-django to deploy Django 
#using Nginx, Celery, Redis, and Postgresql with Docker.
FROM postgres:11-alpine

COPY ./compose/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin && rmdir /usr/local/bin/maintenance