function deleteObj(id) {
    if (!id) {
        return null
    }

    let ajax = new XMLHttpRequest()
    ajax.open('DELETE', `http://localhost:5000/ingredients/delete/${id}`, true)
    ajax.setRequestHeader('Content-Type', 'application/json')

    ajax.onload = (() => {
        const res = JSON.parse(ajax.responseText)
        console.log(res)
        if (!res.error) {
            document.getElementById(`ingredient_${id}`).remove()
        } else {
            alert('Existe uma receita cadastrada com este ingrediente')
        }
    })

    ajax.onerror = (error => {
        console.log('ajax error:', error)
    })

    ajax.send(undefined)
}