from codigo.bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/02/2000',1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()

