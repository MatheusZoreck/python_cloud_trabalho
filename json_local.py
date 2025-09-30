import json

alunos = [
    {"nome": "Ana", "idade": 20, "curso": "ADS"},
    {"nome": "João", "idade": 22, "curso": "CC"}
]

# Salvar
with open("alunos.json", "w", encoding="utf-8") as f:
    json.dump(alunos, f, ensure_ascii=False, indent=4)

# Ler
with open("alunos.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    print("Alunos cadastrados:")
    for aluno in dados:
        print(aluno)