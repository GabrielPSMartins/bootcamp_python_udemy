# Modificando dados no dataframe
import pandas as pd

df = pd.read_csv('House/melbourne.csv')

df.loc[df['SellerG'] == 'Nelson', 'SellerG'] = 'Gabriel'
print(df.loc[df['SellerG'] == 'Gabriel'])
