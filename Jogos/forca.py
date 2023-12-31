import random

def cabecalho():
    print("*********************************")
    print("*** Bem Vindo ao Jogo da Forca***")
    print("*********************************")

def palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    num = random.randrange(0, len(palavras))

    p_secreta = palavras[num].upper()

    return p_secreta

def letras_acertada(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual é a letra? ")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, l_acertadas, p_secreta):
    index = 0
    for letra in p_secreta:
        if (chute == letra):
            l_acertadas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def venceu():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdeu():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar():
    cabecalho()

    p_secreta = palavra_secreta()

    l_acertadas = letras_acertada(p_secreta)

    erros = 0
    print(len(p_secreta))
    print(l_acertadas)

    while( True ):

        chute = pede_chute()

        if (chute in p_secreta):
            chute_correto(chute, l_acertadas, p_secreta)
        else:
            desenha_forca(erros)
            erros += 1
            print("Ops, você errou! Faltam {} tentativas".format(8-erros))


        if(erros == 8 or "_" not in l_acertadas):
            break

        print(l_acertadas)

    if("_" not in l_acertadas):
        print("Você ganhou. A palavra era: ",p_secreta)
        venceu()
    else:
        print("Você perdeu. A palavra era: ",p_secreta)
        perdeu()

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()
