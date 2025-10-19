# Polimorfismo 

class Personagens:
    def atacar(self):
        pass

class Guerreiro(Personagens):
    def atacar(self):
        print('Ataque com espada!')

class Mago(Personagens):
    def atacar(self):
        print('Lançando feitiço!')

class Arqueiro(Personagens):
    def atacar(self):
        print('Disparando flecha!')


# Criando objetos
personagens = [Guerreiro(), Mago(), Arqueiro()]

for personagem in personagens:
    personagem.atacar()