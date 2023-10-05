from datetime import datetime, timedelta

class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_ano = [
            "","Janeiro", "Fevereiro","Março",
            "Abril","Maio","Junho","Julho","Agosto",
            "Setembro","Outubro","Novembro","Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        print(mes_cadastro)
        return meses_ano[mes_cadastro]

    def dia_semana(self):
        dia_lista = [
            "Segunda-Feira","Terça-Feira","Quarta-Feira",
            "Quinta-Feira","Sexta-Feira","Sábado","Domingo"
        ]

        dia_semana = self.momento_cadastro.weekday()
        return dia_lista[dia_semana]

    def format_data(self):
        data_format = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_format

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today()+timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro