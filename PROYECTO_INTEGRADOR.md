# 🏆 Guía del Proyecto Integrador - Talento Tech ML

Este documento define la metodología, los requisitos estándar y el checklist paso a paso para la **Preentrega** y la **Entrega Final**.

---

## 📌 Fase 1: Preentrega del Proyecto

El objetivo de la preentrega es validar la viabilidad del problema, la calidad del dataset y establecer un punto de partida (*baseline*) medible.

### Checklist de la Preentrega:
- [ ] **1. Definición del Problema**:
  - Contexto de negocio o investigación.
  - Objetivo del modelo: ¿Es regresión, clasificación o clustering?
  - Variable objetivo (*target*) identificada con claridad.
- [ ] **2. Origen y Adquisición de Datos**:
  - Fuente documentada (Kaggle, API, archivo CSV/Excel en Google Drive).
  - Descripción de cada atributo (diccionario de datos).
  - Cantidad de registros y columnas iniciales.
- [ ] **3. Análisis Exploratorio de Datos (EDA)**:
  - Detección y tratamiento de valores nulos o inconsistentes.
  - Detección de duplicados y outliers (boxplots, rango intercuartílico).
  - Análisis univariado y bivariado (histogramas, gráficos de dispersión, correlación de Pearson/Spearman).
  - Conclusiones y hallazgos clave del EDA.
- [ ] **4. Modelo Baseline (Línea de Base)**:
  - División de datos en Train / Test (`train_test_split`).
  - Modelo simple de referencia (e.g. `DummyClassifier`, `LinearRegression` básica).
  - Métrica de evaluación inicial para comparar mejoras futuras.

---

## 🚀 Fase 2: Proyecto Integrador Final

La entrega final consolida todo el ciclo de vida de Machine Learning, comparando múltiples modelos, aplicando ingeniería de características y argumentando las decisiones tomadas.

### Checklist de la Entrega Final:
- [ ] **1. Pipeline de Preprocesamiento y Feature Engineering**:
  - Escalado numérico (`StandardScaler`, `RobustScaler`, etc.).
  - Codificación categórica (`OneHotEncoder`, `OrdinalEncoder`, `TargetEncoder`).
  - Creación de nuevas variables relevantes (*feature extraction*).
  - Manejo de desbalance de clases (si aplica: SMOTE, ponderación de pesos de clase).
- [ ] **2. Experimentación Multimodelo**:
  - Entrenamiento de al menos 3 algoritmos distintos (e.g., Logistic/Linear Regression, Random Forest, XGBoost/LightGBM, SVM).
  - Validación cruzada estratificada (*Stratified K-Fold*).
  - Comparación tabular de métricas en Train y Test para diagnosticar overfitting/underfitting.
- [ ] **3. Optimización de Hiperparámetros**:
  - Búsqueda sistemática (`GridSearchCV`, `RandomizedSearchCV`).
  - Comparación del mejor modelo optimizado vs. baseline.
- [ ] **4. Interpretación del Modelo y Negocio**:
  - Importancia de variables (*Feature Importance*, valores SHAP).
  - Matriz de confusión comentada y análisis de costos de errores (falsos positivos vs. falsos negativos).
  - Recomendaciones accionables basadas en las predicciones.
- [ ] **5. Storytelling y Presentación**:
  - Diapositivas o infografía ejecutiva.
  - Código limpio, comentado, con celdas de markdown explicativas y reproducible.

---

## 📂 Enlaces a Espacios de Trabajo

- Cuaderno y artefactos de Preentrega: [`02_proyectos/preentrega/`](02_proyectos/preentrega/)
- Cuaderno y artefactos de Entrega Final: [`02_proyectos/proyecto_final/`](02_proyectos/proyecto_final/)
