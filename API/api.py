from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

gemini.configure(api_key="SUA_CHAVE_API_AQUI") #Adicione aqui sua chave de API do Gemini
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/viagem', methods=['POST'])
def make_trip():
    try:
        dados = request.json
        details = dados.get('details')

        prompt = f""" 
        Crie um itinerário de viagem em HTML para as seguintes informações: {details}.

        **Estrutura do HTML:**

        * **Título (h1):** O título da viagem, com o destino.
        * **Dias da viagem (h2):** Cada dia da viagem deve ter um subtítulo h2 com o dia correspondente.
        * **Duração da viagem (p):** Um parágrafo com a duração total da viagem.
        * **Atividades turísticas (ul):** Para cada dia, adicione uma lista não ordenada (ul) com as atividades turísticas.
        * **Eventos (ol):** Para cada atividade, crie uma lista ordenada (ol) com uma descrição breve.
        * **Sugestão (p):** Um parágrafo com uma sugestão para a viagem.

        **Exemplo de estrutura (sem conteúdo):**

        ```html
        <h1>Título da Viagem</h1>
        <p>Duração da Viagem: ... dias</p>

        <h2>Dia 1</h2>
        <ul>
        <li>
            <h3>Atividade 1</h3>
            <ol>
            <li>Descrição breve</li>
            </ol>
        </li>
        <li>
            <h3>Atividade 2</h3>
            <ol>
            <li>Descrição breve</li>
            </ol>
        </li>
        </ul>

        <h2>Dia 2</h2>
        <ul>
        </ul>

        ...
        """
        
        resposta = model.generate_content(prompt)
        print(resposta)

        viagem = resposta.text.strip().split('\n')

        return jsonify(viagem), 200
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)