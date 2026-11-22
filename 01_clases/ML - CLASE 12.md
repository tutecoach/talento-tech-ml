---
title: "ML - CLASE 12"
source: "https://gamma.app/docs/ML-CLASE-12-9yqwzf9m86fs3f7?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/b2e8eb73ab95481693ad99d9c8d147b3/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 12 | Creación de pipelines

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

Clase 11

#### Introducción al clustering

- Introducción al clustering.
- Algoritmo K-Means: teoría y aplicación.
- Evaluación de clustering: inercia y silhouette score.

Clase 12

#### Creación de pipelines

- Creación de pipelines en scikit-learn.
- Automatización del flujo completo.
- Introducción a GridSearchCV para optimización.

Clase 13

#### Comparativa y evaluación de modelos

- Comparativa y evaluación de modelos.
- Selección del mejor modelo según métricas.

## Objetivos de la clase

En esta clase vamos a dar un paso fundamental hacia la organización y profesionalización de nuestros modelos. Aprenderemos a automatizar flujos de trabajo y optimizar modelos de machine learning.

---

1

#### Integración

Aprender a integrar múltiples etapas de procesamiento en un único bloque reproducible.

2

#### Automatización

Construir pipelines que encadenen transformación de datos y entrenamiento de modelos.

3

#### Optimización

Introducir GridSearchCV para probar múltiples combinaciones de hiperparámetros automáticamente.

## Pipelines y automatización

---

## ¿Qué es un pipeline?

Un pipeline es una herramienta que encadena todas las etapas del flujo de trabajo en un solo objeto, de forma ordenada y reutilizable.

Funciona como una línea de producción para nuestros modelos de machine learning.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/df298f7f70df4ff5ac24fb2e08de7f60/original/AD_4nXcz9FoSlmWnZQmK4YRSVse2Q2-qXh_uu35Y9LPv9UEMonq9wKwltUFzmfTbaN68C4YmCVGTn2JRo-hmmzd2JjvAdquhpACR_mOqXgeXS43BE_J9YfkklmH85q8XOtW7IdtgL9ycgmZGO_NDAM7726g.png)

## Beneficios de los pipelines

#### Consistencia

Garantiza que los pasos se ejecuten siempre en el mismo orden.

#### Reproducibilidad

Facilita replicar el mismo proceso con diferentes datos.

#### Prevención de errores

Evita problemas como data leakage o transformaciones inconsistentes.

#### Compartible

Permite compartir todo el flujo de trabajo fácilmente.

![](https://cdn.gamma.app/5k42ay5jcl12uau/e90e6250430a4fe8af8294f0877ad5ab/optimized/Manufacturing-Process-bro.svg)

## Analogía: La cinta transportadora

#### Datos crudos

Entran por un extremo del pipeline.

#### Transformaciones

Pasan por estaciones de procesamiento.

#### Modelo

Se entrena con los datos transformados.

#### Predicciones

Salen por el otro extremo.

## Estructura de un pipeline en scikit-learn

#### Pipeline completo

Objeto que encadena todos los pasos

#### Lista de pasos

Secuencia ordenada de transformaciones y modelo

#### Pasos individuales

Cada paso tiene un nombre y una función asociada

![](https://cdn.gamma.app/5k42ay5jcl12uau/d5cd712235fb4453b80ae2e0abc680c2/optimized/Collaboration-bro.svg)

## Componentes de un pipeline

1

#### Transformadores

Procesan y modifican los datos (StandardScaler, OneHotEncoder, etc.)

2

#### Transformadores personalizados

Creados para necesidades específicas del proyecto

3

#### Estimador final

El modelo de machine learning (LogisticRegression, RandomForest, etc.)

## Automatización del flujo completo

#### Consistencia garantizada

Mismo procesamiento para entrenamiento y prueba

#### Reproducibilidad mejorada

Fácil de aplicar a nuevos conjuntos de datos

#### Prevención de data leakage

Transformaciones aplicadas en el orden correcto

![](https://cdn.gamma.app/5k42ay5jcl12uau/054350d4834247f984e88f58ee9dca37/optimized/Data-extraction-bro.svg)

## Ventajas de la automatización

#### Ahorro de tiempo

Elimina la necesidad de repetir manualmente cada paso del proceso.

#### Reducción de errores

Minimiza errores humanos en la aplicación de transformaciones.

#### Integración con otras herramientas

Compatible con validación cruzada y búsqueda de hiperparámetros.

#### Colaboración facilitada

Código más limpio y fácil de compartir con el equipo.

## Ejemplo de flujo automatizado

#### Datos de entrada

Conjunto de datos sin procesar

#### Limpieza

Manejo de valores faltantes

#### Transformación

Escalado y codificación

#### Entrenamiento

Ajuste del modelo

#### Evaluación

Métricas de rendimiento

## GridSearchCV

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/e5254b87beb64455bacc277b7fb4e393/optimized/Analyze-bro.svg)

## Introducción a GridSearchCV

#### ¿Qué es?

Una herramienta para buscar sistemáticamente la mejor combinación de hiperparámetros para un modelo.

Evalúa todas las combinaciones posibles de los valores especificados mediante validación cruzada.

## Funcionamiento de GridSearchCV

#### Definir el espacio de búsqueda

Especificar los hiperparámetros y sus posibles valores a probar.

#### Aplicar validación cruzada

Cada combinación se evalúa con k-fold cross-validation.

#### Seleccionar el mejor modelo

Se identifica la combinación con mejor rendimiento promedio.

#### Reentrenar con los mejores parámetros

El modelo final utiliza la configuración óptima encontrada.

## Hiperparámetros vs. Parámetros

#### Hiperparámetros

- Configurados antes del entrenamiento
- No se aprenden de los datos
- Ejemplos: C en LogisticRegression, max\_depth en DecisionTree

#### Parámetros

- Aprendidos durante el entrenamiento
- Derivados de los datos
- Ejemplos: coeficientes, pesos, umbrales

#### Optimización

- GridSearchCV optimiza hiperparámetros
- El algoritmo optimiza parámetros
- Ambos afectan el rendimiento final

## Integración de pipeline y GridSearchCV

#### Pipeline estructurado

Organiza el flujo de trabajo en pasos secuenciales.

#### GridSearchCV aplicado

Busca los mejores hiperparámetros para todo el pipeline.

#### Validación cruzada

Evalúa cada combinación con múltiples particiones.

#### Modelo optimizado

Resultado final con la mejor configuración encontrada.

![](https://cdn.gamma.app/5k42ay5jcl12uau/8ec5ae0ac3264bc08c696c77bd698082/optimized/Binary-code-bro.svg)

## Ventajas de GridSearchCV

#### Automati-zación

Prueba múltiples configuraciones sin intervención manual.

#### Objetividad

Evita el sesgo de seleccionar hiperparámetros "a ojo".

#### Rendimiento

Mejora los resultados del modelo de forma sistemática.

#### Integración

Funciona perfectamente con pipelines existentes.

## Prevención de errores comunes

#### Data leakage

Cuando información del conjunto de prueba "contamina" el entrenamiento.

#### Transformaciones inconsistentes

Aplicar diferentes transformaciones a entrenamiento y prueba.

#### Overfitting en la búsqueda

Probar demasiados hiperparámetros puede llevar a sobreajuste.

#### Tiempos excesivos

Búsquedas demasiado exhaustivas pueden ser computacionalmente costosas.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Ventajas de pipelines

¿Qué beneficios ofrecen frente a ejecutar cada paso por separado? ¿Qué problemas ayudan a evitar?

2

#### Riesgos de no automatizar

¿Qué errores podemos cometer si no automatizamos correctamente el flujo de trabajo?

3

#### Uso de GridSearchCV

¿Cuándo tiene sentido usar GridSearchCV y cuándo es mejor usar valores por defecto?

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

## Ejercicio Práctico

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

## 📄¡Nuevo cuestionario en Campus!

> [!note] Note
> No olvides que los cuestionarios son de carácter obligatorio para poder avanzar con la cursada.

Gamma