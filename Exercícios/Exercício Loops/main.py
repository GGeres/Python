
y = 0
z = 0
w = 0
while True:
    try:
        x = input('Digite um número: ')
        if x == str('Pronto') or x == str('pronto'):
            break
        num = int(x)
        y = y + num
        w = w + 1
        z = y/w
    except:
        print('Entrada inválida')


print(y, w, z)



