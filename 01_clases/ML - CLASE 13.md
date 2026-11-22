---
title: "ML - CLASE 13"
source: "https://gamma.app/docs/ML-CLASE-13-s2v4lrc7kdcceas?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/c82fbaf8ceb742d7979815f869163ac8/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 13 | Comparativa y evaluación de modelos

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 12

#### Creación de pipelines

- Creación de pipelines en scikit-learn.
- Automatización del flujo completo.
- Introducción a GridSearchCV para optimización.

Clase 13

#### Comparativa y evaluación de modelos

- Comparativa y evaluación de modelos.
- Selección del mejor modelo según métricas.

Clase 14

#### Proyecto guiado (Parte 1)

- Desarrollo guiado: EDA y preprocesamiento de un dataset real.
- Entrenamiento y evaluación de un modelo supervisado.
- Visualización y análisis de resultados.

## Objetivos de la clase

En esta clase exploraremos cómo comparar y evaluar diferentes modelos de machine learning para seleccionar el más adecuado según métricas específicas.

---

1

#### Comparativa de modelos

Análisis sistemático de diferentes algoritmos aplicados al mismo problema.

2

#### Evaluación de rendimiento

Métricas y visualizaciones para medir la efectividad de cada modelo.

3

#### Selección del mejor modelo

Criterios para elegir la solución más adecuada según el contexto.

## Modelos y algoritmos

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/e92a0f1284a640fc978c0e4aa993a776/optimized/Data-analysis-bro.svg)

## Importancia de la comparación

La comparación de modelos es una etapa crucial que permite evaluar diferentes estrategias para un mismo problema con criterios consistentes.

No se trata solo de rendimiento numérico, sino de comprender cómo se comportan los modelos frente a los mismos datos.

Esta práctica nos ayuda a evitar elecciones apresuradas y a respaldar decisiones con evidencia concreta.

![](https://cdn.gamma.app/5k42ay5jcl12uau/038786e3dd6e421a91cfe49457b9c8f8/optimized/Visual-data-bro.svg)

## Más allá de la precisión

#### Interpretabilidad

Algunos modelos son más fáciles de explicar, lo que puede ser crucial en áreas como salud o educación.

#### Eficiencia computacional

El tiempo de entrenamiento y predicción puede ser determinante en aplicaciones en tiempo real.

#### Estabilidad

Un buen modelo debe mantener su rendimiento con diferentes conjuntos de datos.

## Algoritmos a comparar

#### Regresión Logística

Simple, interpretable, eficiente para relaciones lineales.

#### K-Nearest Neighbors

Intuitivo, no paramétrico, sensible a la escala.

#### Árboles de Decisión

Fácil interpretación, captura relaciones no lineales.

#### Random Forest

Robusto, preciso, menos interpretable.

## Criterios de comparación

#### Exactitud general

Proporción de casos predichos correctamente.

1

#### Métricas específicas

Precisión, recall, F1-score, área bajo la curva ROC.

2

#### Estabilidad del modelo

Consistencia en validación cruzada.

3

## Matriz de confusión

La matriz de confusión nos permite ver no solo cuántas predicciones fueron correctas, sino también cómo se equivocó el modelo y en qué dirección.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/882d00ad6e9e4d7cad3ebbbc513f0fb9/original/image.png)

## Interpretación de la matriz

#### Verdaderos positivos (TP)

El modelo predijo "sí" y era "sí".

#### Verdaderos negativos (TN)

El modelo predijo "no" y era "no".

#### Falsos positivos (FP)

El modelo predijo "sí" pero era "no".

#### Falsos negativos (FN)

El modelo predijo "no" pero era "sí".

![](https://cdn.gamma.app/5k42ay5jcl12uau/98957167ac50400cbaee09a35fcde2ff/optimized/Hospital-bed-bro.svg)

## Costo de los errores

### (Falsos positivos y falsos negativos)

#### Detección de fraude

Un falso negativo (no detectar un fraude) puede ser más grave que un falso positivo (frenar una transacción válida).

#### Diagnóstico médico

No detectar una enfermedad grave (falso negativo) puede tener consecuencias fatales.

#### Filtro de spam

Un correo importante clasificado como spam (falso positivo) puede ser más problemático que spam en la bandeja de entrada.

## Curva ROC

La curva ROC (*Receiver Operating Characteristic*) representa el compromiso entre la tasa de verdaderos positivos (TPR) y la tasa de falsos positivos (FPR).

- Eje X: Tasa de falsos positivos
- Eje Y: Tasa de verdaderos positivos

Un modelo ideal tendría un punto en el ángulo superior izquierdo (0% de falsos positivos y 100% de verdaderos positivos).

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/7dc18ee25f97428180c59febff49850e/original/image.png)

## Área bajo la curva (AUC)

1.0

#### Modelo perfecto

Discriminación perfecta entre clases.

0.5

#### Modelo aleatorio

Equivalente a predecir al azar.

\<0.5

#### Modelo inviable

Peor que predecir al azar.

El AUC mide la capacidad del modelo para distinguir entre clases. No depende de un umbral específico, lo que lo convierte en una medida global del rendimiento.

![](https://cdn.gamma.app/5k42ay5jcl12uau/8d15be5b7d5a490a9a880d1fa5919245/optimized/Analytics-bro.svg)

## Ventajas del AUC-ROC

#### Independencia del umbral

Evalúa el rendimiento del modelo en todos los posibles umbrales de decisión.

#### Robustez ante desbalance

Útil en conjuntos de datos con clases desbalanceadas donde la accuracy puede ser engañosa.

#### Comparabilidad

Permite comparar directamente diferentes modelos con un solo valor numérico.

![](https://cdn.gamma.app/5k42ay5jcl12uau/0453c8848b084bd38758e8832f362dd3/optimized/Business-Plan-bro.svg)

## Validación cruzada

#### División de datos

Separar los datos en k subconjuntos (folds).

#### Entrenamiento iterativo

Entrenar el modelo k veces, usando k-1 folds para entrenar y 1 para validar.

#### Evaluación de estabilidad

Analizar el rendimiento promedio y la desviación estándar entre folds.

## Tiempo de entrenamiento

<svg width="100%" viewBox="0 0 724.4444444444445 372.44444444444446" height="100%" preserveAspectRatio="none" overflow="visible"><line x1="141.3125" y1="8" x2="141.3125" y2="340.44444444444446" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" opacity="0.5"></line><line x1="335.3125" y1="8" x2="335.3125" y2="340.44444444444446" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" opacity="0.2"></line><line x1="529.3125" y1="8" x2="529.3125" y2="340.44444444444446" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" opacity="0.2"></line><line x1="723.3125" y1="8" x2="723.3125" y2="340.44444444444446" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" opacity="0.2"></line><g transform="translate(141.3125, 8)"><g transform="translate(0, 0)"><g transform="translate(0, 0)"><rect height="55.421188630490946" width="582.1319444444445" x="0" y="23.751937984496124" radius="5" fill="#122b3aff" opacity="0"></rect><g opacity="1" style="cursor: pointer; transition: opacity 0.25s;"><path d="M5,23.751937984496124 h55 a5,5 0 0 1 5,5 v45.421188630490946 a5,5 0 0 1 -5,5 h-55 h-5v-5 v-45.421188630490946 v-5h5z" fill="#122b3aff"></path></g></g></g><g transform="translate(0, 0)"><g transform="translate(0, 0)"><rect height="55.42118863049096" width="582.1319444444445" x="0" y="102.9250645994832" radius="5" fill="#1c425aff" opacity="0"></rect><g opacity="1" style="cursor: pointer; transition: opacity 0.25s;"><path d="M5,102.9250645994832 h93 a5,5 0 0 1 5,5 v45.42118863049096 a5,5 0 0 1 -5,5 h-93 h-5v-5 v-45.42118863049096 v-5h5z" fill="#1c425aff"></path></g></g></g><g transform="translate(0, 0)"><g transform="translate(0, 0)"><rect height="55.421188630490946" width="582.1319444444445" x="0" y="182.0981912144703" radius="5" fill="#255979ff" opacity="0"></rect><g opacity="1" style="cursor: pointer; transition: opacity 0.25s;"><path d="M5,182.0981912144703 h145 a5,5 0 0 1 5,5 v45.421188630490946 a5,5 0 0 1 -5,5 h-145 h-5v-5 v-45.421188630490946 v-5h5z" fill="#255979ff"></path></g></g></g><g transform="translate(0, 0)"><g transform="translate(0, 0)"><rect height="55.421188630490974" width="582.1319444444445" x="0" y="261.27131782945736" radius="5" fill="#2f7098ff" opacity="0"></rect><g opacity="1" style="cursor: pointer; transition: opacity 0.25s;"><path d="M5,261.27131782945736 h443 a5,5 0 0 1 5,5 v45.421188630490974 a5,5 0 0 1 -5,5 h-443 h-5v-5 v-45.421188630490974 v-5h5z" fill="#2f7098ff"></path></g></g></g></g><g transform="translate(0, 0)"><g transform="translate(141.3125, 8)"><g transform="translate(0, 0)"><line x1="0" y1="51.462532299741596" x2="-6" y2="51.462532299741596" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="-4" y="0.33em" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="-6" y="51.462532299741596" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="end"><tspan x="-6" dy="0em">Regresión Logística</tspan></text></svg></g> <g transform="translate(0, 0)"><line x1="0" y1="130.63565891472868" x2="-6" y2="130.63565891472868" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="-4" y="0.33em" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="-6" y="130.63565891472868" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="end"><tspan x="-6" dy="0em">KNN</tspan></text></svg></g> <g transform="translate(0, 0)"><line x1="0" y1="209.80878552971578" x2="-6" y2="209.80878552971578" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="-4" y="0.33em" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="-6" y="209.80878552971578" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="end"><tspan x="-6" dy="0em">Árbol de Decisión</tspan></text></svg></g> <g transform="translate(0, 0)"><line x1="0" y1="288.98191214470285" x2="-6" y2="288.98191214470285" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="-4" y="0.33em" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="-6" y="288.98191214470285" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="end"><tspan x="-6" dy="0em">Random Forest</tspan></text></svg></g> <line x1="0" y1="0.5" x2="0" y2="340.94444444444446" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2"></line></g><g transform="translate(141.3125, 348.44444444444446)"><g transform="translate(0, 0)"><line x1="0" y1="0" x2="0" y2="6" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="0" y="4" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="0" y="16" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="end"><tspan x="0" dy="0em">0</tspan></text></svg></g> <g transform="translate(0, 0)"><line x1="194" y1="0" x2="194" y2="6" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="0" y="4" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="194" y="16" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="middle"><tspan x="194" dy="0em">1.5</tspan></text></svg></g> <g transform="translate(0, 0)"><line x1="388" y1="0" x2="388" y2="6" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="0" y="4" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="388" y="16" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="middle"><tspan x="388" dy="0em">3</tspan></text></svg></g> <g transform="translate(0, 0)"><line x1="582" y1="0" x2="582" y2="6" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2" stroke-linecap="square"></line><svg x="0" y="4" font-size="var(--chakra-fontSizes-sm)" style="overflow: visible;"><text transform="" x="582" y="16" fill="currentColor" font-family="var(--body-font)" font-size="var(--chakra-fontSizes-sm)" font-weight="var(--body-font-weight)" userselect="none" text-anchor="middle"><tspan x="582" dy="0em">4.5</tspan></text></svg></g><line x1="0.5" y1="0" x2="582.6319444444445" y2="0" fill="transparent" shape-rendering="crispEdges" stroke="currentColor" stroke-width="2"></line></g></g></svg>

El tiempo de entrenamiento puede ser crucial en aplicaciones que requieren reentrenamiento frecuente o procesamiento en tiempo real.

## Criterios de selección

#### Rendimiento

Accuracy, precisión, recall, F1-score, AUC

#### Estabilidad

Consistencia en validación cruzada

#### Eficiencia

Tiempo de entrenamiento y predicción

#### Interpretabilidad

Capacidad de explicar las decisiones

#### Complejidad

Facilidad de implementación y mantenimiento

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Comparar modelos

¿Qué factores deberías tener en cuenta al comparar dos modelos con resultados similares en términos de accuracy?

2

#### Matriz de confusión

¿En qué situaciones una matriz de confusión aporta más información que un simple porcentaje de aciertos?

3

#### ROC y AUC

¿Por qué es útil la curva ROC y el valor AUC en contextos con clases desbalanceadas?

## ⚙️Ejercicios prácticos

---

## ⚙️ Una decisión que importa

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

En **Talento Lab**, el equipo se preparaba para presentar tres modelos candidatos a un nuevo cliente del sector salud. Habían trabajado con datos sensibles sobre pacientes y enfermedades poco frecuentes, y querían asegurarse de elegir la solución más adecuada.

Silvia insistió: “*No se trata solo de quién acierta más, sino de quién se equivoca menos donde no puede fallar*”.

## Ejercicio práctico

```
Obligatorio
```

El objetivo de este ejercicio es que puedas **comparar al menos dos modelos distintos** aplicados al mismo problema, y que justifiques cuál elegirías para entregar como solución final.

---

#### Selección

Elegí al menos dos algoritmos que ya conozcas (por ejemplo, regresión logística, KNN, árbol de decisión, random forest).

#### Entrenamiento

Entrenalos utilizando el mismo conjunto de datos (puede ser el Titanic o uno de Kaggle).

#### Evaluación

Evaluá su rendimiento utilizando los mecanismos vistos (matriz de confusión, curva ROC y AUC, etc)

## Ejercicio práctico

```
Obligatorio
```

---

#### Registrá

Registrá los resultados de forma organizada (puede ser en una tabla o en celdas separadas).

#### Justificá

Redactá una breve justificación técnica indicando qué modelo elegirías, por qué es el más adecuado para ese problema, qué limitaciones encontraste, etc.

Gamma

<svg style="width: 0px; height: 0px; position: absolute; top: -100%; left: -100%;"><text id="__react_svg_text_measurement_id_gamma" style="font-family: currentColor; font-size: currentColor; font-weight: currentColor;">3.5</text></svg> <svg aria-hidden="true" style="width: 0px; height: 0px; position: absolute; top: -100%; left: -100%;"><text id="__react_svg_text_measurement_id">4.5</text></svg>