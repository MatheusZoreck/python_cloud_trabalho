from flask import Flask, jsonify

app = Flask(__name__)

alunos = ["Ana", "João", "Maria"]

@app.route("/")
def home():
    return "Bem-vindo à API Flask!"

@app.route("/alunos")
def listar_alunos():
    return jsonify(alunos)

@app.route("/saudacao/<nome>")
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo à API."

@app.route("/curso/<curso>")
def curso(curso):
    return f"Você está no curso de {curso}."

if __name__ == "__main__":
    app.run(debug=True)