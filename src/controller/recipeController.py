from flask import Blueprint, render_template, request

from src.controller.ingredientController import get_ingredients

recipe_controller = Blueprint('recipe', __name__, url_prefix='/recipes')


@recipe_controller.route('/')
def index():
    recipes = get_recipes()
    return render_template('recipe/recipe.html', title='Receitas', data={'recipes': recipes})


@recipe_controller.route('/create', methods=['GET', 'POST'])
def create_recipe():
    if request.method == 'POST':
        name = request.form.get('name')
        ingredients = request.form.get('ingredients')

    stored_ingredients = get_ingredients()
    return render_template('recipe/create-recipe/create-recipe.html', data={'stored_ingredients': stored_ingredients})


@recipe_controller.route('/edit/<id>')
def get_recipe_by_id(id):
    recipes = get_recipes()
    recipe = find_recipe(recipes, id)
    return render_template('recipe/edit-recipe/edit-recipe.html', data={'recipe': recipe})


@recipe_controller.route('/getRecipes', methods=['GET'])
def get_recipes():
    return [
        {
            'id': 1,
            'name': 'Bolo de fubá',
            'ingredients': {
                'Ovo': '3',
                'Oléo': '1 xícara',
                'Fubá': '1 xícara'
            },
            'steps': '1 - Misturar, 2 - Bater, 3 - Degustar',
            'created-at': '22/03/2021'
        },
        {
            'id': 2,
            'name': 'Bolo de chocolate',
            'ingredients': {
                'Ovo': '3',
                'Oléo': '1 xícara',
                'Fubá': '1 xícara',
                'Leite condensado': '1'
            },
            'steps': '1 - Misturar, 2 - Bater, 3 - Degustar',
            'created-at': '22/03/2021'
        }
    ]


def find_recipe(recipe_list, recipe_id):
    recipe_id = int(recipe_id)
    for recipe in recipe_list:
        if recipe['id'] == recipe_id:
            return recipe
