# Operadores Aritméticos

num1 = 15
num2 = 38

print(num1 + num2)  # Adição
print(num1 - num2)  # Subtração
print(num1 * num2)  # Multiplicação
print(num1 / num2)  # Divisão
print(num1 // num2) # Divisão inteira
print(num1 % num2)  # Módulo
print(num1 ** num2) # Exponenciação


# Desconto

preco = float(input("Digite o preço: "))
desconto = int(input("Digite quanto de desconto tem esse produto: "))

novo_preco = preco - (preco * desconto / 100)

print(f"Novo preço: R${novo_preco}")