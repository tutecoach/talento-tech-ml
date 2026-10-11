---
title: "ML - CLASE 05"
source: "https://gamma.app/docs/ML-CLASE-05-Ejercicios-uvg9lsbcy9divzs?mode=doc"
author:
published:
created: 2026-10-01
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
ML- CLASE 05 - Ejercicios

## ⚙️Ejercicios prácticos

---

## ⚙️Ejercicio práctico

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

El modelo que había impresionado al equipo de **Talento Lab** resultó ser una advertencia más que un logro. Lo que parecía un éxito —una precisión de más del 98%— fue en realidad una ilusión: el modelo había aprendido demasiado bien... los datos que ya conocía.

Ahora sabemos que no basta con entrenar un modelo, hay que saber evaluarlo de manera rigurosa y honesta. Para completar esta etapa, deberás aplicar todo lo aprendido en esta clase y reflexionar sobre cómo tus decisiones afectan el comportamiento del modelo.

## Ejercicio práctico

```
Obligatorio
```

---

#### Preparación

Cargá el dataset del Titanic ([este mismo que venís utilizando en clases anteriores](https://drive.google.com/file/d/1PD0A9xtChEvgEtL4uEkwiJZ4KGaQSk5h/view?usp=drive_link)) y preparalo para el modelado, asegurándote de tratar los valores faltantes y seleccionar las variables que usarás como entrada y salida.

#### División

Dividí el dataset en conjuntos de entrenamiento y prueba. Probá al menos dos proporciones distintas (por ejemplo, 80/20 y 70/30) usando train\_test\_split de scikit-learn.

## Ejercicio práctico

```
Obligatorio
```

---

#### Entrenamiento

Entrená un modelo de clasificación simple, como una regresión logística, sobre cada partición, y medí su desempeño en ambos conjuntos (entrenamiento y prueba). Documentá los resultados.

#### Reflexión

Reflexioná sobre lo observado: ¿El modelo se desempeñó mejor con una proporción que con otra? ¿Detectás señales de overfitting o underfitting?

## Ejercicio práctico

```
Obligatorio
```

---

#### Validación cruzada

Aplicá validación cruzada (5-fold) sobre el mismo modelo. Compará el rendimiento promedio obtenido con esta técnica respecto de las divisiones simples. ¿Qué diferencias encontrás? ¿Cuál te parece más confiable?

ML - CLASE 05 - Ejercicios