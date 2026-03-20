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
        
# Programa principal

lista = Lista()
lista.inserir_final(Carro('bmw', 'x7', 750000))
lista.inserir_final(Carro('audi', 'q5', 35000))

lista.imprimir()
