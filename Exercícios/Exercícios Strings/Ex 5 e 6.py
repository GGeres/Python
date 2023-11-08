#Exercício 5:

exemplo = 'X-DSPAM-Confidence:0.8475'

last_part = exemplo.find(':')
#print(last_part)

last_part_text = exemplo[last_part+1:]
print(last_part_text)