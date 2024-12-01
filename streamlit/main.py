# streamlit run main.py
import streamlit as st
import pandas as pd
import pickle

from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

import sys
sys.path.append("../")
from src.soporte_transformers import (
    load_models,
    load_options,
    realizar_prediccion
)
# Cargar las listas de opciones
lista_tipo_propiedad, lista_habitaciones, lista_aseos, lista_floor, lista_municipality,lista_district,lista_ascensor,lista_distancia = load_options()
# Cargar los modelos y transformadores entrenados
target_encoder, one_hot_encoder, robust_scaler, modelo_xgb =  load_models()

# Configurar la página de Streamlit
st.set_page_config(
    page_title="Predicción de Precios de Casas",
    page_icon="🏠",
    layout="centered",
)

# Título y descripción
st.title("🏠 Alquilator PRO 5000")
st.write("Usa esta aplicación para predecir el precio del alquiler de una casa basándote en sus características. ¡Sorpréndete con la magia de los datos! 🚀")

# Mostrar una imagen llamativa
st.image(
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994",  # URL de la imagen
    caption="Conoce el precio estimado del alquiler de tu vivienda.",
    use_container_width=True,
)
st.write("Actualmente el modelo está limitado a seleccionar opciones sobre lo que ya conoce.")

# Formularios de entrada
st.header("🔧 Características de la casa")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
with col1:
    tipo_propiedad = st.selectbox("Tipo de propiedad", lista_tipo_propiedad, help="Selecciona el tipo de casa.")
    rooms = st.selectbox("Número de Habitaciones",lista_habitaciones,help="Selecciona el número de habitaciones.")

with col2:
    size_propiedad = st.number_input("Tamaño en m²", min_value=10, max_value=600, value=80, step=10, help="Selecciona los m² que quieres.")
    bathrooms = st.selectbox("Número de Aseos",lista_aseos,help="Selecciona el número de aseos.")

with col3:
    floor = st.selectbox("Piso Deseado",lista_floor,help="Selecciona el piso, si no lo sabes, selecciona 'desconocido'.")
    municipio = st.selectbox("Municipio",lista_municipality,help="Selecciona el municipio si no lo sabes, selecciona 'desconocido'.")

with col4:
    ascensor = st.selectbox("¿Tiene Ascensor?",lista_ascensor,help="Selecciona si tienes ascensor, si no lo sabes, selecciona 'desconocido'.")
    distrito = st.selectbox("Distrito",lista_district,help="Selecciona el municipio si no lo sabes, selecciona 'desconocido'.")

dist_centro = st.selectbox("Distancia al Centro",lista_distancia,help="Selecciona la distancia al centro que quieres tener.")

# Botón para realizar la predicción
if st.button("💡 Predecir Precio"):
    prediction = realizar_prediccion(tipo_propiedad,size_propiedad,rooms,bathrooms,floor,municipio,distrito,ascensor,dist_centro,target_encoder,one_hot_encoder,robust_scaler,modelo_xgb)
    # Mostrar el resultado
    st.success(f"💵 El precio estimado del alquiler es: {round(prediction[0],2)} €")
    st.balloons()
