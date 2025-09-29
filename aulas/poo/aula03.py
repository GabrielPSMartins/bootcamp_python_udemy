# Herança
class Animal:
	def __init__(self, nome, cor):
		self.nome = nome
		self.cor = cor
		
	def apresentar(self):
		print(f"Meu nome é {self.nome} e sou {self.cor}")
		
class Gato(Animal):
	def emitir_som(self):
		print("Miau")
		
class Cachorro(Animal):
	def comer(self):
		print("O cachorro está comendo")
	
gato1 = Gato("Kiko", "Branco")
gato1.apresentar()
gato1.emitir_som()	
	
cachorro1 = Cachorro("Nupi", "Preto")
cachorro1.apresentar()
cachorro1.comer()