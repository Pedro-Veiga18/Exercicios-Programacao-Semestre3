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
        
    def inserir_inicio(self, valor):
        novo = No(valor)
        
        # verifica se a lista está vazia
        if self.tamanho == 0:
            #self.inicio = novo
            self.fim = novo
        else:
            novo.dir = self.inicio
            self.inicio.esq = novo
            # self.inicio = novo
        self.inicio = novo
        self.tamanho += 1
        
    def imprimir(self):
        aux = self.inicio
        while aux: # aux != None
            print(aux.dado, end=" ")
            aux = aux.dir
                
    def inserir_final(self, valor):
        novo = No(valor)
        if self.tamanho == 0:
            self.fim = novo
            self.inicio = novo
        else:
            self.fim.dir = novo
            novo.esq = self.fim
            
        self.fim = novo
        self.tamanho += 1    
    
    def pesquisar(self, valor):
        aux = self.inicio
        while aux:
            if aux.dado == valor:
                return aux
            aux = aux.dir
        return None
    
    def remover(self, valor):
        aux = self.pesquisar(valor)
        
        if aux:
            if self.tamanho == 1: # a lista tem apenas um valor
                self.inicio = None
                self.fim = None
            elif aux == self.inicio: # remove o primeiro elemento
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None
            elif aux == self.fim: # remove o último elemento
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None
            aux = None
            self.tamanho -= 1
                
                
                
 
# programa principal
"""
lista = Lista()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)
lista.inserir_final(40)
lista.inserir_final(50)
lista.imprimir()
"""

"""print()
lista.remover(30)
lista.remover(50)
lista.remover(10)
lista.remover(20)
lista.remover(40)
lista.imprimir()
"""