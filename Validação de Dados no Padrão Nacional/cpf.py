class Cpf:

    def __init__(self, doc):
        doc = str(doc)
        if self.cpf_valido(doc):
            self.cpf = doc
        else:
            raise ValueError("CPF Inválido !!")

    def cpf_valido(self, doc):
        if len(doc) == 11:
            return True
        else:
            return False
