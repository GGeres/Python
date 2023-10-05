import re
class Tele_Br:
    def __init__(self, tele):
        if self.valida_tel(tele):
            self.num = tele
        else:
            raise ValueError("Número Incorreto!!")

    def __str__(self):
        return self.format_num()

    def valida_tel(self,tel):
        padrao = "([0-9]{2})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, tel)
        if resposta:
            return True
        else:
            return False

    def format_num(self):
        padrao = "([0-9]{2})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.num)
        num_format = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return num_format