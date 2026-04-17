""" Exercício 01 — Verificar balanceamento de parênteses"""

""" Crie uma função que receba uma string contendo apenas parênteses e 
    verifique se eles estão balanceados, utilizando uma pilha.

    Regras:

    - Cada parêntese de abertura deve ter um correspondente de fechamento
    - Não é permitido fechar antes de abrir
    - A pilha deve estar vazia ao final da verificação


    Caso de teste
    Entrada
    (()())
    Saída 
    True
"""

from collections import deque

def verificar_valores(valores: str) -> bool:
    pilha = deque()
    
    for i in valores:
        if i == "(":
            pilha.append(i)
        elif i == ")":
            # Regra: Não é permitido fechar antes de abrir
            if len(pilha) == 0:
                return False
            pilha.pop()
    
    # Regra: A pilha deve estar vazia ao final da verificação
    return len(pilha) == 0
        

# Teste
valores = input("Digite uma sequencia de parenteses: ")
print(verificar_valores(valores))