lista = [10,20,30,40]
N = 4
for i in range(N):
    if  i == (N-1):
        print(lista[i])
    else:
        print(lista[i], end = '.')

'''diferenca = -3
if diferenca < 0:
            diferenca *= -1
print(diferenca)'''
    
testeDivisor = 12%3
print(testeDivisor)


lista_letras = ["a","x","f","c","r","g","h","a","a","g","b","d"]
print(sorted(lista_letras))

palavra = "Azul"
lista_palavra = list(palavra)
print(lista_palavra)
lista1 = ["verde"]
lista2 = ["verde"]
if lista1 == lista2:
    print(True)
print(sorted(palavra))

'''n = int(input())
lista_num2 = []
for i in range(n):
    lista_num2.append(input())
lista_num1 = [1,2,3,4,5]
print("lista 1:", len(lista_num1))
print("lista 2:", len(lista_num2))'''

lista_sorted_teste = ["verde","amarelo"]
print(sorted(lista_sorted_teste))

lista_classe_teste = ["10",[1,2,3]]
print(type(lista_classe_teste[1]))