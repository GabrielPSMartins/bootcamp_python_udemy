# print com f-string

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
fruta_favorita = input("Digite sua fruta favorita: ")
print(f"Olá {nome}, Sua idade é {idade} anos e sua fruta favorita é {fruta_favorita}.")
print(f"Olá {nome}, daqui 10 anos você terá {idade + 10} anos.")  # Note: idade is a string, this will concatenate '10' to the string