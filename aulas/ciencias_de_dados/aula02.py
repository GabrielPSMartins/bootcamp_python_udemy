# Utilizando as funções do pandas para manipulação de dados (Loc e Sorted)
import pandas as pd

dados = pd.read_csv('Fifa/fifa.csv')

print(dados)

# Buscando um item específico
print("-----------------------------------------------------")
print(dados.loc[dados['Nationality'] == 'Brazil'])

print("-----------------------------------------------------")
# Ordena as linhas
print(dados.sort_values(['Name', 'Age']))