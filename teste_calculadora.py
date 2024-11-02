import pytest
from Calculadora import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_soma(calculadora):
    calculadora.numero1 = 2
    calculadora.numero2 = 3
    assert calculadora.soma() == 5

def test_subtracao(calculadora):
    calculadora.numero1 = 5
    calculadora.numero2 = 2
    assert calculadora.subtracao() == 3

def test_multiplicacao(calculadora):
    calculadora.numero1 = 3
    calculadora.numero2 = 4
    assert calculadora.multiplicacao() == 12

def test_divisao(calculadora):
    calculadora.numero1 = 10
    calculadora.numero2 = 2
    assert calculadora.divisao() == 5

def test_divisao_por_zero(calculadora):
    calculadora.numero1 = 10
    calculadora.numero2 = 0
    with pytest.raises(ZeroDivisionError):
        calculadora.divisao()
