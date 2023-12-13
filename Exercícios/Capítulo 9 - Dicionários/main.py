#Dicionários:
'''
É como uma lista, mas generalizada
Numa lista, o índice deve ser um Int, já um dicionário, pode se de (qualquer) tipo.

Um dicionário é como o mapeamento entre um conjunto de índices (as chaves) e
um conjunto de valores.
Cada chave localiza um valor
A associoção entre uma chave e um valor é chamado de ítem.

Exemplo:
Um dicionário para mapear palavras em Ingles para o Português.


'''

#Exemplo de Dicionário como Conjunto de Contadores:
#Histograma
'''
word = 'Carnotauros'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
'''

#Exemplo para Leitura em Arquivos:
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
exit()

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)