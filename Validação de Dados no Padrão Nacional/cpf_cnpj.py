from validate_docbr import CPF
from validate_docbr import CNPJ



class documento:
    @staticmethod
    def cria_doc(doc):
        if len(doc) == 11:
            return DocCPF(doc)
        elif len(doc) == 14:
            return DocCNPJ(doc)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

class DocCPF():
    def __init__(self, doc):
        if self.valida(doc):
            self.cpf = doc
        else:
            raise ValueError("CPF Inválido !!")

    def __str__(self):
        return self.format()

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def valida(self, doc):
        validador = CPF()
        return validador.validate(doc)

class DocCNPJ:
    def __init__(self, doc):
        if self.valida(doc):
            self.cnpj = doc
        else:
            raise ValueError("CNPJ Inválido !!")
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()

    def valida(self, doc):
        validador = CNPJ()
        return validador.validate(doc)





