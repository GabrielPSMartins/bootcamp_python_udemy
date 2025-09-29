def demonstracao(primeiro, *args, opcional=None, **kwargs):
    """
    Demonstra a ordem de captura de diferentes tipos de argumentos.
    Parâmetros:
        primeiro: argumento posicional obrigatório.
        *args: empacota argumentos posicionais adicionais em uma tupla.
        opcional: exemplo de argumento nomeado com valor padrão (pode ser omitido).
        **kwargs: empacota argumentos nomeados adicionais em um dicionário.
    """
    print("Primeiro argumento:", primeiro)
    print("Args adicionais:", args)
    print("Parâmetro opcional:", opcional)
    print("Argumentos nomeados extras:", kwargs)

# Exemplo de uso:
demonstracao(123, 'a', 'b', opcional='Valor opcional', cor='vermelho', tamanho=42)
