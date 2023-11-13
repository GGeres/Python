#Ex1:
'''
def corte(x):
    del x[0]
    length = len(x)
    del x[length-1]
    meio(x)

def meio(x):
    return print(x)

aot = ['Eren', 'Mikasa', 'Armin', 'Jean', 'Sasha', 'Connie']
corte(aot)
'''

#Exercício 6

numlist = list()

maximo = None
minimo = None
while True:
    try:
        x = input('Digite um número: ')
        if x == str('Pronto') or x == str('pronto'):
            break
        num = float(x)
        numlist.append(num)
    except:
        print('Entrada inválida')


print('Média: ',sum(numlist)/len(numlist))
print('Máximo: ',max(numlist))
print('Mínimo: ', min(numlist))

