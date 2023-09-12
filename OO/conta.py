class Conta:
    def __init__(self, num, tit, saldo, lim):
        print("Construindo objeto ... {}".format(self))
        self.num = num
        self.tit = tit
        self.saldo = saldo
        self.lim = lim

    def extrato(self):
        print("O saldo do titular {} é de {}".format(self.tit, self.saldo))

    def deposita(self, valor):
        self.saldo += valor
    def saca(self, valor):
        self.saldo -= valor