""" Exercício 03 — Remover duplicatas consecutivas
    Crie uma função que receba uma string e remova pares de caracteres iguais consecutivos 
    utilizando uma pilha.

    Regras

    Percorrer a string caractere por caractere
    Se o topo da pilha for igual ao caractere atual, remover o topo
    Caso contrário, empilhar o caractere
    Reconstruir a string ao final


    Caso de teste
    Entrada
    abbaca

    Saída esperada
    ca

"""

from collections import deque

valor = input("Digite uma sequencia de caracteres para eu remover os pares repetidos: ")

def remover_par(valor:str)-> str: 
    pilha = deque()
    texto = ""

    for i in valor:
        if len(pilha) == 0 :
            pilha.append(i)
        else :
            if i == pilha[-1]: 
                pilha.pop()
            else:
                pilha.append(i)
    
    for i in pilha:
        texto += i

    return texto



    

print(remover_par(valor))


