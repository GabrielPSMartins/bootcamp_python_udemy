# Criando sets


lista1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
lista2 = [5, 6, 7, 8, 9, 10, 11, 12]

num1 = set(lista1)
num2 = set(lista2)

print(num1 | num2)  # União
print(num1 & num2)  # Interseção
print(num1 - num2)  # Diferença
print(num1 ^ num2)  # Diferença simétrica

print(len(num1))