def imprime_msg():
    print("Minha primeira função")
    
imprime_msg()

def imprime_mensagem2():
    msg = "Variável Local"
    print(msg)
    
imprime_mensagem2()
#teste variaveis chamadas, a variavel local(da função) entra no lugar da "global" quando chamada a função
variavel = "global"
def imprime3():
    variavel = "local"
    print(variavel)
imprime3()

a = 1
def incrementa():
    a = 12
    a = a + 1
    print(a)
    
incrementa()
print(a)
print()
def imprime4(mensagem1):
    print(mensagem1)

bomdia = "bom dia"
imprime4(bomdia)

def imprime5(x, y = 0):
    print(x +y)
    
imprime5(1)
imprime5(1,2)
    