from validate_docbr import CNPJ
from cpf_cnpj import documento

#cpf_um = Cpf("42200696825")
#print(cpf_um)

ex_cnpj = "35379838000112"

ex_cpf = "42200696825"
#cnpj = CNPJ()

doc1 = documento.cria_doc(ex_cnpj)

doc2 = documento.cria_doc(ex_cpf)

print(doc1)
print(doc2)
