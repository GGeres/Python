

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__like = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__like
    def dar_like(self):
        self.__like += 1


class Serie:
    def __init__(self, nome, ano, temp):
        self.__nome = nome.title()
        self.ano = ano
        self.temp = temp
        self.__like = 0

    @property
    def likes(self):
        return self.__like

    def dar_like(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme("os vingadores", 2012, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} min - Likes {vingadores.likes}')


game_of_thrones = Serie("game of thrones", 2011, 8)
game_of_thrones.dar_like()
print(f'Nome: {game_of_thrones.nome} - Ano: {game_of_thrones.ano} - Temporadas: {game_of_thrones.temp} - Likes: {game_of_thrones.likes}')
