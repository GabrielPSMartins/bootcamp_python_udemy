# Filtrando dados com condições
import pandas as pd

df = pd.read_csv('House/melbourne.csv')

# Filtrando casas com 3 quartos e do tipo 'h' (house)
filter1 = df.loc[(df['Rooms'] == 3) & (df['Type'] == 'h')]
print(filter1)