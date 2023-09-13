n = int(input())
lista = []
media = 0.0
somatorio = 0.0

for i in range(n):
    lista.append(float(input()))
print(lista)

for item in lista:
    media += item
    
print(media)  
media = media/len(lista)
print(media)

for item in lista:
    somatorio += (item - media)**2
variancia = ((somatorio/(n-1)))
desvioPadrao = variancia**(1/2)
print(variancia)
print(desvioPadrao)