import json
import requests

# Faz uma solicitação à API de clima
response = requests.get('https://api.open-meteo.com/v1/forecast')
print(response)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Carrega os dados JSON da resposta
    dados_clima = json.loads(response)

    # Acessa os dados do clima
    temperatura = dados_clima['temperatura']
    umidade = dados_clima['umidade']
    descricao = dados_clima['descricao']

     # Exibe as informações do clima
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
    print(f"Descrição: {descricao}")
else:
    print("Falha ao obter dados do clima")