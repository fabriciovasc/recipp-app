const savedIngredients = [];

function create() {
    if (!savedIngredients.length) {
        return null
    }

    let count = savedIngredients.length

    savedIngredients.forEach((obj, index) => {
        let ajax = new XMLHttpRequest()
        ajax.open('POST', 'http://localhost:5000/ingredients/create', true)
        ajax.setRequestHeader('Content-Type', 'application/json')

        ajax.onload = (() => {
            count--
            const res = JSON.parse(ajax.responseText)
            if (count == 1) {
                if (!res.error) {
                    window.location.href = '/ingredients/'
                }
            } else {
                if (res.error) {
                    alert('Erro de cadastro')
                }
            }
        })

        ajax.onerror = (error => {
            console.log('ajax error:', error)
        })

        ajax.send(JSON.stringify(obj))
    })
}

function addIngredient() {
    document.getElementById('submit-ingredients').disabled = false;
    const ingredient = document.getElementById('ingredient-name')
    savedIngredients.push({name: ingredient.value})
    ingredient.value = ''
    const listIngredients = document.getElementById('listIngredients')
    listIngredients.innerText = savedIngredients.map(i => i.name).join(', ')
}
