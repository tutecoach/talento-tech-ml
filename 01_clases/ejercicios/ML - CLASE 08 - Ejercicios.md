---
title: "ML - CLASE 08"
source: "https://gamma.app/docs/ML-CLASE-08-Ejercicios-bywo863q3vgqaxl?mode=doc"
author:
published:
created: 2026-10-03
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
ML - CLASE 08 - Ejercicios

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

ML - CLASE 08 - Ejercicios