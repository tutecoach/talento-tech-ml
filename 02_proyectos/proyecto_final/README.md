# 🏆 Entrega Final del Proyecto Integrador

Este directorio centraliza las consignas oficiales, el checklist de control, el material de referencia y la preparación de la **Entrega Final** del Proyecto Integrador de Machine Learning (Comisión #26240).

---

## 📂 Artefactos en este directorio

| Archivo | Descripción |
| :--- | :--- |
| [`ML_Consigna_Entrega_Final.md`](ML_Consigna_Entrega_Final.md) | Consigna oficial de la Entrega Final (etapas obligatorias, formato y criterios de entrega). |
| [`CHECKLIST_ENTREGA_FINAL.md`](CHECKLIST_ENTREGA_FINAL.md) | Checklist interactivo transcrito de `ML - Checklist Entrega Final.docx` (Partes A, B y revisión final). |
| [`ML - Checklist Entrega Final.docx`](ML%20-%20Checklist%20Entrega%20Final.docx) | Documento oficial original de verificación previa a la entrega. |
| [`ML_Referencia_Docente_Pre_entrega26.ipynb`](ML_Referencia_Docente_Pre_entrega26.ipynb) | Notebook de referencia docente actualizado al 21/11/2026 (modelos supervisados, `GridSearchCV` y `K-Means`). *Solo referencia; no reemplaza la preentrega propia.* |

---

## 📌 Pautas Oficiales de la Entrega Final

- **Continuidad obligatoria sobre la Pre-Entrega:** Se trabaja **continuando el mismo notebook en Google Colab** utilizado en la Pre-Entrega ([`../preentrega/Pre_entrega26.ipynb`](../preentrega/Pre_entrega26.ipynb)), **no en un notebook nuevo**, verificando su ejecución completa de principio a fin e incorporando feedback si lo hubo.
- **Requisito previo:** Completar el **cuestionario de autoevaluación del Campus Virtual** (obligatorio).
- **Alcance técnico (Bloques B1–B7):**
  1. **B1. Elección del modelo:** Al menos un modelo justificado según el tipo de problema (opcional: segundo modelo para comparar).
  2. **B2. Entrenamiento:** Entrenamiento sobre `train` y generación de predicciones sobre `test`.
  3. **B3. Evaluación:** Métricas acordes al problema (clasificación: *accuracy*, *precision*, *recall*, *F1-score*, matriz de confusión; regresión: *MAE*, *RMSE*, *R²*) y tabla comparativa si hay múltiples modelos.
  4. **B4. Validación cruzada:** Aplicación de *cross-validation* (ej. 5 folds), reportando media, desvío y comparación contra test.
  5. **B5. Visualización e interpretación:** Gráficos de resultados, importancia de variables (cuando aplique) y análisis de aciertos/errores y sus causas.
  6. **B6. Conclusiones:** Reflexión, límites del modelo, posibilidades de mejora y utilidad práctica.
  7. **B7. Anexo final:** Link al dataset original, referencias externas y aclaraciones / links a archivos adicionales en la carpeta.
- **Modalidad y formato de entrega:**
  - **No requiere presentación oral**: todo el análisis queda documentado en el notebook.
  - **Plazo:** 7 días (Clase 16).
  - **Carpeta en Google Drive:** Nombrada como `HERNANDEZ MATIAS H - Comisión 26240 - TPI Machine Learning`, incluyendo los **sets de datos originales** y el **notebook de Google Colaboratory**, con **permisos de lectura públicos** y **edición para el instructor responsable**.
  - **Envío:** Compartir el enlace de la carpeta de Google Drive en el **Campus Virtual** (apartado de Entrega de Proyecto Final, Clase 16).
