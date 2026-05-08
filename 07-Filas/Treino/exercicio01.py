from collections import deque

clientes = ["João", "Maria", "Pedro"]

def atender_clientes(clientes:list) -> list:
    fila = deque()
    
    for i in range(len(clientes)) :
        fila.append(clientes[i])

    for i in range(2) :
        print(f"Cliente {fila[0]} sendo atendido")
        fila.popleft()
        
    clientes = []
    for i in fila:
        clientes.append(i)

    return clientes      

print(atender_clientes(clientes))  