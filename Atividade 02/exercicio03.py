class Paciente:
    def __init__(self, nome, prioritario):
        self.nome = nome
        self.prioritario = prioritario
        self.esq = None
        self.dir = None
        
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    
    #a)    
    def inserir(self, nome, prioritario):
        novo = Paciente(nome, prioritario)
        
        if self.tamanho == 0:
            self.fim = novo
            self.inicio = novo
            self.tamanho += 1 
            return
              
        elif novo.prioritario == 'c':
            self.fim.dir = novo
            novo.esq = self.fim
            self.fim = novo
            self.tamanho += 1 
            return
        
        elif novo.prioritario == 'p':
            aux = self.inicio
            
            if aux.prioritario != 'p':
                novo.dir = self.inicio
                self.inicio.esq = novo
                self.inicio = novo
                self.tamanho += 1 
                
            
            else:       
                while aux is not None and aux.prioritario == 'p':
                    aux = aux.dir
                
                if aux is None:
                    self.fim.dir = novo
                    novo.esq = self.fim
                    self.fim = novo
                    self.tamanho += 1 
                else:
                    novo.esq = aux.esq
                    novo.dir = aux
                    aux.esq.dir = novo
                    aux.esq = novo
                    self.tamanho += 1 
    
    
    #b)
    def atender(self):
        if self.tamanho == 0:
            return None
        
        elif self.tamanho == 1:
            aux = self.inicio
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
            return aux
        
        else:
            aux = self.inicio          
            aux.dir.esq = None
            self.inicio = aux.dir
            aux.dir = None          
            self.tamanho -= 1
            return aux
                 

    #c)    
    def exibir(self):
        aux = self.inicio
        while aux: 
            print(aux.nome, aux.prioritario, end=" ")
            print()
            aux = aux.dir


    #d)
    def buscar(self, nome):
        aux = self.inicio
        posicao_atual = 1
        while aux:
            if aux.nome == nome:
                return posicao_atual, aux.prioritario
            aux = aux.dir
            posicao_atual += 1
            
        return None
    




def gerar_menu():
    print('[1] Inserir paciente')
    print('[2] Atender paciente')
    print('[3] Exibir lista de pacientes')
    print('[4] Buscar paciente')
    print('[5] Sair')
    
def main():
    
    while True:
        gerar_menu()
       
        opcao = int(input())
        
        match opcao:
            
            case 1:
                nome = input('Nome do paciente: ')
                prioritario = input('Prioridade do paciente ("p" para prioritário e "c" para comum): ')
                
                lista.inserir(nome, prioritario)
                print('Paciente inserido com sucesso!')
            
            case 2:
                paciente = lista.atender()
                
                if paciente is None:
                    print('Não há pacientes na fila.')
                else:
                    print(f'Paciente atendido: {paciente.nome} ({paciente.prioritario})')
            
            case 3:
                print('\nLista de pacientes:')
                lista.exibir()
                print()
            
            case 4:
                nome = input('Digite o nome do paciente: ')
                encontrou = lista.buscar(nome)
                
                if encontrou is None:
                    print('Paciente não encontrado.')
                else:
                    posicao, prioritario = encontrou
                    print(f'Paciente encontrado na posição {posicao} ({prioritario})')
            
            case 5:
                print('Obrigado por usar nosso sistema')
                break
            
            case _:
                print('Opção inválida!')
                
        
# Programa principal
lista = Lista()

if __name__ == '__main__':
    main()
            
