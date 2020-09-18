import shutil

project_structure = "{{cookiecutter.structure}}"


# Se o projeto não utilizar POSTGRES, remove o diretorio de modelos
if project_structure == "API":
    shutil.rmtree("src/models/")
    shutil.rmtree("scripts/")
