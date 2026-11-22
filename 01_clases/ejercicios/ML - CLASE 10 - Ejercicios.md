---
title: "ML - CLASE 10"
source: "https://gamma.app/docs/ML-CLASE-10-Ejercicios-hert6xy37unhltu?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
ML - CLASE 10 - Ejercicios

## ⚙️Ejercicios prácticos

---

## ⚙️ Del árbol al bosque en Talento Lab

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

Después de analizar en profundidad los árboles de decisión, Sabrina planteó una inquietud al equipo de Talento Lab: “*¿Y si un solo árbol no alcanza? ¿Y si en lugar de elegir uno,usamos muchos?*”. Luis recordó haber leído sobre un enfoque que hacía justamente eso, y Silvia propuso que lo pusieran a prueba.

Así comenzaron a trabajar con **Random Forest**, combinando múltiples árboles para obtener predicciones más estables. Esta vez, no bastaba con entender una sola secuencia de decisiones: había que ver qué tan bien se comportaba el modelo general, y también qué variables estaban guiando las decisiones colectivas.

## Ejercicio práctico

```
Obligatorio
```

Tu objetivo es evaluar si el bosque realmente supera al árbol solitario, y entender en qué situaciones eso puede marcar la diferencia. Para ello:

---

#### Datos de origen

Utilizá el dataset del Titanic y preparalo como hiciste en las clases anteriores.

#### Entrenamiento

Entrená un modelo de clasificación usando **RandomForestClassifier** de **Scikit-learn**. No limites la cantidad de árboles, usá los valores por defecto para comenzar.

## Ejercicio práctico

```
Obligatorio
```

---

#### Evaluación

Evaluá su rendimiento con las métricas habituales: **precisión**, **recall**, **F1-score** y **matriz de confusión**. Comparalo con el árbol individual que entrenaste en la clase anterior.

#### Visualizá

Visualizá la importancia de las variables (**feature\_importances\_**) y construí un gráfico de barras que muestre qué predictores tuvieron más peso en el modelo.

## Ejercicio práctico

```
Obligatorio
```

---

#### Documentá y experimentá:

Escribí una breve reflexión:

¿el Random Forest mejoró la predicción respecto al árbol? ¿Se volvió más difícil de explicar? ¿Qué variables fueron clave?

Probá entrenar el modelo con n\_estimators=10, 50 y 100, y compará si hay diferencias en el rendimiento o la estabilidad.

Gamma