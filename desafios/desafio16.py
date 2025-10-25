"""
Para este desafio, crie uma lista de frutas que inclui "maçã" três vezes
e outras frutas da sua escolha. Use um loop for para contar quantas vezes
"maçã" aparece na lista e imprima o resultado.
"""

frutas = ["maçã", "banana", "laranja", "maçã", "uva", "maçã", "pera"]

const = 0 
for i in frutas: 
    if i == "maçã":
        const += 1

print(const)