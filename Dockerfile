FROM python:3.9
MAINTAINER Ray Sin

ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN git clone https://github.com/q8977452/django-rest-demo.git
RUN cd django-rest-demo
RUN pip install -r requirements.txt


ENTRYPOINT python food_project/manage.py runserver 0.0.0.0:80