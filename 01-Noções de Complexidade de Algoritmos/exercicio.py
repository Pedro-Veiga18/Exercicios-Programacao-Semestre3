lista = [7, 8, 10, 11, 13, 7]
medias = []
soma = 0
for i in range(len(lista)):
    soma += lista[i]
    medias.append(soma / (i+1))

print(medias)  

    

