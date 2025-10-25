# Lambda dentro de uma função

def somar(x):
    fun2 = lambda x: x + 10
    return fun2(x) * 4

print(somar(5))  # Chama a função somar com o argumento 5