#Leitura de Texto:

fnome = input('Digite o nome de um arquivo: ')
try:
    fhand = open(fnome)

except:
    print('File cannot be openned: ', fnome)
    exit()

text = dict()
for text in fhand:
    word = input('Digite uma palavra: ')
    if word in text:
        print(word)
    elif word == 'exit':
        exit()
    else:
        print('Word not found')