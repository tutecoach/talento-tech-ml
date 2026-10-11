---
title: "ML - CLASE 07"
source: "https://gamma.app/docs/ML-CLASE-07-xg48w2tefjnzkfp?mode=doc"
author:
published:
created: 2026-10-03
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
ML- CLASE 07

![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/bf6b6b8e43574d7e81909d6c52dc2e06/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 07 | Regresión logística

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 06

#### Predecir con regresión lineal

- Regresión Lineal: teoría y aplicación.
- Métricas de regresión: MAE, MSE, RMSE, R².
- Implementación práctica en scikit-learn.

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

## Objetivos de la clase

Nos introduciremos en el mundo de la clasificación binaria, utilizando como punto de partida la regresión logística. Aprenderemos a identificar cuándo un problema requiere predecir una categoría en lugar de un valor numérico, y entenderemos cómo la regresión logística, a pesar de su nombre, permite estimar la probabilidad de que un caso pertenezca a una clase u otra.

---

1

#### Introducción a la clasificación binaria

Identificar cuándo un problema requiere predecir una categoría en lugar de un valor numérico.

2

#### Regresión logística

Entender cómo estimar probabilidades para tomar decisiones de clasificación.

3

#### Métricas de evaluación

Aprender a evaluar modelos con precisión, recall, F1-score y matriz de confusión.

## Clasificación binaria

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/b834e5f2dbec4b69a46281b61a4a158f/optimized/Duplicate-bro.svg)

## ¿Qué es un problema de clasificación?

En aprendizaje automático, un problema de **clasificación** busca determinar a qué categoría pertenece un caso.

La variable objetivo es **categórica**, no numérica. El modelo predice una etiqueta como "sí/no" o "positivo/negativo".

La **clasificación binaria** es un caso particular con solo dos clases posibles.

## Ejemplos de clasificación binaria

#### Salud

Predecir si un paciente tiene una determinada enfermedad basándose en sus análisis clínicos.

#### Correo electrónico

Detectar si un email es "spam" o "correo legítimo" analizando su contenido.

#### Finanzas

Determinar si un cliente pagará o no un préstamo según su historial crediticio.

#### Transporte

Predecir si un pasajero sobrevivió o no a un accidente, como el del Titanic.

## Regresión logística

---

## Regresión logística

#### Combinación lineal

Se construye una fórmula similar a la regresión lineal con las variables predictoras.

#### Transformación sigmoide

El resultado se transforma para obtener valores entre 0 y 1 (probabilidades).

#### Interpretación probabilística

El modelo indica la probabilidad de pertenecer a la clase positiva.

#### Umbral de decisión

Si la probabilidad supera 0.5, se predice la clase 1; si no, la clase 0.

## Diferencias entre regresión lineal y logística

#### Regresión lineal

- Predice valores numéricos continuos
- Salida: cualquier número real
- Ejemplo: predecir el monto de un reclamo

1

#### Regresión logística

- Predice probabilidades de clase
- Salida: número entre 0 y 1
- Ejemplo: predecir si habrá un reclamo

2

#### Tipo de pregunta

- Lineal: "¿Cuánto?"
- Logística: "¿Sí o no?"

3

![](https://cdn.gamma.app/5k42ay5jcl12uau/01b825c74ca4431f86c007d1bca4f413/optimized/Information-tab-bro.svg)

## Ventajas de la regresión logística

#### Eficiencia computacional

Rápida de entrenar y de hacer predicciones, incluso con grandes conjuntos de datos.

#### Interpretabilidad

Los coeficientes indican la importancia y dirección de cada variable.

#### Salida probabilística

Proporciona no solo una decisión, sino la probabilidad de cada clase.

#### Pocos hiperparámetros

Más sencilla de ajustar que modelos más complejos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/8cf07ecc27e74fe59c205effb398a1be/optimized/Visual-data-bro.svg)

## Limitaciones de la regresión logística

#### Relaciones lineales

Asume que existe una relación lineal entre las variables predictoras y el logaritmo de las probabilidades.

#### Multicolinealidad

El rendimiento puede degradarse cuando las variables predictoras están altamente correlacionadas.

#### Datos complejos

Puede tener un rendimiento inferior a modelos más sofisticados en problemas con relaciones complejas.

#### Valores atípicos

Es sensible a outliers que pueden distorsionar los coeficientes del modelo.

## Ejemplo: Seguros

#### Regresión lineal

Predecir el **monto** de los reclamos que recibirá un cliente en un año.

Resultado: $0, $2.000, $50.000...

Uso: Calcular riesgos, precios o primas.

#### Regresión logística

Predecir **si un cliente presentará o no** un reclamo en el próximo año.

Resultado: Sí (1) o No (0)

Uso: Segmentar clientes por riesgo.

## Ejemplo: educación

#### ¿Qué nota obtendrá el estudiante?

Regresión Lineal: Predice un valor numérico continuo (0-10)

#### ¿Aprobará el estudiante?

Regresión Logística: Predice una categoría (Aprueba/No aprueba)

#### La elección depende de la pregunta

El tipo de respuesta que buscamos determina el modelo a utilizar

## Métricas de evaluación

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/f0d489c1553d4395bf4a962fabe2cc4d/optimized/Financial-data-bro.svg)

## Métricas para evaluar modelos de clasificación

A diferencia de los modelos de regresión, en clasificación evaluamos decisiones: ¿el modelo acertó o se equivocó al asignar una clase?

#### Precisión (Accuracy)

Porcentaje total de aciertos del modelo.

#### Recall (Sensibilidad)

Capacidad para detectar correctamente los casos positivos.

#### F1-Score

Equilibrio entre precisión y sensibilidad.

#### Matriz de confusión

Visualización detallada de aciertos y errores.

## Precisión (Accuracy)

#### Definición

La **precisión** mide el porcentaje total de aciertos del modelo, sin distinguir entre clases.

#### Cálculo

Se calcula dividiendo la cantidad de predicciones correctas por el total de predicciones.

#### Utilidad

Es útil cuando las clases están **balanceadas**, pero puede ser engañosa cuando una clase es mucho más frecuente.

## Recall (Sensibilidad)

#### ¿Qué mide?

El **recall** mide la capacidad del modelo para detectar correctamente los casos positivos.

#### ¿Qué pregunta responde?

De todos los casos realmente positivos, ¿cuántos identificó el modelo?

#### ¿Cuándo es crucial?

Es crucial cuando los **falsos negativos** son costosos o peligrosos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/f322076264b843a8ad8a4c7bdc84cc85/optimized/Hospital-patient-bro.svg)

## Importancia del Recall

#### Diagnóstico médico

No queremos dejar pasar a pacientes enfermos. Es preferible tener algunos falsos positivos que perder casos reales.

#### Detección de fraude

El costo de no detectar un fraude real suele ser mayor que el de investigar algunas transacciones legítimas.

#### Control de calidad

Es mejor rechazar algunas piezas buenas que dejar pasar productos defectuosos.

## F1-Score (equilibrio)

#### Precisión

De los casos que predije como positivos, ¿cuántos lo eran realmente?

#### Recall

De todos los casos positivos reales, ¿cuántos detecté?

#### F1-Score

Media armónica que penaliza desequilibrios entre precisión y recall

#### Aplicación

Útil en clases desbalanceadas o cuando los errores tienen consecuencias distintas

## Matriz de confusión

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/308e52572fa34532a09d577caeae5822/optimized/Mathematics-bro-1.svg)

## Matriz de confusión

#### Predicción: positivo

#### Predicción: negativo

#### Real: positivo

Verdaderos positivos (VP)

Falsos negativos (FN)

#### Real: negativo

Falsos positivos (FP)

Verdaderos negativos (VN)

## Ejemplo: Matriz de confusión del Titanic

#### Verdaderos positivos (VP)

Personas que sobrevivieron y el modelo predijo correctamente que sobrevivieron.

#### Falsos negativos (FN)

Personas que sobrevivieron pero el modelo predijo que no sobrevivieron.

#### Falsos positivos (FP)

Personas que no sobrevivieron pero el modelo predijo que sobrevivieron.

#### Verdaderos negativos (VN)

Personas que no sobrevivieron y el modelo predijo correctamente que no sobrevivieron.

## Utilidad de la catriz de confusión

#### Cálculo de métricas

Permite derivar precisión, recall, F1-score y otras métricas.

#### Identificación de patrones de error

Revela si el modelo confunde más un tipo de casos que otros.

#### Ajuste del umbral de decisión

Ayuda a decidir si modificar el punto de corte (0.5) para favorecer precisión o recall.

#### Toma de decisiones informadas

Fundamental cuando las predicciones tienen consecuencias reales.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Regresión logística vs. lineal

¿Por qué la regresión logística es más adecuada que la lineal para problemas de clasificación binaria?

2

#### Valor de las probabilidades

¿Qué ventajas tiene trabajar con probabilidades en lugar de decisiones binarias directas?

3

#### Interpretación de métricas

¿Qué indica un modelo con precisión alta pero F1-score bajo sobre su comportamiento?

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

ML - CLASE 07