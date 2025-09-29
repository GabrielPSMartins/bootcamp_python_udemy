# Argumentos xargs nomeando parametros

def agencia(**carro):
	return carro
	
print(agencia(marca="Gol", cor="Branca", motor=1.0, placa=1234))
print(agencia(marca="Gol", cor="Branca"))
print(agencia(marca="Gol", cor="Branca", motor=1.0))