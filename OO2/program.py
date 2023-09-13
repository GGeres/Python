class Programa:
    def __init__(self, nome, duracao):
        self._nome = nome.title()
        self.duracao = duracao
        self._like = 0

    @property
    def likes(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        

class Serie(Programa):
    def __init__(self, nome, ano, temp):
        super().__init__(nome, ano)
        self.temp = temp
        