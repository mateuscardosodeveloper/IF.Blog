# Construindo uma rede social :technologist:
Desenvolvimento de uma rede social, pensando neste tempo de pandemia para aproximar as pessoas.

Trabalho do curso de Engenharia de Software IFPR, matéria Construção de Software.
# Como excutar na sua maquina :gear:

* Primeiro é necessário ter instalado o [python 3.6](https://www.python.org/) e o [pipenv](https://pipenv.pypa.io/en/latest/).

* Apos instalar as ferramentas, crie um arquivo .env dentro da pasta /app.
```properties
#contendo o screaty key, para o django funcionar.
SECRET_KEY = 'k@k@%pmp6$v*6)&&$5#+e#9$f%t8pv^*aoawpgacqa1ycr1b1n'
```
* Agora excute os seguintes comandos no terminal dentro da pasta /app.

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
* para acessar o painel de admin, é necessário criar um super usuário.

```bash
python manage.py createsuperuser
# insira um email e a senha.
# URL do painel admin http://127.0.0.1:8000/admin/
```

