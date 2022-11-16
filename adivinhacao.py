def jogarAdivinhacao():
    from random import randrange
    from decora import caveira_word, trofeu
    numero = randrange(1,101)

    print(f"{'='*19}\n Jogo de Adivinhar\n{'='*19}\n\n"
          f"Escolha sua dificuldade\nO numero sera entre 1 e 100!")

    dificuldade = int(input("(1) Facil\n(2) Medio\n(3) Dicil\nDigite o numero da dificuldade que deseja: "))

    if dificuldade == 1:
        tentativas = 12
    elif dificuldade == 2:
        tentativas = 9
    else:
        tentativas = 5
    for a in range(tentativas):
        print(f"Tentativa {a + 1} de {tentativas}")
        palpite = int(input("Qual numero voce acredita ser o certo?\n"))
        if palpite < numero:
            print("O numero correto e maior")
        elif palpite > numero:
            print("O numero correto e menor")
        if palpite == numero:
            print("Voce ganhou!")
            trofeu()
            a = a-1
            break

    if (a+1) == tentativas:
        print("Voce perdeu :(\nTente outra vez")
        caveira_word(numero)

if __name__ == "__main__":
    jogarAdivinhacao()