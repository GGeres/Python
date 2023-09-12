class Conta:
    def __init__(self, num, tit, saldo, lim):
        print("Construindo objeto ... {}".format(self))
        self.__num = num
        self.__tit = tit
        self.__saldo = saldo
        self.__lim = lim

    def extrato(self):
        print("O saldo do titular {} é de {}".format(self.__tit, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)