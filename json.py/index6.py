import requests
import json

tempo = requests.get("https://cep.awesomeapi.com.br/json/05424020")

print(tempo)


print(tempo.json())

print('\n')

tempo_cpf = tempo.json()

ten = json.dumps(tempo_cpf, indent=4)

print(ten)

