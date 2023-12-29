# Semester Project With Django

Follow the instructions ...

## Setup

### Virtual Env
- Python 3.11

![img.png](documentation/Screenshot_virtual_env.png)

- Install required packages
```shell
$ pip install -r requirements.txt
```

### Database
- start manage.py terminal

<img src="documentation/Screenshot_start_manage_py_terminal.png" alt="" height="300"/>

<img src="documentation/Screenshot_manage_py_terminal.png" alt="" height="150"/>

- Migrations

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






