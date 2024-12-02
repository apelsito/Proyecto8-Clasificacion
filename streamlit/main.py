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
lista_business_travel,lista_department,lista_distance_from_home,lista_education,lista_education_field,lista_gender,lista_job_level,lista_job_role,lista_marital_status,lista_num_companies_worked,lista_percent_salary_hike,lista_stock_option_level,lista_training_times_last_year,lista_environment_satisfaction,lista_job_satisfaction,lista_work_life_balance,lista_job_involvement = load_options()
# Cargar los modelos y transformadores entrenados
target_encoder, one_hot_encoder, robust_scaler, modelo_xgb =  load_models()

# Configurar la página de Streamlit
st.set_page_config(
    page_title="Predicción de Salida de Empleados",
    page_icon="🏠",
    layout="centered",
)

# Título y descripción
st.title("🏠 Recursos Humanos Pro 5000")
st.write("Usa esta aplicación para predecir si un empleado se va de la empresa ¡Sorpréndete con la magia de los datos! 🚀")

# Mostrar una imagen llamativa
st.image(
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994",  # URL de la imagen
    caption="Conoce si un empleado se va de la empresa",
    use_container_width=True,
)

# Formularios de entrada
st.header("🔧 Sobre el Empleado:")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)
col11, col12 = st.columns(2)
col13, col14 = st.columns(2)

with col1:
    edad = st.number_input("Edad Empleado",min_value=18,max_value=80,step=1)
    viajes = st.selectbox("Frecuencia Viajes Empleado",lista_business_travel,help="Selecciona la frecuencia de Viaje del Empleado.")

with col2:
    departamento = st.selectbox("Departamento del Empleado",lista_department,help="Selecciona el Departamento del Empleado.")
    distancia_a_casa = st.selectbox("Distancia a casa",lista_distance_from_home,help="Selecciona la distancia a casa del empleado.")

with col3:
    educacion = st.selectbox("Educación Empleado",lista_education,help="Selecciona la educación del empleado.")
    area_educacion = st.selectbox("Área educativa",lista_education_field,help="Selecciona el área educativa del empleado.")

with col4:
    genero = st.selectbox("Género del empleado",lista_gender,help="Selecciona el género del empleado.")
    nivel_laboral = st.selectbox("Nivel laboral",lista_job_level,help="Selecciona el nivel laboral.")

with col5:
    rol_laboral = st.selectbox("Rol Laboral",lista_job_role,help="Selecciona el rol laboral.")
    estado_marital = st.selectbox("Estado marital",lista_marital_status,help="Selecciona el estado marital.")

with col6:
    sueldo_mensual =  st.number_input("Sueldo Mensual Empleado (Rupees)",min_value=1000,max_value=999999999,step=1)
    companies_previas = st.selectbox("Empresas en las que ha trabajado",lista_num_companies_worked)

with col7:
    aumento_salario_porcentual = st.selectbox("Porcentaje Extra Sueldo",lista_percent_salary_hike)
    opciones_bolsa = st.selectbox("Prioridad Compra Acciones de la Empresa",lista_stock_option_level)

with col8:
    anios_trabajados = st.number_input("Años Trabajados",min_value=0,max_value=100,step=1)
    cursos_acometidos_anio_pasado = st.selectbox("Cursos Realizados Año Pasado",lista_training_times_last_year)

with col9:
    anios_en_empresa = st.number_input("Años Trabajados en la empresa",min_value=0,max_value=100,step=1)
    satisfaccion_ambiente_trabajo = st.selectbox("Satisfacción del Ambiente de Trabajo",lista_environment_satisfaction)

with col10:
    anios_desde_ascenso = st.number_input("Años desde el último ascenso",min_value=0,max_value=100,step=1)
    anios_con_el_manager = st.number_input("Años Trabajados con el manager",min_value=0,max_value=100,step=1)

with col11:
    satisfaccion_laboral = st.selectbox("Satisfacción Laboral",lista_job_satisfaction)
    balance_vida_trabajo = st.selectbox("Balance Vida-Trabajo del Empleado",lista_work_life_balance)


participacion_laboral = st.selectbox("Participación Laboral del Empleado",lista_job_involvement)

# Botón para realizar la predicción
if st.button("💡 Predecir Salida del Empleado"):
    prediction = realizar_prediccion(lista_business_travel,lista_department,lista_distance_from_home,lista_education,lista_education_field,lista_gender,lista_job_level,lista_job_role,lista_marital_status,lista_num_companies_worked,lista_percent_salary_hike,lista_stock_option_level,lista_training_times_last_year,lista_environment_satisfaction,lista_job_satisfaction,lista_work_life_balance,lista_job_involvement,target_encoder,one_hot_encoder,robust_scaler,modelo_xgb)
    # Mostrar el resultado
    if prediction[0] == 0:
        st.success(f"El empleado es muy probable que no se vaya!.")
        st.balloons()
    else:
        st.success(f"El empleado tiene altas probabilidades de irse.")
    
