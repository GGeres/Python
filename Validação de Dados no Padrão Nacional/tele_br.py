import re
class Tele_Br:
    def __init__(self, tele):
        if self.valida_tel(tele):
            self.num = tele
        else:
            raise ValueError("Número Incorreto!!")

    def valida_tel(self,tel):
        padrao = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao, tel)
        if resposta:
            return True
        else:
            return False