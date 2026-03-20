# Uma concessionária de veículos deseja desenvolver um pequeno sistema para organizar
# seu estoque de automóveis. Cada veículo possui as seguintes informações: marca, modelo e valor.

# Para armazenar os veículos, a concessionária decidiu utilizar a estrutura de lista
# duplamente encadeada implementada em aula. Cada nó da lista deverá armazenar um
# objeto da classe Carro.

from lista_dupla import Lista

class Carro:
    def __init__(self, marca: str, modelo: str, valor: float):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        
    def __str__(self):
        return f'marca: {self.marca} <-> modelo: {self.modelo} <-> valor: R${self.valor}\n'


def ticket_medio():
    aux = lista.fim
    valor_medio = 0
    while aux:
        valor_medio += aux.dado.valor
        aux = aux.esq
    print(f'Valor médio dos carros --> {valor_medio / lista.tamanho} ')


def mais_caro():
    aux = lista.inicio
    valor = 0
    while aux:
        if aux.dado.valor > valor:
            valor = aux.dado.valor 
            carro_mais_caro = aux.dado
        aux = aux.dir
    print(f'Carro mais caro --> {carro_mais_caro}')


def pesquisar():
    modelo = input('Modelo para pesquisa: ')
    aux = lista.inicio
    while aux:
        if aux.dado.modelo == modelo:
            print(aux.dado, end='\n')
        aux = aux.dir
        

def cadastar():
    marca = input('Informe a marca -->')
    modelo = input('Informe o modelo -->')
    valor = float(input('Informe o valor -->'))
    lista.inserir_final(Carro(marca, modelo, valor))

    
def gerar_menu():
    print('[1] Cadastrar carros')
    print('[2] Listar carros')
    print('[3] Buscar carros pelo modelo')
    print('[4] Encontrar o carro mais caro')
    print('[5] Calcular o valor médio dos carros')
    print('[6] Finalizar')
    
def main():
    while True:
        gerar_menu()
        opcao = int(input())
        
        match opcao:
            case 1:
                cadastar()
            case 2:
                lista.imprimir()
            case 3:
                pesquisar()
            case 4:
                mais_caro()
            case 5:
                ticket_medio()
            case 6:
                print('Obrgiado por usar nosso App')
            case _:
                print('Opção inválida')
                
        
# Programa principal
lista = Lista()

if __name__ == '__main__':
    main()


