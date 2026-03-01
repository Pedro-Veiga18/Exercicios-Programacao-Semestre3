#Complexidade: O(n3)
def verificar(A: list) -> int:
    existe = 0
    for i in range(2, len(A)):
        for j in range(i):
            for k in range(j):
                if A[i] == A[j] + A[k] and j != k:
                    existe = 1
                    
    return existe          

def existe_soma(existe: int):
    if existe == 1:
        print("Existe um elemento que é a soma de dois anteriores.")  
    elif existe == 0:
        print("Nenhum elemento é a soma de dois anteriores." )            

def main():
    #a) 
    A = []
    n = int(input("Digite a quantidade de números inteiros: "))
    for i in range(n):
        A.append(int(input("Insira o número: ")))
        
    #b)
    existe = verificar(A)
    
    #c)
    existe_soma(existe)
    

#Programa principal
if __name__ == '__main__':
    main()