def le_matriz():
    matriz = []
    while True:
        linha_num = input().split()
        if linha_num == []:
            return matriz
        linha = []
        for i in linha_num:
            linha.append(int(i))
        matriz.append(linha)
print(le_matriz())

        
    