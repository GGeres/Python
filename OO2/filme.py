

class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temp):
        self.nome = nome.title()
        self.ano = ano
        self.temp = temp


vingadores = Filme("os vingadores", 2012, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} min.')

game_of_thrones = Serie("game of thrones", 2011, 8)
print(f'Nome: {game_of_thrones.nome} - Ano: {game_of_thrones.ano} - Temporadas: {game_of_thrones.temp}')
