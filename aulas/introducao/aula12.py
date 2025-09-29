# Funções 
# DRY - Don't repeat youself
# print() é uma função que apenas mostra dados no console
# return é uma instrução que encerra a função e devolve um valor ao código chamador, permitindo usá‑lo em expressões e variáveis

def client1(nome):
	print(f"Olá {nome}")

def client2(nome):
	return f"olá {nome}"
	
client1("Maria")
print(client2("Jose"))
