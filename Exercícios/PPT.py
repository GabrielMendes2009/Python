saida = True

while saida:
    
    usr1 = int(input("Jogador 1, escolha: \n1- Pedra\n2- Papel\n3- Tesoura\nR "))
    usr2 = int(input("Jogador 2, escolha: \n1- Pedra\n2- Papel\n3- Tesoura\nR "))
    
    match usr1:
        case 1:
            if usr2 == 1:
                 print("Empate!! (Pedra x Pedra)\n")
            elif usr2 == 2:
                 print("Vitória do Jogador 2!! (Pedra x Papel)\n")
            elif usr2 == 3:
                 print("Vitória do Jogador 1!! (Pedra x Tesoura)\n")
            else:
                 print("O número escolhido pelo Jogador 2 está incorreto!!\n")
                 saida = False
        case 2: 
            if usr2 == 1:
                 print("Vitória do Jogador 1!! (Papel x Pedra)\n")
            elif usr2 == 2:
                 print("Empate!! (Papel x Papel)\n")
            elif usr2 == 3:
                 print("Vitória do Jogador 2!! (Papel x Tesoura)\n")
            else:
                 print("O número escolhido pelo Jogador 2 está incorreto!!\n")
                 saida = False
        case 3:
            if usr2 == 1:
                 print("Vitória do Jogador 2!! (Tesoura x Pedra)\n")
            elif usr2 == 2:
                 print("Vitória do Jogador 1!! (Tesoura x Papel)\n")
            elif usr2 == 3:
                 print("Empate!! (Tesoura x Tesoura)\n")
            else:
                 print("O número escolhido pelo Jogador 2 está incorreto!!\n")
                 saida = False
        case _:
            print("O número escolhido pelo Jogador 1 está incorreto!!\n")
            saida = False
