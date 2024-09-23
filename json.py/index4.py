import json

carro_dictionary = {
    "marca":"honda",
    "modelo":"HRV",
    "cor":"prata"
}
# dictionary -> objeto json

carros_list = ["honda","volkswagem","ford","fiat","chevrolet"]
#list -> array json

carros_tupla = ("honda","volkswagem","ford","fiat","chevrolet")
#tupla -> array json 

carros_j = json.dumps(carro_dictionary,indent=4,separators=(": ","="),sort_keys=True)

print(carros_j)
print(carros_tupla)
print(carros_j)

print('\n')

jogador = '{"nome":"Bruno","time":"Aviadores","vivo":"True","energia":100,"mochila":["pederneira","corda","linha","arame"],"aeronav":[{"tipo":"Transporte","habilidade":80},{"tipo":"Ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

mostra = json.loads(jogador)

for c in jogador:
    print(c)