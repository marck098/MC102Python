'''lista_numeros  = [1,2,3,4,5,6,7,8,9]
(lista_numeros[0], lista_numeros[8]) = (lista_numeros[8], lista_numeros[0]) #troca variaveis de lugar sem precisar criar uma var_auxiliar
print(lista_numeros)'''


#bubbleSort
def bubbleSort(lista):
    n = len(lista)
    for i in range(n-1, 0, -1): #percorre a lista em um range cada vez menor, fazendo com que os valores jpa modificados não sejam verificados, otimizando o programa
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j+1], lista[j]
    print(lista)
    
lista_desordenada = [55,11,27,39,80,2]
print("bubbleSort: ")
bubbleSort(lista_desordenada)
    
#Selection Sort
'''Este metódo é mais recomendo quando temos muitos dados, já que realizada menos trocas do que os demais algarismo'''
# cria uma função para encontrar o menor indice a partir de uma posição inicial dada
def indiceMenor(lista, inicio):
    minimo = inicio
    n = len(lista)
    for j in range(inicio + 1, n):
        if lista[minimo] > lista[j]:
            minimo = j
    return minimo

def selectionSort(lista):
    n  = len(lista)
    for i in range(n):
        minimo = indiceMenor(lista, i)
        lista[i],lista[minimo] = lista[minimo], lista[i]
    print(lista)
print("selectionSort: ")
selectionSort(lista_desordenada)

#insertionSort

'''Se os elementos da lista estiverem quase ordenados, o Insertion Sort é mais adequado por realizar menos trocas'''
def insertion(lista, i):
    j = i - 1
    while (j >= 0) and (lista[j] > lista[i]):
        j = j - 1
    lista[j+1:i+1] = [lista[i]] + lista[j + 1:i]

def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        insertion(lista, i)
    