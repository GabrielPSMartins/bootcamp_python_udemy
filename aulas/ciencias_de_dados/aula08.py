# Filtrando com Regx e Condicionais
import pandas as pd
import re

df = pd.read_csv('House/melbourne.csv')

filter = df.loc[df['Address'].str.contains('^59', flags=re.I) & (df['Price'] <= 500000)]
print(filter) 