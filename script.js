async function submitForm(){
    const detailsInputs = document.getElementsByClassName('detail')
    const details = []
    for (let i = 0; i < detailsInputs.length; i++) {
        if (detailsInputs[i].value) {
            details.push(detailsInputs[i].value)
        }
    }
    
    if (details.length < 3){
        alert('Por favor, preencha os três três campos!')
        return 
    }

    const data = {details: details}

    try {
        const response = await fetch('http://localhost:5000/receita', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}, 
            body: JSON.stringify(data)
        })
        
        const result = await response.json()

        const responseDiv = document.getElementById('response')
        if (result.viagem) {
            responseDiv.innerHTML = result.viagem
        } else {
            responseDiv.innerHTML = `<p>Erro: ${result.Erro}</p>`
        }
        responseDiv.style.display = 'block'
    } catch (error) {
        const responseDiv = document.getElementById('response')
        responseDiv.innerHTML = `<p>Erro: ${error.message}</p>`
        responseDiv.style.display = 'block'
    }
}

