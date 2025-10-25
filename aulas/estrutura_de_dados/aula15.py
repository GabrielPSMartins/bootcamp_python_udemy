# Atualizando itens no dicionário

aluno = {
    "nome": "Gabriel",
    "idade": 21,
    "curso": "Sistemas de Informação",
}

aluno.update({"curso": "Ciência da Computação"})  # Atualizando o curso
# aluno.update({"período": "Noturno"})  # Adicionando um novo par chave-valor

del aluno["idade"]  # Removendo a idade

print(aluno)
print(aluno.get("curso"))  # Acessando o valor atualizado do curso