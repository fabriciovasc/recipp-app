# Recipp 

## Aluno
- Fabrício da Cunha Vasconcellos

## Objetivo
- Desenvolver um sistema Web para criação de receitas em Python

## Tecnologias
- MySQL
- Flask
- SQLAlchemy
- Jinja2
- Gunicorn
- HTML5, CSS e Javascript

# Configuração

## Requerimentos mínimos
- Python V3.6 ou >
- MySQL Database

## Inicialização do ambiente

#### Clonar e atualizar repositório
```
git clone https://github.com/fabsvas/recipp-app.git
cd recipp-app
git checkout master
git pull
```

#### Instalando virtualenv
```
pip/pip3 install virtualenv
```

#### Inicializando ambiente virtual no Linux
```
 python/python3 -m venv env
 source env/bin/activate
```

#### Inicializando ambiente virtual no Windows
```
 python/python3 -m venv env
 cd env/Scripts
 activate
```

#### Instalação das dependências
```
pip/pip3 install -r requirements.txt
```

#### Conexão com o banco de dados

Configure a conexão com o MySQL no arquivo **.env** localizado na raiz do projeto de acordo com o exemplo a seguir
```
MYSQL_DATABASE=receitas
MYSQL_HOST=localhost
MYSQL_PORT=3306 // porta padrão
MYSQL_USERNAME=root // usuário do servidor MySQL
MYSQL_PASSWORD=1234554321 // senha do usuário do servidor MySQL
```

#### Criando schema e tabelas
```
python/python3 wsgi.py create_db
```

Uma vez iniciado, será criado o schema **receitas** e as respectivas tabelas:
- [x] ingredient
- [x] recipe
- [x] recipe_ingredient  

Após subir a aplicação com sucesso encerre para inicializar com o **Gunicorn** ou **WSGI**

## Subindo a aplicação

#### Para rodar a aplicação

> Gunicorn 

**Atente-se, o _Gunicorn_ só funcionará em _sistemas UNIX_**
```
gunicorn --bind <host:porta> wsgi:app

Exemplo: gunicorn --bind 0.0.0.0:1234 wsgi:app
```

> WSGI
```
python/python3 wsgi.py
```

## Entregas parciais

- [Entrega 1 - Protótipo navegável](https://youtu.be/KG1fHToLZtw)
- [Entrega 2 - Persistência de dados](https://youtu.be/4iKZfBt7s8k)
