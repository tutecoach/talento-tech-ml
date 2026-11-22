---
title: "ML - CLASE15"
source: "https://gamma.app/docs/ML-CLASE15-9srse731a90ujui?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/92573d6acb7041279503a6f2a107454a/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 15 | Proyecto guiado (Parte 2)

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 14

#### Proyecto guiado (Parte 1)

- Desarrollo guiado: EDA y preprocesamiento de un dataset real.
- Entrenamiento y evaluación de un modelo supervisado.
- Visualización y análisis de resultados.

Clase 15

#### Proyecto guiado (Parte 2)

- Finalización del desarrollo guiado: optimización y documentación.
- Presentación de resultados y recomendaciones.
- Guía para el Proyecto Final Integrador.

Clase 16

#### Realimentación y cierre

- Presentación de los proyectos de los estudiantes.
- Retroalimentación grupal.
- Cierre del curso.

## Objetivos de la clase

Bienvenidos a la segunda parte de nuestro proyecto guiado de Machine Learning aplicado al sector salud. Hoy completaremos el proceso iniciado anteriormente, entrenando y evaluando modelos para predecir enfermedades cardíacas.

---

1

#### Entrenar modelos

Aplicaremos algoritmos supervisados sobre datos clínicos ya preprocesados.

2

#### Evaluar rendimiento

Utilizaremos métricas específicas para analizar cada modelo.

3

#### Analizar resultados

Interpretaremos los hallazgos desde una perspectiva crítica y profesional.

## Proyecto guiado: Exploración, limpieza y preprocesamiento de datos clínicos

En esta clase completaremos el proyecto guiado iniciado en la clase anterior, aplicando modelos de Machine Learning sobre los datos clínicos ya preprocesados.

A partir del dataset limpio y transformado, **entrenaremos** distintos algoritmos supervisados, **evaluaremos** su rendimiento utilizando métricas específicas y **analizaremos los resultados** obtenidos desde una perspectiva crítica y profesional.

El objetivo es que puedas experimentar de forma práctica cómo se selecciona un modelo en función no solo de su precisión, sino también de su robustez, interpretabilidad y adecuación al contexto.

Se buscará que el análisis no quede limitado a un único número, sino que se base en la combinación de varias herramientas: **matriz de confusión**, **métricas de clasificación**, **curva ROC**, y una tabla comparativa final.

## Comparar modelos

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/57b6185378284ad9bb5dc4016fe4efd9/optimized/Analysis-bro.svg)

## Más allá de la precisión

#### Consideraciones clave

La selección de modelos no se limita a un único número. Debemos considerar múltiples factores:

- Robustez del modelo
- Interpretabilidad
- Adecuación al contexto clínico

#### Herramientas de evaluación

Utilizaremos diversas herramientas para evaluar:

- Matriz de confusión
- Métricas de clasificación
- Curva ROC
- Tabla comparativa

## Comparar modelos: Una tarea fundamental

#### Decisión informada

Elegir el modelo más adecuado para el problema

#### Análisis crítico

Evaluar rendimiento desde múltiples perspectivas

#### Experimentación

Entrenar diferentes algoritmos sobre los mismos datos

![](https://cdn.gamma.app/5k42ay5jcl12uau/72926c5cc191461f8c87d28ddb985c44/optimized/Problem-solving-bro.svg)

## Preguntas clave para la evaluación

#### Comportamiento

¿Cómo se comporta el modelo frente a casos positivos y negativos?

#### Errores

¿Qué tipo de errores comete con mayor frecuencia?

#### Estabilidad

¿Es estable su rendimiento ante cambios en los datos?

#### Comprensibilidad

¿Es comprensible su lógica de decisión, o es una "caja negra"?

## Modelos a comparar

#### Regresión Logística

Modelo lineal que estima probabilidades. Fácil de interpretar y muy utilizado en contextos clínicos.

#### Random Forest

Ensamble de árboles de decisión. Alta precisión y robustez ante datos ruidosos.

#### Árbol de Decisión (opcional)

Modelo simple y directo. Muy interpretable pero menos preciso que modelos más complejos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/7184b87ec8ff435aa7a1c3923ed792c9/optimized/Doctors-bro.svg)

## Regresión Logística: Características

#### Modelo lineal

Estima la probabilidad de pertenecer a una clase mediante una función logística.

#### Interpretabilidad

Permite observar la influencia relativa de cada variable en la predicción.

#### Eficiencia

Rápido de entrenar y con bajo costo computacional.

#### Uso clínico

Ampliamente utilizado en medicina por su transparencia y simplicidad.

![](https://cdn.gamma.app/5k42ay5jcl12uau/98d481ff910b4db9bd2e693fc7e4991d/optimized/cherry-tree-bro.svg)

## Random Forest: Características

#### Múltiples árboles

Construye varios árboles de decisión sobre subconjuntos aleatorios del dataset.

#### Aleatoriedad

Utiliza muestreo aleatorio de datos y variables para crear diversidad.

#### Votación

Promedia los resultados de todos los árboles para obtener la predicción final.

#### Robustez

Maneja bien datos ruidosos, valores atípicos y variables correlacionadas.

![](https://cdn.gamma.app/5k42ay5jcl12uau/2e79ea22d54c407a83263478d0b77e74/optimized/Collaboration-bro.svg)

## Pasos del proceso de modelado

#### Definición de variables

Identificar predictores y variable objetivo en los datos preprocesados.

#### División del dataset

Separar en conjuntos de entrenamiento y prueba para evaluación objetiva.

#### Entrenamiento de modelos

Aplicar al menos dos algoritmos supervisados utilizando el pipeline definido.

#### Evaluación y comparación

Analizar métricas, visualizaciones y construir tabla comparativa.

## Métricas de evaluación

#### Exactitud (Accuracy)

Proporción de predicciones correctas sobre el total. Aunque intuitiva, puede ser engañosa en datasets desbalanceados donde una clase predomina significativamente.

#### Precisión (Precision)

Mide la proporción de casos positivos identificados correctamente entre todos los casos clasificados como positivos.

#### Sensibilidad (Recall)

Indica qué proporción de casos realmente positivos fueron identificados correctamente.

#### F1-Score

Media armónica entre precisión y recall. Proporciona un balance entre ambas métricas, especialmente útil en situaciones con datasets desbalanceados.

#### Matriz de confusión

Visualización tabular que muestra verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos, permitiendo un análisis detallado de los errores del modelo.

#### Curva ROC y AUC

La curva ROC muestra la relación entre la tasa de verdaderos positivos y falsos positivos. El área bajo esta curva (AUC) cuantifica la capacidad del modelo para distinguir entre clases.

## Interpretación de métricas

#### Accuracy

Proporción de predicciones correctas sobre el total.

#### Precision

De los casos que predije positivos, ¿cuántos realmente lo son?

#### Recall

De todos los casos realmente positivos, ¿cuántos logré identificar?

#### F1-Score

Media armónica entre precision y recall.

## Selección del modelo

---

## Criterios de selección del modelo

#### Rendimiento

Métricas cuantitativas como accuracy, precision, recall y F1-score.

#### Interpretabilidad

Capacidad de explicar las decisiones del modelo al equipo médico.

#### Robustez

Estabilidad ante variaciones en los datos de entrada.

#### Aplicabilidad

Adecuación al contexto clínico y facilidad de implementación.

![](https://cdn.gamma.app/5k42ay5jcl12uau/72d728d9a09d4aacaded798e76601b3b/optimized/Consulting-bro.svg)

## Ventajas de la regresión logística

#### Alta interpretabilidad

Los coeficientes indican la influencia de cada variable en la predicción.

#### Eficiencia computacional

Requiere menos recursos y tiempo de entrenamiento.

#### Probabilidades calibradas

Ofrece estimaciones de probabilidad bien calibradas.

#### Aceptación médica

Ampliamente utilizado y aceptado en la literatura médica.

![](https://cdn.gamma.app/5k42ay5jcl12uau/d811e473fbe348c89c81d067b0e6daa3/optimized/Bigfoot-bro.svg)

## Ventajas de Random Forest

#### Mayor precisión

Suele superar a modelos más simples en términos de rendimiento.

#### Robustez

Menos susceptible al sobreajuste y a datos ruidosos.

#### Captura relaciones complejas

Puede modelar interacciones no lineales entre variables.

#### Importancia de variables

Proporciona medidas de la relevancia de cada predictor.

## Limitaciones

#### Regresión logística

- Asume relaciones lineales entre variables
- Sensible a valores atípicos
- Puede tener problemas con variables correlacionadas
- Limitada capacidad para capturar interacciones complejas

#### Random Forest

- Menor interpretabilidad ("caja negra")
- Mayor costo computacional
- Requiere más hiperparámetros para ajustar
- Puede ser difícil de explicar a personal no técnico

## Consideraciones para el contexto clínico

#### Interpretabilidad

Los médicos necesitan entender por qué el modelo toma ciertas decisiones.

#### Impacto clínico

Valorar las consecuencias de falsos positivos y negativos.

#### Confiabilidad

El modelo debe ser estable y consistente en sus predicciones.

3

#### Integración

Facilidad para incorporar el modelo en los sistemas hospitalarios existentes.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Criterios de decisión

¿Qué factores, además de los números, consideramos para elegir el modelo más adecuado?

2

#### Tipos de error

¿Qué es más grave en este contexto: falsos positivos o falsos negativos?

3

#### Comunicación

¿Qué modelos son más fáciles de explicar a un equipo no técnico?

4

#### Implementación real

¿Cómo influyen factores como tiempo de respuesta en la elección del modelo?

## ⚙️Ejercicios prácticos

---

## ⚙️ Comparar para decidir

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

Después de una semana de intenso trabajo con el nuevo cliente del sector salud, el equipo de **Talento Lab** dejó listo un pipeline de preprocesamiento completamente funcional. Los datos ya están limpios, transformados y preparados para entrenar modelos que puedan predecir la presencia de enfermedad cardíaca a partir de información clínica.

Silvia fue clara: “*Ahora que tenemos los datos bien preparados, necesitamos evaluar diferentes modelos y quedarnos con el que mejor se adapte a este caso*”.

## Ejercicio práctico

```
Obligatorio
```

Tu rol en esta etapa es aplicar ambos modelos, compararlos en base a sus métricas y visualizaciones, y ayudar al equipo a elegir con evidencia cuál es más conveniente para esta situación clínica. Para eso, deberás:

---

#### Dividir el dataset

Dividir el dataset en conjuntos de entrenamiento y prueba.

#### Valores faltantes

Entrenar los modelos seleccionados utilizando el pipeline definido anteriormente.

#### Evaluar

Evaluar el rendimiento de cada modelo utilizando: Matriz de confusión Accuracy, precision, recall, F1-score Curva ROC

## Ejercicio práctico

```
Obligatorio
```

---

#### Tabular

Construir una tabla comparativa de métricas clave.

#### Reflexionar

Redactar una reflexión técnica sobre cuál modelo es más adecuado y por qué.

#### (Opcional)

Guardar el pipeline + modelo elegido para reutilizarlo en producción.

## 📂Proyecto final integrador

---

## Consigna

---

```
Obligatorio
```

### Contexto y objetivo

A lo largo de este curso, exploramos de manera progresiva y aplicada las distintas etapas que forman parte del desarrollo de un modelo de **aprendizaje automático**. Desde la exploración y preparación de los datos hasta la implementación y evaluación de modelos, cada clase sentó las bases para comprender cómo transformar un conjunto de datos en una herramienta útil para la toma de decisiones.

El **Proyecto Integrador** tiene como objetivo poner en práctica todo lo aprendido. A través de este trabajo, cada estudiante desarrollará su propio proyecto de **Machine Learning**, aplicando cada una de las etapas del proceso, desde la limpieza y codificación de los datos hasta la validación y análisis del rendimiento del modelo final.

## Consigna

---

```
Obligatorio
```

### Entrega final

La **entrega final** debe continuar el trabajo iniciado en la **Pre-Entrega**. Se espera que el estudiante retome ese notebook y complete las siguientes etapas:

**Actividades:**

**1- Elección del modelo** o modelos a utilizar (al menos uno). Justificación según el tipo de problema (clasificación o regresión).

**2- Entrenamiento del modelo** con el conjunto de entrenamiento.

**3- Evaluación con métricas adecuadas**, según el tipo de modelo (ej.: MAE, RMSE, R², precisión, recall, F1-score, matriz de confusión).

**4- Aplicación de validación cruzada (cross-validation)** para estimar el rendimiento del modelo de manera más robusta.

## Consigna

---

```
Obligatorio
```

### Entrega final

**5 - Visualización de resultados** e interpretación de errores o aciertos del modelo.

**6 - Conclusiones**: reflexión sobre el modelo entrenado, posibilidades de mejora, y utilidad práctica del proyecto.

**7 - Anexo final:** incluir el link al dataset utilizado, referencias si se usaron fuentes externas, y aclaraciones que se consideren necesarias.

Se espera que el notebook esté organizado, bien comentado, y que el código esté acompañado de explicaciones claras y observaciones propias. No se requiere presentación oral.

## 📄Pautas de entrega y evaluación:

```
Plazo de entrega: 7 días (clase 16)
```

```
Formato: Una carpeta en Google Drive a la que se nombrará respetando el siguiente formato: Apellido y nombre del alumno - Comisión xxx - TPI Machine Learning que contenga, como mínimo:
```

---

- Los **sets de datos originales**.
- Un **archivo de Google Colaboratory**: contendrá diferentes bloques de texto y código, siguiendo los pasos y pautas enumerados en la consigna.
- Incluir al final un bloque de texto llamado “Anexo” con descripción y links a todos los archivos adicionales que haya incluido en la carpeta.

## Pautas de entrega y evaluación:

---

Todos los archivos deben estar con permisos de lectura públicos, y de edición para el instructor responsable de evaluar.

Se debe priorizar el uso de Google Colaboratory para todas las actividades.

**Entrega:** La entrega se realiza **en el campus virtual,** compartiendo el link a **la carpeta de Google Drive**, dentro de la clase 16 en el apartado de Entrega de Proyecto Final. A fines de agilizar la corrección de trabajos, el instructor o tutor podrían solicitar una modalidad accesoria. **Se trabajará sobre el mismo archivo de la etapa de preentrega, respetando las mismas pautas**.

**Evaluación:** Los criterios de evaluación están especificados en la siguiente: Rúbrica de Evaluación - Preentrega Data Analytics

Gamma