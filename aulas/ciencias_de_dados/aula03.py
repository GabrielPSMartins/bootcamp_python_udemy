# Adicionando uma coluna
import pandas as pd

dados = pd.read_csv('Fifa/fifa.csv')

print(dados)

dados['Total'] = dados['Acceleration'] + dados['Agility'] + dados['Reactions']
print("-----------------------------------------------------")
print(dados)

print("-----------------------------------------------------")
dados = dados[['Name', 'Total']]
print(dados.sort_values('Total', ascending=False))