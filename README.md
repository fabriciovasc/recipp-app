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

## Iniciar projeto
- Clonar e atualizar repositório
```
git clone https://github.com/fabsvas/recipp-app.git
cd recipp-app
git checkout master
git pull
```

- Instalando virtualenv
```
pip/pip3 install virtualenv
```

- Inicializando ambiente virtual
```
 python/python3 -m venv env
 source env/bin/activate
```

- Instalação das dependências
```
pip/pip3 install -r requirements.txt
```

- Configurando ambiente

Configure a conexão com o MySQL no arquivo **.env** localizado na raiz do projeto de acordo com o exemplo a seguir
```
MYSQL_DATABASE=receitas
MYSQL_HOST=localhost
MYSQL_PORT=3306 // porta padrão
MYSQL_USERNAME=root // usuário do servidor MySQL
MYSQL_PASSWORD=1234554321 // senha do usuário do servidor MySQL
```

- Criando collection (banco de dados)

Uma vez iniciado, será criado a collection **receitas**, após subir a aplicação com sucesso encerre para inicializar com o Gunicorn ou WSGI
```
python/python3 wsgi.py create_db
```

- Inicializando aplicação

Gunicorn (somente em shell)
```
gunicorn --bind IP:PORTA wsgi:app

gunicorn --bind 0.0.0.0:1234 wsgi:app
```

WSGI (windows terminal ou shell)
```
python/python3 wsgi.py
```

- Acessando aplicação

Acesse **http://localhost:1234** para acessar o sistema de gerenciamento de receitas

## Entregas parciais

- [Entrega 1 - Protótipo navegável](https://youtu.be/KG1fHToLZtw)
