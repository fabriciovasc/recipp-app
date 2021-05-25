function createRecipe() {
    const obj = prepareForm()

    if (!obj) {
        alert('Preencha todos os campos e tente novamente!')
    }

    let ajax = new XMLHttpRequest()
    ajax.open('POST', 'http://localhost:5000/recipes/create', true)
    ajax.setRequestHeader('Content-Type', 'application/json')

    ajax.onload = (() => {
        const res = JSON.parse(ajax.responseText)
        if (!res.error) {
            window.location.href = '/recipes/'
        } else {
            alert('Erro')
        }
    })

    ajax.onerror = (error => {
        console.log('ajax error:', error)
    })

    ajax.send(JSON.stringify(obj))
}

function prepareForm() {
    const checkedElements = Array.prototype.filter.call(document.getElementsByClassName('ingredient-item'), el => {
        return el.children[0].checked
    })
    const ingredients = checkedElements.map(el => el.children[0].id.split('_').pop())
    if (!ingredients.length) {
        return null
    }

    const name = document.getElementById('recipe_name')
    if (!name.value) {
        return null
    }

    const steps = document.getElementById('recipe_steps')
    if (!steps.value) {
        return null
    }

    return {
        ingredients,
        name: name.value,
        steps: steps.value
    }
}