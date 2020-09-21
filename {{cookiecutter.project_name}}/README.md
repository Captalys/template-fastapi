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
├── docker-compose.yaml
├── Dockerfile-dev
├── entrypoint-dev.sh
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
├── src/
│   ├── app.py
│   ├── core/
│   │   ├── base.py
│   │   ├── crawler.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── resources/
│   │   ├── crawler.py
│   │   ├── healthcheck.py
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   └── utils/
│       ├── __init__.py
│       └── urls.py
└── tests/

```
