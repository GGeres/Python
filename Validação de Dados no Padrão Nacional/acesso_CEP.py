
class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_Valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")


    def cep_Valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False