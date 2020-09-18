#!/bin/bash

until psql ${DATABASE_URL} -c '\q'; do
    echo "Aguardando conectividade com o POSTGRES"
    sleep 2
done;
echo "Executando o processo localmente no Docker";

uvicorn src.app:app --host 0.0.0.0 --port {{cookiecutter.api_port}} --reload  --log-level trace;