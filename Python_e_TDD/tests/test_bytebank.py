from ..codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        # Para um teste sempre começar desse jeito
        # Para testes utilizar o Conceito de Given(Para o Contexto Esperado)/When(Para a Ação)/Then(Para o Desfecho)
        # Given:
        entrada = '13/03/2000'
        esperado = 24

        funcionario_teste = Funcionario('João', entrada, 1111)
        # When:
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Gustavo_Geres_deve_retornar_Geres(self):
        entrada = ' Gustavo Geres ' #Given/Contexto
        esperado = 'Geres'

        gustavo = Funcionario(entrada, '13/02/2000', 1111)
        resultado = gustavo.sobrenome() #When

        assert resultado == esperado
