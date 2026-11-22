---
title: "ML - CLASE 07"
source: "https://gamma.app/docs/ML-CLASE-07-Ejercicios-sxwdkqiiy4xjj74?mode=doc"
author:
published:
created: 2026-10-03
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
ML- CLASE 07 - Ejercicios

## ⚙️Ejercicios prácticos

---

## ⚙️Tomando decisiones en Talento Lab.

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

Luego del primer intento de modelado con regresión lineal, los resultados no fueron del todo alentadores. A partir de allí, el equipo de Talento Lab entendió que era momento de cambiar de enfoque.

Sabrina propuso aplicar regresión logística para abordar un nuevo objetivo: predecir si un pasajero del Titanic sobrevivió o no, en función de algunas características conocidas como clase, edad, sexo y cantidad de familiares a bordo. Luis recordó que ahora no se trataría de estimar un número, sino de tomar una decisión binaria basada en una probabilidad.

## Ejercicio práctico

```
Obligatorio
```

---

#### Selección de variables

Usá el dataset del Titanic (o un dataset binario similar) y preparalo para entrenar un modelo de **regresión logística**. Seleccioná al menos 3 o 4 variables predictoras, y definí claramente cuál es la variable objetivo.

#### Entrenamiento

Entrená el modelo con LogisticRegression de Scikit-learn. Mostrá cómo se comporta en términos de precisión general (accuracy).

## Ejercicio práctico

```
Obligatorio
```

---

#### Calcular métricas

Calculá las siguientes métricas de evaluación: precisión, recall, F1-score, e imprimí la matriz de confusión. Usá classification\_report y confusion\_matrix.

#### Interpretar resultados

Agregá una celda de texto interpretando los resultados obtenidos: *¿el modelo acierta más en los positivos o en los negativos? ¿Qué tipo de errores comete más?*

ML - CLASE 07 - Ejercicios