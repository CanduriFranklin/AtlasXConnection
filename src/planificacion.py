# src/planificacion.py
from .utils import realizar_inferencia

def simular_red(datos):
    """
    Simula escenarios de red utilizando el modelo Granite.
    """
    try:
        prompt = f"Simula un escenario de red con los siguientes datos:\n{datos}"
        resultado = realizar_inferencia(prompt)
        return resultado
    except Exception as e:
        return f"Error al simular red: {e}"

def predecir_mantenimiento(datos):
    """
    Predice necesidades de mantenimiento utilizando el modelo Granite.
    """
    try:
        prompt = f"Predice necesidades de mantenimiento para la siguiente infraestructura:\n{datos}"
        resultado = realizar_inferencia(prompt)
        return resultado
    except Exception as e:
        return f"Error al predecir mantenimiento: {e}"