'''
Mini desafio: Calcular quantos dias um produto duraria se a pessoa
usar X porções por dia
'''

total_porcoes = int(input("Digite quantas porções o produto tem: "))
porcoes_dia = int(input("Digite a quantidade de porções que você usa por dia: "))

dias = total_porcoes / porcoes_dia
print(f"Dias que o produto duraria: {dias:.0f}")