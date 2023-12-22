# Semester Project With Django

Follow the instructions ...

## Setup
```bash
$ makemigrations exercise
$ migrate exercise
```


Reset DB and populate with fake data:

- install packages: django-seed, psycopg2
- in manage.py@terminal:

```bash
$ reset_db --noinput
$ makemigrations exercise
$ migrate exercise
$ seed exercise --number=3
```







