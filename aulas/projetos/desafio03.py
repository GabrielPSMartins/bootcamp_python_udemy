'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

lista1 = Funcionários que tem carro e trabalham a noite
lista2 = Funcionários que tem carro e trabalham durante o dia
lista3 = Funcionários que não tem carro
'''

funcionarios = ["Gabriel", "Paulo", "Kaio", "Matheus", "Pietro", "Marcelo", "Julio"]
turno_dia = ["Gabriel", "Paulo", "Kaio", "Matheus"]
turno_noite = ["Pietro", "Marcelo", "Julio"]
tem_carro = ["Gabriel", "Paulo", "Kaio", "Matheus"]

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).intersection(tem_carro)
print(lista3)