# # dicionario = {}
# # c = "chave"
# # n = "valor"
# # dicionario[c] = []
# # dicionario[c].append(n)
# # print(dicionario)
# # dicionario[c].append("valor 2")
# # print(dicionario)
# # if "azul"  not in dicionario.keys():
# #     dicionario["azul"] = []
# #     dicionario["azul"].append("amarelo")
# # if "amarelo" not in dicionario["azul"]:
# #     dicionario["azul"].append("amarelo")
# # print(dicionario)
# # print("ok")

# # lista = ["a","b","c","d"]
# # palavra = "-".join(lista)
# # print(palavra)

# # dicionario = {"a":[1,2,3],"b":[4,5,6,],"c":[7,8,9]}
# # for i in dicionario.keys():
# #     print("keys")
# #     print(i)
# # for i in dicionario.values():
# #     print("values")
# #     print(i)
# # lista = ["a","b","c","d"]
# # lista[1] = 10
# # print(lista)
# # palavra = "verde"
# # palavra[3] = "k"

# # dicionario_geral = {
# #     "pessoa1": {'posição':[1,2],'valor':10,'movimentos':'abcsnedasd'},
# # 'pessoa2':{'posição':[4,6],'valor':19,'movimentos':'asuidhasid'}
# # }

# # print(dicionario_geral)

# # Função para calcular o valor do tesouro encontrado por um caçador
# # Função para calcular o valor do tesouro encontrado por um caçador
# def calcular_valor_tesouro(mapa, linha_inicial, coluna_inicial, movimentos):
#     valor_tesouro = 0

#     for movimento in movimentos:
#         if movimento == 'N':
#             linha_inicial -= 1
#         elif movimento == 'S':
#             linha_inicial += 1
#         elif movimento == 'O':
#             coluna_inicial -= 1
#         elif movimento == 'L':
#             coluna_inicial += 1

#         # Verifica se a posição atual contém um tesouro e atualiza o valor do tesouro
#         if 0 <= linha_inicial < len(mapa) and 0 <= coluna_inicial < len(mapa[0]):
#             valor_tesouro += mapa[linha_inicial][coluna_inicial]
#             mapa[linha_inicial][coluna_inicial] = 0

#     return valor_tesouro

# # Função principal
# def main():
#     resultados = []

#     while True:
#         try:
#             n, m = map(int, input().split())
#             mapa = [list(map(int, input().split())) for _ in range(n)]
#             q = int(input())

#             for cacador in range(1, q + 1):
#                 linha_inicial, coluna_inicial = map(int, input().split())
#                 movimentos = input().strip()  # Remova espaços em branco no início e no final da string
#                 valor_tesouro = calcular_valor_tesouro(mapa, linha_inicial, coluna_inicial, movimentos)
#                 resultados.append(f"Caçador C{cacador}: T{valor_tesouro}")

#         except EOFError:
#             break

#     # Imprima todos os resultados ao final
#     for resultado in resultados:
#         print(resultado)

# if __name__ == "__main__":
#     main()
# ruas_horizontais = [int(i) for i in input().split()]
# print(ruas_horizontais)
# lista = [int(i) for i in range(7,10)]
# print(lista)
numeroInt = 475
numero = str(numeroInt)
crescente  = int(''.join(sorted(numero)))
decrescente  = int(''.join(sorted(numero,reverse = True)))
