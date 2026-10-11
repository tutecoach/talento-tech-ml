---
title: "ML - CLASE 04"
source: "https://gamma.app/docs/ML-CLASE-04-guzl3h7jozg8c9d?mode=doc"
author:
published:
created: 2026-09-30
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/ce8df580e51640ce9fc67a8cdb008d5c/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 04 | Transformación de datos

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

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

Clase 05

#### División y validación del dataset

- División en conjuntos de entrenamiento y prueba.
- Conceptos de overfitting y underfitting.
- Introducción a la validación cruzada.

## Objetivos de la clase

Comenzaremos a trabajar sobre la transformación de variables, tanto categóricas como numéricas, aplicando técnicas como la codificación, la normalización y la estandarización. También introduciremos el concepto de ingeniería de características, entendiendo su importancia en la construcción de modelos efectivos.

---

1

#### Feature Engineering

Aprenderemos a crear, seleccionar y transformar características para mejorar el rendimiento del modelo.

2

#### Codificación de variables

Transformaremos variables categóricas en formatos numéricos que los algoritmos puedan procesar.

3

#### Normalización y estandarización

Aplicaremos técnicas para escalar variables numéricas y mejorar el rendimiento de los modelos.

## Preparación de datos

---

## Importancia de la preparación de datos

#### Datos crudos

Información sin procesar, con múltiples formatos y escalas

#### Transformación

Conversión a formatos adecuados para algoritmos

#### Modelo efectivo

Mayor capacidad de generalización y precisión

Una vez que los datos han sido explorados, limpiados y comprendidos en profundidad, comienza una etapa crítica en todo proyecto de aprendizaje automático: prepararlos para el modelo. Esta fase no suele ser visible en los resultados finales, pero es decisiva para que el algoritmo pueda aprender correctamente.

## El proceso de transformación

#### Datos crudos

Información original sin procesar

#### Transformación

Codificación, escalado y selección

#### Datos preparados

Listos para alimentar algoritmos

#### Modelo entrenado

Capaz de generar predicciones precisas

Los algoritmos de Machine Learning no trabajan directamente con datos "crudos". Requieren información organizada, cuantificable y libre de ambigüedades. Por eso, necesitamos transformar nuestros datos a un formato adecuado para que puedan ser interpretados y procesados sin errores.

![](https://cdn.gamma.app/5k42ay5jcl12uau/399fcbe2180e4e11b380991c7612b61e/optimized/Consulting-bro.svg)

## ¿Por qué transformar los datos?

#### Compatibilidad con algoritmos

Los modelos de machine learning requieren entradas numéricas y en formatos específicos para poder procesarlas correctamente.

#### Mejora del rendimiento

Datos bien transformados permiten que los algoritmos converjan más rápido y encuentren patrones más precisos.

#### Eliminación de sesgos

Escalando variables numéricas evitamos que aquellas con valores más grandes dominen injustamente el modelo.

Esta etapa incluye tareas como convertir texto en números, escalar valores que están en diferentes magnitudes, identificar y tratar valores extremos, y repensar qué variables son verdaderamente útiles para la tarea que queremos resolver.

## Feature engineering

---

## Introducción a Feature Engineering

#### Creación

Generar nuevas variables a partir de las existentes

#### Selección

Elegir las variables más relevantes

#### Transformación

Modificar variables para mejorar su utilidad

#### Eliminación

Descartar variables redundantes o irrelevantes

Una de las claves del éxito en cualquier proyecto de Machine Learning no está únicamente en elegir el algoritmo adecuado, sino en cómo representamos los datos que le damos al modelo. Esta tarea se conoce como **ingeniería de características, o feature engineering.**

## ¿Qué es una Feature?

#### Definición

Una **feature** es una columna o variable del conjunto de datos que contiene información relevante para el modelo. Cada fila (o instancia) representa un caso particular —por ejemplo, una compra, un cliente o un producto— y las columnas son las características que describen ese caso.

#### Ejemplos

- Precio de un producto
- Fecha de una transacción
- Categoría de un artículo
- Ubicación geográfica
- Edad de un cliente
- Método de pago utilizado

El **feature engineering consiste en crear, seleccionar, transformar o eliminar características** con el objetivo de mejorar el rendimiento del modelo. Es una combinación de intuición, análisis, experiencia con los datos y conocimiento del dominio del problema.

![](https://cdn.gamma.app/5k42ay5jcl12uau/b5da1e4d011d4ce7a92e3c89c5a6adf2/optimized/Analysis-bro-1.svg)

## Ejemplos de Feature Engineering

#### Extracción temporal

En lugar de usar la fecha completa, podríamos extraer el mes o el día de la semana, si creemos que la demanda varía según la estacionalidad.

#### Codificación de categorías

Si tenemos una columna con "tipo de envío", podríamos transformarla en variables numéricas para que el modelo la interprete.

#### Variables derivadas

Podríamos crear una nueva variable calculando el margen de ganancia a partir del precio de venta y el costo, si esa relación es importante.

## Variables categóricas

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/70e4d8b6af3140bd92a9a953c72f041f/optimized/Data-analysis-bro.svg)

## Variables categóricas: Un desafío

#### Variables nominales

No tienen un orden específico entre sus valores. Ejemplos: colores (rojo, azul, verde), ciudades, marcas de productos o géneros musicales.

#### Variables ordinales

Representan una **jerarquía** o un **orden** específico. Ejemplos: niveles educativos, categorías de satisfacción (bajo, medio, alto) o tallas de ropa (S, M, L, XL).

#### El problema

Los algoritmos de Machine Learning no son buenos para trabajar directamente con texto. Necesitan entradas numéricas, por lo que debemos transformar esas categorías en números.

## Label Encoding: Transformación ordinal

#### Categoría original

Masculino

Femenino

Otro

#### Valor codificado

0

1

2

**Label Encoding consiste en asignar a cada categoría un número entero**. Es una técnica sencilla y rápida, pero solo debe usarse cuando hay un orden lógico entre las categorías, como en una variable ordinal.

Si usamos Label Encoding con variables nominales, el modelo podría interpretar que hay una jerarquía donde no la hay, lo que generaría errores. Por ejemplo, podría asumir que "Masculino" (0) es "menor" que "Femenino" (1).

## One-Hot Encoding: transformación nominal

#### Color Original

#### Rojo

#### Azul

#### Verde

Rojo

1

0

0

Azul

0

1

0

Verde

0

0

1

Esta técnica crea una nueva columna para cada categoría, con valores binarios (0 o 1) que indican si ese registro pertenece o no a la categoría. Este método es más seguro cuando trabajamos con variables nominales, ya que no introduce ningún orden implícito entre categorías.

## Comparación de técnicas de codificación

#### Label Encoding

**Ventajas:**

- Simple y rápido de implementar
- No aumenta la dimensionalidad
- Ideal para variables ordinales

**Desventajas:**

- Introduce orden artificial en variables nominales
- Puede confundir al modelo con relaciones inexistentes

#### One-Hot Encoding

**Ventajas:**

- No introduce jerarquías artificiales
- Representa fielmente variables nominales
- Funciona bien con la mayoría de algoritmos

**Desventajas:**

- Aumenta significativamente la dimensionalidad
- Puede generar matrices dispersas
- Problemático con categorías con muchos valores

## Variables numéricas y el problema de la escala

100.000

#### Precio máximo

Rango de la variable "Precio"

50

#### Cantidad máxima

Rango de la variable "Cantidad"

1

#### Descuento máximo

Rango de la variable "Descuento"

Estas diferencias de escala pueden afectar negativamente el rendimiento de algunos modelos, ya que ciertas variables numéricamente más grandes pueden "dominar" al resto, incluso si no son más importantes en términos predictivos.

Para solucionar este problema usamos técnicas de escalado de variables que permiten que todas las características contribuyan de manera equilibrada al modelo.

## Normalización y Estandarización

---

## Normalización (Min-Max Scaling)

#### La Fórmula

X\_normalizado = (X - Xmínimo) / (Xmáximo - Xmínimo)

Esto asegura que el valor más bajo de la variable se convierta en 0 y el más alto en 1, y que todos los demás valores queden proporcionalmente en ese rango.

#### Aplicación

Es especialmente útil cuando sabemos que los datos tienen un rango acotado y vamos a utilizar modelos basados en distancias, como K-Nearest Neighbors o K-Means.

#### Beneficios

Mejora el rendimiento de algoritmos sensibles a la escala, acelera la convergencia durante el entrenamiento y facilita la comparación entre diferentes variables.

## Estandarización (Z-score Scaling)

#### La fórmula

X\_estandarizado = (X - media) / desviación estándar

Esto significa que, tras la transformación, la mayoría de los valores estarán entre -2 y 2, y los valores extremos estarán más alejados, pero con una distribución centrada.

#### Aplicación

Es más adecuada cuando los datos no tienen un rango fijo y se usarán modelos que asumen una distribución normal (como regresión logística, SVM o redes neuronales).

#### Beneficios

Reduce el impacto de valores extremos, mejora la convergencia de algoritmos que asumen normalidad y facilita la interpretación estadística de los datos.

## ¿Qué técnica de escalado elegir?

#### Normalización (Min-Max)

- Cuando necesitamos valores acotados entre 0 y 1
- Para algoritmos basados en distancias (KNN, K-Means)
- Cuando la distribución no es gaussiana
- Para redes neuronales con funciones sigmoides

#### Estandarización (Z-score)

- Cuando hay valores atípicos significativos
- Para algoritmos que asumen normalidad
- Para regresión logística y SVM
- Cuando queremos preservar la forma de la distribución

#### Sin escalado

- Para árboles de decisión
- Para Random Forest
- Para Gradient Boosting
- Cuando la escala original tiene significado relevante

![](https://cdn.gamma.app/5k42ay5jcl12uau/8dcf4dd6895842f4883452007a7d135b/optimized/Analyze-bro.svg)

## Detección de outliers (valores atípicos)

#### Visualización

Los gráficos como boxplots, histogramas o diagramas de dispersión permiten identificar visualmente valores que se alejan significativamente del comportamiento general de los datos.

#### Métodos estadísticos

Se puede considerar outlier a todo dato que se encuentre a más de tres desviaciones estándar de la media, o utilizar el rango intercuartílico para establecer límites razonables.

#### Detección automática

Existen métodos automáticos y más complejos que se utilizan cuando se trabaja con grandes volúmenes de datos o sistemas en tiempo real.

## Causas de los outliers

#### Errores de medición

Fallos en sensores, instrumentos o sistemas de registro que producen valores incorrectos.

#### Errores humanos

Equivocaciones al introducir datos manualmente, como confundir unidades o posiciones decimales.

#### Variabilidad natural

Fenómenos reales pero inusuales que ocurren raramente en la población estudiada.

#### Cambios en el proceso

Alteraciones en el sistema que generan datos que se desvían del comportamiento habitual.

4

## Tratamiento de outliers

#### Identificación

Utilizar métodos visuales y estadísticos para detectar valores atípicos en el conjunto de datos.

#### Análisis

Investigar el origen de los outliers para determinar si son errores o valores legítimos pero inusuales.

#### Decisión

Elegir la estrategia más adecuada: eliminar, corregir, transformar o mantener los valores atípicos.

#### Implementación

Aplicar la estrategia seleccionada y documentar las acciones realizadas para garantizar la transparencia del proceso.

## Estrategias para manejar Outliers

#### Eliminación

Eliminar completamente los registros que contienen valores atípicos. Apropiado cuando son claramente errores o cuando representan un porcentaje muy pequeño de los datos.

#### Corrección

Modificar los valores atípicos si se puede determinar el valor correcto. Útil cuando se identifican errores específicos como errores de digitación o unidades incorrectas.

#### Truncamiento

Limitar los valores extremos a un umbral máximo o mínimo razonable. Adecuado cuando los outliers son legítimos pero su magnitud distorsiona el análisis.

#### Transformación

Aplicar funciones matemáticas como logaritmos para reducir el impacto de valores extremos sin eliminarlos. Útil para distribuciones muy sesgadas.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Necesidad de transformación

¿Por qué es necesario transformar los datos antes de entrenar un modelo de Machine Learning? ¿Qué problemas podría generar no hacerlo?

2

#### Impacto de la escala

¿Cómo influye la escala de las variables numéricas en el comportamiento de los modelos? ¿Qué técnicas existen para resolver posibles desbalances?

3

#### Gestión de outliers

Frente a la presencia de valores atípicos en un dataset, ¿qué criterios utilizarías para decidir si conservarlos, corregirlos o eliminarlos?

4

#### Elección de codificación

¿Qué consecuencias podría tener una elección incorrecta?

## ⚙️Ejercicios prácticos

---

## ⚙️Trabajamos con datos en TechLab.

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

El equipo de **Talento Lab** se dividió tareas para preparar el conjunto de datos recibido por el cliente.

Ahora es tu turno: como parte del equipo, te corresponde aplicar algunas de las transformaciones fundamentales que permitirán que el modelo pueda ser entrenado en etapas futuras. No se trata solo de aplicar técnicas: se trata de tomar decisiones informadas, documentar tus elecciones y justificar por qué cada transformación es necesaria.

## Ejercicio práctico

```
Obligatorio
```

Utilizando el dataset titanic (lo podes encontrar [**ACA**](https://drive.google.com/file/d/1NGiCEP8_2hILAC8nOQvC_UZlYzgenv0f/view?usp=drive_link)) o utilizando un dataset rea desde Kaggle, realizá las siguientes tareas dentro de un cuaderno Jupyter (Google Colab):

---

1

#### Identificá

Identificá variables categóricas y numéricas dentro del dataset. Analizá si alguna columna con texto puede codificarse y con qué técnica.

2

#### Aplicá técnicas

Aplicá técnicas de codificación sobre al menos dos variables categóricas. Justificá tu elección explicando por qué usaste cada técnica.

3

#### Escalá

O estandarizá al menos dos variables numéricas. Indicá qué técnica usaste en cada caso (Min-Max o Z-score) y por qué.

4

#### Buscá Outliers

Usá un gráfico (boxplot, histograma o scatterplot) para visualizarlos y explicá qué decisión tomarías: ¿los conservarías, los eliminarías o aplicarías alguna transformación?

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5yq1ea3085dnxt6/8068a888885a47b69a684f5c6d17c2bd/original/advertencia.png)

## 📄¡Nuevo cuestionario en Campus!

> [!note] Note
> No olvides que los cuestionarios son de carácter obligatorio para poder avanzar con la cursada.

ML - CLASE 04