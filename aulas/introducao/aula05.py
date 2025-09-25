# Operadores relacionais e Operadores lógicos

num1 = 10
num2 = 3

print(num1 == num2) # igual, idêntico
print(num1 != num2) # diferente
print(num1 > num2) # maior que
print(num1 < num2) # menor que
print(num1 >= num2) # maior ou igual a
print(num1 <= num2) # menor ou igual a

# Para dirigir tem que ter mais de 18 anos e ter carteira
idade = int(input("Qual é a sua idade? "))
carteira = False
verificador = idade >= 18 and carteira
print(verificador)

