i = 0

while i != 5:    
    print("[1] - Pizza Marguerita")
    print("[2] - Pizza Calabresa")
    print("[3] - Pizza Pepperoni")
    print("[4] - Pizza Mussarela")
    print("[5] - Sair")
    
    i = int(input("Escolha um sabor de Pizza:"))
    
    if i == 1:
        print("Pizza Marguerita")
    elif i == 2:
        print("Pizza Calebresa")
    elif i == 3:
        print("Pizza Pepperoni")
    elif i == 4:
        print("Pizza Calebresa")
    elif i == 5:
        break
    else:
        print("Opção Inválida")
    print("")
    
    
    