import random

def jogar():

    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000

    print("\nQual nível de dificuldade desejado?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("\nDefina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    #comando if - estrutura de comparação
    #comando for - estrutura de repetição
    #comando break - quebra de laço
    #break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
    #função range
    #função int

    for rodada in range (1, total_de_tentativas + 1):
        print(f'\nTentativa {rodada} de {total_de_tentativas}')
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Somente números entre 1 e 100!")

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Acertou! Pontuação final: {pontos} pontos!")
            break
        else:
            if(maior):
                print("Errou. Maior do que numero secreto.\n")
            elif(menor):
                print("Errou. Menor do que numero secreto.\n")
            if (rodada == total_de_tentativas):
                print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos.")  

            pontos_perdidos = abs(numero_secreto - chute) #40 - 20
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()