from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

gemini.configure(api_key="AIzaSyDqPqxbooA3im6ZQrXhRWEOio6SE4G81IE") #Adicione aqui sua chave de API do Gemini
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/viagem', methods=['POST'])
def make_trip():
    try:
        dados = request.json
        details = dados.get('details')

        prompt = f""" 
Crie um itinerário de viagem em HTML para as seguintes informações: {details}. Se por acaso não encontrar a atividade turística para o local informado, diga que não encontrou tais eventos naquela localização e forneça uma sugestão de outro evento. Se você não encontrar a localização pedida, retorne que você não pode encontrar, e somente isso. Não esqueça de sempre retornar uma estrutura HTML, pois sua resposta será aplicada diretamente em minha aplicação. Não escreva "``html" na sua resposta. Na frente do nome de cada atividade insira um emoji correspondente. Se você receber informações que julgar aleatórias ou sem sentido, retorne exatemente isso <h3>Suas informações parecem ser aleatorizadas ou sem sentido. Por favor, digite novamente.</h3>. Nos eventos, retorne o nome dos locais na localização fornecida. Se a localização estiver assim "nome XX", considere que o primeiro é o nome da cidade, e o segundo é o estado.

<h1 style="text-align:center;">Título da Viagem</h1>
<p style="text-align:center;">Duração da Viagem: ... dias</p>

<h2 style="text-align:center;">Dia 1</h2>
<ul style="text-align:center;">
    <li><h3>Atividade 1</h3></li>
    <p style="text-align:center;">Descrição breve</p>

    <li><h3>Atividade 2</h3></li>
    <p style="text-align:center;">Descrição breve</p>

    ... Repita a estrutura anterior com base no numero de dias da viagem."
</ul>

<h2 style="text-align:center;">Dia 2</h2>
<ul style="text-align:center;">
</ul>

<p style="text-align:center;">Sugestão: ...</p>
"""


        
        resposta = model.generate_content(prompt)
        print(resposta)

        viagem = resposta.text.strip().split('\n')

        return jsonify(viagem), 200
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)