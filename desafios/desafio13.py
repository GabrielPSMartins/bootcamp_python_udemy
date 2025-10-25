"""
Para este desafio, crie uma lista de frutas e outra de vegetais.
Use um "for loop" aninhado (Nested for loop) para imprimir todas as
combinações possíveis de frutas e vegetais, com a fruta primeiro e o vegetal
em segundo.
"""

frutas = ["morango", "banana", "maçã"]
vegetais = ["cenoura", "alface", "tomate"]

for fruta in frutas:
    for vegetal in vegetais:
        print(f"{fruta} - {vegetal}")