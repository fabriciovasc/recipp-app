import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

from src.model.ingredientModel import db as ingredient
from src.model.recipeModel import db as recipe

load_dotenv(find_dotenv())

try:
    template_dir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'src')
    template_dir = os.path.join(template_dir, 'view')

    app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)

    _USERNAME = os.getenv('MYSQL_USERNAME')
    _PASS = os.getenv('MYSQL_PASSWORD')
    _DB = os.getenv('MYSQL_DATABASE')
    _HOST = os.getenv('MYSQL_HOST')
    _PORT = os.getenv('MYSQL_PORT')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{_USERNAME}:{_PASS}@{_HOST}:{_PORT}/{_DB}'

    ingredient.init_app(app)
    recipe.init_app(app)


except Exception as err:
    print(f'Error: {err}')


def initialize_db(flask):
    db = SQLAlchemy(flask)
    engine = db.create_engine(f'mysql://{_USERNAME}:{_PASS}@{_HOST}:{_PORT}/{_DB}', {})
    try:
        engine.execute(f'CREATE DATABASE {_DB}')
    except Exception as err:
        print(f'Error database: {err}')
        pass
    with flask.app_context():
        ingredient.create_all()
        recipe.create_all()


@app.route('/')
def root():
    # TODO: add render source
    return render_template('')


if __name__ == '__main__':
    app.run()
