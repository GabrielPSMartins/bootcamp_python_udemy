# Funções em sets

lista1 = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9])
s1 = {1, 2, 3, 4, 5}

s1.add(6)
s1.update([7, 8, 9])
s1.remove(2)
s1.discard(10)  # Não gera erro se o elemento não existir
s1.pop()  # Remove um elemento aleatório

print(lista1)
print(s1)