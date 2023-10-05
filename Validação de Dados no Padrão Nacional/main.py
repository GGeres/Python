from validate_docbr import CNPJ
from cpf_cnpj import CPF

#cpf_um = Cpf("42200696825")
#print(cpf_um)
ex_cnpj = "35379838000112"
cnpj = CNPJ()
print(cnpj.validate(ex_cnpj))

