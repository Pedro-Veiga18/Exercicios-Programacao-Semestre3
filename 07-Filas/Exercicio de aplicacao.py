from collections import deque

def vender(transacao) -> float:
    fila = deque()
    montante = 0
    
    for t in transacao:
        tipo = t[0]
        if tipo == 'C':
            qtd = t[1]
            valor = t[2]
            fila.append([qtd, valor])
        elif tipo == 'V':
            qtd_venda = t[1]
            valor_venda = t[2]
            
            while qtd_venda > 0:
                lote = fila[0]
                if lote[0] <= qtd_venda:
                    montante += lote[0] * (valor_venda - lote[1])
                    qtd_venda -= lote[0]
                    fila.popleft()
                else:
                    lote[0] -= qtd_venda
                    montante += qtd_venda * (valor_venda - lote[1])
                    qtd_venda = 0
                    
    return montante
                    


# programa principal
transacao = [('C', 100, 20), 
             ('C', 20, 24), 
             ('C', 200, 36), 
             ('V', 150, 30)]

montante = vender(transacao)
print(f'Montante R$ {montante:.2f}')