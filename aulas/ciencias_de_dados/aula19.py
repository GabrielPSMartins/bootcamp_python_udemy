# Adicionando com for loop

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gas = pd.read_csv("Gas/gas_prices.csv")

list_countries = ["USA", "Canada", "Mexico"]

for country in gas:
    if country in list_countries:
        plt.plot(gas["Year"], gas[country], label=country)


plt.xticks(gas["Year"][::4])

plt.xlabel("Years")
plt.ylabel("Price (in USD)")

plt.legend()
plt.savefig("grafico_gas.png")
