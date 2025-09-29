def exibir_informacoes(**dados):
    """
    Exibe pares chave=valor passados como argumentos nomeados.
    Parâmetro:
        **dados: empacota todos os argumentos nomeados em um dicionário chamado `dados`.
    """
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

# Exemplo de uso:
exibir_informacoes(nome="Juliano", idade=27, cidade="Rio de Janeiro")
