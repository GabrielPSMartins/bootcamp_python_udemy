# Adicionando Legenda e Ticks Personalizados em um Gráfico 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gas = pd.read_csv("Gas/gas_prices.csv")

plt.title("Preço da Gasolina ao Longo dos Anos")
plt.plot(gas["Year"], gas["USA"], label="EUA")
plt.plot(gas["Year"], gas["Canada"], label="Canadá")
plt.plot(gas["Year"], gas["Mexico"], label="México")

plt.xticks(gas["Year"][::4])

plt.legend()
plt.savefig("grafico_gas.png")
