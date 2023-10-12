lista1 = [ 1, 2, 3, 4, 5, 10, 47]
lista2 = [2, 5, 7, 1, 10, 9, 18,4]
lista3 = []
for i in lista1:
    print("i ",i)
    for j in lista2:
        print("j ",j)
        if i == j:
            lista3.append(i)
print(lista3)