# Argumentos xargs com números

def soma(*numeros):
	resultado = 0
	for num in numeros:
		resultado += num
	return resultado
	
x = soma(1, 2, 3, 4, 5)
print(x)