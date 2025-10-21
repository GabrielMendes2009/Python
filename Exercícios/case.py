OPC = 0
saida = True

while saida:
    print("1- Para receber um 'bom dia!!'")
    print("2- Para receber um 'boa tarde!!'")
    print("3- Para receber um 'boa noite!!'")
    print("4- Sair")
    OPC=int(input("Intruduza uma opção: "))
    
    match OPC:
        case 1:
            print("Bom Dia!!!\n")
        case 2: 
            print("Boa Tarde!!!\n")
        case 3:
            print("Boa Noite!!!\n")
        case 4:
            saida = False
            print("Adeus!!!!")

