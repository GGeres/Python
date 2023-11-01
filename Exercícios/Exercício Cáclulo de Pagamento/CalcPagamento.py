def calculoPagamento(hour,pay):
    if int(hour) < 40:
        payment = int(hour)*float(pay)
    else:
        payment = ((int(hour)-40)*1.5 + 40) * float(pay)
    pFinal = ('O valor a ser pago será: R$ {}'.format(payment, round(2)))
    print(pFinal)
