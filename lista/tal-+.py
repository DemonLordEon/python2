lista1 = [3, 7, -10, -11, 2]
listaPlus = []
listaMinus = []

for i in range(len(lista1)):
    if lista1[i] < 0:
        listaMinus.append(lista1[i])
    else:
        listaPlus.append(lista1[i])
    
    
print(listaPlus)
print(listaMinus)