# Looping dentro de dicionário

aluno = {
    "nome": "Gabriel",
    "idade": 21,
    "curso": "Ciência da Computação"
}

for keys, values in aluno.items():
    print(keys, values)  # Imprime as chaves e valores do dicionário