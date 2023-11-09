# python shout:
'''
fnome = input('Digite o nome de um arquivo: ')
try:
    fhand = open(fnome)
except:
    print('File cannot be openned: ', fnome)
    exit()

count = 0
for text in fhand:
    text = text.rstrip()
    if text.find('F' and 'R' and 'b' and 'S'):
        print(text.upper())
'''

#Exercício 2:
'''
fnome = input('Digite o nome de um arquivo: ')
try:
    fhand = open(fnome)
except:
    print('File cannot be openned: ', fnome)
    exit()

y = 0
x = 0
z = 0
for line in fhand:
    line = line.rstrip()
    media = line.find(':')
    if line.startswith('X-DSPAM-Confidence'):
        media_text = line[media + 1:]
        x = x + float(media_text)
        y = y + 1
        z = x / y

print(z)
'''

#Exercício 3:

fnome = input('Digite o nome de um arquivo: ')
try:
    fhand = open(fnome)
except:
    if fnome == 'The Beatles':
        print('John, Paul, George e Ringo'.upper())
    else:
        print('File cannot be openned: ', fnome)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were ', count, 'subjects lines in ', fnome)
