

# Proyecto: Predicción de Retención de Empleados 🏢

## 🎯 Objetivo

El objetivo principal de este proyecto es construir un modelo de machine learning capaz de predecir si un empleado permanecerá en la empresa o decidirá marcharse. A través de este análisis, se busca identificar patrones y los factores más relevantes que influyen en la retención y rotación del personal, como:

- Satisfacción laboral.
- Horas trabajadas.
- Relaciones con los jefes.
- Promociones o aumentos salariales.

Además de construir un modelo predictivo preciso, el proyecto pretende interpretar los resultados obtenidos para proponer estrategias prácticas que ayuden a mejorar la retención de empleados, contribuyendo a crear un entorno laboral más saludable y efectivo.

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
│   │   ├── 02_gestion_datos.ipynb
│   │   ├── 03_eda_gestionado.ipynb
│   │   ├── 04_encoding.ipynb
│   │   ├── 05_feature_scaling.ipynb
│   │   ├── 06_outliers.ipynb
│   │   ├── 07_desbalanceo.ipynb
│   │   ├── 08_modelos.ipynb
│   │   ├── 09_obtener_mejor_modelo.ipynb
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
- Se realiza después **tomek**

### Fase 8: Ejecución y Comparación de Modelos Predictivos
#### Modelos Usados:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBooster
---
# Resultados del Mejor Modelo (Modelo 4)
- Mejor modelo XGBooster:
- Tiene un test kappa alto.
- Mantiene un buen equilibrio entre train y test. No es overfitting.
- Es un modelo que es rápido y eficiente y nos permite ajustarle parámetros sin muchos quebraderos de cabeza.

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
