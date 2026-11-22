---
title: "ML - CLASE 14"
source: "https://gamma.app/docs/ML-CLASE-14-eympxlfn344pj98?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/0c9e2716760e45b2899c0ccb77bf9cb7/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 14 | Proyecto guiado (Parte 1)

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 13

#### Comparativa y evaluación de modelos

- Comparativa y evaluación de modelos.
- Selección del mejor modelo según métricas.

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

## Objetivos de la clase

En esta clase iniciaremos el desarrollo completo de un proyecto de Machine Learning completo. El objetivo es abordar un caso real utilizando un dataset clínico auténtico, que servirá como ejemplo concreto del tipo de trabajo que luego deberán replicar los estudiantes en su **Proyecto Final Integrador**.

---

1

#### Presentación del dataset

El dataset que trabajaremos en este proyecto guiado recopila información clínica de pacientes sometidos a estudios cardiovasculares.

2

#### Selección de variables

El dataset está compuesto por 16 variables, que combinan datos numéricos, categóricos y de identificación. Determinaremos cuales son importantes para el proyecto.

3

#### División del dataset

Realizaremos la división del dataset en un conjunto de entrenamiento y otro de prueba.

## Proyecto guiado: Exploración, limpieza y preprocesamiento de datos clínicos

Comenzamos hoy este proyecto guiado, donde **desarrollaremos un modelo de Machine Learning** aplicado al ámbito clínico. A lo largo de dos clases, exploraremos un dataset real de pacientes cardiovasculares, realizando desde el análisis exploratorio hasta la implementación de un modelo predictivo.

Este proyecto servirá como ejemplo concreto del trabajo que **resume los pasos vistos en las clases anteriores y ayudará a realizar el Proyecto Final Integrador**.

Comenzaremos con la exploración, limpieza y preprocesamiento de datos, para luego avanzar hacia el entrenamiento y evaluación del modelo.

## Detalles del dataset

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/3074486af0764ab58f21750fa0e7d0e4/optimized/Doctors-bro.svg)

## Contexto clínico

#### Relevancia en salud

La predicción temprana de enfermedades cardíacas mediante aprendizaje automático puede mejorar la calidad de vida de los pacientes y optimizar recursos sanitarios.

#### Datos clínicos

El dataset recopila información de pacientes sometidos a estudios cardiovasculares, incluyendo variables como edad, sexo, tipo de dolor, presión arterial y colesterol.

#### Objetivo predictivo

Identificar la probabilidad de que un paciente presente una enfermedad cardíaca a partir de múltiples indicadores clínicos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/317e62b0ad3341e089735003c9447198/optimized/Cardiologist-bro.svg)

## Valor pedagógico

#### Problema claro y relevante

La detección de enfermedad cardíaca a partir de variables clínicas es un caso comprensible y significativo, facilitando la interpretación de resultados y su conexión con situaciones reales.

Se trata de un caso clásico de clasificación supervisada, alineado con los ejes principales trabajados en el curso.

#### Estructura equilibrada

Presenta una combinación balanceada de variables numéricas y categóricas, permitiendo aplicar diversas estrategias de preprocesamiento: imputación de valores faltantes, codificación de categorías y escalado de datos.

Esta diversidad ofrece una excelente oportunidad para revisar y consolidar procedimientos aprendidos anteriormente.

## Oportunidades didácticas

#### Valores faltantes

Permite aplicar técnicas de imputación en columnas como trestbps, chol, slope, ca y thal, evaluando su impacto en los resultados.

#### Codificación categórica

Requiere implementar estrategias como one-hot o label encoding para variables con múltiples niveles, reflexionando sobre cada enfoque.

#### Atributos mixtos

La combinación de variables numéricas y cualitativas habilita la construcción de pipelines de preprocesamiento combinados.

#### Variable objetivo adaptable

Permite enfoques de clasificación binaria o multiclase según el nivel de profundidad deseado.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1bb6c39740aa43098b6ebf0d70256cdc/optimized/Information-tab-bro.svg)

## Características técnicas

#### Valores faltantes reales

Incluye valores ausentes en varias columnas, lo que permite aplicar técnicas de imputación y discutir su impacto en el modelo final.

#### Variables categóricas multinivel

Contiene categorías con múltiples niveles, haciendo necesario implementar codificaciones adecuadas (one-hot o label encoding) y reflexionar sobre las implicancias de cada enfoque.

#### Volumen adecuado

Con 920 registros, el dataset tiene un tamaño ideal para entornos educativos: permite realizar pruebas sin tiempos excesivos y es suficientemente amplio para observar patrones y aplicar validación cruzada.

## Estructura

#### Formato Tabular

Estructura clásica para clasificación supervisada

#### Filas = pacientes

Cada fila representa un paciente distinto

#### Columnas = variables

Cada columna aporta información para la predicción

## Variables

---

## Variables numéricas

#### Edad (age)

Edad del paciente en años. Variable fundamental para el análisis de riesgo cardiovascular.

#### Presión arterial (trestbps)

Presión arterial en reposo medida en mm Hg. Indicador clave de la salud cardiovascular.

#### Colesterol (chol)

Nivel de colesterol sérico en mg/dl. Factor de riesgo importante para enfermedades cardíacas.

#### Frecuencia cardíaca (thalch)

Frecuencia cardíaca máxima alcanzada. Indicador de capacidad y respuesta cardiovascular.

## Variables categóricas

#### Sexo (sex)

Indica el sexo del paciente con valores "Male" y "Female". Factor relevante en la epidemiología cardiovascular.

#### Tipo de Dolor (cp)

Describe el tipo de dolor en el pecho, con categorías como "typical angina" o "asymptomatic".

#### Electrocardiograma (restecg)

Resultados del electrocardiograma en reposo, con múltiples categorías diagnósticas.

#### Prueba de Talio (thal)

Resume los resultados de una prueba de esfuerzo con talio, importante para la evaluación cardíaca.

## Variables booleanas y objetivo

#### Azúcar en sangre (fbs)

Indica si el azúcar en sangre en ayunas es mayor a 120 mg/dl (True/False)

#### Angina (exang)

Presencia de angina inducida por ejercicio (True/False)

#### Variable objetivo (num)

Grado de enfermedad cardíaca (0-4), que convertiremos en binaria para clasificación

![](https://cdn.gamma.app/5k42ay5jcl12uau/7518c969330e4aeb9f10158f04a5df72/optimized/Business-Plan-bro.svg)

## Variables de identificación

#### ID del paciente

Identificador único para cada paciente en el dataset

#### Origen del dato (dataset)

Procedencia original: Cleveland, Hungary, Switzerland o VA Long Beach

#### Uso en el modelo

Estas variables no serán utilizadas como predictores en el modelo

## Análisis exploratorio

---

## Pasos del análisis exploratorio

1

#### Carga del dataset

Importación y visualización inicial de los datos para comprender su estructura general y detectar problemas evidentes a primera vista.

2

#### Exploración de variables

Revisión detallada de tipos de datos, valores únicos y distribución de la variable objetivo para entender el comportamiento de cada característica.

3

#### Análisis de valores faltantes

Identificación sistemática de datos ausentes y evaluación de su impacto potencial en el modelo predictivo.

## Pasos de preprocesamiento

#### Tratamiento de valores faltantes

Aplicación de estrategias como imputación por la media o por la categoría más frecuente según el tipo de variable.

#### Codificación de variables categóricas

Transformación de categorías en formatos numéricos interpretables por algoritmos de machine learning.

#### Estandarización de variables numéricas

Normalización de escalas para evitar que variables con rangos amplios dominen el modelo.

#### División del dataset

Separación en conjuntos de entrenamiento y prueba para una evaluación objetiva del modelo.

![](https://cdn.gamma.app/5k42ay5jcl12uau/cada4b5ae81c4dd2b37df28f7aa2915f/optimized/Pipeline-maintenance-bro.svg)

## Construcción del Pipeline

1

#### Definición de transformadores

Creación de objetos para cada tipo de transformación necesaria

2

#### Agrupación por tipo

Organización de variables según el procesamiento requerido

3

#### Integración en pipeline

Combinación de todos los pasos en una estructura secuencial

## Análisis de valores faltantes

#### Visualización de datos faltantes

El mapa de calor muestra la distribución de valores ausentes en el dataset. Las columnas trestbps, chol, slope, ca y thal presentan valores faltantes que requerirán tratamiento específico.

#### Porcentaje por columna

La variable 'ca' presenta el mayor porcentaje de valores faltantes (aproximadamente 25%), seguida por 'thal' (19%). Las demás variables afectadas tienen menos del 10% de datos ausentes.

#### Estrategia de imputación

Para variables numéricas como trestbps y chol, utilizaremos imputación por la media. Para categóricas como slope, ca y thal, aplicaremos imputación por la moda (valor más frecuente).

![](https://cdn.gamma.app/5k42ay5jcl12uau/cb98660a103f4ff4bbf4271b5303d8f3/optimized/Mathematics-bro-1.svg)

## Tratamiento de valores faltantes

#### Variables numéricas

Para trestbps (presión arterial) y chol (colesterol), aplicamos imputación por la media estadística de cada columna. Esta estrategia preserva la distribución general de los datos sin introducir valores extremos.

- Media de trestbps: 131.7 mm Hg
- Media de chol: 246.5 mg/dl

#### Variables categóricas

Para slope, ca y thal, utilizamos imputación por la moda (valor más frecuente). Esta técnica es apropiada para variables categóricas donde no existe un orden natural entre los valores.

- Moda de slope: "flat"
- Moda de ca: "0"
- Moda de thal: "normal"

#### Verificación

Tras la imputación, verificamos que no queden valores faltantes en el dataset. Esta comprobación es crucial antes de avanzar con la codificación y el modelado.

## Codificación de variables categóricas

#### Variables binarias

Para variables como 'sex', 'fbs' y 'exang', aplicamos Label Encoding, transformando los valores en 0 y 1.

- sex: Female=0, Male=1
- fbs: False=0, True=1
- exang: False=0, True=1

#### Variables multinivel

Para variables como 'cp', 'restecg', 'slope' y 'thal', aplicamos One-Hot Encoding, creando columnas binarias para cada categoría.

- cp: 4 columnas nuevas
- restecg: 3 columnas nuevas
- slope: 3 columnas nuevas
- thal: 3 columnas nuevas

#### Variable objetivo

Transformamos 'num' en binaria: 0 para "sin enfermedad" y 1 para "con enfermedad" (valores originales 1-4).

Si visualizamos la distribución de las principales variables categóricas del dataset, notamos que el dolor de pecho asintomático es el más frecuente, mientras que los resultados de ECG normales predominan. La distribución por género muestra una mayor presencia de pacientes masculinos en la muestra.

## Estandarización de variables numéricas

#### ¿Por qué estandarizar?

La estandarización es crucial para algoritmos sensibles a la escala como regresión logística, SVM y k-NN. Sin este paso, variables con rangos amplios (como el colesterol) dominarían sobre variables con rangos pequeños (como oldpeak).

Además, la estandarización acelera la convergencia durante el entrenamiento y mejora la interpretabilidad de los coeficientes del modelo.

#### Método aplicado

Utilizamos StandardScaler de scikit-learn, que transforma cada variable restando la media y dividiendo por la desviación estándar. Esto resulta en variables con media 0 y desviación estándar 1.

Las variables numéricas estandarizadas son: age, trestbps, chol, thalch, oldpeak y ca (tras su codificación numérica).

## División del dataset

70%

#### Conjunto de entrenamiento

Datos utilizados para entrenar el modelo y ajustar sus parámetros

30%

#### Conjunto de prueba

Datos reservados para evaluar el rendimiento del modelo entrenado

42

#### Semilla aleatoria

Valor fijo para garantizar reproducibilidad en la división

## Pipeline

---

## Construcción del pipeline de preprocesamiento

#### Pipeline integrado

Estructura que combina todos los pasos de preprocesamiento

#### ColumnTransformer

Aplica transformaciones específicas según el tipo de variable

#### Transformadores individuales

Imputers, encoders y scalers para cada grupo de variables

![](https://cdn.gamma.app/5k42ay5jcl12uau/63ee884925834b2184a690e5b39c15a4/optimized/At-work-bro.svg)

## Beneficios del pipeline

#### Automatización

Aplica automáticamente todas las transformaciones en el orden correcto, reduciendo errores manuales y garantizando consistencia en el procesamiento.

#### Prevención de fugas de datos

Asegura que las estadísticas para la estandarización se calculen solo con datos de entrenamiento, evitando la filtración de información del conjunto de prueba.

#### Validación cruzada

Facilita la implementación de validación cruzada, aplicando el mismo preprocesamiento a cada fold de manera consistente y reproducible.

#### Reutilización

Permite guardar y reutilizar todo el flujo de preprocesamiento para nuevos datos, manteniendo la coherencia en producción.

![](https://cdn.gamma.app/5k42ay5jcl12uau/b0bfa90f24ec4df2a4aff9e26ffc3197/optimized/Data-report-bro.svg)

## Preparación para el modelado

1

#### Datos limpios

Dataset sin valores faltantes y con variables correctamente formateadas

2

#### Variables transformadas

Categorías codificadas y variables numéricas estandarizadas

3

#### Conjuntos separados

Datos divididos en entrenamiento y prueba

4

#### Pipeline construido

Estructura de preprocesamiento lista para aplicar a nuevos datos

![](https://cdn.gamma.app/5k42ay5jcl12uau/4c5f1ceafc7744b2a35bd9bcad47d975/optimized/Coding-workshop-bro.svg)

## Próximos pasos: Modelado y evaluación

1

#### Entrenamiento de modelos

Aplicaremos diversos algoritmos de clasificación como Regresión Logística, Random Forest y SVM utilizando el pipeline de preprocesamiento construido en esta etapa.

2

#### Evaluación de rendimiento

Analizaremos métricas específicas como precisión, recall y F1-score, y visualizaremos los resultados mediante matrices de confusión y curvas ROC para determinar el modelo más adecuado.

3

#### Interpretación clínica

Discutiremos las implicaciones prácticas de los resultados en el contexto médico, considerando tanto el rendimiento técnico como la aplicabilidad en entornos clínicos reales.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Valores faltantes

¿Qué impacto puede tener la forma en que tratamos los valores faltantes sobre el rendimiento y la confiabilidad de un modelo de clasificación?

2

#### Codificación de variables

¿Por qué es importante codificar correctamente las variables categóricas antes de entrenar un modelo? ¿Qué problemas podrían surgir si no lo hacemos?

3

#### Escalado

¿Cómo influye la escala de las variables numéricas en el comportamiento de algunos algoritmos de Machine Learning?

## ⚙️Ejercicios prácticos

---

## ⚙️ Preparando el modelo para una clínica

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

El equipo de **Talento Lab** fue convocado por una clínica que busca implementar un sistema de apoyo a la decisión médica. El objetivo es utilizar modelos predictivos para anticipar si un paciente podría estar en riesgo de padecer una enfermedad cardíaca, a partir de una serie de variables clínicas recolectadas en los chequeos regulares.

Tu tarea es preparar el conjunto de datos clínicos para el entrenamiento de un modelo de clasificación que prediga la presencia de enfermedad cardíaca.

## Ejercicio práctico

```
Obligatorio
```

Para eso, deberás:

---

#### Dataset

Cargar el dataset y realizar un análisis exploratorio detallado.

#### Valores faltantes

Identificar y resolver los valores faltantes presentes en distintas columnas.

#### Codificar variables

Codificar las variables categóricas según corresponda.

## Ejercicio práctico

```
Obligatorio
```

---

#### Estandarizar

Estandarizar las variables numéricas.

#### Dividir el dataset

Dividir el dataset en conjuntos de entrenamiento y prueba.

#### Pipeline

Construir un pipeline de preprocesamiento reutilizable que integre todos estos pasos.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5yq1ea3085dnxt6/8068a888885a47b69a684f5c6d17c2bd/original/advertencia.png)

## 📄¡Nuevo cuestionario en Campus!

> [!note] Note
> No olvides que los cuestionarios son de carácter obligatorio para poder avanzar con la cursada.

Gamma