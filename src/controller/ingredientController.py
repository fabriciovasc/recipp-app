from flask import Blueprint, render_template, request

ingredient_controller = Blueprint('ingredient', __name__, url_prefix='/ingredients')


@ingredient_controller.route('/')
def index():
    ingredients = get_ingredients()
    return render_template('ingredient/ingredient.html', title='Ingredientes', data={'ingredients': ingredients})


@ingredient_controller.route('/create', methods=['GET', 'POST'])
def create_ingredients():
    if request.method == 'POST':
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
