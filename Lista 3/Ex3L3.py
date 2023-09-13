lista1 = []
lista2 = []
lista1_string = ""
lista2_string = ""

n = int(input("tamanho lista 1: "))
for lista in range(n):
    lista1.append(int(input("elemento lista1: ")))
print(lista1)

m = int(input("tamanho lista 2: "))
for lista in range(m):
    lista2.append(int(input("elemento lista2: ")))
print(lista2)

for i in lista1:
    lista1_string += str(i)
    print(lista1_string)
for j in lista2:
    lista2_string += str(j)
    print(lista2_string)

count = lista2_string.count(lista1_string)
print(count)