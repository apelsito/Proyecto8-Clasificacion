# Análisis y Modelado: Predicción de Precios de Casas 🏠

# Descripción del Proyecto 💡

Este proyecto tiene como objetivo desarrollar un modelo predictivo capaz de estimar el precio de propiedades inmobiliarias en Madrid, utilizando un conjunto de datos real con 40 columnas. Estas columnas incluyen información clave sobre las propiedades, como su tamaño, ubicación, número de habitaciones, tipo de propiedad y más. 

El propósito principal es ofrecer una herramienta útil para agentes inmobiliarios, compradores y vendedores, que permita tomar decisiones más informadas basadas en datos.

## 🎯 Objetivo
1. **Carga y Exploración de Datos**:
   - Identificar patrones en los datos.
   - Detectar valores atípicos y posibles inconsistencias.

2. **Preprocesamiento**:
   - Limpieza y preparación de datos.
   - Codificación de variables categóricas.
   - Escalado de variables numéricas.
   - Gestión de valores nulos y outliers.

3. **Modelado**:
   - Entrenamiento de múltiples modelos de Machine Learning.
   - Evaluación de su desempeño utilizando métricas como RMSE y R².

4. **Visualización**:
   - Mostrar gráficamente la importancia de las variables.
   - Analizar los errores y predicciones del modelo.

5. **Optimización**:
   - Ajustar hiperparámetros para maximizar la precisión del modelo.

## Estructura del Proyecto 🗂️

```bash
Proyecto7-PrediccionCasas/
├── datos/                      # Archivos de datos CSV y PKL para el proyecto.
│   ├── lista_opciones/         # Lista de opciones para los menús de streamlit.
│   ├── modelos-encoders/       # Lista de PKLs de los modelos y encoders ya entrenados.
│
├── jupyter_notebooks/          # Notebooks de Jupyter con los modelos probados.
│   ├── Modelo X/               # Carpeta del modelo
│   │   ├── 00_Sobre_El_Modelo.md
│   │   ├── 01_eda_inicial.ipynb
│   │   ├── 02_gestion_nulos.ipynb
│   │   ├── 03_eda_sin_nulos.ipynb
│   │   ├── 04_encoding.ipynb
│   │   ├── 05_feature_scaling.ipynb
│   │   ├── 06_gestion_outliers.ipynb
│   │   ├── 07_regresion_lineal.ipynb
│   │   ├── 08_decision_tree.ipynb
│   │   ├── 09_gradient_boosting.ipynb
│   │   ├── 10_XGBoost.ipynb
│ 
├── src/                        # Archivos .py para funciones auxiliares del proyecto.
│
├── streamlit/                  # Web para realizar predicciones de forma rápida y bonita
│    ├── main.py                # Configuración Web
│    ├── prueba_modelo.ipynb 
│
└── README.md                   # Descripción del proyecto, instrucciones de instalación y uso.
```
# Instalación y Requisitos 🛠️

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.x** 🐍
- **Jupyter Notebook** 📓 para ejecutar y visualizar los análisis de datos
- **Bibliotecas de Python**:
    - [pandas](https://pandas.pydata.org/docs/) para manipulación y análisis de datos 🧹
    - [numpy](https://numpy.org/doc/stable/) para cálculos numéricos y manejo de matrices 🔢
    - [matplotlib](https://matplotlib.org/stable/index.html) para crear gráficos básicos 📊
    - [seaborn](https://seaborn.pydata.org/) para visualizaciones estadísticas avanzadas 📈
    - [tqdm](https://tqdm.github.io/) para mostrar barras de progreso en procesos largos ⏳
    - [xgboost](https://xgboost.readthedocs.io/) para la implementación de modelos basados en Gradient Boosting 🌟
    - [scikit-learn](https://scikit-learn.org/stable/) para modelado predictivo y preprocesamiento, incluyendo:
        - `LinearRegression`, `DecisionTreeRegressor`, `RandomForestRegressor`, `GradientBoostingRegressor`, y `XGBRegressor` para tareas de regresión
        - `train_test_split`, `GridSearchCV`, `KFold`, `LeaveOneOut` y `cross_val_score` para partición de datos y validación de modelos
        - `StandardScaler` para el escalado de variables
        - Métricas como `r2_score`, `mean_squared_error`, `mean_absolute_error` para evaluar los modelos
    - [pickle](https://docs.python.org/3/library/pickle.html) para serializar y cargar modelos y objetos 🛠️

## Configuración Adicional

- Configura `pd.options.display.float_format` para un formato más claro en los valores flotantes.
- Añade rutas personalizadas al sistema usando `sys.path.append` para facilitar el acceso a los módulos personalizados del proyecto.

## Instalación 🛠️

1. Clona este repositorio para visualizarlo en vscode:
```bash
git clone https://github.com/apelsito/Proyecto8-Clasificacion
cd Proyecto8-Clasificacion
```
# Resumen de lo realizado en el Modelo final: 

## Fase 1: Análisis Inicial
   - Se realiza un eda inicial
---
## Fase 2: Gestión Datos
### Se gestionan los datos, eliminando:
- Columna EmployeeID

### Se eliminan duplicados
- Tras eliminar EmployeeID surgieron los duplicados
- Al verlos, los datos coincidian en categorías que descartaba la idea de que fueran coincidencias que pudieran ocurrir
### Se gestionan los datos, eliminando:
- Columna EmployeeCount
- StandardHours
- Over18
- PerformanceRating

### Se vuelven de numéricas a categóricas:
- Education
- JobLevel
- StockOptionLevel
- TrainingTimesLastYear
- JobInvolvement
- PercentSalaryHike
- DistanceFromHome

### Se gestionan los nulos de:
- NumCompaniesWorked
- EnvironmentSatisfaction
- JobSatisfaction
- WorkLifeBalance
- Se eliminan las filas nulas donde Attrition era "NO"

- Se rellena mediante **IterativeImputer** con **RandomForest** las filas con nulos donde **Attrition** fuera "Yes"

- Se redondea el valor rellenado al más cercano, al ser una categoría no podían ser decimales

- Se categorizan tras gestionar los nulos de:
   - NumCompaniesWorked
   - EnvironmentSatisfaction
   - JobSatisfaction
   - WorkLifeBalance
---

---
### Fase 4 Encoding
- Se realiza el encoding de las columnas categóricas:
    - Target Encoder para Ordinales
    - OneHot Encoder para Nominales
---
### Fase 5: Feature Scaling
   - Se realiza Robust Scaler
---
### Fase 6: Gestión Outliers
   - No se tocan los Outliers
---
### Fase 7: Desbalanceo
- Se realiza **smotenc** incluyendo categorías para evitar generar nuevas

### Fase 8: Ejecución y Comparación de Modelos Predictivos
#### Modelos Usados:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBooster
---
# Resultados del Mejor Modelo (Modelo 4)


# Streamlit
Se ha creado una web con streamlit en local que permite al usuario realizar predicciones sobre un empleado en caso de querer ejecutarla deberá:

1. abrir la terminal de python
2. ir a la carpeta **streamlit**
3. ejecutar: 
```bash
   streamlit run main.py
```
Se le pedirá un correo electrónico en la consola, puede saltarse el paso si le da enter de nuevo

Se abrirá una ventana de su explorador con la web lista para poder usarse.

# Contribuciones 🤝

Las contribuciones a este proyecto son muy bienvenidas. Si tienes alguna sugerencia, mejora o corrección, no dudes en ponerte en contacto o enviar tus ideas.

Cualquier tipo de contribución, ya sea en código, documentación o feedback, será valorada. ¡Gracias por tu ayuda y colaboración!

# Autores y Agradecimientos ✍️

## Autor ✒️
**Gonzalo Ruipérez Ojea** - [@apelsito](https://github.com/apelsito) en github

## Agradecimientos ❤️
Quiero expresar mi agradecimiento a **Hackio** y su equipo por brindarme la capacidad y las herramientas necesarias para realizar este proyecto con solo una semana de formación. Su apoyo ha sido clave para lograr este trabajo.
