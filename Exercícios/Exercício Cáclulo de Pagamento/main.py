from CalcPagamento import calculoPagamento


horas = ('Digite as horas: \n')
taxa = ('Digite a taxa: \n')
hour = input(horas)
try:
    hour = int(hour)
    pay = float(input(taxa))
    try:
        calculoPagamento(hour, pay)
    except:
        print('Erro!! Insira um número!')
except:
    print('Erro!! Insira um número!')