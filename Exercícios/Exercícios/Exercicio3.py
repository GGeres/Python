'''
x = 43
x = x + 1
print(x)
'''
# Exercício 1 acima

'''
name = input("Digite seu nome: \n")
print(name)
'''
# Exercício 2 acima

'''
horas = ('Digite as horas: \n')
taxa = ('Digite a taxa: \n')
hour = input(horas)
try:
    hour = int(hour)
    pay = float(input(taxa))
    try:
        if int(hour) < 40:
            payment = int(hour)*float(pay)
        else:
            payment = ((int(hour)-40)*1.5 + 40) * float(pay)
        pFinal = ('O valor a ser pago será: R$ {}'.format(payment, round(2)))
        print(pFinal)
    except:
        print('Erro!! Insira um número!')
except:
    print('Erro!! Insira um número!')
'''

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
#Exercício 4 acima

#Verificador de Notas:

'''
Pontuação Nota
>= 0.9 - A
>= 0.8 - B
>= 0.7 - C
>= 0.6 - D
 < 0.6 - F
'''
'''
pontuacao = ('Digite a pontuação: ')
ponto = input(pontuacao)

try:
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
except:
    print('Pontuação Inválida!!')
'''
#Exercício 5 acima

'''
import random

for i in range(10):
    x = random.randint(1,5)
    print(x)
'''
#Exercício 6 acima



'''
def repetir_Letra():
    print_LetraSOAD()
    print_LetraSOAD()

def print_LetraSOAD():
    print('Life is a Waterfall')
    print('We´re one in the river and one again after the fall')

print(repetir_Letra())
'''


















