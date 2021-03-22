from flask import Blueprint, render_template

recipe_controller = Blueprint('recipe', __name__, url_prefix='/recipes')


@recipe_controller.route('/')
def index():
    recipes = get_recipes()
    return render_template('recipe/recipe.html', title='Receitas', data={'recipes': recipes})


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
            'created-at': '22/03/2021'
        }
    ]
