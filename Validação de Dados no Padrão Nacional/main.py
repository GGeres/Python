from datetime import datetime, timedelta

from datas_br import DatasBR


cadastro = DatasBR

print(cadastro.format_data())

hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatada)
print(type(hoje_formatada))
