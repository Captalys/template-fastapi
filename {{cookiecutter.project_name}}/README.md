# fastapi example 

How Captalys is working in Python FastAPI to build Services APIs to its internal processes.

## General guidelines

1. RESTful APIs, follows some guidelines provided by [WhiteHouse/api-standards](https://github.com/WhiteHouse/api-standards)
2. Documentation and consistency of APIs are very important to us
3. Tests, we would think about what need to be tested.
4. Program towards interfaces instead of concrete implementations

### Configuration


You need to provide an environment variable called `DATABASE_URL` in
order to the project work properly.


### Structure

Tree structure that will be created:

```shell script
.
├── conftest.py
├── docker-compose.yaml
├── Dockerfile
├── Dockerfile-dev
├── entrypoint-dev.sh
├── entrypoint.sh
├── jenkinsfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── scripts/
│   ├── Dockerfile-psql
│   └── schema.sql
├── setup.py
├── sonar-project.properties
├── src/
│   ├── app.py
│   ├── core/
│   │   └── __init__.py
│   ├── exceptions/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models/
│   │   ├── fake_db.py
│   │   └── __init__.py
│   ├── routes/
│   │   ├── example.py
│   │   ├── healthcheck.py
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   └── utils/
│       └── __init__.py
└── tests/


```


In order to this project work correctly with jenkins, all additional packages need to be included in the `setup.py` file inside `install_requires`.

### Testing

When running the project locally it includes `pytest` and `coverage`. In order to run them use the following command:

```shell script

# Pytest
$ docker exec <project_name>-api coverage run -m pytest

# Coverage report
$ docker exec <project_name>-api coverage report -m
```