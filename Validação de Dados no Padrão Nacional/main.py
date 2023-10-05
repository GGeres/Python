from validate_docbr import CNPJ
from tele_br import Tele_Br
import re

tele = "5511995217041"
tele_obj = Tele_Br(tele)

padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
resposta = re.search(padrao, tele)

print(resposta.group())