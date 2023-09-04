import random

def jogar():
    print("********************************")
    print("Bem Vindo ao jogo de Advinhações")
    print("********************************")

    num_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5


    for rodada in range(1, tentativas +1):
        print("Tentativa {} de {} ". format(rodada,tentativas))
        chute_str = input("Digite um número de 1 a 100: ")

        print("Você chutou ", chute_str)
        chute = int(chute_str)

        if( chute <1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == num_secreto
        acima = chute > num_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!!".format(pontos))
            break
        else:
            p_perdidos = abs(num_secreto - chute)
            pontos = pontos - p_perdidos
            if(acima):
                print("Seu chute foi maior que o número secreto. Tente novamente.")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(num_secreto, pontos))
            else:
                print("Seu chute foi menor que o número secreto. Tente Novamente.")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(num_secreto, pontos))

    print("Fim de Jogo!!")

if(__name__ == "__main__"):
    jogar()
