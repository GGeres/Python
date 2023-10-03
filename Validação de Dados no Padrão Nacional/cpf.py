class Cpf:

    def __init__(self, doc):
        doc = str(doc)
        if self.cpf_valido(doc):
            self.cpf = doc
        else:
            raise ValueError("CPF Inválido !!")
    def __str__(self):
        return self.format_cpf()

    def cpf_valido(self, doc):
        if len(doc) == 11:
            return True
        else:
            return False
    def format_cpf(self):
        parte_um = self.cpf[:3]
        parte_dois = self.cpf[3:6]
        parte_tres = self.cpf[6:9]
        parte_quatro = self.cpf[9:]
        return ("{}.{}.{}-{}".format(parte_um, parte_dois, parte_tres, parte_quatro))