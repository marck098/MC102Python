msg = "olá mundo"
print(msg)

print("Você respondeu \"Sim\".")
print("\\")

print("Joe's Car")
print("Quebra de \nlinha")
print("\tTabulação") #tabulação padrão 8 espaços em branco

print(msg[1])  #strings são listas imutaveis assim como tuplas.

print(format(10, "d"))
print(format(-13, "+d"))
print(format(+13, "+d"))
print(format(3.23123123, "+.10f"))
print(format(3.23123123, "+.4f"))

frutas = "Frutas: {0}, {1} e {2}"
print(frutas.format("abacaxi", "mamão", "morango"))
pets = "quem é mais inteligente {1} ou {0} ?"
print(pets.format("cão", "gato"))
soma = " {0} + {1} = {2}"
print(soma.format(3, 4, 4+3))
pi = "o valor de pi é {0:.4f}"
print(pi.format(3.14159265))

cabeçalho = "{0}, {1} de {2} de {3}"
print(cabeçalho.format("Campinas", 15, "Junho", 2023))

msg1 = "oi"
msg2 = "g" + msg1 + "aba"
print(msg2)
print(msg2 * 5)
print("abc-"*3) 

print(len(msg2))

print ("pipido" in  "paralelepipido")
msgTeste = "        oiiii,       tudo bem?"
print(msgTeste)
print(msgTeste.strip())
msgSplit = msgTeste.split()
print(msgSplit)

'''a, b, c = [int(i) for i in input().split()]
print(a,b,c)
numeros = [float(i) for i in input().split()]
print(numeros)'''

frutas = ["mamão", "uva", "abacate"]
txt = ", ".join(frutas)
print(txt)
str = "socorro"
lista = list(str)
print(lista) 
replaceString = str.replace("o", "x")
print(replaceString.capitalize())
print("OLÁ".lower())
print("olá".upper())
print("123124".isnumeric()) 

