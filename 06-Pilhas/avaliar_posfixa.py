from collections import deque

def avaliar(expressao: str) -> str:
    pilha = deque()
    
    for ch in expressao:
        if ch != ' ':
            if ch == '+': 
                y = pilha.pop()
                x = pilha.pop()
                resultado = x + y
                pilha.append(resultado)
            elif ch == '-': 
                y = pilha.pop()
                x = pilha.pop()
                resultado = x - y
                pilha.append(resultado)
            
            elif ch == '*': 
                y = pilha.pop()
                x = pilha.pop()
                resultado = x * y
                pilha.append(resultado)
            
            elif ch == '/': 
                y = pilha.pop()
                x = pilha.pop()
                resultado = x // y
                pilha.append(resultado)
                
            elif ch == '^': 
                y = pilha.pop()
                x = pilha.pop()
                resultado = x ** y
                pilha.append(resultado)
                
            elif ch == '%': 
                y = pilha.pop()
                x = pilha.pop()
                resultado = x % y
                pilha.append(resultado)
            
                
            else:
                pilha.append(int(ch))
                
    resultado_final = pilha.pop()
        
    return resultado_final
                



# Programa principal
expressao = input('Informe a expressão posfixa --> ')
valor = avaliar(expressao)
print(valor)