# SETUP

#### env

1.setup venv
a.python3 -m venv env
b.source env/bin/activate

##### django App

admin folder contain the django app
2.install django
a.python3 -m pip install Django
3.django admin init
a.django-admin startproject admin
4.server start
a.cd admin
b.python3 manage.py runserver
5.setup dockerfile
6.setup docker compose

---

##### flask app

main folder contain the flask app

1. create requiments file

# General commands

### docker

1. docker-compose up
2. docker-compose exec backend sh

### manage.py

1. python manage.py startapp products//generate new app called products
2. python manage.py makemigrations
3. python manage.py migrate
