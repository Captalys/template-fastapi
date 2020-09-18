#!/bin/bash

cd /app/

eval $(guardian bootApp --app {{cookiecutter.project_name}}) DATADOG_SERVICE_NAME={{cookiecutter.project_name}} DATADOG_ENV=${CURRENT_ENVIRONMENT} uvicorn src.app:app --host 0.0.0.0 --port {{cookiecutter.api_port}} --log-level error;
