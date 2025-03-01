echo 'from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from src.config import API_KEY, SERVICE_URL, ASSISTANT_ID

def realizar_inferencia(datos):
    # Configuración de autenticación
    authenticator = IAMAuthenticator(API_KEY)
    assistant = AssistantV2(
        version="2023-06-15",
        authenticator=authenticator
    )
    assistant.set_service_url(SERVICE_URL)

    # Realizar inferencia
    response = assistant.message(
        assistant_id=ASSISTANT_ID,
        session_id="session_id",
        input={
            "message_type": "text",
            "text": f"Realizar inferencia con: {datos}"
        }
    ).get_result()
    return response
' > src/utils.py