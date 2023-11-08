#Exercício 1
'''
aot = 'Eren Yeager'
#print(len(aot))

indice = len(aot)


while indice > 0:
    letra = aot[indice-1]
    print(letra)
    indice = indice - 1
'''

#Exercício 2
'''
exemplo = 'fruta'
print(exemplo[:])
'''

#Exercício 3
'''
def contagem(palavra,caracter):
    contagem = 0
    for letra in palavra:
        if letra == caracter:
            contagem = contagem + 1
    return print(contagem)

palavra = input('Digite uma palavra: \n')
caracter = input('Qual letra você deseja contar? \n')
contagem(palavra, caracter)
'''

#Exercício 4
'''
palavra = input('Digite uma palavra: \n')
caracter = input('Qual letra você deseja contar? \n')

print(palavra.count(caracter))
'''

#Operador de Formatação:

