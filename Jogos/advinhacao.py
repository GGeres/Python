import random

print("********************************")
print("Bem Vindo ao jogo de Advinhações")
print("********************************")

num_secreto = random.randrange(1,101)
tentativas = 3



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
        print("Você acertou!!")
        break
    else:
        if(acima):
            print("Seu chute foi maior que o número secreto. Tente novamente.")
        else:
            print("Seu chute foi menor que o número secreto. Tente Novamente.")

print("Fim de Jogo!!")
