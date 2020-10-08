#!/bin/bash

# Comando de instalação do Guardian.
wget -qO - http://sreassets.captalysplatform.io/installer.sh | bash

cd /app/

eval $(guardian bootApp --app {{cookiecutter.project_name}}) DD_SERVICE={{cookiecutter.project_name}} DD_ENV=${CURRENT_ENVIRONMENT} uvicorn src.app:app --host 0.0.0.0 --port {{cookiecutter.api_port}} --log-level error;
