import json

from flask import Blueprint, render_template, request, current_app, Response
from flask_sqlalchemy import SQLAlchemy

from src.model.models import Recipe as RecipeModel
from src.model.models import Ingredient as IngredientModel

from src.controller.ingredientController import get_ingredients

recipe_controller = Blueprint('recipe', __name__, url_prefix='/recipes')


@recipe_controller.route('/', methods=['GET'])
def index():
    try:
        recipes = get_recipes().json['recipes']

    except Exception as error:
        print(error)
        recipes = []

    return render_template('recipe/recipe.html', title='Receitas', recipes=recipes)


def get_recipes():
    try:
        recipes = RecipeModel.query.all()
        if not recipes:
            raise Exception('Nenhuma receita')

        recipes = list(map(lambda x: {'id': x.id, 'name': x.name, 'ingredients': list(
            map(lambda ing: {'id': ing.id, 'name': ing.name}, x.ingredients)), 'steps': x.steps,
                                      'created_at': str(x.created_at)},
                           recipes))

        res = json.dumps({'recipes': recipes})
        return Response(res, mimetype='application/json', status=200)

    except Exception as error:
        res = json.dumps([])
        print(error)
        return Response(res, mimetype='application/json', status=500)


@recipe_controller.route('/create', methods=['GET', 'POST'])
def create_recipe():
    if request.json:
        try:
            db = SQLAlchemy(current_app)
            obj = request.json

            name = obj['name']
            steps = obj['steps']
            ingredient_ids = obj['ingredients']

            ingredients = list(map(lambda x: IngredientModel.query.filter_by(id=x).first(), ingredient_ids))

            recipe = RecipeModel(
                name=name,
                steps=steps,
                ingredients=ingredients
            )

            with current_app.app_context():
                db.session.merge(recipe)
                db.session.commit()

            res = json.dumps({'message': 'Receita cadastrada!', 'error': False})
            return Response(res, mimetype='application/json', status=200)

        except Exception as error:
            res = json.dumps({'message': str(error), 'error': True})
            return Response(res, mimetype='application/json', status=200)
    else:
        try:
            stored_ingredients = get_ingredients().json['ingredients']
        except Exception as error:
            print(error)
            stored_ingredients = []
        return render_template('recipe/create-recipe/create-recipe.html',
                               data={'stored_ingredients': stored_ingredients})


@recipe_controller.route('/edit/<_id>')
def get_recipe_by_id(_id):
    recipe = RecipeModel.query.filter_by(id=_id).first()
    return render_template('recipe/edit-recipe/edit-recipe.html', recipe=recipe)

