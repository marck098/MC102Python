# Leitura da entrada
p = list(input())
msg = list(input())
i = 0
print(p)


   
for index_p, letra_p in enumerate(p):
    for index_msg, letra_msg in enumerate(msg):
        if letra_p in msg and i == 0:
            for j in range(len(msg)):  
                if msg[j] == letra_p[index_p]:
                    msg[j] = p[len(p)-1]
            i += 1
        elif p[(len(p) - 1 - index_p)] == letra_msg: # 1-1-4 == r
            msg[index_msg] = p[(len(p) - 1 - index_p)]

        
    
print(msg)
            
        
        # se o index <= tamanho de p-1
        # se a primeira letra de P invertido for igual letra de msg[ultimo index p-1] então msg[ultimo index p-1] msg recebe p[0] em todas as ocorrencias
        # se a segunda letra de p invertido for igual a letra de na posição 
        
        # se a terceira letra de p for igual a segunda letra de msg então a msg recebe segunda letra de p
        # se a letra não posição i de P for igual a  letra posição i-1 de msg, msg recebe a letra na posição a i-1 de P
