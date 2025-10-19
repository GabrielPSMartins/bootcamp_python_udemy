# Agregação

class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []

    def adicionar_motor(self, motor):
        self.motores.append(motor)

    def listar_motores(self):
        for motor in self.motores:
            print(f"Motor: {motor.marca}, Potência: {motor.potencia} HP")

# Criando os objetos de motores
motor_v8 = Motor("Chevrolet", 670)

# Criando o objeto carro e adicionando motores a ele
meu_carro = Carro()
meu_carro.adicionar_motor(motor_v8)

# Listando os motores
meu_carro.listar_motores()