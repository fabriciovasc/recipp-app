import json

from flask import Blueprint, render_template, request, current_app, Response
from flask_sqlalchemy import SQLAlchemy

from src.model.models import Ingredient as IngredientModel

ingredient_controller = Blueprint('ingredient', __name__, url_prefix='/ingredients')


@ingredient_controller.route('/')
def index():
    try:
        ingredients = get_ingredients().json['ingredients']
    except Exception as error:
        print(error)
        ingredients = []
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

        except Exception as error:
            res = json.dumps({'message': str(error), 'error': True})
            return Response(res, mimetype='application/json', status=500)
    else:
        return render_template('ingredient/create-ingredient/create-ingredient.html', title='Adicionar ingredientes')


@ingredient_controller.route('/edit/<_id>', methods=['GET', 'PUT'])
def update_ingredient(_id):
    if request.json:
        try:
            db = SQLAlchemy(current_app)
            obj = request.json

            ingredient = IngredientModel.query.filter_by(id=_id).first()
            ingredient.name = obj['name']

            with current_app.app_context():
                db.session.merge(ingredient)
                db.session.commit()

            res = json.dumps({'message': 'Ingrediente atualizado com sucesso', 'error': False})
            return Response(res, mimetype='application/json', status=200)
        except Exception as error:
            res = json.dumps({'message': str(error), 'error': True})
            return Response(res, mimetype='application/json', status=500)
    else:
        ingredient = IngredientModel.query.filter_by(id=_id).first()
        return render_template('ingredient/edit-ingredient/edit-ingredient.html', title='Editar ingrediente',
                               ingredient=ingredient)


@ingredient_controller.route('/delete/<_id>', methods=['DELETE'])
def delete_ingredient(_id):
    try:
        db = SQLAlchemy(current_app)

        with current_app.app_context():
            db.session.query(IngredientModel).filter_by(id=_id).delete()
            db.session.commit()

        res = json.dumps({'message': 'Ingrediente excluído', 'error': False})
        return Response(res, mimetype='application/json', status=200)

    except Exception as error:
        res = json.dumps({'message': str(error), 'error': True})
        return Response(res, mimetype='application/json', status=500)


@ingredient_controller.route('/getIngredients')
def get_ingredients():
    try:
        ingredients = IngredientModel.query.all()
        if not ingredients:
            raise Exception('Nenhum ingrediente')

        ingredients = list(map(lambda x: {'id': x.id, 'name': x.name, 'created_at': str(x.created_at)}, ingredients))
        res = json.dumps({'ingredients': ingredients})
        return Response(res, mimetype='application/json', status=200)

    except Exception as error:
        res = []
        return Response(res, mimetype='application/json', status=500)
