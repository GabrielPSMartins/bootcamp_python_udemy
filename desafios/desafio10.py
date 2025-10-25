"""
Comece com a lista "frutas" do desafio anterior.
Primeiro, remova a fruta "manga" da lista usando o método remove(). Depois
disso, remova o último item da lista usando o comando del. Por fim, 
imprima a lista modificada na tela.
"""

frutas = ["maça", "morango", "banana", "manga", "uva", "abacaxi"]

frutas.remove("manga")
del frutas[-1]
print(frutas)   