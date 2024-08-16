# Assistente de viagens - README
## Descrição
O Assistente de Viagens é uma aplicação web que permite aos usuários inserir informações de viagem e gerar uma viagem personalizada com base nessas informações. A aplicação é composta por uma interface de usuário intuitiva onde as informações podem ser adicionados, e um backend que utiliza um modelo generativo para criar a viagem.

## Funcionalidades
- Adicionar informações: O usuário pode adicionar várias informações que deseja utilizar na viagem.
- Gerar viagem: Ao submeter os informações, uma viagem é gerada e exibida na tela, formatada em HTML.
## Estrutura do Projeto
- HTML (index.html): Estrutura a interface do usuário, permitindo a inserção de informações e a visualização da viagem gerada.
- CSS (style.css): Estiliza a interface, proporcionando uma experiência de usuário agradável.
- JavaScript (script.js): Manipula as interações do usuário, e faz a requisição ao backend para gerar a viagem.
- Backend (app.py): Utiliza o Flask para criar uma API que recebe os informações, comunica-se com o modelo generativo para criar a viagem, e retorna o resultado em formato HTML.
## Como Executar
### Requisitos
- Python 3.x
- Flask
- Flask-CORS
- Google Generative AI (Biblioteca gemini)
## Passos para Configuração
- Clone o repositório:
git clone https://github.com/otavioDev07/RoteiroDeViagens.git
cd RoteiroDeViagens

- Instale as dependências do Python:
pip install flask flask-cors google-generativeai

- Gere sua chave de API em: https://aistudio.google.com/app/u/1/apikey
- Adicione sua chave API do Google Generative AI no arquivo app.py na linha:
gemini.configure(api_key="SUA_CHAVE_API_AQUI")

- Execute a aplicação Flask:
python api.py

- Abra o arquivo index.html no navegador:
Utilize um servidor local, como Live Server no VS Code, ou abra o arquivo diretamente em seu navegador.

## Uso
- Insira as três informações no formulário da aplicação.
- Clique em "Gerar viagem".
- A viagem gerada será exibida na tela.
## Licença
Este projeto é licenciado sob a Licença MIT.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Contato
Para mais informações, entre em contato pelo email: netootavio223@outlook.com
