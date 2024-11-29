# Modelo 1
- Se realiza un eda inicial
### Gestión Datos
- Se gestionan los datos, eliminando:
    - Columna EmployeeID
    - Columna EmployeeCount
    - StandardHours
    - Over18
    - PerformanceRating

- Se vuelven de numéricas a categóricas:
    - Education
    - JobLevel
    - StockOptionLevel
    - TrainingTimesLastYear
    - JobInvolvement
    - PercentSalaryHike
    - DistanceFromHome

- Se gestionan los nulos de:
    - NumCompaniesWorked
    - EnvironmentSatisfaction
    - JobSatisfaction
    - WorkLifeBalance

- Se eliminan las filas nulas donde Attrition era "NO"

- Se rellena mediante IterativeImputer con RandomForest las filas con nulos donde Attrition fuera "Yes"

- Se redondea el valor rellenado al más cercano, al ser una categoría no podían ser decimales

- Se categorizan tras gestionar los nulos de:
    - NumCompaniesWorked
    - EnvironmentSatisfaction
    - JobSatisfaction
    - WorkLifeBalance
### Encoding
- Se realiza el encoding de las columnas categóricas:
    - Target Encoder para Ordinales
    - OneHot Encoder para Nominales

### feature-Scaling
- Se realiza 


### Outliers
- Se gestionan los outliers con Isolation Forest agrupando por:
    - No es outlier: No se detecto nunca como outlier
    - Improbable outlier: Se detecto menos del 60% de las veces como outlier
    - Probable outlier: se detecto 60% o más de las veces como outlier
    - Total outlier: se detecto siempre como outlier

- Se eliminan Total y Probable donde Attrion sea "No"
- No se toca ningún outlier cuyo Attrition sea "Yes"

### Desbalanceo
