---
title: "ML - CLASE 12"
source: "https://gamma.app/docs/ML-CLASE-12-Ejercicios-ru8pr2wp342bwdx?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
ML - CLASE 12 - Ejercicios

## ⚙️Ejercicios prácticos

---

## ⚙️ Un patrón oculto

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

El equipo de **Talento Lab** debía comparar varios modelos para predecir suscripciones a un servicio digital, usando un dataset anónimo. Para evitar errores y repetir código, decidieron automatizar el proceso con pipelines y optimizar cada modelo con **GridSearchCV.**

Sabrina organizó los flujos, Luis definió los hiperparámetros y todo se ejecutó en pocas líneas. El trabajo, antes manual y largo, se volvió ágil y reproducible. El cliente pudo elegir el mejor modelo con claridad, y el equipo comprobó el valor de trabajar con orden y buenas prácticas.

## Ejercicio práctico

```
Obligatorio
```

Ahora te toca a vos aplicar lo aprendido. A partir de un conjunto de datos como el del Titanic o cualquier otro que elijas, construí un flujo completo de trabajo utilizando un pipeline.

---

#### Modelo

Elegí un modelo supervisado que ya conozcas (por ejemplo, regresión logística, árbol de decisión o random forest).

#### Pipeline

Construí un pipeline que incluya al menos:

1. una transformación (como escalado o imputación),
1. y el modelo elegido.

## Ejercicio práctico

```
Obligatorio
```

---

#### Evaluación

Evaluá el pipeline con validación cruzada usando **cross\_val\_score**.

#### GridSearchCV

Luego usá **GridSearchCV** para probar distintas combinaciones de hiperparámetros (por ejemplo, distintos valores de **C**, **max\_depth**, **n\_estimators**, etc.).

## Ejercicio práctico

```
Obligatorio
```

---

#### Informá y reflexiona:

Informá la mejor combinación de hiperparámetros encontrada, y la puntuación promedio obtenida en validación cruzada.

¿El modelo con parámetros óptimos mejoró respecto al original?

¿Qué aprendiste del proceso?

Gamma