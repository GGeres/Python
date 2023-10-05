from datetime import datetime

class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

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
        print(data_format)