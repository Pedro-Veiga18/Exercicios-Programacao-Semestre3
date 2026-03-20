# Uma empresa de logística mantém duas filas de processamento de pedidos representadas 
# por listas duplamente encadeadas. A lista A contém pedidos de clientes premium. 
# A lista B contém pedidos de clientes comuns.
# Para garantir prioridade equilibrada, o sistema precisa gerar uma nova lista onde os
# pedidos sejam intercalados.

# Implemente um método que intercale duas listas e retorne a lista resultante. Por
# exemplo: Lista A: 1 3 5 e Lista B: 2 4 6. Resultado esperado: 1 2 3 4 5 6.


from lista_dupla import Lista

def intercalar(lista1: Lista, lista2: Lista) -> Lista:
    nova = Lista()
    p1 = lista1.inicio
    p2 = lista2.inicio
    
    while p1 is not None and p2 is not None:
        nova.inserir_final(p1.dado)
        nova.inserir_final(p2.dado)
        p1 = p1.dir
        p2 = p2.dir
    
    # ainda tem elemento na lista 1 ?
    while p1 is not None:
        nova.inserir_final(p1.dado)
        p1 = p1.dir
    
    # ainda tem elemento na lista 2 ?  
    while p2 is not None:
        nova.inserir_final(p2.dado)
        p2 = p2.dir
        
              
    return nova

A = Lista()   
A.inserir_final(1)
A.inserir_final(3)
A.inserir_final(5)

B = Lista()   
B.inserir_final(2)
B.inserir_final(4)
B.inserir_final(6)

C = intercalar(A, B)
C.imprimir()

