print("********************************")
print("Bem Vindo ao jogo de Advinhações")
print("********************************")

num_secreto = 42




chute_str = input("Digite seu número: ")
print("Você chutou ", chute_str)
chute = int(chute_str)

acertou = chute == num_secreto
acima = chute > num_secreto

if(acertou):
    print("Você acertou!!")
else:
    if(acima):
        print("Seu chute foi maior que o número secreto. Tente novamente.")
    else:
        print("Seu chute foi menor que o número secreto. Tente Novamente.")
