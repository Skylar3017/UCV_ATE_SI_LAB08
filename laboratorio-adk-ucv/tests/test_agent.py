import pytest

from agente_ucv.agent import (explicar_concepto, calcular_promedio)


def test_api():
    resultado = explicar_concepto("api")
    assert resultado["status"] == "success"


def test_concepto_no_encontrado():

    resultado = explicar_concepto("robotica")
    assert resultado["status"] == "not_found"
    
def test_calcular_promedio():

    resultado = calcular_promedio(18, 16, 20)
    assert resultado["status"] == "success"
    assert resultado["promedio"] == pytest.approx(18.0)




