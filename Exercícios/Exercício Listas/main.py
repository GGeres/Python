#Listas:

aot = ['Eren', 'Mikasa', 'Armin']
sec = ['Erwin', 'Levi', 'Hange']
Paradis = aot + sec

marley = ['Reiner', 'Annie', 'Bertholt', 'Ymir']
print(Paradis[1:6])

#Mutação de Listas:
'''
Em consoles, pode-se substituir os elementos de uma lista em 
tempo real.

Ex:
>>> aot = ['1', '2', '3']
>>> print(aot)
['1', '2', '3']

>>> aot[1] = '4'
>>> print(aot)
['1', '4', '3']

Pode-se utilizar o IN em listas
'''

#Métodos de Listas:

'''
.append:
Adiciona um elemento ao final de uma lista.

.extend
extend leva uma lista como um argumento para o método append e adiciona todos
os elementos o final de uma lista:
Ex:
t1 = ['Eren', 'Mikasa', 'Armin']
t2 = ['Jean', 'Sasha', 'Connie']
t1.extend(t2)
print(t1)
['Eren', 'Mikasa', 'Armin', 'Jean', 'Sasha', 'Connie']

.sort
Ordena uma lista do menor para o maior
>>> t1 = ['5','3','9','1']
>>> t1.sort()
[1,3,5,9]

'''

#Apagando Elementos:

'''
.pop
Apaga um elemento da lista
Modifica a lista e retorna o elemento que foi removido. Se você não fornecer
um índice, ele deleta e retorna o último elemento da lista.

.del
Caso não precise do valor removido

.remove
Para remover pelo elemento e não pelo índice.

'''

#Listas e Funções:
'''
sum()
Funciona quando os elementos da lista são números
Ele faz a somatoria dos elementos.

E outras funções funcionam como funções de strings.

'''
total = 0
count = 0
while(True):
    inp = input('Eneter a number: ')
    if inp == 'done' or inp == 'Done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total/count
print('Average: ', average)



