---
title: "ML - CLASE 08"
source: "https://gamma.app/docs/ML-CLASE-08-ur8s98xiup99sy4?mode=doc"
author:
published:
created: 2026-10-03
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/a57d63ffa3024c998d4bef1e87b829f7/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 08 | K-Nearest Neighbors

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 07

#### Regresión logística

- Regresión Logística para clasificación.
- Métricas de clasificación: precisión, recall, F1-score.
- Matriz de confusión e interpretación de resultados.

Clase 08

#### K-Nearest Neighbors

- Algoritmo K-Nearest Neighbors (KNN).
- Selección de "k" óptimo.
- Implementación práctica en clasificación.
- Consigna de la Pre-entrega.

Clase 09

#### Árboles de Decisión

- Árboles de Decisión: estructura y poda.
- Implementación y visualización del árbol.
- Overfitting en árboles

## Objetivos de la clase

Exploraremos un nuevo enfoque para resolver problemas de clasificación binaria: el algoritmo de los **K vecinos más cercanos (KNN)**. A diferencia de los modelos vistos anteriormente, KNN no busca ajustar una fórmula ni estimar una probabilidad, sino que toma sus decisiones **observando directamente los datos más próximos al caso a clasificar**.

---

1

#### Comprender el funcionamiento de KNN

Entender cómo este algoritmo utiliza la proximidad para clasificar.

2

#### Analizar el concepto de distancia

Explorar cómo las medidas de distancia influyen en las predicciones.

3

#### Evaluar el rendimiento

Comparar KNN con otros modelos como la regresión logística.

## K-Nearest Neighbors

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/ae0b7adc62074529a75de849e43e5ef9/optimized/Analyze-bro.svg)

## ¿Qué es K-Nearest Neighbors?

KNN es un algoritmo de aprendizaje supervisado que clasifica nuevos casos según la mayoría de clases entre sus vecinos más cercanos.

A diferencia de otros modelos, KNN no busca ajustar una fórmula ni estimar probabilidades.

## Funcionamiento básico

#### Almacenar datos

El modelo guarda todos los ejemplos del conjunto de entrenamiento.

#### Calcular distancias

Para cada nuevo caso, mide la distancia a todos los puntos conocidos.

#### Seleccionar vecinos

Identifica los k puntos más cercanos al nuevo caso.

#### Votar por mayoría

Asigna la clase más frecuente entre los k vecinos seleccionados.

## La Importancia de la distancia

#### Distancia Euclidiana

La más común. Mide la separación "en línea recta" entre dos puntos en el espacio de variables.

#### Distancia de Manhattan

Suma de las diferencias absolutas. Como moverse en una cuadrícula urbana.

#### Distancia de Minkowski

Generalización que incluye a las anteriores como casos particulares.

## Selección del Valor de k

#### k bajo (1-3)

Mayor sensibilidad al ruido. Riesgo de sobreajuste.

#### k medio (5-10)

Balance entre precisión y generalización.

#### k alto (15+)

Mayor estabilidad. Posible subajuste y pérdida de patrones locales.

#### Validación

Probar diferentes valores y evaluar rendimiento.

![](https://cdn.gamma.app/5k42ay5jcl12uau/ac5f967d87ae48adb153fbec8aaea435/optimized/Mathematics-bro.svg)

## Efecto del valor de k

El valor de k influye directamente en la forma de la frontera de decisión. Valores pequeños crean fronteras más detalladas pero irregulares.

![](https://cdn.gamma.app/5k42ay5jcl12uau/6939717241594326b1e59f59d1dfb01a/optimized/Visual-data-bro.svg)

## La necesidad de escalar variables

#### Problema

Variables con diferentes escalas pueden dominar el cálculo de distancias. Por ejemplo, la edad (1-100) vs. tarifa (1-500).

#### Solución

Normalizar (MinMaxScaler) o estandarizar (StandardScaler) todas las variables antes de aplicar KNN.

## Métodos de escalado

#### Normalización

Transforma valores al rango \[0,1\]

#### Estandarización

Transforma a media 0 y desviación estándar 1

#### Escalado robusto

Menos sensible a valores atípicos

## Ventajas de KNN

#### Simplicidad

Fácil de entender e implementar. No requiere entrenamiento en sentido clásico.

#### Flexibilidad

Se adapta bien a relaciones no lineales entre variables.

#### Datasets pequeños

Funciona bien cuando no hay muchos datos disponibles.

## Limitaciones de KNN

#### Computacionalmente costoso

Lento en predicción con datasets grandes. Requiere calcular todas las distancias.

#### Sensible al ruido

Valores atípicos pueden afectar significativamente las predicciones.

#### Maldición de la dimensionalidad

Pierde efectividad con muchas variables (dimensiones).

A medida que aumenta el número de dimensiones, el concepto de "cercanía" pierde significado. Los puntos tienden a estar equidistantes entre sí.

## Cuándo usar KNN

1

#### Casos ideales

Datasets pequeños o medianos con pocas dimensiones

2

#### Casos aceptables

Problemas donde la interpretabilidad no es crítica

3

#### Casos a evitar

Datasets muy grandes o con muchas dimensiones

## Aplicaciones prácticas

#### Sistemas de recomendación

Sugerir productos similares a los que el usuario ha mostrado interés.

#### Diagnóstico médico

Comparar casos con pacientes similares para apoyar decisiones clínicas.

#### Análisis crediticio

Evaluar riesgos comparando con perfiles financieros similares.

## Optimización de KNN

#### Selección de características

Eliminar variables irrelevantes para reducir dimensionalidad y mejorar rendimiento.

#### Ponderación por distancia

Dar más peso a vecinos más cercanos que a los más lejanos.

#### Estructuras de datos eficientes

Usar KD-Trees o Ball Trees para acelerar la búsqueda de vecinos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### KN vs. regresión logística

¿En qué se diferencia el razonamiento que hace KNN del que realiza un modelo como la regresión logística?

2

#### Valor de k

¿Qué consecuencias podría tener elegir un valor de k demasiado bajo o demasiado alto en un problema real?

3

#### Escalar variables

¿Por qué es tan importante escalar las variables antes de aplicar KNN? ¿Qué podría pasar si no lo hacemos?

## 📂Pre-entrega de proyecto

---

## ⚙️Revisión de progreso

```
Obligatorio
```

---

### Proyecto integrador

Tiene como objetivo poner en práctica todo lo aprendido. A través de este trabajo, cada estudiante desarrollará su propio proyecto de **Machine Learning**.

Para favorecer una mejor planificación del trabajo y permitir instancias de retroalimentación formativa, el proyecto se dividirá en dos entregas: esta **Pre-Entrega**, a mitad del curso, y una **Entrega Final**, al cierre.

### Entregable

Esta etapa **no requiere aún la elección ni el entrenamiento** de un modelo, pero debe dejar todo preparado para comenzar con el proceso de modelado en la segunda parte del curso.

La Pre-Entrega debe presentarse como un **cuaderno Jupyter** (Google Colab) que incluya las secciones que se detallan a continuación:

## Pre-entrega de proyecto

---

```
Obligatorio
```

#### Requerimientos:

- **Selección del dataset:** indicar origen, breve descripción del problema que aborda y justificación de su elección.
- **Análisis exploratorio inicial (EDA):** distribución de variables, detección de valores faltantes, análisis de correlaciones, visualizaciones básicas.
- **Limpieza de datos:** tratamiento de valores nulos, duplicados, outliers (si corresponde).

- **Transformaciones básicas:** codificación de variables categóricas, escalado de variables numéricas, creación o eliminación de variables (si fuera necesario).
- **Selección de variables relevantes** para el modelo.
- **División del dataset e** n conjuntos de entrenamiento y prueba.

## Pre-entrega de proyecto

---

```
Obligatorio
```

Se recomienda utilizar datasets moderados en tamaño y complejidad, preferentemente tabulares, para enfocarse en aplicar correctamente las etapas del proceso más que en resolver problemas técnicos complejos.

Se espera que el notebook esté **organizado**, bien **comentado**, y que el código esté acompañado de explicaciones claras y **observaciones propias**. No se requiere presentación oral.

## Pre-entrega de proyecto

```
A partir de la Clase N° 8 tendrás 7 días de corrido para realizar la autoevaluación y la entrega en el campus virtual
```

---

```
Obligatorio
```

Esta instancia evaluativa es de carácter obligatorio y es un punto clave dentro de la cursada ya que nos permitirá evaluar tu progreso en el recorrido y asegurar que estás en el camino correcto en la construcción del **Proyecto Final Integrador**.

### Cuestionario de autoevaluación

- Te permitirá reflexionar sobre tu propio aprendizaje, progreso y cumplimiento de las consignas o rúbricas previamente establecidas y en caso de ser necesario realizar las modificaciones o ajustes correspondientes antes de realizar la Pre-Entrega.
- Se encontrará disponible en el Campus Virtual.

### Pre-entrega de proyecto:

- Se evaluará la aplicación de los conocimientos adquiridos en la realización de un proyecto.
- La realización progresiva de los " **Ejercicios prácticos** " te guiará paso a paso hacia la realización de la " **Pre - Entrega** " y el " **Proyecto Integrador Final** "

## ⚙️Ejercicios prácticos

---

## ⚙️Una nueva mirada: clasificar por cercanía

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

Después de comparar los resultados del modelo de regresión logística, Silvia propuso que el equipo de Talento Lab probara un enfoque diferente. “ *Esta vez no vamos a entrenar una fórmula ni a estimar una probabilidad. Vamos a observar cómo se comportan los datos alrededor de cada caso* ”, explicó, mientras escribía “KNN” en la pizarra virtual.

Sabrina, curiosa, preguntó: “ *¿Vamos a tomar decisiones mirando a los vecinos?*”. Luis, que ya había leído sobre el tema, asintió: *“Exacto. Clasificamos a cada nuevo pasajero según lo que hicieron los más parecidos a él* ”. Matías, un poco escéptico, comentó que le parecía demasiado simple. Pero Silvia insistió: “ *Justamente por eso lo vamos a probar. A veces, mirar bien a los datos dice más que cualquier modelo matemático* ”.

## Ejercicio práctico

```
Obligatorio
```

---

#### Datos de origen

Utilizá el mismo dataset del Titanic que trabajaste en clases anteriores. Asegurate de seleccionar variables numéricas relevantes y de escalarlas correctamente antes de aplicar el modelo.

#### Entrenamiento

Entrená un modelo de clasificación usando *KNeighborsClassifier* de Scikit-learn. Probá al menos dos valores distintos de k (por ejemplo, 3 y 7).

## Ejercicio práctico

```
Obligatorio
```

---

#### Evaluación

Evaluá el rendimiento del modelo con las siguientes métricas: *precisión*, *recall*, *F1-score* y *matriz de confusión*. Usá *classification\_report* y *confusion\_matrix*.

#### Regresión logística

Agregá una celda de texto donde compares los resultados con los obtenidos usando regresión logística. ¿Mejoró el rendimiento? ¿Qué diferencias observás en los errores?

## Ejercicio práctico

```
Obligatorio
```

---

#### Importante:

Recordá que KNN es un modelo muy sensible al valor de k, a la escala de los datos y a la distribución de las clases. La clave está en observar con criterio cómo y por qué toma sus decisiones.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5yq1ea3085dnxt6/8068a888885a47b69a684f5c6d17c2bd/original/advertencia.png)

## 📄¡Nuevo cuestionario en Campus!

> [!note] Note
> No olvides que los cuestionarios son de carácter obligatorio para poder avanzar con la cursada.

ML - CLASE 08