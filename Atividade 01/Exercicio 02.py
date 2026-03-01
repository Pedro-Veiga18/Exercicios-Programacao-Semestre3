def insercao(A):
    n = len(A)
    for j in range(1, n):
        valor = A[j]
        i = j - 1
        while i >= 0 and valor < A[i]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = valor



def frequencia(A: list):
    todos = []
    numero = []
    mais_f = 0
    maior = 0
        
    for i in range(len(A)):
        if A[i] not in numero:
            numero.append(A[i])           
            vezes = []
            vezes.append(A[i])
            for j in range (i +1, len(A)):
                if A[i] == A[j]:
                    vezes.append(A[i])
            todos.append(vezes)          
                
        
    for k in range(len(todos)):        
        if len(todos[k]) > mais_f:
            mais_f = len(todos[k])
            maior = numero[k]
     
     
    #c)       
    mesma_f = True
    f1 = len(todos[0])

    for f in todos:
        if len(f) != f1:
            mesma_f = False
    
    if mesma_f == True:
        print("Todos os valores apresentam a mesma frequência")
    else:
        print(f"O número com maior frequência é {maior}, com f = {mais_f}")

                          
        
def main():
    #a) 
    A = []
    n = int(input("Digite a quantidade de números inteiros: "))
    max_inter = 4 * n
    print(f"Insira números entre 0 e {max_inter}")
    for i in range(n):
        numero = int(input("Insira o número: "))
        if numero >= 0 and numero <= max_inter:
            A.append(numero)
        else:
            print("Número fora do intervalo")
            return
        
    #b)
    insercao(A)
    frequencia(A)
    
    

    
    
    


#Programa principal
if __name__ == '__main__':
    main()