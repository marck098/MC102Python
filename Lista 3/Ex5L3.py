lista1 = [ 1, 2, 3, 4, 5]
lista2 = [2, 5, 7, 1, 9, 18]
lista3 =  lista1 + lista2
print(lista3)
lista4 = []

for i in lista3:
    if i not in lista4:
        lista4.append(i)
print(sorted(lista4))
