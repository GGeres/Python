def computarNotas(ponto):
    ponto = float(ponto)
    if ponto >= 0.0 and ponto <= 1.0:
        if ponto < 0.6:
            print("F")
        elif ponto >= 0.6 and ponto < 0.7:
            print('D')
        elif ponto >= 0.7 and ponto < 0.8:
            print('C')
        elif ponto >= 0.8 and ponto < 0.9:
            print('B')
        elif ponto >= 0.9:
            print('A')
    else:
        print('Pontuação Inválida!!')


pontuacao = ('Digite a pontuação: ')
ponto = input(pontuacao)

try:
    computarNotas(ponto)
except:
    print('Pontuação Inválida!!')