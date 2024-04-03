from Python_e_TDD.codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_02_2000_deve_retornar_24(self):
        # Para um teste sempre começar desse jeito
        # Para testes utilizar o Conceito de Given(Para o Contexto Esperado)/When(Para a Ação)/Then(Para o Desfecho)
        # Given:
        entrada = '13/02/2000'
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        # When:
        resultado = funcionario_teste.idade()

        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calc_bonus_recebe_1000_retorna_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000000000_retorna_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000000

            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado