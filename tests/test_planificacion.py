echo 'import pytest
from src.planificacion import simular_red

def test_simular_red():
    datos = "datos_ejemplo"
    resultado = simular_red(datos)
    assert resultado is not None
' > tests/test_planificacion.py