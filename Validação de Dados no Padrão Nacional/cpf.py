from validate_docbr import CPF
class Cpf:

    def __init__(self, doc):
        doc = str(doc)
        if self.cpf_valido(doc):
            self.cpf = doc
        else:
            raise ValueError("CPF Inválido !!")
    def __str__(self):
        return self.format_cpf()

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida")
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)