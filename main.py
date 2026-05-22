from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
    <h1>Bem-vindo!</h1>

    <a href="/fatos">Veja um fato aleatório</a><br><br>

    <a href="/motivacao">Veja uma frase motivacional</a>
    '''

@app.route("/fatos")
def frases():
    facts_list = [
        "Uma forma de combater a dependência tecnológica é buscar atividades que tragam prazer e melhorem o humor.",

        "Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, fazendo com que passemos o máximo de tempo possível consumindo conteúdo.",

        "As redes sociais têm pontos positivos e negativos, e devemos estar atentos a ambos ao utilizar essas plataformas."
    ]

    return f'<p>{random.choice(facts_list)}</p>'

# NOVA ROTA
@app.route("/motivacao")
def motivacao():
    frases_motivacionais = [
        "O sucesso é a soma de pequenos esforços repetidos diariamente.",
        
        "Nunca desista dos seus objetivos.",
        
        "Grandes conquistas começam com pequenas atitudes.",
        
        "A disciplina leva você onde a motivação não consegue.",
        
        "Seu futuro depende do que você faz hoje."
    ]

    return f'<h2>{random.choice(frases_motivacionais)}</h2>'

app.run(debug=True)
