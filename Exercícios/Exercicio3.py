#x = 43
#x = x + 1
#print(x)

# Exercício 1 acima

#name = input("Digite seu nome: \n")
#print(name)

# Exercício 2 acima


horas = ('Digite as horas: \n')
taxa = ('Digite a taxa: \n')
try:
    hour = input(horas)
    pay = input(taxa)
    if int(hour) < 40:
        payment = int(hour)*float(pay)
    else:
        payment = int(hour)*(float(pay)*1.5)
    pFinal = ('O valor a ser pago será: R$ {}'.format(payment, round(2)))
    print(pFinal)
except:
    print('Erro!! Insira um número!')


# Exercício 3 acima

'''larg = 17
alt = 12.0

ver1 = larg//2
print(ver1)
print(type(ver1))

ver2 = larg/2.0
print(ver2)
print(type(ver2))

ver3 = alt/3
print(ver3)
print(type(ver3))

ver4 = 1 + 2 * 5
print(ver4)
print(type(ver4))
'''

