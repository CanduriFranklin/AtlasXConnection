# src/config.py
# src/config.py
import os

# Configuración de IBM
API_KEY = os.getenv("b59LXfXIKYmPdykpiOQjl08RW3C1VRP4_ivsGM9PuuZY")  # Reemplaza con tu token de IBM Cloud
SERVICE_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
PROJECT_ID = os.getenv("IBM_PROJECT_ID", "80a0d1f8-fb3e-4a4a-8ecb-fba2fbd0f678")  # Reemplaza con tu project_id
MODEL_ID = "ibm/granite-3-8b-instruct"

# Configuración de PostgreSQL
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "atlasxconnection"),
    "user": os.getenv("DB_USER", "atlasuser"),
    "password": os.getenv("DB_PASSWORD", "atlaspassword"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432))
}