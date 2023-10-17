matriz1 = [1,2,3]
matriz2 = [[1,2,3], 
           [4,5,6]]

def identifica_matriz(lista):
    coluna = []
    for i in (range(len(lista))):
        if type(lista[i]) == list:
            coluna.append(len(lista[i]))
            lin = len(lista)
            col = max(coluna)
            return print("É matriz de dimensões:", (lin,col))
        else:
            return print("Não é matriz:", ())
        
identifica_matriz(matriz1)
identifica_matriz(matriz2)
