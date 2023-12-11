#Leitura de Texto:

fnome = input('Digite o nome de um arquivo: ')
try:
    fhand = open(fnome)

except:
    print('File cannot be openned: ', fnome)
    exit()

for text in fhand:
    text = dict()
    word = input('Digite uma palavra: ')
    if word in text:
        print(word)
    else:
        print('Word not found')