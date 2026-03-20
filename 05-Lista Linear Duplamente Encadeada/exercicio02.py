# Uma plataforma de streaming utiliza um sistema de recomendação que mantém uma
# sequência de conteúdos sugeridos para cada usuário. Essa sequência é armazenada em
# uma lista duplamente encadeada, onde cada elemento representa um conteúdo recomendado.

# Com o objetivo de variar as sugestões apresentadas ao usuário, o sistema
# periodicamente realiza uma rotação na lista de recomendações. Essa rotação consiste
# em deslocar os primeiros elementos da lista para o final da estrutura, preservando a
# ordem relativa dos demais elementos.

# Por exemplo, considere a seguinte lista de recomendações: 10 20 30 40 50. Se o sistema
# aplicar uma rotação de k = 2 posições, os dois primeiros elementos devem ser movidos
# para o final da lista, resultando em: 30 40 50 10 20.

from lista_dupla import Lista

def rotacionar(lista: Lista, n: int) -> None:
    # não há rotação
    if n == 0 or lista.tamanho == 1 or n == lista.tamanho:
        return 
    
    # calcular o valor do deslocamento quando n for maior que o tamanho
    n = n % lista.tamanho
    
    # se o valor de n for múltiplo, não rotaciona
    if n == 0:
        return
    
    # auxiliar para percorrer a lista e encontrar o "novo" início
    aux = lista.inicio
    for _ in range(n):
        aux = aux.dir
        
    # configura o novo inicio e o novo fim
    novo_inicio = aux
    novo_fim = aux.esq
    
    novo_inicio.esq = None
    novo_fim.dir = None
    
    lista.fim.dir = lista.inicio
    lista.inicio.esq = lista.fim
    
    lista.fim = novo_fim
    lista.inicio = novo_inicio

lista = Lista()
lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_final(30)
lista.inserir_final(40)
lista.inserir_final(50)


rotacionar(lista, 22)
lista.imprimir()