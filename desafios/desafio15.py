"""
Para este desafio, crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim que
chegar a 5 usando o comando "break". Em seguida, crie um segundo loop que imprima os números de 1
a 10, mas pule o número 5 usando o comando "continue".
"""

for i in range(1, 11):
    if i > 5:
        break
    print(i)

for i in range(1, 11):
    if i == 5:
        continue
    print(i)