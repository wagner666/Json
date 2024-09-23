import json



# Abre o arquivo JSON em modo de leitura
with open('json.py\dados.json') as arquivo:
    # Carrega os dados JSON
    dados = json.load(arquivo)
    
    dados_escala = json.dumps(dados,indent=4, sort_keys=True)

# Agora você pode acessar os dados carregados como um objeto Python
print(dados_escala)








# Define uma string contendo dados JSON
# json_string = '{"nome": "Joao", "idade": 25}'

#  # Carrega os dados JSON da string
# dados = json.loads(json_string)

# # Agora você pode acessar os dados carregados como um objeto Python
# print(dados)