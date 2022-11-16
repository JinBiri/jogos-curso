
import decora
def escolher_palavra():
    from random import choice
    palavras = open("palavras_forca.txt", "r")
    palavra = palavras.read()
    words = list(map(str, palavra.split()))
    return choice(words).upper()

def jogarForca():

    print("*********************\n*** JOGO DA FROCA ***\n*********************")

    tentativas = 7
    palavra_secreta = escolher_palavra()
    print(palavra_secreta)
    misterio = "_"*len(palavra_secreta)
    enforcou = acertou = False
    while(not enforcou and not acertou):
        index = 0
        chute = (input("Digite uma letra\n-->")).upper()
        for i in palavra_secreta:
            if chute == i:
                misterio = misterio[:index] + i + misterio[index+1:]
                print(f"Voce acertou a letra na posicao {index+1}\n--> {misterio} <--")
            index += 1
        if chute not in palavra_secreta:
            tentativas = tentativas - 1
            decora.desenha_forca(tentativas)
            print(f"Voce nao acertou nenhuma letra\nTentativas restantes --> {tentativas} tenativas!")
            if tentativas == 0:
                decora.caveira_word(palavra_secreta)
                enforcou = True
        if (misterio == palavra_secreta):
            print(f"Voce acertou a palavra '{palavra_secreta}', parabens\nTe sobrou {tentativas} restantes\n")
            decora.trofeu()
            acertou = True

if __name__ == "__main__":
    jogarForca()


