#Exercício 2:

import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

conta = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    if line.startswith('From'):
        words = line.split()
    for word in words:
        if word not in conta:
            conta[word] = 1
        else:
            conta[word] += 1

        print(line)
print(conta)

#Terminar outra hora