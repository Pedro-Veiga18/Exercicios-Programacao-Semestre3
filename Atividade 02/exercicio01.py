class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        
        
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    
    #a)
    def inserir(self, valor): #insere um valor no final da lista
        novo = No(valor)
        if self.tamanho == 0: #se a lista estiver vazia
            self.inicio = novo
            self.fim = novo
            novo.dir = novo
            novo.esq = novo
            self.tamanho += 1
        else:                 
            self.fim.dir = novo
            novo.esq = self.fim
            self.fim = novo
            novo.dir = self.inicio
            self.inicio.esq = novo
            self.tamanho += 1
            
            
    #b)
    def inserir_posicao(self, posicao, valor): #insere um valor na posição desejada
        novo = No(valor)
        
        
        if self.tamanho == 0: #se a lista estiver vazia
            self.inicio = novo
            self.fim = novo
            novo.dir = novo
            novo.esq = novo
            self.tamanho += 1
            return
            
        elif posicao == 1: #se for inserir no inicio
            novo.dir = self.inicio
            self.inicio.esq = novo        
            self.inicio = novo
            novo.esq = self.fim
            self.fim.dir = novo
            self.tamanho += 1
            return
        
        elif posicao > self.tamanho: #se for inserir em uma posição maior que a lista
            novo.esq = self.fim
            novo.dir = self.inicio
            self.fim.dir = novo
            self.inicio.esq = novo
            self.fim = novo
            self.tamanho += 1
            return
                    
        else: #se for inserir no meio
            aux = self.inicio
            posicao_atual = 1
            
            while posicao_atual < posicao:
                aux = aux.dir
                posicao_atual += 1
            
            novo.esq = aux.esq
            novo.dir = aux
            aux.esq.dir = novo
            aux.esq = novo
            self.tamanho += 1
    
    
    #c)        
    def imprimir(self): #imprime a lista completa
        aux = self.inicio
        while aux: 
            print(aux.dado, end=" ")
            aux = aux.dir
            if aux == self.inicio:
                break
         
            
    def pesquisar(self, valor): #encontra um valor na lista
        aux = self.inicio
        while aux:
            if aux.dado == valor:
                return aux
            aux = aux.dir
            if aux == self.inicio:
                break
        return None
    
    
    #d) 
    def remover(self, valor): #remove um valor da lista
        aux = self.pesquisar(valor) #serve para encontrar o valor que sera removido
        
        if aux:
            if self.tamanho == 1: 
                self.inicio = None
                self.fim = None
            elif aux == self.inicio:
                self.inicio = aux.dir
                self.inicio.esq = self.fim
                self.fim.dir = self.inicio
            elif aux == self.fim: 
                self.fim = aux.esq
                self.fim.dir = self.inicio
                self.inicio.esq = self.fim
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None
            aux = None
            self.tamanho -= 1

    
