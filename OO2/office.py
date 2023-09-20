class Func:
    def regis_hora(self, horas):
        print('Horas registradas.')

    def show_task(self):
        print('Fez muita coisa...')

class Caelum(Func):
    def show_task(self):
        print('Fez muita coisa, Caelumer!')

    def bcdmes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos deste mês')

class Alura(Func):
    def show_task(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas no fórum')

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

jose = Junior()
jose.busca_perguntas_sem_respostas()

luan = Pleno()
luan.busca_perguntas_sem_respostas()
luan.bcdmes()
luan.show_task()