print("********************************")
print("Bem Vindo ao jogo de Advinhações")
print("********************************")

num_secreto = 42

chute_str = input("Digite seu número: ")
print("Você chutou ", chute_str)
chute = int(chute_str)
if(chute == num_secreto):
    print("Você acertou!!")
else:
    print("Você errou.")