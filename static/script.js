async function submitForm(){
    loading(0)
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
        const response = await fetch('http://127.0.0.1:5000/viagem', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}, 
            body: JSON.stringify(data)
        })
        
        const result = await response.json()

        const responseDiv = document.getElementById('response')
        if (result) {
            const viagem = result.join('')
            responseDiv.innerHTML = viagem
            loading(1)
        } else {
            responseDiv.innerHTML = `<p>Erro: ${result.Erro}</p>`
        }
        responseDiv.style.display = 'block'
    } catch (error) {
        const responseDiv = document.getElementById('response')
        responseDiv.innerHTML = `<p>Erro: ${error.message}</p>`
        responseDiv.style.display = 'block'
        loading(1)
    }
}

function loading(a){
    const load = document.getElementById('loading')
    const response = document.getElementById('response')
    const button = document.getElementById('buttonViagem')
    if (a == 0){
        button.disabled = true;
        load.style.display = 'block';
        response.style.display = 'none';
    } else {
        button.disabled = false;
        load.style.display = 'none';
        response.style.display = 'block';
    }
}

