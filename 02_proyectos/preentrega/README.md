# 📋 Preentrega del Proyecto Integrador — Machine Learning (Comisión #26240)

Este directorio contiene todo el material correspondiente a la **Preentrega Oficial**, estructurado y validado conforme a la consigna y la rúbrica docente.

---

## 📂 Archivos y Entregables del Proyecto:

1. **[`Pre_entrega26.ipynb`](Pre_entrega26.ipynb)**:
   - Cuaderno Jupyter oficial de la Preentrega (formato Google Colab).
   - Enlace directo a Google Colab: [Abrir en Google Colab](https://colab.research.google.com/drive/1Zff5mrXXnKZtKsUyN2mEs869GO3ItfZX)
   - Contiene 24 celdas organizadas secuencialmente:
     * Portada institucional y ficha técnica.
     * **Sección 1:** Selección y justificación del dataset (Spotify Tracks) + Diccionario de variables.
     * **Sección 2:** Análisis Exploratorio de Datos (EDA) en profundidad (distribuciones, correlaciones con máscara triangular, subplots y boxplots de comparación).
     * **Sección 3:** Limpieza rigurosa de datos (desduplicación por `track_id`, eliminación de nulos, tratamiento de inconsistencias de duración).
     * **Sección 4:** Transformaciones básicas y Feature Engineering (definición del target `is_hit`, binarización de `explicit`, descarte fundamentado de identificadores y justificación sobre `track_genre`).
     * **Sección 5:** Selección de variables, partición estratificada Train/Test (80/20) y escalado metodológico sin fuga de información (*Data Leakage*).
     * **Sección 6:** Conclusiones formales y hoja de ruta para la experimentación multimodelo en la Entrega Final (KNN, Regresión Logística, Árboles, Random Forest).

2. **[`informe_preentrega.md`](informe_preentrega.md)**:
   - Resumen ejecutivo formal y memoria técnica con la síntesis de hallazgos del EDA, justificación de decisiones metodológicas y hoja de ruta para el modelado.
   - Sincronizado en Google Drive: [Ver en Drive](https://drive.google.com/file/d/1tcMhIpNUQkEyH5HMjPLhBmPFIPT-Nt30/view?usp=drivesdk)

3. **[`ML_Consigna_Pre-entrega.md`](ML_Consigna_Pre-entrega.md)**:
   - Consigna original del curso y rúbrica de evaluación provista por la cátedra.
