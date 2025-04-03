def apresenta_lista(lista):
    """
    Função que recebe uma lista de produtos e devolve uma string formatada.
    """
    if not lista:
        return "Nenhum produto encontrado."
    
    resultado = "Produtos encontrados:\n"
    for produto in lista:
        resultado += f"- {produto}\n"
    
    return resultado