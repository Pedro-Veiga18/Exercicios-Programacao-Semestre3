from collections import deque

valor = [5, 10, 15, 20]

def retornar_primeiro(valor:list ) -> int :
    fila = deque()

    for i in range(len(valor)) :
        fila.append(valor[i])

    return fila[0]

print(retornar_primeiro(valor))