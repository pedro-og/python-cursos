import forca
import adivinhacao


def escolhe_jogo():


    print("\n*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")


    print("\n(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o Jogo? "))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar() 


if(__name__ == "__main__"):
    escolhe_jogo()