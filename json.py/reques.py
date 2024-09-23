# import requests

# print('#####################')
# print('### Consultar CEP ###')
# print('#####################')
# print()

# cep_input = input('Digite o CEP para consulta: ')

# if len(cep_input) != 8:
#     print('Quantidade de dígitos inválida!')
# else:
#     response = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
#     data = response.json()

#     if 'erro' in data:
#         print('CEP não encontrado.')
#     else:
#         print(f'CEP: {data["cep"]}')
#         print(f'Logradouro: {data["logradouro"]}')
#         print(f'Bairro: {data["bairro"]}')
#         print(f'Cidade: {data["localidade"]}')
#         print(f'Estado: {data["uf"]}')


import phonenumbers
from phonenumbers import geocoder
import requests

# Número de telefone (substitua pelo número que você deseja rastrear)
numero_telefone = "+5515996462127"

# Normaliza o número de telefone
telefone_ajustado = phonenumbers.parse(numero_telefone, "BR")

# Obtém a descrição da localização
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(f"Localização do número {numero_telefone}: {local}:")



