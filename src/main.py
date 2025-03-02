# src/main.py
import streamlit as st
from .adquisiciones import analizar_adquisiciones
from .planificacion import simular_red, predecir_mantenimiento
from .recursos import asignar_recursos

st.title("AtlasXConnection - Public Network Management Platform")

# Menú de opciones
opcion = st.sidebar.selectbox(
    "Selecciona un módulo",
    ["Políticas y Adquisiciones", "Diseño y Planificación", "Asignación de Recursos"]
)

def manejar_modulo(titulo, texto_area, funcion):
    st.header(titulo)
    datos = st.text_area(texto_area)
    if st.button("Ejecutar"):
        try:
            resultado = funcion(datos)
            st.write(resultado)
        except Exception as e:
            st.error(f"Error al ejecutar la función: {e}")

if opcion == "Políticas y Adquisiciones":
    manejar_modulo("Análisis de Adquisiciones", "Ingresa los datos de adquisiciones", analizar_adquisiciones)

elif opcion == "Diseño y Planificación":
    manejar_modulo("Simulación de Redes", "Ingresa los datos de la red", simular_red)

elif opcion == "Asignación de Recursos":
    manejar_modulo("Asignación de Recursos", "Ingresa los datos de recursos", asignar_recursos)