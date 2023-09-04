def jogar():

    print("*********************************")
    print("*** Bem Vindo ao Jogo da Forca***")
    print("*********************************")

    p_secreta = "banana"

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = input("Qual é a letra? ")

        index = 0
        for letra in p_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}.".format(letra, index))
            index = index + 1


        print("Jogando...")

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()
