# Programação Orientada a Objetos

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def mostrar_nome(self):
        print(f"O nome da pessoa é {self.nome}")

    def mostrar_idade(self):
        print(f"A idade da pessoa é {self.idade}")

    def mostrar_profissao(self):
        print(f"A profissão da pessoa é {self.profissao}")

    def adicionar_idade(self):
        self.idade += 1
        print(f"A idade da pessoa agora é {self.idade}.")

    def mudar_profissao(self, nova_profissao):
        self.profissao = nova_profissao
        print(f"A profissão da pessoa agora é {self.profissao}.")

pessoa1 = Pessoa("João", 30, "Engenheiro")
pessoa2 = Pessoa("Maria", 25, "Médica")

print('\nPessoa 1:')
pessoa1.mostrar_nome()
pessoa1.mostrar_idade()
pessoa1.mostrar_profissao()
pessoa1.adicionar_idade()
pessoa1.mudar_profissao("Gerente")

print('\nPessoa 2:')
pessoa2.mostrar_nome()
pessoa2.mostrar_idade()
pessoa2.mostrar_profissao()
pessoa2.adicionar_idade()
pessoa2.mudar_profissao("Diretora")