# Erros com Else e finally

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Por favor, digite um valor númerico.")
finally:
    print("código ok")



# else: 
#    print("Usuario um valor correto")
#    resultado = valor * 2
#    print(resultado)
