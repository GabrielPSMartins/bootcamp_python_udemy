# Selecionando itens em arrays

import numpy as np

a = np.array([[10, 20, 30], [40, 50, 60]])
print(a)

# Selecionando o item na linha 1, coluna 2
item1 = a[1, 2]
print("Item selecionado:", item1)

# Selecionando todos os itens da linha 0
item2 = a[0,:]
print("Itens da linha 0:", item2)