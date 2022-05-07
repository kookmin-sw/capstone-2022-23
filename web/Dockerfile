FROM ubuntu:20.04


RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa


RUN apt-get update
RUN apt install -y python3.9
RUN apt install -y python3-pip
RUN apt install -y python3.9-dev libpq-dev


# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
RUN update-alternatives --config python3


RUN apt-get install -y net-tools
RUN apt-get install -y dnsutils
RUN apt-get update


ENV PYTHONUNBUFFERED 0


WORKDIR /code


COPY requirements.txt /code/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
# FROM python:3

# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt

# ENV DOCKERIZE_VERSION v0.2.0  
# RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
#     && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
# COPY ./entry.sh /code/entry.sh

# COPY . /code/

# ENTRYPOINT [ "/code/entry.sh" ]
# EXPOSE 8000  

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# EXPOSE 8000