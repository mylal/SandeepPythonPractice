FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /testapp

ADD . /testapp

COPY ./requirements.txt /testapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /testapp