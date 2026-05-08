from exercicio01 import Lista

#Testes para o código
lista = Lista()

lista.inserir(10)
lista.inserir(20)
lista.inserir(30)

print("Lista após inserções no final:")
lista.imprimir()
print(f"\nTamanho: {lista.tamanho}")

#Inserir no inicio

lista.inserir_posicao(1, 5)

print("\nInserir 5 no inicio:")
lista.imprimir()
print()
#Inserir no meio
lista.inserir_posicao(3, 15)

print("\nInserir 15 no meio:")
lista.imprimir()
print()
#Inserir no final (maior)
lista.inserir_posicao(100, 40)

print("\nInserir 40 na posicao 100 (nao existe):")
lista.imprimir()
print()
#Remover do meio
lista.remover(15)

print("\nRemover 15:")
lista.imprimir()
print()

