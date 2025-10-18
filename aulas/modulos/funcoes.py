def somar():
    print("Essa função vai somar valores")

def mult():
    print("Essa função vai multiplicar valores")


def procurar_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1