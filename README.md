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
![img.png](documentation/Screenshot_pip_install.png)

### Configure Django Project for IDE (PyCharm)

![img.png](documentation/Screenshot_Pycharm_Settings_Django.png)

### Run Configuration to start app from IDE

<img src="documentation/Screenshot_RunConfigurationSettings_DjangoServer.png" alt="" height="200"/>

DJANGO_SETTINGS_MODULE in den Environment variables setzen!
<img src="documentation/Screenshot_RunConfigurationSettings_DjangoSettingsModule.png" alt="" height="400"/>



### Database
- start manage.py terminal

<img src="documentation/Screenshot_start_manage_py_terminal.png" alt="" height="300"/>

<img src="documentation/Screenshot_manage_py_terminal.png" alt="" height="150"/>

- Migrations
```shell
$ makemigrations
$ migrate
```

- Für ein paar Dummy Daten (ohne Dateien)
```shell
seed exercise --number=3
```

## Notes for Development
### Generate requirements.txt from imports only (no dev tools)
```shell
$ pipreqs --force
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






