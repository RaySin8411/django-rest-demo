FROM python:3.9
MAINTAINER Ray Sin

ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN git clone https://github.com/q8977452/django-rest-demo.git
RUN pip install django
RUN pip install djangorestframework


ENTRYPOINT python django-rest-demo/food_project/manage.py runserver 0.0.0.0:80