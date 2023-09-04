def jogar():

    print("*********************************")
    print("*** Bem Vindo ao Jogo da Forca***")
    print("*********************************")

    p_secreta = "banana".upper()
    l_acertadas = ["_", "_", "_", "_", "_", "_"]


    erros = 0
    print(len(p_secreta))
    print(l_acertadas)

    print(l_acertadas)

    while( True ):

        chute = input("Qual é a letra? ")
        chute = chute.strip().upper()

        if (chute in p_secreta):
            index = 0
            for letra in p_secreta:
                if(chute == letra):
                    l_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas".format(6-erros))


        if(erros == 6 or "_" not in l_acertadas):
            break

        print(l_acertadas)

    if("_" not in l_acertadas):
        print("Você ganhou. A palavra era: ",p_secreta)
    else:
        print("Você perdeu. A palavra era: ",p_secreta)

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()
