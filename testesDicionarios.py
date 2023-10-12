dicionario = {}
print(type(dicionario))
localizacao = {

    "Lat": -22.837352,
    "Lon": -47.288282
}

print(localizacao)
dicionario1 = dict({})

dicionario2 = {
    1.2: True,
    123: "Um Dois Três",
    "cat" : "dog",
    ("X","Y"): (1,3,4)
}
print(dicionario2)

dicionario3 = {
    "Z":1,
    "A":2,
    "C":3
}
print(dicionario3)
print(dicionario3["A"])

dicionario4 = {
    "Nome":"Marcos",
    "Idade":24,
    "Profissão":"Estatistico"
}
print("Nome" in dicionario4)
print(dicionario4.get("Nome"))
print(len(dicionario4))
dicionario4["Cidade"] = "Campinas"
print(dicionario4)

dicionario4["Cidade"] = "São Paulo"
print(dicionario4)

valor_removido = dicionario4.pop("Cidade") # a declaração .del tbm remove mas não retorna o valor removido, apenas deleta
print(dicionario4)                          
print(valor_removido)
print()
valor_removido = dicionario4.popitem() # remove ultimo par de chave,valor e retorno eles como uma tupla
print(dicionario4)                          
print(valor_removido)

dic01 = { 
    "A" : "Amora",
    "B" : "Boba",
    "C" : "Cachorro"
    }
dic02 = { 
    "C": "Cachorro 2",
    "D" : "Doido",
    "E" : "Estou",
    "F" : "Facil"
    }

dic01.update(dic02)
print(dic01)
print(dic01.keys())
print(list(dic01.keys()))
print(dic01.values())
print(list(dic01.values()))
print(dic01.items()) #gera uma uma lista de tuplas

for letras in dic01.keys():
    print("Letras:",letras)

for frutas in dic01.values():
    print("Fruta:",frutas)

for (letras,frutas) in dic01.items():
    print("Fruta com Letra", letras, ":",frutas)

dic03 = {"Nome":"Joao", "Idade":20}
#print("03",dic03)
#dic04 = dic03
#print("04",dic04)
#dic03["Nome"] = "Maria"
#print("04mod",dic04)
#print("03   ",dic03)
''' "copiar" um dicionario desta forma n é eficaz pois as variaveis estão ligadas aos objetos,
então uma alteração no dicionario copiado irá alterar o original tbm'''

dic03copy = dic03.copy()
print("03 copy",dic03copy)
dic03copy["Nome"] = "Lara"
print("03 copy",dic03copy)
print("03",dic03) #com metodo .copy() o dicionario oginal n é alterado

lista_chaves = ["Alice", "Carlos", "Lara"]
lista_valores = ["Camisa", "Blusa", "Vestido"]
pessoas = dict(zip(lista_chaves,lista_valores))
print(pessoas)

pessoas = {}
n = int(input("Qtd de pessoas: "))

for i in range(n):
    nome = input("nome: ")
    idade = int(input("idade: " ))
    sexo = input("Sexo: ")
    pessoas[nome] = [idade, sexo]
print(pessoas)
print(pessoas["Lara"][1])






