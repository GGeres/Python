def cria_conta(num, tit, saldo, lim):
    conta = {"num": num, "tit": tit, "saldo": saldo, "lim": lim }
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))
