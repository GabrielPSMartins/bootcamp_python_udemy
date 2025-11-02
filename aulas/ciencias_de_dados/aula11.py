# Introdução ao Numpy

import numpy as np
import sys

listaA = [1, 2, 3, 4, 5]
listaB = np.array([1, 2, 3, 4, 5])

print(listaA)
print(listaB)

print(f'Tamanho da lista padrão: {sys.getsizeof(listaA)} bytes')
print(f'Tamanho do array Numpy: {sys.getsizeof(listaB)} bytes')