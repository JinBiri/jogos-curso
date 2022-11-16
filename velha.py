from decora import trofeu, velha

#Menu inicial que inicia o jogo ou o encerra,
def jogarVelha():
    resposta = False
    while resposta is False:
        menu = int(input("Jogo da Velha\n(1) Jogar\n(0) Sair\n--> "))
        if menu == 1:
            jogar()
        elif menu == 0:
            print("Saindo...")
            resposta = False

#Funcao que realiza as jogadas de cada jogador
def jogar():
    jogada = 0

    while vencedor() == 0:
        jogador = (jogada%2)+1
        print(f"\nVez do jogador {jogador}")
        exibir()
        linha = int(input("Qual linha?\n-> "))-1
        coluna = int(input("Qual coluna?\n->"))-1
        if board[linha][coluna] == 0:
            if jogador == 1:
                board[linha][coluna] = 1
            elif jogador == 2:
                board[linha][coluna] = -1
        else:
            print(f"A linha {linha} com a coluna {coluna} ja esta prenchida.")
            jogada -= 1

        if vencedor() == 1:
            print(f"O jogador {jogador} venceu!")
            trofeu()

        if jogada == 12:
            print("Deu velha!")
            velha()
            break

        jogada +=1

#Verifica todas as possibilidades de um vencedor
def vencedor():
    #checar linhas
    for i in range(3):
        pontos = board[i][0] + board[i][1] + board[i][2]
        if pontos == 3 or pontos == -3:
            return 1

    #checar colunas
    for i in range(3):
        pontos = board[0][i] + board[1][i] + board[2][i]
        if pontos == 3 or pontos == -3:
            return 1

    #checar diagonais
    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0

#Exibe o estado atual do tabulerio
def exibir():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')
        print("\n")

#Cria o tabuleiro e inicia o jogo
board= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

if __name__ == "__main__":
    jogarVelha()