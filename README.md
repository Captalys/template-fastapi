#### Introdução
___
Este repositório contém o template base para a criação de novos robôs utilizando `fastApi`.



#### Utilização
____

Para utilizar o template deve-se instalar o cookiecutter, instruções [aqui](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).

Após a instalação ser concluída, pode-se utilizar o template de duas formas:

```shell script

# Diretamente do git
$ cookiecutter <url do repositório>/template-api-robo

# Clonando e executando localmente
$ git clone <url do repositório>/template-api-robo

cookiecutter template-api-robo

```

Após a execução de um dos comandos acima, serão solicitadas as informações para criação do projeto. **Importante**: o nome do projeto é utilizado para parametrizar diversas configurações dentro da arvore de diretórios, inclusive o `jenkinsfile`. Sendo assim, deve-se ter atenção no momento de escolher o nome. Caso deseje checar todos locais onde a variável com o nome do projeto é utilizada, basta acessar o diretório onde está o template e digitar:

```shell script
 grep -Fr "cookiecutter.project_name"
```
