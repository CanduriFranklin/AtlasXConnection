echo 'import pytest
from src.adquisiciones import analizar_adquisiciones

def test_analizar_adquisiciones():
    datos = "datos_ejemplo"
    resultado = analizar_adquisiciones(datos)
    assert resultado is not None
' > tests/test_adquisiciones.py