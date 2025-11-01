# abrindo um arquivo CSV com Pandas

import pandas as pd

dados = pd.read_csv('Fifa/fifa.csv')

print(dados)


print("-----------------------------------------------------")
# Mostra as 5 primeiras seções, mas posso colocar entre Parenteses a quantidade
print(dados.head())

print("-----------------------------------------------------")
# Mostra as 5 últimas seções
print(dados.tail())

print("-----------------------------------------------------")
dados.columns # mostra as colunas
print(dados.columns)

print("-----------------------------------------------------")
# Mostra a quantidade de linhas
print(dados.index)

print("-----------------------------------------------------")
print(dados[['Name', 'Nationality']])

print("-----------------------------------------------------")
#Localiza as informações conforme index enviado
print(dados.iloc[0:4])