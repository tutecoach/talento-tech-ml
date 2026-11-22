---
title: "ML - CLASE 10"
source: "https://gamma.app/docs/ML-CLASE-10-uwlmfkd2p88f62h?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/061176a95d2b451f86c4a8e238ee5c10/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 10 | Random Forest

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 09

#### Árboles de Decisión

- Árboles de Decisión: estructura y poda.
- Implementación y visualización del árbol.
- Overfitting en árboles

Clase 10

#### Random Forest

- Random Forest: conceptos y ventajas.
- Implementación práctica.
- Importancia de variables.

Clase 11

#### Introducción al clustering

- Introducción al clustering.
- Algoritmo K-Means: teoría y aplicación.
- Evaluación de clustering: inercia y silhouette score.
- Ejercicios.

## Objetivos de la clase

Bienvenidos a nuestra clase sobre Random Forest, donde descubriremos cómo la combinación de múltiples árboles de decisión puede generar modelos más robustos y precisos para el aprendizaje supervisado.

---

1

#### Conceptos de Random Forest

Fundamentos y ventajas del modelo de bosque aleatorio.

2

#### Implementación práctica

Aplicación al conjunto de datos del Titanic.

3

#### Importancia de variables

Análisis de la contribución de cada predictor.

## Random Forest

---

## ¿Qué es un Random Forest?

Un **Random Forest** es un modelo de aprendizaje automático que combina múltiples árboles de decisión para resolver problemas de clasificación o regresión.

Su lógica se basa en una idea simple pero poderosa: varios modelos débiles, si son lo suficientemente diversos, pueden combinarse para formar un modelo fuerte.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/uploaded-images/NZX2oTNUige53zP2U-31q.png)

## ¿Cómo funciona?

#### Votación colectiva

Cada árbol "vota" por una clase y la clase más votada es la predicción final.

#### Mejor generalización

Al promediar decisiones de varios modelos, se logra mejor capacidad de generalización.

#### Reducción de errores

La diversidad de opinión ayuda a reducir errores individuales.

![](https://cdn.gamma.app/5k42ay5jcl12uau/08924258b6d54b44ba459f6db46effe2/optimized/olive-tree-bro.svg)

## Funcionamiento interno

1

#### Diversidad de árboles

Cada árbol se entrena con datos y variables diferentes.

2

#### Votación colectiva

Todos los árboles emiten su predicción.

3

#### Resultado final

Se combina la opinión de todos los árboles.

## Analogía médica

#### Consulta médica

Diez médicos de distintas especialidades evalúan a un paciente.

#### Decisión colectiva

Si 8 dicen que sí y 2 que no, se elige la opción más votada.

#### Diagnóstico confiable

La diversidad de opinión genera una decisión más confiable.

## Muestreo con reemplazo (Bootstrap)

#### Datos originales

Conjunto completo de entrenamiento.

#### Selección aleatoria

Muestreo con reemplazo para cada árbol.

#### Árboles diversos

Cada árbol ve una versión distinta de los datos.

#### Variación garantizada

Algunos registros se repiten, otros quedan fuera.

![](https://cdn.gamma.app/5k42ay5jcl12uau/90ec1c0f5dfa4f788a3c4d5133680439/optimized/Decision-fatigue-bro.svg)

## Selección aleatoria de variables

#### Variables disponibles

Conjunto completo de predictores.

#### Subconjunto aleatorio

Selección de solo algunas variables por nodo.

#### Árboles únicos

Cada árbol aprende patrones diferentes.

## Agregación de predicciones

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/uploaded-images/9d78ptceFRWWoeGEn-MVS.png)

#### Clasificación

Se realiza una votación por mayoría: la clase más votada es la predicción final.

#### Regresión

Se promedian los valores predichos por cada árbol para obtener la estimación final.

Esta combinación reduce la varianza del modelo y mejora la estabilidad.

![](https://cdn.gamma.app/5k42ay5jcl12uau/a47e41d72f7f4a1ab8c11aac3792a674/optimized/cherry-tree-bro.svg)

## Ventajas de Random Forest

#### Alta precisión

Mejora el rendimiento respecto a un árbol individual.

#### Menor sobreajuste

La aleatoriedad evita que los árboles memoricen los datos.

#### Versatilidad

Funciona bien con diversos tipos de datos.

#### Importancia de variables

Permite saber cuáles predictores aportan más al modelo.

![](https://cdn.gamma.app/5k42ay5jcl12uau/ef5117a8acca4d3484b9fab423f743a6/optimized/No-data-bro.svg)

## Limitaciones de Random Forest

#### Pérdida de interpretabilidad

El conjunto completo es difícil de explicar con reglas claras.

#### Mayor costo computacional

Entrenar muchos árboles consume más tiempo y memoria.

#### Sensibilidad a variables irrelevantes

Su rendimiento puede verse afectado con muchas variables sin valor.

## Utilidad de la importancia de variables

#### Interpretación del modelo

Entender qué factores están guiando al modelo, incluso sin visualizar todos los árboles.

#### Identificación de variables irrelevantes

Detectar predictores que podrían eliminarse para simplificar futuros modelos.

#### Selección de características

Conservar solo las variables más útiles para mejorar el rendimiento.

#### Comunicación de resultados

Explicar a otros sectores cuáles variables tienen más impacto.

![](https://cdn.gamma.app/5k42ay5jcl12uau/75babb8a14e940f88ef8911d296b9204/optimized/Forest-bro.svg)

## Ajuste de hiperparámetros

**n\_estimators**

Número de árboles (100 por defecto)

**max\_depth**

Profundidad máxima de cada árbol

**min\_samples\_split**

Mínimo de muestras para dividir un nodo

**min\_samples\_leaf**

Mínimo de muestras en un nodo hoja

**max\_features**

Número de variables a considerar en cada división

## Conceptos clave

#### Sobreajuste

Cómo Random Forest lo reduce mediante la diversidad.

#### Generalización

Mejora en la capacidad de predecir casos nuevos.

#### Importancia de variables

Identificación de predictores clave.

3

#### Ensambles

Combinación de modelos para mejorar rendimiento.

#### Aleatoriedad

Uso controlado para generar diversidad.

5

![](https://cdn.gamma.app/5k42ay5jcl12uau/dae560285c8f437583c0298403b195b5/optimized/Problem-solving-bro.svg)

## Ventajas en problemas complejos

#### Precisión superior

Especialmente en problemas con muchas variables.

#### Robustez

Menor sensibilidad a ruido y valores atípicos.

#### Equilibrio

Entre complejidad y capacidad predictiva.

## Comparativa de modelos

#### Modelo

#### Precisión

#### Interpreta-bilidad

#### Velocidad

#### Memoria

**Regresión Logística**

Media

Alta

Rápida

Baja

**Árbol de Decisión**

Media

Alta

Media

Baja

**Random Forest**

Alta

Media

Lenta

Alta

**Redes Neuronales**

Muy Alta

Baja

Muy Lenta

Muy Alta

![](https://cdn.gamma.app/5k42ay5jcl12uau/315bd371502e466ead7cb88fb0a53320/optimized/Bigfoot-bro.svg)

## Arboles vs. Bosques

#### Árbol de Decisión

- Más interpretable
- Menor precisión
- Mayor riesgo de sobreajuste
- Entrenamiento más rápido

#### Random Forest

- Menos interpretable
- Mayor precisión
- Menor riesgo de sobreajuste
- Entrenamiento más lento

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Ventajas concretas

¿Qué ventaja ofrece Random Forest frente a un único árbol de decisión?

2

#### Aleatoriedad y rendimiento

¿Cómo contribuyen la aleatoriedad y la combinación al rendimiento?

3

#### Interpretabilidad

¿Cómo compensar la pérdida de interpretabilidad en Random Forest?

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

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5yq1ea3085dnxt6/8068a888885a47b69a684f5c6d17c2bd/original/advertencia.png)

## 📄¡Nuevo cuestionario en Campus!

> [!note] Note
> No olvides que los cuestionarios son de carácter obligatorio para poder avanzar con la cursada.

Gamma