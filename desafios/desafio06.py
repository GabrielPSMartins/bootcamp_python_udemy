'''
Crie um script que solicita ao usuário dois números. EM seguida, o script vai precisar imprimir a soma, subtração, a multiplicação e a divisão (resultado decimal)
e a exponenciação (primeiro número elevado ao segundo número) desses dois números.
'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o primeiro número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
expo = num1 ** num2


print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Exponenciação: {expo}")