---
title: "ML - CLASE 05"
source: "https://gamma.app/docs/ML-CLASE-05-fkb16krex8b6ldx?mode=doc"
author:
published:
created: 2026-10-01
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/75131857177c4a1d8a6a7ce6855bb797/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 05 | División y validación del dataset

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 04

#### Transformación de datos

- Feature engineering y selección de variables.
- Normalización y estandarización de datos.
- Codificación de variables categóricas.

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

## Objetivos de la clase

Aprenderemos herramientas fundamentales para entrenar y evaluar modelos de aprendizaje automático de manera confiable.

---

1

#### División de datos

Aprenderemos a dividir conjuntos de datos en entrenamiento y prueba.

2

#### Conceptos clave

Comprenderemos overfitting y underfitting para diagnosticar modelos.

3

#### Validación cruzada

Conoceremos técnicas para evaluar modelos de forma robusta.

## Dividir los datos

---

## ¿Por qué dividir los datos?

#### Entrenamiento

Al entrenar un modelo de Machine Learning, le enseñamos a **reconocer patrones**.

#### Evaluación invalida

Usar los mismos datos para entrenar y evaluar es como examinar a un estudiante con las mismas preguntas que estudió.

3

#### Evaluación honesta

La división del dataset nos permite obtener una evaluación honesta y prevenir el sobreajuste.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1a025ccd19a94c98b96c9328e849f068/optimized/Skipping-rope-bro.svg)

## Conjunto de entrenamiento

#### Mayor porción

Generalmente representa el 70-80% del dataset total.

#### Ajuste de parámetros

El algoritmo analiza estos datos y ajusta sus parámetros internos.

#### Identificación de patrones

Cuantos más datos, mejor podrá identificar patrones complejos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/d7d89c45cb164cb6a4f9171521be9d80/optimized/Exams-bro.svg)

## Conjunto de prueba

#### Datos reservados

Porción del dataset que queda reservada, generalmente 20-30%.

#### Simulación del mundo real

Simula datos que el modelo encontrará en producción.

#### Evaluación honesta

Permite medir el rendimiento real del modelo con datos nunca vistos.

## Proporciones comunes

#### 80/20

La división más común: 80% entrenamiento, 20% prueba.

#### 70/30

Alternativa frecuente cuando se necesita más datos de prueba.

#### 90/10

Útil cuando el dataset es muy grande.

![](https://cdn.gamma.app/5k42ay5jcl12uau/37919148f3384c52ab74f0ec1a017fda/optimized/Video-game-developer-bro.svg)

## Consecuencias de no dividir

#### Resultados engañosos

El modelo parece excelente pero no refleja su rendimiento real.

#### Falta de generalización

El modelo repite lo que vio pero no aprende a generalizar.

#### Decisiones equivocadas

Como construir un puente probado solo en condiciones ideales.

![](https://cdn.gamma.app/5k42ay5jcl12uau/450fdc94ab0348fb8451570fa15d04bd/optimized/Analyze-bro.svg)

## Limitaciones del Train/Test Split

#### Dependencia de la división

La evaluación depende exclusivamente de cómo se haya hecho la partición de datos.

Si por azar el conjunto de prueba queda con casos muy fáciles o muy difíciles, la evaluación será engañosa.

## Overfitting / Underfitting

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/0af4bcfe034348ceaa05ca6b714ed1f8/optimized/Design-stats-bro.svg)

## Overfitting: El sobreajuste

#### ¿Qué es?

Ocurre cuando un modelo aprende demasiado bien los datos de entrenamiento, memorizando detalles específicos en lugar de patrones generales.

#### Síntomas

- Alta precisión en entrenamiento
- Baja precisión en prueba
- Modelo demasiado complejo

## Analogía del overfitting

#### Memorización sin comprensión

Como un estudiante que memoriza preguntas exactas del simulacro pero no entiende el tema.

#### Exceso de complejidad

El modelo crea demasiadas reglas y condiciones internas.

#### Falsa sensación de éxito

Funciona bien en pruebas internas pero falla en situaciones reales.

![](https://cdn.gamma.app/5k42ay5jcl12uau/8ebc286c54324072b064075d8a854476/optimized/Site-Stats-bro.svg)

## Underfitting: El subajuste

#### Modelo demasiado simple

No capta los patrones relevantes.

#### Entrenamiento insuficiente

No se le da suficiente tiempo para aprender.

#### Datos inadecuados

Mala representación o transformación de variables.

## Analogía del Underfitting

#### Comprensión básica

Como un estudiante que solo entendió lo básico y no puede resolver ejercicios.

#### Herramienta inadecuada

Intentar resolver un problema complejo con un modelo demasiado simple.

#### Patrones incompletos

El modelo no logra captar relaciones importantes en los datos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/4086b0007b534b50bf90ee24c0978fd0/optimized/software-tester-bro.svg)

## Detectando Overfitting y Underfitting

#### Sobreajuste (Overfitting)

Alta precisión en entrenamiento pero baja en prueba.

#### Subajuste (Underfitting)

Baja precisión tanto en entrenamiento como en prueba.

#### Generalización adecuada

Rendimiento razonablemente bueno en ambos conjuntos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/7d1a8d8cc69748c3abdb67aac6b5640a/optimized/Presentation-bro.svg)

## Previniendo el Underfitting

#### Algoritmos más complejos

Utilizar modelos con mayor capacidad expresiva.

#### Mejor selección de variables

Incluir características más relevantes para el problema.

#### Mayor tiempo de entrenamiento

Permitir más iteraciones para que el modelo aprenda.

#### Más datos

Proporcionar mayor cantidad de ejemplos para el aprendizaje.

## Previniendo el Overfitting

#### División correcta

Separar adecuadamente datos de entrenamiento y prueba.

#### Validación cruzada

Evaluar el modelo con diferentes particiones de datos.

#### Regularización

Penalizar modelos que se ajustan demasiado a los datos.

#### Reducción de variables

Eliminar columnas que no aportan valor o generan ruido.

![](https://cdn.gamma.app/5k42ay5jcl12uau/23b3aa077f224caab08476d3c1564e94/optimized/At-work-bro.svg)

## El punto de equilibrio

#### Generalización óptima

El modelo aprende patrones sin memorizar detalles irrelevantes.

#### Complejidad adecuada

Ni demasiado simple ni excesivamente complejo.

#### Representación correcta

Variables relevantes y bien transformadas.

## Validación cruzada

---

## Concepto

#### Dataset dividido

Se divide el dataset en varios fragmentos o "pliegues" y se entrena el modelo múltiples veces.

#### Evaluación repetida

La validación cruzada evalúa el modelo varias veces, utilizando diferentes particiones del conjunto de datos.

#### Uso eficiente de datos

Cada parte del dataset cumple el rol de "prueba" al menos una vez, aprovechando mejor los datos disponibles.

![](https://cdn.gamma.app/5k42ay5jcl12uau/8dbc701ce2d644b6879dd19dea850504/optimized/Duplicate-bro.svg)

## K-Fold Cross validation

#### División en K pliegues

Se divide el dataset en K partes iguales (generalmente 5 o 10).

#### Entrenamiento múltiple

Se entrenan K modelos, cada vez usando K-1 pliegues para entrenar y 1 para probar.

#### Promedio de resultados

Se calcula el rendimiento promedio de todas las evaluaciones.

## Ventajas de la validación cruzada

#### Uso completo del dataset

Permite usar todos los datos tanto para entrenamiento como para prueba.

#### Estimación más estable

Proporciona una medida más confiable del rendimiento del modelo.

#### Comparación justa

Ideal para comparar diferentes modelos de forma objetiva.

#### Útil con pocos datos

Especialmente valioso cuando el dataset es pequeño.

## Reflexión final

1

#### Evaluación correcta

Medir rigurosamente cuánto aprende un modelo.

2

#### Punto de equilibrio

Ni demasiado simple ni excesivamente complejo.

3

#### Generalización

Un buen modelo no solo aprende, sino que generaliza.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Entrenamiento

¿Qué consecuencias puede tener entrenar y evaluar un modelo con los mismos datos?

2

#### Overfitting y Underfitting

¿Qué ventajas tiene la validación cruzada respecto a una simple división entre entrenamiento y prueba?

3

#### Validación cruzada

¿Qué ventajas tiene la validación cruzada respecto a una simple división entre entrenamiento y prueba?

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

Cargá el Dataset del Titanic ([este mismo que venís utilizando en clases anteriores](https://drive.google.com/file/d/1PD0A9xtChEvgEtL4uEkwiJZ4KGaQSk5h/view?usp=drive_link)) y preparalo para el modelado, asegurándote de tratar los valores faltantes y seleccionar las variables que usarás como entrada y salida.

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

ML - CLASE 05