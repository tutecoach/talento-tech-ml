---
title: "ML - CLASE 06"
source: "https://gamma.app/docs/ML-CLASE-06-ffw5ek0vdmrw5wg?mode=doc"
author:
published:
created: 2026-10-01
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/2d48fcfa22244615bfbd1a4375ace041/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 06 | Predecir con regresión lineal

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 05

#### División y validación del dataset

- División en conjuntos de entrenamiento y prueba.
- Conceptos de overfitting y underfitting.
- Introducción a la validación cruzada.

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

## Objetivos de la clase

Hoy aprenderemos a predecir valores numéricos continuos utilizando uno de los modelos más simples y potentes del aprendizaje automático.

---

1

#### Regresión lineal

Teoría y aplicación práctica del modelo.

2

#### Métricas de regresión

MAE, MSE, RMSE y R².

3

#### Implementación

Uso práctico en scikit-learn.

## Regresión lineal

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/8600e58328164d5badbbdf394c6c0027/optimized/Analysis-bro.svg)

## ¿Qué es la regresión lineal?

La regresión lineal es un modelo de Machine Learning supervisado que predice valores numéricos continuos a partir de variables independientes.

Su objetivo es ajustar una línea recta que represente la relación entre variables.

![](https://cdn.gamma.app/5k42ay5jcl12uau/5297d56b109c4276b970a7fc00c0f69c/optimized/Mathematics-bro.svg)

## La fórmula básica

#### Regresión Lineal Simple

y = a·x + b

Donde x es la variable predictora, y es la variable objetivo, a es la pendiente y b el valor de y cuando x = 0.

#### Regresión lineal múltiple

y = a₁·x₁ + a₂·x₂ +... + a·x + b

Incorpora múltiples variables predictoras para mejorar la precisión.

![](https://cdn.gamma.app/5k42ay5jcl12uau/4dd48e7981444c7a85c575d28c26315d/optimized/Ecommerce-campaign-bro.svg)

## Ejemplos de aplicación

#### Inmobiliaria

Predecir precios de viviendas según tamaño, ubicación y características.

#### Finanzas

Estimar ingresos mensuales basados en edad, educación y experiencia.

#### Logística

Anticipar tiempos de entrega según distancia, transporte y clima.

#### E-commerce

Calcular valor esperado de productos según búsquedas y ventas previas.

![](https://cdn.gamma.app/5k42ay5jcl12uau/3bf0417185c54a57b6a60ac15933d2d9/optimized/Version-control-bro.svg)

## Cuándo usar regresión lineal

#### Variable numérica continua

El objetivo es predecir un número, no una categoría.

#### Relación aproximadamente lineal

Las variables muestran tendencia lineal en gráficos de dispersión.

#### Necesidad de interpretabilidad

Se requiere una solución rápida, eficiente y fácil de explicar.

![](https://cdn.gamma.app/5k42ay5jcl12uau/59fbacf49f2e472aaa715a5d78d71ece/optimized/Yes-or-no-bro.svg)

## Regresión vs. clasificación

#### Regresión

Predice valores numéricos continuos:

- ¿Cuánto costará?
- ¿Cuántas unidades se venderán?
- ¿Cuál será el tiempo de espera?

#### Clasificación

Asigna categorías o etiquetas:

- ¿Es este cliente leal?
- ¿Este email es spam?
- ¿Este tumor es benigno?

## MAE - Error absoluto medio

#### ¿Qué es?

Promedio de las diferencias absolutas entre predicciones y valores reales.

Dato: Si el MAE es 8.500, el modelo se equivoca en promedio por 8.500 unidades.

#### Fácil de interpretar

#### Mantiene unidades originales

#### No exagera errores grandes

## MSE - Error cuadrático medio

#### ¿Qué es?

Promedio de los errores elevados al cuadrado.

#### Características

- Penaliza errores grandes
- Unidades al cuadrado (difícil interpretación)
- Útil para minimizar desviaciones importantes

Ideal cuando errores grandes son más problemáticos que errores pequeños.

## RMSE - Raíz del error cuadrático medio

#### Definición

Raíz cuadrada del MSE combina sensibilidad a errores grandes con interpretabilidad.

#### Ventajas

Recupera las unidades originales. Ofrece balance entre MAE y MSE.

#### Aplicación

Ideal para estimaciones de valor o tiempo donde errores grandes importan.

![](https://cdn.gamma.app/5k42ay5jcl12uau/c54a13236ac047afbb3b4a96b04136ab/optimized/Consulting-bro.svg)

## R² - Coeficiente de determinación

#### Modelo perfecto

Explica toda la variabilidad de los datos.

#### Buen modelo

Explica 70% de la variabilidad.

#### Modelo débil

Explica solo 30% de la variabilidad.

#### Modelo inútil

No explica nada mejor que el promedio.

## Comparación de métricas

**Métrica**

**Ventajas**

**Desventajas**

**Cuándo usarla**

**MAE**

Fácil interpretación

No distingue entre errores grandes y pequeños

Cuando todos los errores son igualmente importantes

**MSE**

Penaliza errores grandes

Unidades al cuadrado

Cuando errores grandes son críticos

**RMSE**

Balance entre MAE y MSE

Más sensible a valores atípicos

Para interpretación en unidades originales

**R²**

Mide poder explicativo

No indica precisión absoluta

Para comparar modelos diferentes

## Evaluación del modelo

#### Interpretación

Comprender qué significan las métricas en contexto.

#### Comparación

Contrastar diferentes métricas para evaluación completa.

#### Cálculo

Obtener valores numéricos que cuantifican el rendimiento.

#### Medición

Evaluar objetivamente la calidad de las predicciones.

## Algunos tips:

#### Tipo de problema

¿Qué pregunta intentamos responder con nuestro modelo?

1

#### Elección de modelo

¿Es el modelo adecuado para nuestro objetivo?

2

#### Evaluación

¿Cómo medimos el éxito de nuestras predicciones?

3

#### Interpretación

¿Qué significan los resultados en nuestro contexto?

4

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Importancia de múltiples métricas

¿Por qué es crucial evaluar un modelo con varias métricas?

2

#### Aplicaciones prácticas

¿En qué problemas reales es útil la regresión lineal?

3

#### Interpretación de R²

¿Qué significa un R² cercano a cero en un modelo aparentemente bueno?

4

#### Selección de variables

¿Qué criterios aplicar para elegir variables predictoras?

## ⚙️Ejercicios prácticos

---

## ⚙️Trabajamos con datos en TechLab.

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

Silvia recibió una nueva solicitud: estimar el gasto promedio por cliente, y lo comunicó al equipo de **Talento Lab**.

Luis propuso utilizar regresión lineal como punto de partida, ya que es un modelo fácil de interpretar y puede dar respuestas rápidas. Sabrina y Matías se encargarán de preparar las variables y analizar las métricas. Silvia les recuerda que no basta con hacer predicciones, sino que es necesario justificar por qué un modelo funciona.

Ahora es tu turno. Como parte del equipo, deberás replicar este primer modelo de regresión lineal utilizando un conjunto de datos real, construyendo un modelo funcional, y evaluar su desempeño usando múltiples métricas.

## Ejercicio práctico

```
Obligatorio
```

---

#### Datos de origen

Seleccioná un conjunto de datos que contenga al menos una variable numérica continua como objetivo a predecir (por ejemplo: precio, duración, cantidad, consumo, etc.). Puede ser uno de Kaggle, Datos Abiertos, UCI o una fuente confiable.

#### Preparar el dataset

Realizá una preparación mínima del dataset: limpieza, selección de variables relevantes y división en conjuntos de entrenamiento y prueba.

## Ejercicio práctico

```
Obligatorio
```

---

#### Entrenamiento

Entrená un modelo de regresión lineal utilizando Scikit-learn. Luego, realizá predicciones sobre el conjunto de prueba

#### Métricas

Calculá al menos cuatro métricas: MAE, MSE, RMSE y R². Agregá una breve interpretación de cada resultado, explicando qué significa y cómo lo evaluarías enfunción del contexto del problema.

## Ejercicio práctico

```
Obligatorio
```

---

#### Documentación

Documentá todo tu trabajo en un cuaderno Jupyter.

Asegurate de incluir celdas de texto que expliquen tu razonamiento, tus elecciones y tus observaciones sobre los resultados obtenidos.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5yq1ea3085dnxt6/8068a888885a47b69a684f5c6d17c2bd/original/advertencia.png)

## 📄¡Nuevo cuestionario en Campus!

> [!note] Note
> No olvides que los cuestionarios son de carácter obligatorio para poder avanzar con la cursada.

ML - CLASE 06