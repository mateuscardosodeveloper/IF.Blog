# Construindo uma rede social :technologist:
Desenvolvimento de uma rede social, pensando neste tempo de pandemia para aproximar as pessoas.

Trabalho do curso de Engenharia de Software IFPR, matéria Construção de Software.
# Como excutar na sua maquina :gear:

* Primeiro é necessário ter instalado o [python 3.6](https://www.python.org/) e o [pipenv](https://pipenv.pypa.io/en/latest/).

* Apos instalar as ferramentas, entre na pasta app/ e execute os comandos no terminal:

```bash
# Para entrar no ambiente
pipenv shell
# Para instalar as dependências
pipenv install 
```
* Antes de excutar o projeto é necessario criar o banco de dados.
```bash
# Cria as tabelas no banco de dados 
python manage.py migrate
```
* Agora excute o projeto.
```bash
# Excutar projeto
python manage.py runserver
```
* Para excutar os tests.

```bash
python manage.py test
```

