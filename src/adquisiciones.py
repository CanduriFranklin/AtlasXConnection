# src/adquisiciones.py
from src.utils import realizar_inferencia

def analizar_adquisiciones(datos):
    """
    Analiza datos de adquisiciones utilizando el modelo Granite.
    """
    prompt = f"Analiza los siguientes datos de adquisiciones y proporciona recomendaciones:\n{datos}"
    resultado = realizar_inferencia(prompt)
    return resultado    # src/adquisiciones.py
    from .utils import realizar_inferencia
    
    def analizar_adquisiciones(datos):
        """
        Analiza datos de adquisiciones utilizando el modelo Granite.
        """
        try:
            prompt = f"Analiza los siguientes datos de adquisiciones y proporciona recomendaciones:\n{datos}"
            resultado = realizar_inferencia(prompt)
            return resultado
        except Exception as e:
            return f"Error al analizar adquisiciones: {e}"