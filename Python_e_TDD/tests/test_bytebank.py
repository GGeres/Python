import sys

sys.path.append('C:/Users/gusta/OneDrive/Documentos/ESTUDOS/Python/Python_e_TDD/codigo')

from codigo.bytebank import Funcionario

class TestClass:
    def test_checagem_de_idade(self):
        # Para um teste sempre começar desse jeito
        # Para testes utilizar o Conceito de Given(Para o Contexto Esperado)/When(Para a Ação)/Then(Para o Desfecho)
        # Given:
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('João', entrada, 1111)
        # When:
        resultado = funcionario_teste.idade()

        assert resultado == esperado
