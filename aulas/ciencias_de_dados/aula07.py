# Filtrando com Expressões Regulares

import pandas as pd
import re

df = pd.read_csv('House/melbourne.csv')

# Filtrando endereços que contenham 'Turner St' ou 'Turner Rd'
filter = df.loc[df['Address'].str.contains('Turner St|Turner Rd', flags=re.I)]
print(filter)