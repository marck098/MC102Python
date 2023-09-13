#Escreva um programa que leia n números inteiros e imprima quantos deles estão nos
#seguintes intervalos: [0, 25], [26, 50], [51, 75] e [76, 100]. Por exemplo, para n = 10 e os
#seguintes números {2, 61, −1, 0, 88, 55, 3, 121, 25, 75}, seu programa deve imprimir:
i = 0
n = int(input("Quantidade de Números: "))
lista = []
while i <= n:
    if i == n:
        break
    num = int(input("Insira um numero: "))
    lista.append(num)
    i += 1    

print(lista)
print("2")
j = 0
inter0_25 = 0
inter26_50 = 0
inter51_75 = 0
inter76_100 = 0
NumForaIntervalo = 0

while j < n:
    print("0")
    if lista[j] >= 0 and  lista[j]<= 25:
        inter0_25 += 1
    elif lista[j] >= 26 and  lista[j]<= 50:
        inter26_50 += 1
    elif lista[j] >= 51 and  lista[j]<= 75:
        inter51_75 += 1
    elif lista[j] >= 76 and  lista[j]<= 100:
        inter76_100 += 1
    else:
      NumForaIntervalo += 1
    j += 1
    
print("[0,25]: ", inter0_25)
print("[26,50]: ", inter26_50)
print("[51,75]: ", inter51_75)
print("[76,100]: ", inter76_100)
print("Fora dos Intervalos: ", NumForaIntervalo)