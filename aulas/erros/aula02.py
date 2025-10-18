# Erros com input

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Por favor, digite um valor númerico.")