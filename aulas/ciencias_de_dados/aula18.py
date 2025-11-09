# Formatando label e cores

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gas = pd.read_csv("Gas/gas_prices.csv")

plt.title("Preço da Gasolina ao Longo dos Anos")
plt.plot(gas["Year"], gas["USA"], 'r.--', label="EUA")
plt.plot(gas["Year"], gas["Canada"], 'g.-', label="Canadá")
plt.plot(gas["Year"], gas["Mexico"], 'b.-', label="México")

plt.xticks(gas["Year"][::4])

plt.xlabel("Years")
plt.ylabel("Price (in USD)")

plt.legend()
plt.savefig("grafico_gas.png")
