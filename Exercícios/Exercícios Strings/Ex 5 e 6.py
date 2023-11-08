#Exercício 5:

data = '0.8475'
exemplo = 'X-DSPAM-Confidence:%s' %(data)

last_part = exemplo.find(':')
#print(last_part)

last_part_text = exemplo[last_part+1:]
print(last_part_text)