def somar(*numeros):
    """
    Soma uma quantidade variável de números.
    Parâmetro:
        *numeros: empacota todos os argumentos posicionais em uma tupla chamada `numeros`.
    Retorna:
        A soma de todos os valores passados.
    """
    total = 0
    for numero in numeros:
        total += numero
    return total

# Exemplos de uso:
print(somar(1, 2, 3))       
print(somar(5, 10, 15, 20)) 