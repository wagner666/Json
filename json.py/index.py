import requests


requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print("\n")

print(requisicao)
print("\n")

print(requisicao.json())
print("\n")

dc_requisicao = requisicao.json()

# Usando len para obter o número de chaves no dicionário
num_chave = len(dc_requisicao)
print("\n")

# Usando range para iterar sobre o número de chaves
for i in range(num_chave):
    chave = list(dc_requisicao)

print(chave)
print("\n")

print(dc_requisicao['USDBRL']['bid'])