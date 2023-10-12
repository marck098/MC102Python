
a = int(input())
b = int(input())

def main ():
    print(amigos(a,b))
    
def amigos(a, b):
    lista_divisoresA =[]
    lista_divisoresB =[]
    teste_amigo_a = 0
    teste_amigo_b = 0
    for i in range(a):
        if i != 0:
            aux = a % i
            if aux == 0:
                lista_divisoresA.append(i)
    for i in range(b):
        if i != 0:
            aux = b % i
            if aux == 0:
                lista_divisoresB.append(i)
    teste_amigo_a = sum(lista_divisoresA)
    teste_amigo_b = sum(lista_divisoresB)
    if teste_amigo_b == a and teste_amigo_a == b:
        return True
    else: 
        return False
main()

