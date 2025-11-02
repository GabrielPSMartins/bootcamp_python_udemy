# Agrupando dados com GroupBy
import pandas as pd

df = pd.read_csv('House/melbourne.csv')

df.groupby(['SellerG']).mean() # Agrupa os dados por 'SellerG' e calcula a média para cada grupo
df.groupby(['SellerG']).sum().sort_values('Price', ascending=False) # Agrupa por 'SellerG', soma os valores e ordena por 'Price' em ordem decrescente
df = df.groupby(['SellerG']).count() # Conta o número de ocorrências para cada 'SellerG'
