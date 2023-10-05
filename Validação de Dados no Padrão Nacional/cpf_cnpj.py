from validate_docbr import CPF
from validate_docbr import CNPJ
class CpfCnpj:

    def __init__(self, doc, type_doc):
        self.type_doc = type_doc
        doc = str(doc)
        if self.type_doc == 'cpf':
            if self.cpf_valido(doc):
                self.cpf = doc
            else:
                raise ValueError("CPF Inválido !!")
        elif self.type_doc == "cnpj":
            if self.cnpj_valido(doc)

    def __str__(self):
        return self.format_cpf()

    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida")
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)