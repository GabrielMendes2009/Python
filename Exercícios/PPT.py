usr1 = int(input("Jogador 1, escolha: \n1- Pedra\n2- Papel\n3- Tesoura\nR "))

usr2 = int(input("Jogador 2, escolha: \n1- Pedra\n2- Papel\n3- Tesoura\nR "))

saida = True

while saida:
    match usr1:
        case 1:
            if usr2 == 1:
                 print("Empate!! (Pedra x Pedra)")
            elif usr2 == 2:
                 print("Vitória do Jogador 2!! (Pedra x Papel)")
            elif usr2 == 3:
                 print("Vitória do Jogador 1!! (Pedra x Tesoura)")
            else:
                 print("O número escolhido pelo Jogador 2 está incorreto!!")
        case 2: 
            if usr2 == 1:
                 print("Vitória do Jogador 1!! (Papel x Pedra)")
            elif usr2 == 2:
                 print("Empate!! (Papel x Papel)")
            elif usr2 == 3:
                 print("Vitória do Jogador 2!! (Papel x Tesoura)")
            else:
                 print("O número escolhido pelo Jogador 2 está incorreto!!")
        case 3:
            if usr2 == 1:
                 print("Vitória do Jogador 2!! (Tesoura x Pedra)")
            elif usr2 == 2:
                 print("Vitória do Jogador 1!! (Tesoura x Papel)")
            elif usr2 == 3:
                 print("Empate!! (Tesoura x Tesoura)")
            else:
                 print("O número escolhido pelo Jogador 2 está incorreto!!")
        case _:
            print("O número escolhido pelo Jogador 1 está incorreto!!")
            saida = False
