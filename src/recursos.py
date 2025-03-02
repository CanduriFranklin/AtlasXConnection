# src/recursos.py# src/recursos.py
from .utils import realizar_inferencia

def asignar_recursos(datos):
    """
    Asigna recursos de manera óptima utilizando el modelo Granite.
    """
    try:
        prompt = f"Asigna recursos de manera óptima para los siguientes datos:\n{datos}"
        resultado = realizar_inferencia(prompt)
        return resultado
    except Exception as e:
        return f"Error al asignar recursos: {e}"