def jogar():

    print("\n*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")
    
    palavra_secreta = "segredo".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 6

    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros -= 1

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas





        print(letras_acertadas)
        print(f"Você tem {erros} tentativas.")


    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo.")


    
if(__name__ == "__main__"):
    jogar()