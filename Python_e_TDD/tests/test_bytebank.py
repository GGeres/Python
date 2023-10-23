from ..codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        # Para um teste sempre começar desse jeito
        # Para testes utilizar o Conceito de Given(Para o Contexto Esperado)/When(Para a Ação)/Then(Para o Desfecho)
        # Given:
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('João', entrada, 1111)
        # When:
        resultado = funcionario_teste.idade()

        assert resultado == esperado
