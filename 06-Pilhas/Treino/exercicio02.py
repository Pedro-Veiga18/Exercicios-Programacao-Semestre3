""" Exercício 02 — Inverter uma palavra utilizando pilha
    Crie uma função que receba uma string e retorne essa string invertida utilizando uma pilha.

    Regras

    Empilhe cada caractere da palavra
    Desempilhe todos os elementos para formar a nova string
    Não utilizar funções prontas de inversão

    Caso de teste
    Entrada
    python

    Saída esperada
    nohtyp

"""


from collections import deque

valor = input("Digite uma palavra para ser invertida ")

def inverter_string(valor: str) -> str:
    pilha = deque()
    invertido = ""    

    for i in valor:
        pilha.append(i)

    while pilha: 
        invertido += pilha[-1]
        pilha.pop()


    return invertido


print(inverter_string(valor))


