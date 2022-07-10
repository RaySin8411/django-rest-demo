FROM python:3.9
MAINTAINER Ray Sin

ENV PYTHONBUFFERED 1

RUN mkdir /django-files
WORKDIR /django-files

RUN git clone https://github.com/q8977452/django-rest-demo.git
RUN pip install -r requirements.txt


ENTRYPOINT python django-rest-demo/food_project/manage.py runserver 0.0.0.0:80