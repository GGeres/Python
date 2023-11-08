
y = 0
z = 0
w = 0
maximo = None
minimo = None
while True:
    try:
        x = input('Digite um número: ')
        if x == str('Pronto') or x == str('pronto'):
            break
        num = int(x)
        y = y + num
        w = w + 1
        z = y/w
        if maximo is None or num > maximo:
            maximo = num
        if minimo is None or num < minimo:
            minimo = num
    except:
        print('Entrada inválida')


print(y, w, z, 'Máximo: ',maximo, 'Mínimo: ', minimo)

