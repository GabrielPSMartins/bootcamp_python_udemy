"""
Para este desafio, crie uma lista de números de 1 a 10. Use um 'for loop' para iterar sobre
a lista. Se o número atual da iteração for par, imprima "O número [número] é par". Se o 
número for ímpar, imprima "O número [número] é ímpar".cle
"""

numeros = list(range(1, 11))

for numero in numeros:
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")
