# Modelo 3
- Se realiza un eda inicial
### Gestión Datos
- Se gestionan los datos, eliminando:
    - Columna EmployeeID
- Se eliminan duplicados

- Se gestionan los datos, eliminando:
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
- Se realiza Robust Scaler

### Outliers
- No se tocan los Outliers

### Desbalanceo
- Se realiza smotenc incluyendo categorías para evitar generar nuevas