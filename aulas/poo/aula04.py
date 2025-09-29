# Herança multipla e Herança de Multinivel

class Animal():
	def __init__(self, nome):
		self.nome = nome

class Predador(Animal):
	def cacando(self):
		print(f"O animal {self.nome} está caçando!")
	
class Presa(Animal):
	def fugindo(self):
		print(f"O animal {self.nome} está sendo caçado!")
	
class Coelho(Presa):
	pass
	
class Tigre(Predador):
	pass
	
class Golfinho(Predador, Presa):
	pass
	
coelho1 = Coelho("Carlos")
tigre1 = Tigre("Roberto")
golfinho1 = Golfinho("Luiz")

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()