# src/utils.py# src/utils.py
import requests
from .config import API_KEY, SERVICE_URL, PROJECT_ID, MODEL_ID
from .database import execute_query

def realizar_inferencia(prompt):
    """
    Realiza una inferencia utilizando el modelo Granite de IBM.
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    body = {
        "input": f"<|start_of_role|>system<|end_of_role|>You are Granite, an AI language model developed by IBM in 2024. You are a cautious assistant. You carefully follow instructions. You are helpful and harmless and you follow ethical guidelines and promote positive behavior.<|end_of_text|><|start_of_role|>assistant<|end_of_role|>{prompt}",
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 900,
            "min_new_tokens": 0,
            "repetition_penalty": 1
        },
        "model_id": MODEL_ID,
        "project_id": PROJECT_ID
    }

    try:
        response = requests.post(
            SERVICE_URL,
            headers=headers,
            json=body
        )

        response.raise_for_status()

        data = response.json()
        resultado = data["results"][0]["generated_text"]

        # Guardar el resultado en la base de datos
        query = """
        INSERT INTO inferencias (prompt, resultado)
        VALUES (%s, %s);
        """
        execute_query(query, (prompt, resultado))

        return resultado
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error en la solicitud: {e}")
    except Exception as e:
        raise Exception(f"Error al realizar la inferencia: {e}")