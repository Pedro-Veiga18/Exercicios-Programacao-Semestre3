class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        
class ABB:
    def __init__(self):
        self.raiz = None
        
    # Método para inserir um dado na árvore binária de busca
    def inserir(self, dado):
        self.raiz = self._inserir(self.raiz, dado)
        
    # Método recursivo para inserir um dado na árvore
    def _inserir(self, no, dado):
        if no is None:
            return No(dado)
        
        if dado < no.dado:
            no.esq = self._inserir(no.esq, dado)
        elif dado > no.dado:
            no.dir = self._inserir(no.dir, dado)
        
        return no
    
    # Método para fazer o percurso em ordem
    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado
    
    # Método auxiliar recursivo para fazer o percurso em ordem
    def _em_ordem(self, no, resultado):
        if no is None:
            return
        
        self._em_ordem(no.esq, resultado)
        resultado.append(no.dado)
        self._em_ordem(no.dir, resultado)
        
    # Método para remover um elemento da árvore
    def remover(self, dado):
        self.raiz = self._remover(self.raiz, dado)
    
    # Método auxiliar (recursivo) para remover um elemento
    def _remover(self, no, dado):
        if no is None:
            return None
        
        if dado < no.dado:
            no.esq = self._remover(no.esq, dado)
        elif dado >  no.dado:
            no.dir = self._remover(no.dir, dado)
        else:
            # Caso 1 -> O nó não tem filhos (é uma folha)
            if no.esq is None and no.dir is None:
                return None
            
            # Caso 2 -> O nó só tem um filho
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq
            
            # Caso 3 -> O nó tem dois filhos
            sucessor = self.buscar_menor(no.dir)
            no.dado = sucessor.dado
            no.dir = self._remover(no.dir, sucessor.dado)
            
        return no
    
    def buscar_menor(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
            
            
        return atual
        
        
            
        
        
        
        
############################################
if __name__ == '__main__':
    print('*' * 85)
    arvore = ABB()
    arvore.inserir(15)
    arvore.inserir(7)
    arvore.inserir(10)
    arvore.inserir(25)
    arvore.inserir(20)
    arvore.inserir(35)
    
    print(arvore.em_ordem())
    
    arvore.remover(20)
    print(arvore.em_ordem())
    
    arvore.remover(7)
    print(arvore.em_ordem())
    
    arvore.remover(15)
    print(arvore.em_ordem())
    
    
        
    