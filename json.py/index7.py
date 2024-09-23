import json
import pandas as pd
import matplotlib.pyplot as plt


# Abre o arquivo JSON em modo de leitura
with open('json.py\dados.json') as arquivo:
    # Carrega os dados JSON
    dados = json.load(arquivo)

    # Carregar os dados para um DataFrame do Pandas
    df = pd.DataFrame(dados)

    # Mostra os dados com DataFrame
    print(df)

    # Plotar um gráfico simples com os dados
    df.plot(kind='bar')

    # Definir os rótulos do eixo x com os nomes dos dados
    plt.xticks(range(len(df)), df.columns)

    
    plt.ylabel('Valores')

    plt.show()