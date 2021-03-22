from flask import Blueprint, render_template

ingredient_controller = Blueprint('ingredient', __name__, url_prefix='/ingredients')


@ingredient_controller.route('/')
def index():
    ingredients = get_ingredients()
    return render_template('ingredient/ingredient.html', title='Ingredientes', data={'ingredients': ingredients})


@ingredient_controller.route('/getIngredients', methods=['GET'])
def get_ingredients():
    return [
        {
            'id': 1,
            'name': 'Ovo',
            'created_at': '22/03/2021'
        },
        {
            'id': 2,
            'name': 'Óleo',
            'created_at': '22/03/2021'
        },
        {
            'id': 3,
            'name': 'Fubá',
            'created_at': '22/03/2021'
        },
        {
            'id': 4,
            'name': 'Leite condensado',
            'created_at': '22/03/2021'
        }
    ]
