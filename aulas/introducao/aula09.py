# Funções - são um bloco de construções que realizam uma tarefa específica

def somar(x, y):
	return x + y	

total = somar(4, 5)
print(f"O resultado da soma é de: {total}")

def calcular_desconto(preco, porcentagem):
	return preco - (preco * porcentagem / 100)
	
valor_final = calcular_desconto(100, 20)
print(f"O valor final com desconto é de R${valor_final:.2f}")
