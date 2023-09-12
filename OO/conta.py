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
        if(self.__pode_sacar(valor) ):
            self.__saldo -= valor
        else:
            print("O valor {} não pode ser sacado.".format(valor))

    def __pode_sacar(self, valor_sacar):
        valor_disp = self.__lim + self.__saldo
        return valor_sacar <= valor_disp

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    def get_tit(self):
        return self.__tit
    def get_lim(self):
        return self.__lim
    def set_lim(self, lim):
        self.__lim = lim

    @property
    def saldo(self):
        return self.__saldo
    @property
    def tit(self):
        return self.__tit
    @property
    def lim(self):
        return self.__lim
    @lim.setter
    def lim(self, lim):
        self.__lim = lim


