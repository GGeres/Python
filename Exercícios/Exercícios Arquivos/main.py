#Arquivos de Textos:

'''Uma sequência de linhas'''
'''
Memória secundária, ou arquivos são permanentes 
num software. Quando o programa é desligado, a informação não se perde.
Primeiro, será apresentado como ler ou escrever um arquivo.
'''

#Abrindo um arquivo:
'''
Quando se abre um arquivo, você está pedindo 
para o sistema operacional achá-lo por
nome e ter certeza que ele existe.
'''

'''
Usa-se a função open()
'''

#Lendo arquivos:
'''
Indicado para contar o tamanho do arquivo.
'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be openned: ', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were ', count, 'subjects lines in ', fname)