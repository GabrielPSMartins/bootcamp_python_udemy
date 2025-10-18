# Extraindo variáveis de uma lista

produtos = ['notebook', 'tablet', 'smartphone ', 'monitor']

item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)