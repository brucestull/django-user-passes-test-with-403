# Useful Commands and Links

## Commands

### This Project

1. `pipenv install django==4.2.1`
1. `pipenv shell`
1. `django-admin startproject forbidden_project .`
1. `python manage.py runserver`
1. <http://localhost:8000/>
1. `django-admin startapp forbidden_app`
1. `python manage.py migrate`
1. `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`

### Django Create `SECRET_KEY`

* `python manage.py shell`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`

## Development Server Links

* Server Root:
  * <http://localhost:8000/>
* Admin:
  * <http://localhost:8000/admin/>
  * <http://localhost:8000/users/>

## Repository Links

* Repository [`README.md`](../README.md)
