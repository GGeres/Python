class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

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
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} min'

class Serie(Programa):
    def __init__(self, nome, ano, temp):
        super().__init__(nome, ano)
        self.temp = temp
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temp} temporadas - {self.likes} Likes'

senhor = Filme("o senhor dos anéis - a sociedade do anel",2001, 178)


LOU = Serie("the last of us", 2023, 1)


lista = [senhor, LOU]

for program in lista:
    print(program)
