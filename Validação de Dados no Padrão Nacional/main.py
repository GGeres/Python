from validate_docbr import CNPJ
from cpf_cnpj import documento

import re

padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto de 11995217041"
resposta = re.search(padrao, texto)
print(resposta.group())
