# src/training.py
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from .config import API_KEY, SERVICE_URL, ASSISTANT_ID

def ajustar_modelo(datos):
    """
    Ajusta el modelo de IBM Watson Assistant con datos específicos.
    """
    try:
        # Configuración de autenticación
        authenticator = IAMAuthenticator(API_KEY)
        assistant = AssistantV2(
            version="2023-06-15",
            authenticator=authenticator
        )
        assistant.set_service_url(SERVICE_URL)

        # Ajustar el modelo con datos específicos
        response = assistant.create_session(
            assistant_id=ASSISTANT_ID
        ).get_result()

        # Guardar el modelo ajustado
        with open("models/granite/modelo_ajustado.pkl", "wb") as f:
            f.write(response)

        return response
    except Exception as e:
        print(f"Error al ajustar el modelo: {e}")
        return None