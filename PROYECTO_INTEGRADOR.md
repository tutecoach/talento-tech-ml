# 🏆 Guía del Proyecto Integrador - Talento Tech ML

Este documento define la metodología, los requisitos estándar y el checklist paso a paso para la **Preentrega** y la **Entrega Final**.

---

## 📌 Fase 1: Preentrega del Proyecto *(Completada — Hito Octubre 2026)*

El objetivo de la preentrega es validar la viabilidad del problema, la calidad del dataset y preparar los conjuntos de entrenamiento y prueba sin fuga de información.

> **Estado:** Entregada en [`02_proyectos/preentrega/Pre_entrega26.ipynb`](02_proyectos/preentrega/Pre_entrega26.ipynb) y documentada en [`02_proyectos/preentrega/informe_preentrega.md`](02_proyectos/preentrega/informe_preentrega.md). Validar ejecución completa de principio a fin al continuar el notebook en Google Colab.

### Checklist de la Preentrega (Parte A):
- [x] **A1. Selección del dataset**:
  - Origen del dataset documentado (Spotify Tracks Dataset en Kaggle).
  - Contexto de negocio y descripción del problema (*Hit Prediction*, clasificación binaria `is_hit`).
  - Justificación de la elección sobre datos tabulares de tamaño y complejidad moderados.
- [x] **A2. Análisis Exploratorio Inicial (EDA)**:
  - Distribución de variables y detección de valores faltantes.
  - Análisis de correlaciones (matriz de Pearson) y visualizaciones univariadas/bivariadas.
- [x] **A3. Limpieza de datos**:
  - Tratamiento de valores nulos, desduplicación lógica por `track_id` y filtrado de anomalías/outliers.
- [x] **A4. Transformaciones básicas**:
  - Codificación numérica/categórica y creación de variable objetivo binaria `is_hit`.
- [x] **A5. Selección de variables relevantes**:
  - Selección fundamentada de atributos psicoacústicos y descarte de metadatos textuales.
- [x] **A6. División en entrenamiento y prueba**:
  - Partición estratificada 80/20 (`train_test_split`) y escalado numérico (`StandardScaler`) sin *data leakage*.

---

## 🚀 Fase 2: Proyecto Integrador Final *(Entrega Final — Parte B)*

La entrega final consolida todo el ciclo de vida de Machine Learning **continuando sobre el mismo notebook de la Pre-Entrega** en Google Colab (no es un notebook nuevo).

> **Documentos oficiales:** [`02_proyectos/proyecto_final/ML_Consigna_Entrega_Final.md`](02_proyectos/proyecto_final/ML_Consigna_Entrega_Final.md) · [`02_proyectos/proyecto_final/CHECKLIST_ENTREGA_FINAL.md`](02_proyectos/proyecto_final/CHECKLIST_ENTREGA_FINAL.md)

### Checklist de la Entrega Final:
- [ ] **0. Requisitos Previos**:
  - Completar el **cuestionario de autoevaluación del Campus Virtual** *(obligatorio)*.
  - Abrir el notebook de la Pre-Entrega en Google Colab, ejecutar de principio a fin sin errores e incorporar feedback (si lo hubo).
- [ ] **B1. Elección del Modelo**:
  - Elegir al menos un modelo y justificar la elección según el tipo de problema (clasificación binaria).
  - *(Opcional/Recomendado)* Sumar modelos adicionales para comparar (ej. Regresión Logística, Árbol de Decisión, Random Forest, KNN).
- [ ] **B2. Entrenamiento**:
  - Entrenar los modelos sobre el conjunto de entrenamiento y generar predicciones sobre el conjunto de prueba.
- [ ] **B3. Evaluación con Métricas Adecuadas**:
  - Clasificación: *accuracy*, *precisión*, *recall*, *F1-score* y matriz de confusión.
  - Explicar qué significan los resultados y armar una tabla comparativa entre modelos.
- [ ] **B4. Validación Cruzada (*Cross-Validation*)**:
  - Aplicar *cross-validation* (ej. 5 folds estratificados), reportar media y desvío de las métricas y comparar contra el conjunto de prueba.
- [ ] **B5. Visualización e Interpretación**:
  - Gráficos de resultados (matrices de confusión, curvas comparativas, etc.) e importancia de variables (*Feature Importance*).
  - Análisis de aciertos y errores del modelo (falsos positivos vs. falsos negativos) y sus posibles causas.
- [ ] **B6. Conclusiones**:
  - Reflexión sobre el modelo entrenado, límites del modelo, posibilidades de mejora y utilidad práctica del proyecto.
- [ ] **B7. Anexo Final**:
  - Link al dataset original, referencias de fuentes externas, descripción/links a archivos adicionales y aclaraciones necesarias.
- [ ] **Revisión y Entrega (No requiere presentación oral)**:
  - Notebook organizado, bien comentado y ejecutado completo (*Entorno de ejecución → Ejecutar todo*).
  - Carpeta en Google Drive nombrada `HERNANDEZ MATIAS H - Comisión 26240 - TPI Machine Learning` con sets de datos originales y el Colab, con permisos de **lectura públicos** y **edición para el instructor**.
  - Link entregado en el Campus Virtual (apartado Entrega de Proyecto Final, Clase 16) dentro del plazo (7 días).

---

## 📂 Enlaces a Espacios de Trabajo

- Cuaderno y artefactos de Preentrega: [`02_proyectos/preentrega/`](02_proyectos/preentrega/)
- Consigna, checklist y artefactos de Entrega Final: [`02_proyectos/proyecto_final/`](02_proyectos/proyecto_final/)
