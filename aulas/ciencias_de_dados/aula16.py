# Criando primeiro gráfico com Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gas = pd.read_csv("Gas/gas_prices.csv")

plt.plot(gas["Year"], gas["USA"])
plt.plot(gas["Year"], gas["Canada"])
plt.plot(gas["Year"], gas["Mexico"])
plt.savefig("grafico_gas.png")
