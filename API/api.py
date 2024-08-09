from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

gemini.configure(api_key="SUA_CHAVE_API_AQUI") #Adicione aqui sua chave de API do Gemini
model = gemini.GenerativeModel('gemini-1.5-flash')

@app.route('/viagem', methods=['POST'])
def make_receita():
    try:
        dados = request.json
        details = dados.get('details')

        prompt = f""" 
        Crie uma receita somente com os seguintes ingredientes: {details}.
        Apresente a receita no formato html com codificação UTF-8, sem o header,
        com o título em hl, subtítulos em h2, tempo de preparo em parágrafo
        acompanhado de um ícone de relógio, rendimento em porções em parágrafo
        acompanhado de um ícone de pratos, a lista de ingredientes em lista não
        ordenada, modo de preparo com passos em lista ordenada, sugestão para
        servir em parágrafo. Também forneça as medidas corretamento e também ingredientes adicionais (opcionais)
        """
        
        resposta = model.generate_content(prompt)
        print(resposta)

        viagem = '\n'.join(resposta.text.strip().split('\n'))

        return jsonify({"viagem": viagem}), 200
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True)