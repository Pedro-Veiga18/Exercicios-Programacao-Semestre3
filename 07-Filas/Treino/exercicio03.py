from collections import deque

paciente = ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo"]

def organizar_fila( paciente: list) -> str :
    fila = deque()
    for i in range(len(paciente)) :
        fila.append(paciente[i])

    while len(fila) > 1: 
        print(f"Paciente {fila[0]} foi atendido")
        fila.popleft()
        aux = fila[0]
        fila.popleft()
        fila.append(aux)
         
    return fila[0]

print(organizar_fila(paciente))