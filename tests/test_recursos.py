import pytest
from src.recursos import asignar_recursos

def test_asignar_recursos():
    datos = "datos_ejemplo"
    resultado = asignar_recursos(datos)
    assert resultado is not None