import json


# Define uma string contendo dados JSON
json_string = '''
[
    {
        "nome": "Ana",
        "idade": 25,
        "profissao": "Desenvolvedora"
    },
    {
        "nome": "Pedro",
        "idade": 35,
        "profissao": "Designer"
    },
    {
        "nome": "Lúcia",
        "idade": 40,
        "profissao": "Analista"
    }
]
'''

# Carrega os dados JSON da string
dados = json.loads(json_string)

# Itera sobre os usuários
for usuario in dados:
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")
    print()

    