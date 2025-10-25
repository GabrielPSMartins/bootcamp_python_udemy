# Verificando itens em uma lista

fruta_desejada = input("Digite a fruta que deseja verificar: ")
frutas = ["banana", "melancia", "uva", "laranja"]

if fruta_desejada.lower() in frutas:
    print(f"{fruta_desejada} está na lista de frutas.")
else:
    print(f"{fruta_desejada} não está na lista de frutas.")