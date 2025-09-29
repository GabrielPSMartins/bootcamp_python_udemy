class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
        self.seta = None        

    def informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} foi ligado.")
        else:
            print(f"O carro {self.modelo} já estava ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro {self.modelo} foi desligado.")
        else:
            print(f"O carro {self.modelo} já estava desligado.")

    def ligar_seta(self, direcao):
        if direcao in ["esquerda", "direita"]:
            self.seta = direcao
            print(f"A seta do carro {self.modelo} está ligada para {self.seta}.")
        else:
            print("Direção inválida. Use 'esquerda' ou 'direita'.")

print("\nCarro 1:")
carro1 = Carro("Fusca", "azul")
carro1.informacoes()
carro1.ligar()
carro1.ligar_seta("esquerda")

print("\nCarro 2:")
carro2 = Carro("Civic", "preto")
carro2.informacoes()
carro2.desligar()
carro2.ligar_seta("direita")