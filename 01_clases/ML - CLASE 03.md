---
title: "ML - CLASE 03"
source: "https://gamma.app/docs/ML-CLASE-03-t7ugudrt4zeuwrn?mode=doc"
author:
published:
created: 2026-09-30
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/7c2cc01ac62442a7b116a39a9402b3dd/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 03 | ¿Qué es Machine Learning?

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 02

#### Módulos y datos

- Repaso de Pandas, Matplotlib, Seaborn y Plotly.
- Revisión de EDA, limpieza y consolidación de datos.

Clase 03

#### ¿Qué es Machine Learning?

- Introducción al aprendizaje automático.
- Tipos de aprendizaje: supervisado y no supervisado.
- Ciclo de vida de un proyecto de ML.

Clase 04

#### Transformación de datos

- Feature engineering y selección de variables.
- Normalización y estandarización de datos.
- Codificación de variables categóricas.

## Objetivos de la clase

Bienvenidos a nuestra clase sobre Machine Learning. Hoy exploraremos los fundamentos del aprendizaje automático y su importancia en la ciencia de datos moderna.

---

1

#### Establecer base conceptual

Comprender qué es el Machine Learning y su rol en la ciencia de datos.

2

#### Diferenciar tipos de aprendizaje

Conocer las características del aprendizaje supervisado y no supervisado.

3

#### Entender el ciclo de vida

Familiarizarse con las etapas de un proyecto de ML completo.

## Machine Learning

---

## ¿Qué es Machine Learning?

El **Machine Learning** es una rama de la inteligencia artificial que permite a las computadoras aprender de los datos y **realizar predicciones** sin programación explícita.

A diferencia de la programación tradicional, los sistemas ML **ajustan su comportamiento automáticamente** basándose en datos históricos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/ab9db8cd43ef4c5aaaf2257896f19d8a/optimized/Data-extraction-bro.svg) ![](https://cdn.gamma.app/5k42ay5jcl12uau/1c16803ae6a34efdaf85e0f8c47cfea8/optimized/Version-control-bro.svg)

## Programación tradicional vs. ML

#### Programación tradicional

Reglas definidas manualmente por programadores.

#### Limitaciones

Reglas rígidas que no se adaptan a cambios.

#### Machine Learning

El sistema descubre automáticamente las reglas desde los datos.

## Capacidad de generalización

#### Datos de entrenamiento

El modelo aprende de ejemplos históricos.

#### Identificación de patrones

Descubre reglas y relaciones subyacentes.

#### Predicción con nuevos datos

Aplica lo aprendido a situaciones nunca vistas.

## Ventajas del Machine Learning

#### Manejo de grandes volúmenes

Procesa cantidades masivas de datos imposibles de revisar manualmente.

1

#### Descubre relaciones complejas

Identifica patrones no evidentes para el análisis humano.

#### Adaptabilidad

Se ajusta a medida que los datos evolucionan con el tiempo.

#### Mejora continua

Perfecciona sus predicciones con más datos de entrenamiento.

![](https://cdn.gamma.app/5k42ay5jcl12uau/2f51f2a21abd4986acac67cf12a25ff5/optimized/Analysis-bro-1.svg)

## Aplicaciones prácticas

1

#### Reducción de errores

En sistemas de detección de fraudes bancarios.

2

#### Aumento en ventas

Con sistemas de recomendación personalizados.

3

#### Ahorro de tiempo

En procesos de clasificación automática.

## Tipos de aprendizaje

---

## Tipos de aprendizaje

#### Aprendizaje supervisado

Utiliza datos etiquetados para entrenar modelos que predicen resultados específicos.

El modelo aprende la relación entre características y una variable objetivo conocida.

#### Aprendizaje no supervisado

Trabaja con datos sin etiquetar para descubrir patrones y estructuras ocultas.

No hay una variable objetivo predefinida. El sistema encuentra relaciones por sí mismo.

![](https://cdn.gamma.app/5k42ay5jcl12uau/b29a5573f6824cf48f1040b9cb9ecf5f/optimized/Visual-data-bro.svg)

## Aprendizaje supervisado

#### Datos etiquetados

Cada ejemplo tiene una respuesta conocida.

#### Entrenamiento del modelo

Aprende patrones entre características y etiquetas.

#### Predicción

Aplica lo aprendido a nuevos datos sin etiquetar.

## Tipos de problemas supervisados

#### Regresión

Predice valores continuos como precios, temperaturas o cantidades.

#### Clasificación

Asigna categorías como "spam/no spam" o "aprobado/rechazado".

#### Ranking

Ordena elementos según su relevancia o preferencia.

![](https://cdn.gamma.app/5k42ay5jcl12uau/b37604d53ff14325882c277e13321a1d/optimized/Analyze-bro.svg)

## Aprendizaje no supervisado

#### Datos sin etiquetar

Trabajamos con información que no tiene respuestas predefinidas.

#### Descubrimiento de patrones

El algoritmo identifica estructuras y agrupaciones naturales.

#### Interpretación de resultados

Los expertos analizan los grupos para extraer insights valiosos.

## Diferencias clave

#### Característica

#### Aprendizaje supervisado

#### Aprendizaje no supervisado

Datos de entrada

Etiquetados

Sin etiquetar

Objetivo

Predecir resultados

Descubrir patrones

Ejemplos

Regresión, clasificación

Clustering, reducción de dimensionalidad

Evaluación

Métricas precisas

Más subjetiva

## Ciclo de vida

---

## Recolección y comprensión

#### Fuentes diversas

Bases de datos, archivos CSV, APIs, registros históricos.

#### Contexto de los datos

Entender qué representan las variables y cómo fueron recolectadas.

#### Limitaciones y sesgos

Identificar posibles problemas en la recolección de datos.

## Análisis exploratorio (EDA)

#### Visualización

Gráficos y diagramas para detectar patrones y relaciones.

#### Limpieza

Detección y tratamiento de valores nulos y outliers.

#### Estadística descriptiva

Medidas de tendencia central y dispersión para cada variable.

## Preprocesamiento de datos

#### Codificación de variables

Transformar categorías en valores numéricos para los algoritmos.

#### Normalización

Ajustar escalas para que todas las variables tengan pesos similares.

#### Feature engineering

Crear nuevas variables que capturen mejor la información relevante.

#### División de datos

Separar en conjuntos de entrenamiento, validación y prueba.

## Selección y entrenamiento

#### Elección del algoritmo

Seleccionar el modelo adecuado según el tipo de problema y datos disponibles.

#### Ajuste de hiperparámetros

Configurar los parámetros del modelo para optimizar su rendimiento.

#### Entrenamiento

Alimentar el modelo con datos de entrenamiento para que aprenda patrones.

#### Validación cruzada

Evaluar el modelo con diferentes subconjuntos para evitar sobreajuste.

## Evaluación del modelo

#### Métricas para regresión

- Error Cuadrático Medio (MSE)
- Error Absoluto Medio (MAE)
- Coeficiente de determinación (R²)

#### Métricas para clasificación

- Precisión y Recall
- F1-Score
- Área bajo la curva ROC
- Matriz de confusión

![](https://cdn.gamma.app/5k42ay5jcl12uau/0bfbca725f454ebba76a6cdacac996b5/optimized/Data-analysis-bro.svg)

## Implementación y monitoreo

1

#### Desarrollo de API

Crear interfaces para que otros sistemas accedan al modelo.

2

#### Despliegue

Poner el modelo en producción para usuarios finales.

3

#### Monitoreo de rendimiento

Seguimiento continuo de métricas y detección de degradación.

4

#### Reentrenamiento

Actualizar el modelo con nuevos datos periódicamente.

![](https://cdn.gamma.app/5k42ay5jcl12uau/af2117273afe4061a67c6c1d33aa287f/optimized/Statistics-bro.svg)

## Mantenimiento y mejora

#### Optimización continua

Mejora constante del rendimiento y eficiencia.

#### Adaptación a cambios

Ajuste a nuevas condiciones del mercado o comportamientos.

#### Colaboración multidisciplinar

Trabajo conjunto entre científicos de datos e ingenieros.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Impacto empresarial

¿Cómo podría el ML mejorar procesos o decisiones en una empresa?

2

#### Tipos de aprendizaje

¿Qué diferencias hay entre aprendizaje supervisado y no supervisado?

3

#### Ciclo de vida

¿Por qué es importante entender el ciclo completo de un proyecto ML?

## ⚙️Ejercicios prácticos

---

## ⚙️Ejercicio práctico

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

**Talento Lab** está terminando de definir los alcances y el plan de trabajo para el proyecto del cliente de retail. Silvia ha solicitado a todo el equipo un ejercicio preparatorio para que puedan afianzar los conceptos de aprendizaje automático y empezar a pensar en cómo aplicarlos en el proyecto real.

## Ejercicio práctico

```
Obligatorio
```

---

#### Aprendizaje supervisado

Seleccioná un caso o problema mencionado (puede ser del sector retail, salud, finanzas, logística u otro) donde creas que el **aprendizaje supervisado** podría utilizarse para predecir o clasificar algo importante. Describí brevemente cuál sería la variable que el modelo debería predecir.

#### Aprendizaje no supervisado

Elegí también un ejemplo de situación donde un proyecto de **aprendizaje no supervisado** sería útil. Explicá qué tipo de agrupamiento o segmentación podría hacerse y cómo podría beneficiar a la organización.

## Temas

#### Finanzas

Predicción de incumplimiento de pagos: El banco pierde dinero cuando otorga préstamos a personas que luego no pueden pagar

#### Salud

Detección temprana de diabetes: La diabetes es una enfermedad silenciosa. Detectarla cuando ya hay síntomas graves complica el tratamiento.

#### Retail / E-Commerce

Predicción de fuga de clientes: Es mucho más costoso adquirir un cliente nuevo que retener a uno existente.

#### Real estate / inmobiliaria

Valoración de propiedades:Las tasaciones manuales son lentas y subjetivas. El mercado fluctúa rápidamente.

#### Logística

Estimación de tiempo de entrega: Las estimaciones actuales son promedios simples y suelen fallar en horas pico, generando frustración en el cliente.

## Ejercicio práctico

```
Obligatorio
```

---

#### Ciclo de vida

Finalmente, redactá de manera esquemática (en 5 o 6 pasos) cómo se aplicaría el ciclo de vida de un proyecto de Machine Learning para resolver alguno de los casos que seleccionaste.

ML - CLASE 03