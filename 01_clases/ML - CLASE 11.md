---
title: "ML - CLASE 11"
source: "https://gamma.app/docs/ML-CLASE-11-bz8iazmp9n4hs3z?mode=doc"
author:
published:
created: 2026-11-22
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/b8c9c4c502ec4cfa951aef59524d58df/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 11 | Introducción al clustering

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

## Índice

---

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

Clase 12

#### Creación de pipelines

- Creación de pipelines en scikit-learn.
- Automatización del flujo completo.
- Introducción a GridSearchCV para optimización.

## Objetivos de la clase

Bienvenidos a nuestra clase sobre clustering, una poderosa técnica de aprendizaje no supervisado. Descubriremos cómo agrupar datos sin etiquetas previas.

---

1

#### Comprender el clustering

Entender qué es el agrupamiento y cómo se diferencia del aprendizaje supervisado.

2

#### Dominar K-Means

Aprender a utilizar este algoritmo para clasificar elementos en grupos según similitudes.

3

#### Evaluar resultados

Utilizar inercia y silhouette score para medir la calidad de los agrupamientos.

## Clustering

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/6f1c99d24a62455a945ca239678bdc31/optimized/Yes-or-no-bro.svg)

## Aprendizaje No Supervisado vs. Supervisado

#### Aprendizaje supervisado

- Utiliza datos etiquetados
- Predice valores o categorías
- Evalúa con métricas de error

#### Aprendizaje no supervisado

- Trabaja sin etiquetas
- Descubre patrones ocultos
- Evalúa con cohesión y separación

## ¿Qué es y dónde usamos el Clustering?

El **clustering** divide datos en grupos de elementos similares entre sí, sin necesidad de etiquetas previas.

#### Segmentación de clientes

Agrupar consumidores según comportamiento de compra.

#### Clasificación biológica

Agrupar especies según características genéticas.

#### Astronomía

Agrupar galaxias según propiedades físicas.

## K-Means

---

## Algoritmo K-Means

**K-Means** es una técnica que divide los datos en K grupos, minimizando la **varianza** dentro de cada cluster.

1

#### Selección de centroides

Se eligen K puntos aleatorios como centros iniciales de los clusters.

2

#### Asignación de puntos

Cada punto se asigna al centroide más cercano según distancia euclidiana.

3

#### Recálculo de centroides

Se actualizan los centroides como promedio de los puntos asignados.

4

#### Iteración

Se repiten los pasos 2 y 3 hasta que las asignaciones se estabilicen.

## Funcionamiento de K-Means

#### Inicialización

Selección aleatoria de K centroides iniciales

#### Asignación

Cada punto se asigna al centroide más cercano

#### Actualización

Recálculo de centroides como promedio de puntos

#### Convergencia

Repetir hasta estabilidad o máximo de iteraciones

![](https://cdn.gamma.app/5k42ay5jcl12uau/c678fdc0037c446d96a64485c1d7b825/optimized/Version-control-bro.svg)

## Ventajas de K-Means

#### Eficiencia

Rápido incluso con grandes conjuntos de datos.

#### Simplicidad

Fácil de entender e implementar.

#### Escalabili-dad

Funciona bien con muchas observaciones.

#### Interpretabilidad

Resultados claros y visualizables.

![](https://cdn.gamma.app/5k42ay5jcl12uau/f66631951d054650bf20f7ec2d15388d/optimized/No-data-bro.svg)

## Limitaciones de K-Means

#### Elección previa de K

Requiere definir el número de clusters antes de ejecutar el algoritmo.

#### Sensibilidad a valores atípicos

Los outliers pueden distorsionar significativamente los centroides.

#### Asume clusters esféricos

No maneja bien formas complejas o alargadas.

#### Dependencia de inicialización

Resultados pueden variar según los centroides iniciales.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:1200/https://cdn.gamma.app/5k42ay5jcl12uau/a1ebc4c268cc4319976147a6a91196ea/original/Captura-de-pantalla-de-2025-05-20-09-53-56.png)

## Evaluación del Clustering: inercia

#### ¿Qué es la inercia?

Suma de distancias cuadradas entre cada punto y el centroide de su cluster.

#### Compacidad

Mide la compacidad de los clusters: valores más bajos indican clusters más compactos.

#### Método del codo

El "método del codo" ayuda a identificar el número óptimo de clusters.

#### Optimización

La inercia siempre disminuye al aumentar K, por lo que buscamos el punto donde la mejora se estabiliza.

## Método del codo

1

#### Ejecutar K-Means con diferentes valores de K

Probar desde K=1 hasta un valor máximo razonable

2

#### Graficar inercia vs. K

Crear una curva que muestre cómo disminuye la inercia

3

#### Identificar el "codo"

Buscar el punto donde la curva se aplana significativamente

![](https://cdn.gamma.app/5k42ay5jcl12uau/e9a6d5946d2e42afba5feae4881f0474/optimized/Analyze-bro.svg)

## Evaluación del Clustering: Silhouette Score

#### ¿Qué es el silhouette score?

Mide qué tan similar es un punto a su propio cluster en comparación con otros clusters.

- Varía entre -1 y 1
- Valores cercanos a 1: buena asignación
- Valores cercanos a 0: punto en frontera
- Valores negativos: posible mala asignación

Un buen clustering muestra valores altos y consistentes de silhouette score.

## Inercia vs. Silhouette Score

#### Característica

#### Inercia

#### Silhouette Score

**Rango de valores**

0 a infinito (menor es mejor)

\-1 a 1 (mayor es mejor)

**Qué mide**

Compacidad interna

Separación y cohesión

**Uso principal**

Método del codo para elegir K

Validar calidad de clusters

**Limitaciones**

Siempre disminuye con más clusters

Puede ser engañoso con formas complejas

## Alternativas a K-Means

#### DBSCAN

Basado en densidad, detecta clusters de formas irregulares y filtra ruido.

#### Mean Shift

Busca máximos de densidad y determina automáticamente el número de clusters.

#### Modelos de mezcla Gaussiana

Asigna probabilidades de pertenencia a múltiples clusters.

## Clustering jerárquico

#### Agglomerative Clustering

Construye una jerarquía de clusters, fusionando grupos similares.

- Enfoque de abajo hacia arriba
- No requiere especificar K previamente
- Permite visualizar relaciones jerárquicas

El dendrograma muestra cómo se fusionan los clusters a diferentes niveles de similitud.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/274df078bb3d4013aba49313afaaab2f/original/image.png)

## Preparación de datos para Clustering

1

#### Selección de variables

Elegir características relevantes para el agrupamiento.

2

#### Limpieza de datos

Manejar valores faltantes y eliminar outliers extremos.

3

#### Estandarización

Normalizar variables para evitar que las escalas afecten los resultados.

4

#### Reducción de dimensionalidad

Opcional: aplicar PCA para visualizar datos de alta dimensión.

![](https://cdn.gamma.app/5k42ay5jcl12uau/5c91b5c220d449bbbe597a30efd5b7b5/optimized/Mathematics-bro.svg)

## Importancia de la estandarización

#### Sin estandarizar

Variables con rangos amplios dominan el cálculo de distancias.

Ejemplo: ingresos (miles) vs. edad (decenas) harían que el clustering se base principalmente en ingresos.

#### Con estandarización

Todas las variables contribuyen equitativamente.

Métodos comunes: Z-score (media 0, desviación estándar 1) o MinMaxScaler (rango 0-1).

## Interpretación de resultados

#### Análisis de perfiles

Examinar características distintivas de cada cluster mediante estadísticas descriptivas.

#### Visualización

Crear gráficos que muestren la distribución espacial de los clusters.

#### Validación de coherencia

Verificar que los grupos tengan sentido práctico y no solo matemático.

#### Aplicación práctica

Determinar cómo utilizar los clusters para tomar decisiones concretas.

![](https://cdn.gamma.app/5k42ay5jcl12uau/ffb8588b6ab743919cdf0c7f7fb7c664/optimized/Hospital-patient-bro.svg)

## Aplicaciones prácticas del Clustering

#### Marketing

- Segmentación de clientes
- Personalización de ofertas
- Análisis de comportamiento

#### Medicina

- Identificación de patrones en síntomas
- Agrupación de pacientes similares
- Descubrimiento de subtipos de enfermedades

#### Análisis de texto

- Agrupación de documentos similares
- Detección de temas
- Organización de información

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Aplicaciones sin etiquetas

¿En qué situaciones sería más útil aplicar clustering en lugar de un algoritmo supervisado?

2

#### Elección de K

¿Qué consecuencias podría tener elegir un valor incorrecto para "k"?

3

#### Estandarización

¿Por qué es importante normalizar los datos antes de aplicar K-Means?

4

#### Métricas de evaluación

¿Qué ventajas y desventajas tienen la inercia y el silhouette score?

## ⚙️Ejercicios prácticos

---

## ⚙️ Buscando el patrón oculto

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

Retomando el dataset del Titanic con el que venís trabajando, tu desafío será aplicar clustering con K-Means para explorar si es posible encontrar grupos ocultos de pasajeros y pasajeras con características similares.

## Ejercicio práctico

```
Obligatorio
```

Utilizá el dataset del Titanic y preparalo como hiciste en las clases anteriores. Luego, implementá estas etapas:

---

#### Selección de variables

Seleccioná un subconjunto de variables numéricas del dataset que te parezca útil para aplicar K-Means.

#### Estandarización

Recordá estandarizar las variables antes de entrenar el modelo.

#### K-Means

Aplicá K-Means con distintos valores de k (por ejemplo, entre 2 y 6) y evaluá los resultados utilizando la inercia y el silhouette score.

## Ejercicio práctico

```
Obligatorio
```

---

#### Visualización

Elegí el valor de k que te parezca más razonable y visualizá los clústeres resultantes (por ejemplo, con un *scatterplot* de dos variables).

#### Reflexión

Finalmente, reflexioná: ¿Los clústeres encontrados tienen algún sentido práctico? ¿Podés describir las características de cada grupo?.

Gamma