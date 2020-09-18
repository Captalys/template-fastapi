### Introdução 

Este repositório contém a implementação do robô **{{cookiecutter.project_name}}** para extração de fluxo. 


#### Estrutura

Abaixo a arvore de diretórios e arquivos contidos:

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

#### Configuração

Para que o robô funcione corretamente, são necessárias as seguintes configurações:

 - Adicionar as urls que serão consumidas no dicionário contido em `./src/utils/urls.URL_MAPPING`
 - Implementar os métodos `get_flow` e `login` da classe `Crawler` em `./src/core/crawler.py`

As variáveis de ambiente que o robô espera encontrar para funcionar corretamente são:

 - DATABASE_URL: Connection string para o banco de dados do `scorpion` no formato `postgresql://<user>:<pass>@<servidor>:<porta>/<dbname>`

 