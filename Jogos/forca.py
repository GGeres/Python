def jogar():

    print("*********************************")
    print("*** Bem Vindo ao Jogo da Forca***")
    print("*********************************")

    p_secreta = "banana".upper()
    l_acertadas = ["_", "_", "_", "_", "_", "_"]

    acertou = False
    enforcou = False
    erros = 0

    print(l_acertadas)

    while(not acertou and not enforcou):
        chute = input("Qual é a letra? ")
        chute = chute.strip().upper()
        if (chute in p_secreta):
            index = 0
            for letra in p_secreta:
                if(chute.upper() == letra.upper()):
                    l_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in l_acertadas
        print(l_acertadas)

    if(acertou):
        print("Você ganhou.")
    else:
        print("Você perdeu.")

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()
