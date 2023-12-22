# Semester Project With Django

Follow the instructions ...

## Setup
```shell
$ makemigrations
$ migrate
```

```shell
$ createsuperuser
```

Reset DB and populate with fake data:

- install packages: django-seed, psycopg2
- delete all wxyz_*.py files in /migrations
- in manage.py@terminal:

```shell
$ reset_db --noinput
$ makemigrations exercise
$ migrate exercise
$ seed exercise --number=3
```


## Development
### Generate requirements.txt from imports only (no dev tools)
```shell
$ pipreqs --force
```






