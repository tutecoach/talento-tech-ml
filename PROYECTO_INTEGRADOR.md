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

> **Artefactos finales:** [`02_proyectos/proyecto_final/Pre_entrega26.ipynb`](02_proyectos/proyecto_final/Pre_entrega26.ipynb) · [`02_proyectos/proyecto_final/informe_final.md`](02_proyectos/proyecto_final/informe_final.md) · [`02_proyectos/proyecto_final/CHECKLIST_ENTREGA_FINAL.md`](02_proyectos/proyecto_final/CHECKLIST_ENTREGA_FINAL.md)

### Checklist de la Entrega Final:
- [x] **0. Requisitos Previos**:
  - [x] Completar el **cuestionario de autoevaluación del Campus Virtual** *(obligatorio)*.
  - [x] Abrir el notebook de la Pre-Entrega en Google Colab, ejecutar de principio a fin sin errores e incorporar feedback (incluye corrección preventiva de `'Unnamed: 0'`).
- [x] **B1. Elección del Modelo**:
  - Elección justificada según clasificación binaria desbalanceada (`DummyClassifier`, Regresión Logística, KNN, Árbol de Decisión y Random Forest + experimento Audio vs. Audio+Género con `ColumnTransformer`).
- [x] **B2. Entrenamiento**:
  - Entrenamiento sobre `X_train` (`71,678` pistas) y predicciones sobre `X_test` (`17,920` pistas).
- [x] **B3. Evaluación con Métricas Adecuadas**:
  - Accuracy, Precisión, Recall, F1-Score, ROC-AUC, matrices de confusión y tabla comparativa maestra (ganador: `Random Forest Audio+Género`, `F1 = 0.6132`, `ROC-AUC = 0.8628`).
- [x] **B4. Validación Cruzada (*Cross-Validation*)**:
  - `StratifiedKFold(n_splits=5)` reportando media y desvío (`F1 CV = 0.6106 ± 0.0040`, `ROC-AUC CV = 0.8597 ± 0.0014`) comparado contra Test.
- [x] **B5. Visualización e Interpretación**:
  - Matrices de confusión comparativas, curvas ROC superpuestas, árbol de decisión (`plot_tree`), *Feature Importance* y análisis de TP/FP/FN sobre canciones reales.
- [x] **B6. Conclusiones**:
  - Reflexión sobre el modelo ganador, costos de errores, límites exógenos, mejoras futuras y utilidad práctica (+ Bonus K-Means `k=4`).
- [x] **B7. Anexo Final**:
  - Links al dataset en Kaggle/Drive, informe final en Drive, repositorio GitHub, referencias técnicas y aclaraciones metodológicas.
- [ ] **Revisión y Entrega (No requiere presentación oral)**:
  - [x] Notebook organizado, bien comentado y ejecutado completo en local y en Google Colab (`47` celdas sin errores).
  - [x] Permisos configurados en la carpeta de Drive [`HERNANDEZ MATIAS H - Comisión 26240 - TPI Machine Learning`](https://drive.google.com/drive/folders/1qlKrshYD_2ZqjH_gToYyP0Jt4nvjdiUT): **lectura pública** (`anyone` reader) y **edición** para `maximiliano.torreblanca@bue.edu.ar`.
  - [ ] Entregar el enlace de la carpeta en el Campus Virtual (apartado Entrega de Proyecto Final, Clase 16) dentro del plazo.

---

## 📂 Enlaces a Espacios de Trabajo

- Cuaderno y artefactos de Preentrega: [`02_proyectos/preentrega/`](02_proyectos/preentrega/)
- Consigna, checklist y artefactos de Entrega Final: [`02_proyectos/proyecto_final/`](02_proyectos/proyecto_final/)
