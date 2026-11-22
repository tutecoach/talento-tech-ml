# 📄 Informe Técnico y Ejecutivo — Entrega Final de Machine Learning

**Programa:** Talento Tech — Especialización en Machine Learning (Nivel Avanzado)  
**Comisión:** #26240  
**Docente:** Maximiliano Torreblanca | **Tutora:** Agustina Digiesi  
**Estudiante:** Matías Hernández  
**Fecha:** Noviembre 2026  
**Cuaderno Continuado:** [`Pre_entrega26.ipynb`](Pre_entrega26.ipynb)  
**Carpeta de Entrega en Google Drive:** [HERNANDEZ MATIAS H - Comisión 26240 - TPI Machine Learning](https://drive.google.com/drive/folders/1qlKrshYD_2ZqjH_gToYyP0Jt4nvjdiUT)

---

## 1. Resumen Ejecutivo

Este documento consolida la **Entrega Final** del Proyecto Integrador, dando continuidad directa al trabajo de Pre-Entrega sobre el [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) (**114.000** pistas iniciales, **89.598** pistas únicas depuradas).

El problema consiste en una **clasificación binaria moderadamente desbalanceada** (`is_hit = 1` cuando `popularity > 50`, representando el **22,25%** de las pistas depuradas frente al **77,75%** de `No Hit`). A lo largo de la segunda etapa se implementaron y compararon **7 configuraciones supervisadas** (desde un modelo *Baseline* ingenuo hasta pipelines optimizados con `ColumnTransformer` + `GridSearchCV`), validadas con **Stratified K-Fold (5 folds)** y complementadas con **análisis de errores** y **segmentación no supervisada con K-Means**.

### Hallazgo Principal
Utilizando únicamente los **14 atributos acústicos/musicales** (*Solo Audio*), el mejor modelo (**Random Forest optimizado**) alcanzó **`F1 = 0.4470`** y **`ROC-AUC = 0.7049`** en Test. Al incorporar el contexto de género musical (`track_genre`, 113 categorías) mediante `ColumnTransformer` + `OneHotEncoder(handle_unknown='ignore')` sin fuga de datos, **Random Forest (Audio + Género)** escaló a **`F1 = 0.6132`** (+37,2% relativo), **`ROC-AUC = 0.8628`** y **`Accuracy = 0.8094`**, superando claramente al Baseline (`Accuracy = 0.7775`, `F1 = 0.0000`).

---

## 2. Revisión Metodológica Heredada (Parte A) y Corrección Crítica

Sobre la base de la Pre-Entrega (`71.678` registros en `Train` y `17.920` en `Test`, partición estratificada 80/20):
1. **Depuración verificada:** Se eliminaron `24.259` duplicados lógicos por `track_id`, `3` filas con nulos marginales y `142` registros con duración anómala (`< 10 s` o `> 15 min`), reteniendo el **78,59%** (`89.598` canciones únicas) con **0 nulos** y **0 duplicados**.
2. **Corrección preventiva (*Index Leakage*):** En la celda `4.1` se agregó explícitamente el descarte de la columna `'Unnamed: 0'` (ausente en el descarte original), dado que el CSV está ordenado secuencialmente por género y conservar ese índice correlativo habría filtrado el género a los árboles de decisión.
3. **Cero fuga de información:** Todos los escaladores (`StandardScaler`, `MinMaxScaler`) y codificadores (`OneHotEncoder`) se encapsularon en objetos `Pipeline` y `ColumnTransformer` ajustados estrictamente dentro de `Train` y dentro de cada fold de validación cruzada.

---

## 3. Experimentación Multimodelo y Validación Cruzada (Parte B)

### 3.1 Modelos Base — Solo Audio (14 variables)
| Modelo | Accuracy Train | Accuracy Test | Precision (Hit) | Recall (Hit) | F1-Score (Hit) | ROC-AUC Test | F1 CV (5-Fold) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `0. Baseline (Dummy Most Frequent)` | 0.7774 | 0.7775 | 0.0000 | 0.0000 | 0.0000 | 0.5000 | — |
| `1. Regresión Logística (Base)` | 0.7768 | 0.7774 | 0.4902 | 0.0063 | 0.0124 | 0.6340 | 0.0084 ± 0.0018 |
| `2. KNN k=5 (Base)` | 0.8184 | 0.7483 | 0.3831 | 0.2144 | 0.2749 | 0.6319 | 0.2581 ± 0.0048 |
| `3. Árbol de Decisión (Base)` | 0.9940 | 0.6947 | 0.3246 | 0.3440 | 0.3340 | 0.5678 | 0.3205 ± 0.0109 |
| `4. Random Forest (Base)` | 0.9938 | 0.7843 | 0.5819 | 0.1096 | 0.1844 | 0.7057 | 0.1604 ± 0.0072 |

**Diagnóstico de la etapa base:**
- El desbalance de clases (22,25% Hits) provoca que los modelos lineales/ensambles sin ponderación predigan muy pocos positivos (*Recall* de `0.0063` en LogReg Base y `0.1096` en RF Base).
- El **Árbol de Decisión Base** sin poda sufre un **sobreajuste severo** (`0.9940` en Train vs. `0.6947` en Test, `ROC-AUC = 0.5678`).

### 3.2 Optimización con `GridSearchCV` y Experimento Controlado (*Solo Audio vs. Audio + Género*)

| Modelo Optimizado | Hiperparámetros Ganadores | F1 CV (5-Fold) | ROC-AUC CV (5-Fold) | Accuracy Train | Accuracy Test | Precision (Hit) | Recall (Hit) | F1-Score (Hit) | ROC-AUC Test |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `0. Baseline (Dummy)` | `most_frequent` | 0.0000 ± 0.0000 | 0.5000 ± 0.0000 | 0.7774 | 0.7775 | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| `1b. Regresión Logística (Audio)` | `C=1.0, class_weight='balanced'` | 0.3927 ± 0.0051 | 0.6280 ± 0.0045 | 0.5678 | 0.5731 | 0.2895 | 0.6314 | 0.3970 | 0.6336 |
| `2b. KNN (Audio)` | `n_neighbors=5, weights='distance'` | 0.2819 ± 0.0077 | 0.6347 ± 0.0050 | 0.9940 | 0.7527 | 0.4059 | 0.2400 | 0.3016 | 0.6421 |
| `3b. Árbol de Decisión (Audio)` | `max_depth=12, min_samples_split=20, balanced` | 0.4120 ± 0.0029 | 0.6414 ± 0.0021 | 0.6089 | 0.5591 | 0.2946 | 0.7034 | 0.4152 | 0.6436 |
| `4b. Random Forest (Audio)` | `max_depth=15, min_samples_leaf=5, balanced` | 0.4441 ± 0.0025 | 0.7005 ± 0.0028 | 0.7329 | 0.6333 | 0.3364 | 0.6660 | 0.4470 | 0.7049 |
| `5. Regresión Logística (Audio+Género)` | `C=0.5, class_weight='balanced'` | 0.5642 ± 0.0060 | 0.8316 ± 0.0042 | 0.7275 | 0.7230 | 0.4337 | **0.7999** | 0.5625 | 0.8324 |
| **`6. Random Forest (Audio+Género)`** | **`max_depth=None, min_samples_leaf=2, balanced`** | **0.6106 ± 0.0040** | **0.8597 ± 0.0014** | **0.9532** | **0.8094** | **0.5590** | **0.6790** | **0.6132** | **0.8628** |

### Conclusiones de la Comparativa
1. **Estabilidad confirmada:** En todos los modelos optimizados, el desvío estándar de la validación cruzada de 5 folds es mínimo (`≤ 0.0077` en F1 y `≤ 0.0050` en ROC-AUC), y las métricas en Test coinciden estrechamente con la media de CV (`F1 CV = 0.6106` vs. `F1 Test = 0.6132` en el ganador).
2. **Impacto de `class_weight='balanced'` y poda:** La Regresión Logística saltó de `F1 = 0.0124` a `0.3970` en Solo Audio; la poda (`max_depth=12`) eliminó el sobreajuste del Árbol de Decisión elevando su `ROC-AUC` de `0.5678` a `0.6436`.
3. **Valor del Feature Engineering con `ColumnTransformer`:** Incorporar `track_genre` aportó **+0.1662 puntos de F1** y **+0.1579 puntos de ROC-AUC** sobre la mejor alternativa puramente acústica, demostrando que el éxito comercial en Spotify surge de la interacción entre perfil sonoro y nicho/género de audiencia.

---

## 4. Interpretabilidad y Análisis de Errores (Modelo Ganador)

Sobre las **17.920** canciones del conjunto de prueba, **Random Forest (Opt - Audio+Género)** obtuvo:
- **Verdaderos Negativos (TN):** `11.796` (`65.83%`)
- **Verdaderos Positivos (TP):** `2.708` (`15.11%`)
- **Falsos Positivos (FP):** `2.136` (`11.92%`)
- **Falsos Negativos (FN):** `1.280` (`7.14%`)

### Variables Más Influyentes
- En **Solo Audio**, las cinco variables con mayor importancia de Gini fueron `duration_ms` (`0.1138`), `acousticness` (`0.1017`), `liveness` (`0.1005`), `valence` (`0.1001`) y `energy` (`0.0949`).
- En **Audio + Género**, la importancia individual se mantiene liderada por las variables continuas (`duration_ms` `0.0626`, `liveness` `0.0582`, `acousticness` `0.0570`, `loudness` `0.0558`, `energy` `0.0556`), mientras que las 113 variables dummy de `track_genre` distribuyen el resto de la ganancia informativa y explican el salto de `0.7049` a `0.8628` en ROC-AUC.

### Causas Reales de Aciertos y Errores
- **Aciertos de alta confianza (TP):** Canciones en nichos altamente concentrados de hits como `k-pop` (*TAEIL — Starlight*, prob `0.9986`; *TWICE — SCIENTIST*, prob `0.9984`) y `pop-film` (*Nadaan Parinde*, *Guzarish*), donde la combinación de género y producción acústica es consistente.
- **Falsos Positivos (FP):** Temas que suenan y pertenecen al mismo género que un hit (*Audioslave — Shadow on the Sun* en `grunge`, prob `0.9690`; *Armin van Buuren — No Fun* en `progressive-house`, prob `0.9669` pero con `popularity = 0` por indexación/reedición en Spotify). Tienen la "receta sonora", pero carecieron de tracción o sufrieron artefactos del catálogo.
- **Falsos Negativos (FN):** Mega-éxitos impulsados por **factores exógenos no presentes en la tabla** (fama previa del artista, presupuesto de marketing, colaboraciones virales o tendencias en redes), como *Bad Bunny — Moscow Mule* (`latin`, `popularity = 94`, `prob_hit = 0.4917`, al borde exacto del umbral `0.50`), *Charlie Puth & Jung Kook (BTS) — Left and Right* (`dance`, `popularity = 92`, `prob_hit = 0.3834`) y *Shakira & Rauw Alejandro — Te Felicito* (`latin`, `popularity = 90`, `prob_hit = 0.2405`).
- **Géneros con mayor tasa de error:** Subgéneros heterogéneos donde conviven catálogo independiente y hits masivos bajo acústica similar, como `mandopop` (`50.54%` accuracy), `synth-pop` (`51.74%`), `indian` (`52.60%`) y `metalcore` (`54.30%`).

---

## 5. Bonus: Segmentación Acústica No Supervisada (`K-Means`)

Evaluando `k` de 2 a 8 sobre las 9 métricas continuas de audio en `X_train` escaladas con `MinMaxScaler`:
- El **Índice de Silhouette** (muestra de 5.000 pistas) alcanzó su máximo global en **`k = 4`** (**`0.3175`**, inercia **`15.874,22`**), coincidiendo con el codo pronunciado de la curva.

| Cluster | Canciones | Tasa de Hits (%) | Perfil Acústico Dominante (Escala 0–1) | Bautismo Comercial (Playlist) |
| :---: | :---: | :---: | :--- | :--- |
| **0** | 8.743 | **11.99%** | Alta `energy` (0.768), alta `instrumentalness` (0.764), baja `acousticness` (0.072) | **⚡ Electrónica & Rock Instrumental Intenso** |
| **1** | 37.873 | **25.61%** | Máxima `danceability` (0.605), `loudness` (0.805), `valence` (0.543), mínima `instrumentalness` (0.019) | **🔥 Mainstream Pop, Dance & Urbano Comercial** |
| **2** | 5.519 | **19.84%** | Máxima `acousticness` (0.867) e `instrumentalness` (0.846), mínima `energy` (0.211) y `tempo` (0.435) | **🎹 Focus Profundo, Clásica & Ambient** |
| **3** | 19.543 | **21.03%** | Alta `acousticness` (0.702), vocal (`instrumentalness` 0.017), `energy` moderada (0.438) | **☕ Acústico Vocal, Indie & Baladas Chill** |

La segmentación confirma de forma no supervisada que el **Cluster 1** (*Mainstream Pop, Dance & Urbano Comercial*) reúne simultáneamente el mayor volumen del catálogo (`37.873` pistas) y la mayor densidad de éxitos comerciales (**`25.61%` de Hits**), más del doble que el Cluster 0 puramente instrumental energético (`11.99%`).

---

## 6. Conclusiones de Negocio, Límites y Mejoras Futuras

1. **Utilidad Práctica:** El pipeline ganador (`Random Forest Audio+Género`, `ROC-AUC = 0.8628`) es directamente útil como herramienta de **pre-filtrado y curaduría** para playlists editoriales y equipos de *A&R* en sellos discográficos, reduciendo significativamente la búsqueda manual entre miles de lanzamientos diarios.
2. **Costo de los Errores:** En curaduría editorial o descubrimiento de talento, un **Falso Negativo** (`1.280` casos, p. ej. *Bad Bunny — Moscow Mule* en `0.4917`) representa perder un potencial éxito; ajustar el umbral de clasificación desde `0.50` a `0.40` sobre `predict_proba` permitiría capturar aún más hits a costa de un moderado aumento de Falsos Positivos (*Recall* aún mayor, estrategia cubierta por la Regresión Logística Audio+Género con `Recall = 0.7999`).
3. **Límites del Modelo:** Los atributos psicoacústicos por sí solos explican hasta `ROC-AUC ≈ 0.70`, y con género llegan a `0.8628`. El techo restante obedece a variables exógenas ausentes: reputación/seguidores previos del artista, inversión en marketing, presencia en redes sociales (TikTok/Reels) y momento de lanzamiento.
4. **Líneas de Mejora Futura:** Incorporar algoritmos de *Gradient Boosting* (`LightGBM` / `XGBoost`), enriquecer el dataset con métricas históricas de popularidad del artista (cuidando no filtrar la pista objetivo), realizar *threshold tuning* orientado a negocio y evaluar la estabilidad temporal sobre lanzamientos de años posteriores.
