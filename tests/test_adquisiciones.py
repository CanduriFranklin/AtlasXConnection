import pytest
from src.adquisiciones import analizar_adquisiciones

def test_analizar_adquisiciones():
    # Datos de prueba
    datos = "datos_ejemplo"
    resultado = analizar_adquisiciones(datos)
    
    # Verificar que el resultado no sea nulo
    assert resultado is not None