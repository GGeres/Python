from codigo.bytebank import Funcionario

#lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1111)
#print(lucas.idade())

def teste_idade():
    func_teste = Funcionario('João', '13/02/2000', 1111)
    print(f'Teste = {func_teste.idade()}')

teste_idade()