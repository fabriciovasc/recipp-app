import json

from flask import Blueprint, render_template, request, current_app, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from src.model.ingredientModel import Ingredient as IngredientModel

ingredient_controller = Blueprint('ingredient', __name__, url_prefix='/ingredients')


@ingredient_controller.route('/')
def index():
    ingredients = get_ingredients().json
    return render_template('ingredient/ingredient.html', title='Ingredientes', data={'ingredients': ingredients})


@ingredient_controller.route('/create', methods=['GET', 'POST'])
def create_ingredients():
    if request.json:
        try:
            db = SQLAlchemy(current_app)
            obj = request.json

            ingredient = IngredientModel(**obj)

            with current_app.app_context():
                db.session.add(ingredient)
                db.session.commit()

            res = json.dumps({'message': 'Ingrediente cadastrado!', 'error': False})
            return Response(res, mimetype='application/json', status=200)

        except SQLAlchemyError as error:
            res = json.dumps({'message': 'Não foi possível cadastrar o ingrediente!', 'error': True})
            return Response(res, mimetype='application/json', status=500)
    else:
        ingredients = request.form.get('ingredients')
        return render_template('ingredient/create-ingredient/create-ingredient.html', title='Adicionar ingredientes')


@ingredient_controller.route('/edit', methods=['GET', 'PUT'])
def update_ingredients():
    stored_ingredients = get_ingredients()
    if request.method == 'PUT':
        ingredients = request.form.get('ingredients')
    return render_template('ingredient/edit-ingredient/edit-ingredient.html', title='Editar ingredientes',
                           data={'ingredients': stored_ingredients})


@ingredient_controller.route('/getIngredients')
def get_ingredients():
    try:
        ingredients = IngredientModel.query.all()
        if not ingredients:
            raise Exception('Nenhum ingrediente')

        ingredients = list(map(lambda x: {'id': x.id, 'name': x.name, 'created_at': str(x.created_at)}, ingredients))
        res = json.dumps(ingredients)
        return Response(res, mimetype='application/json', status=200)

    except Exception as error:
        res = []
        return Response(res, mimetype='application/json', status=500)

