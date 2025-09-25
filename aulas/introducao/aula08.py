# Listas, dicionários e tuplas

# frutas = ['Abacaxi', 'Laranja']

# # (frutas[0]) Baseado em index
# frutas.append('Melancia')
# frutas.remove('Laranja')
# print(len(frutas))
# print(frutas)

# Listas - usada quanto uso vários valores mutáveis
tarefas = []

tarefas.append('Acordar')
tarefas.append('Escovar os dentes')
tarefas.append('Tomar café da manhã')

print("Minhas tarefas:")
for tarefa in tarefas:
    print(f'Tarefa: {tarefa}')

# Tuplas - usada quando uso vários valores imutáveis
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses[0])

# Dicionários - usada quando uso vários valores mutáveis e imutáveis
aluno = {
    'nome': input('Nome: '),
    'idade': int(input('Idade: ')),
    'cursos': input('Curso: ')
}

print(f"{aluno['nome']} tem {aluno['idade']} anos e está matriculado no curso de {aluno['cursos']}.")

# aluno['idade'] = 22
# aluno['cidade'] = 'São Paulo'

# print(aluno)