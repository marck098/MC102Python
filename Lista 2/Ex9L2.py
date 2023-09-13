#Faça um programa que leia um número inteiro positivo C. O seu programa deve imprimir todas as soluções da equação
#                                        x1 + x2 + x3 = C,
#onde as variáveis x1, x2, e x3 são inteiras não negativas
n = int(input("Valor de C:"))

for i in range(0, n+1):
    for j in range(0, n+1):
        for k in range(0, n+1):
            if i+j+k == n:
                print(i, j , k, "São Soluções para a equação x1 + x2 + x3 = C", sep=",")