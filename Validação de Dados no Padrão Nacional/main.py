from validate_docbr import CNPJ
from cpf_cnpj import CpfCnpj

#cpf_um = Cpf("42200696825")
#print(cpf_um)
ex_cnpj = "35379838000112"
ex_cpf = "42200696825"
#cnpj = CNPJ()
doc = CpfCnpj(ex_cnpj, 'cnpj')
doc2 = CpfCnpj(ex_cpf, 'cpf')

print(doc)
print(doc2)
