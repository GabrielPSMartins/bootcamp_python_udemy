# Exportando os dados
import pandas as pd

dados = pd.read_csv('Fifa/fifa.csv')

print(dados)

dados.to_csv('dados1.csv', index=False)  # Exporta sem o índice

dados.to_excel('dados2.xlsx', index=False)  # Exporta para Excel sem o índice

dados.to_csv('dados3.txt', index=False, sep='\t')  # Exporta para TXT sem o índice
