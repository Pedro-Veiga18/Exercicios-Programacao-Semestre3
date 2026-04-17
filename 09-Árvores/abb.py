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
        
        
        
############################################
if __name__ == '__main__':
    print('*' * 85)
    arvore = ABB()
    arvore.inserir(15)
    arvore.inserir(7)
    arvore.inserir(10)
    arvore.inserir(25)
    
    print(arvore.em_ordem())
    
    
        
    