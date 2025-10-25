'''
Use novamente a lista 'frutas' do desafio anterior.

Primeiro, altere o segundo elemento da lista (índice 1) de "banana" para "morango". Depois disso, adicione a 
fruta "abacaxi" ao final da lista. 
Por fim, imprima a lista modificada na tela.
'''

frutas = ["maça", "banana", "manga", "uva"]

frutas[1] = "morango"
frutas.append("abacaxi")

print(frutas)