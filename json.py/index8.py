import json

# Abrir o arquivo orders.json
with open("json.py\orders.json",) as file:
    # Carregar seu conteúdo e torná-lo um novo dicionário
    data = json.load(file)

    # Excluir o par chave-valor "client" de cada pedido
    for order in data["orders"]:
        del order["client"]

# Abrir (ou criar) um arquivo orders_new.json 
# e armazenar a nova versão dos dados.
with open("orders_new.json", 'w') as file:
    datas= json.dump(data, file, indent=4)

