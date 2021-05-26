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
MYSQL_USERNAME=root // usuário administrador com todos previlégios do servidor MySQL
MYSQL_PASSWORD=1234554321 // senha do usuário administrador do servidor MySQL
```
**Utilize _usuário_ e _senha_ com previlégios de _administrador_**

- Exemplo:
  ```bash
  $ sudo mysql -u root -p
  mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
  mysql> ALTER USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
  mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
  mysql> GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'admin'@'localhost';
  mysql> exit;
  $ sudo service mysql restart 
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
