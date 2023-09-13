

class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temp):
        self.nome = nome
        self.ano = ano
        self.temp = temp


vingadores = Filme("Os Vingadores", 2012, 160)
print(vingadores.nome)

game_of_thrones = Serie("Game of Thrones", 2011, 8)
print(f'Nome: {game_of_thrones.nome} - Ano: {game_of_thrones.ano} - Temporadas: {game_of_thrones.temp}')
