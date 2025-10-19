# Nested Classes - Classes Aninhadas

# Classe Principal
class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_cores, cpu_clock):
        self.modelo = modelo
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)

    def mostrar_configuracao(self):
        print(f"Computador: {self.modelo}")
        self.gpu.mostrar_gpu()
        self.cpu.mostrar_cpu()

    # Classe Aninhada
    class GPU:
        def __init__(self, nome, memoria):
            self.nome = nome
            self.memoria = memoria

        def mostrar_gpu(self):
            print(f"GPU: {self.nome}, Memória: {self.memoria}GB")

    # Classe Aninhada
    class CPU:
        def __init__(self, nome, cores, clock):
            self.nome = nome
            self.cores = cores
            self.clock = clock

        def mostrar_cpu(self):
            print(f"CPU: {self.nome}, Cores: {self.cores}, Clock: {self.clock}GHz")

# Utilização das Classes
meu_computador = Computador("Gaming PC", "NVIDIA RTX 3080", 10, "Intel i9", 8, 5.0)
meu_computador.mostrar_configuracao()
