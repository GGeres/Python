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

