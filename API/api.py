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
        Crie um itinerário de viagem somente com as seguintes informações: {details}.
        O título deve ser em h1, com o destino da viagem.
        Para cada dia da viagem, adicione um subtítulo em h2, indicando o dia correspondente.
        Inclua um parágrafo indicando a duração total da viagem.
        Adicione uma lista não ordenada com as atividades turísticas para cada dia.
        Para cada atividade, crie um evento em lista ordenada com uma descrição breve.
        Inclua um parágrafo com uma sugestão para a viagem.
        """
        
        resposta = model.generate_content(prompt)
        print(resposta)

        viagem = '\n'.join(resposta.text.strip().split('\n'))

        return jsonify({"viagem": viagem}), 200
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)