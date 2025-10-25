# Visualizando itens, keys e values em dicionários

aluno = {
    "nome": "Gabriel",
    "idade": 21,
    "curso": "Ciência da Computação",
    "materias": ["Cálculo", "Algoritmos", "Estruturas de Dados"]
}

print(aluno)

print(aluno.get("materias"))  # Acessa o valor da chave "materias"
print(len(aluno))  # Imprime o número de itens no dicionário
print(aluno.keys())  # Imprime todas as chaves do dicionário
print(aluno.values())  # Imprime todos os valores do dicionário
print(aluno.items())  # Imprime todos os itens (pares chave-valor) do