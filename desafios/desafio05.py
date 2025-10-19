'''
Crie um script que pergunte o nome e a idade do usuário, usando a função input().
Depois disso, o script vai imprimir uma mensagem que diga 'Olá, [nome]! Você tem [idade] anos. 
'''

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

print(f'Olá, {nome}! Você tem {idade} anos.')