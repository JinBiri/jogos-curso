def selecionarJogo():
    while True:
        menuJogo = (input("Escolha qual jogo deseja jogar!!!!\n(1) Adivinhe o numero! -> 1 Jogador\n(2) Jogo da Forca! ->1 Jogador\n"
                             "(3) Jogo da Velha! -> 2 Jogadores\n(4) Sair\n--> "))
        if menuJogo == "1":
            import adivinhacao
            adivinhacao.jogarAdivinhacao()
            break
        elif menuJogo == "2":
            import forca
            forca.jogarForca()
            break
        elif menuJogo == "3":
            import velha
            velha.jogarVelha()
            break
        elif menuJogo == "4":
            break

if __name__ == "__main__":
    selecionarJogo()