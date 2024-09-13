# bookstore
BookStore API

Como configurar o projeto Django + Django Rest API FrameWork + Poetry

1 - instalar o poetry (global) pip install poetry
2 - iniciar um projeto com poetry -> poetry init 
3 - adicionar as dependencias do projeto (pytest, opcionais, etc...)
4 - adicionar o Django -> poetry add django
5 - criar o projeto Django -> poetry run django-admin.py startproject nomeapp
6 - ativar ambiente virtual, poetry shell
7 - instalar o Django Rest Framework -> poetry add djangorestframework 
8 - configurar o settings.py -> abra o arquivo settings.py -> adicionar 'rest_framework' ao INSTALLED_APPS = '['rest_framework',...]'
9 - criar uma nova applicação django -> poetry run python manage.py startapp NOME
10 - rodar migrações pendentes, poetry run python manage.py migrate
11 - verificar servidor -> poetry run python manage.py runserver
12 - (opcional) gerar arquivo das dependencias -> poetry show --tree --no-dev > requirements.txt 

----- 
