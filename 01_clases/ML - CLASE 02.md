---
title: "ML - CLASE 02"
source: "https://gamma.app/docs/ML-CLASE-02-zojufetn8ifd79b?mode=doc"
author:
published:
created: 2026-09-30
description: "Made with Gamma. A new medium for presenting ideas, powered by AI."
tags:
  - "clippings"
---
![](https://cdn.gamma.app/5k42ay5jcl12uau/dcb081424699475893564dde509f9c5d/optimized/Metrics-bro.svg) ![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/f389ba4ff1684e7fb4c912ea7df0011b/original/Mesa-de-trabajo-73-1.png)

## Machine LEARNING

---

### Clase 02 | Módulos y datos

## ¡Les damos la bienvenida! 🚀

🎥 **Vamos a comenzar a grabar la clase.**

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5yq1ea3085dnxt6/8068a888885a47b69a684f5c6d17c2bd/original/advertencia.png)

## ¿Ya viste la “Introducción al programa" disponible en el campus virtual?

> [!note] Note
> La visualización y resolución de un breve cuestionario es de carácter obligatorio para desbloquear los contenidos de las primeras 2 clases

## Índice

---

Clase 01

#### Conceptos básicos

- Presentación del curso y objetivos generales.
- Introducción a Google Colab y Kaggle.
- Revisión de formatos de datasets (CSV, Excel, etc.).

Clase 02

#### Módulos y datos

- Repaso de Pandas, Matplotlib, Seaborn y Plotly.
- Revisión de EDA, limpieza y consolidación de datos.

Clase 03

#### ¿Qué es Machine Learning?

- Introducción al aprendizaje automático.
- Tipos de aprendizaje: supervisado y no supervisado.
- Ciclo de vida de un proyecto de ML.

## Objetivos de la clase

Retomaremos librerías fundamentales como Pandas, Matplotlib, Seaborn y Plotly para consolidar las habilidades necesarias en la manipulación, limpieza y visualización de datos. Además, revisaremos las principales técnicas de Análisis Exploratorio de Datos (EDA), limpieza y consolidación de datasets.

---

1

#### Repaso de herramientas

Reforzaremos el uso de Pandas, Matplotlib, Seaborn y Plotly.

2

#### Análisis exploratorio

Revisaremos técnicas de EDA para entender nuestros datos.

3

#### Limpieza de datos

Aprenderemos a preparar datos para análisis efectivos.

4

#### Consolidación

Integraremos datos de múltiples fuentes de manera coherente.

## Pandas

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/07e2a9daf71c46c9bb2f0490983043c0/optimized/Design-stats-bro.svg)

## Pandas: La herramienta fundamental

#### Origen

Creada por Wes McKinney en 2008 para facilitar la manipulación de datos financieros.

#### Propósito

Ofrece herramientas eficientes para trabajar con datos tabulares similares a hojas de cálculo.

#### Integración

Se combina perfectamente con NumPy, Matplotlib, Seaborn y scikit-learn.

## Características principales de Pandas

#### Versatilidad en fuentes

Lee y escribe datos desde CSV, Excel, SQL, JSON y archivos de texto.

#### Estructuras de datos

Utiliza Series (vectores unidimensionales) y DataFrames (tablas bidimensionales).

#### Manipulación eficiente

Permite filtrar, ordenar, agrupar y transformar datos fácilmente.

#### Análisis estadístico

Genera estadísticas descriptivas y maneja datos faltantes con facilidad.

## Matplotlib

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/3f50a7871a8a4acf9540b7d5404e5989/optimized/Data-analysis-bro.svg)

## Matplotlib: Visualización clásica

#### Origen

Desarrollada por John D. Hunter en 2003 como alternativa a MATLAB.

#### Gráficos estáticos

Crea visualizaciones personalizables y de alta calidad.

#### Flexibilidad

Permite ajustar todos los elementos visuales según necesidades.

#### Exportación

Guarda gráficos en múltiples formatos como PNG, PDF o SVG.

## Capacidades básicas de Matplotlib

#### Tipos de gráficos

Matplotlib ofrece gráficos diversos: líneas para series temporales, barras para categorías, dispersión para relaciones entre variables e histogramas para distribuciones.

#### Opciones de personalización

Permite personalización completa de colores, estilos y leyendas. Soporta múltiples sistemas de coordenadas y proyecciones geoespaciales.

#### Funcionalidades avanzadas

Soporta subplots, visualizaciones 3D y animaciones temporales.

#### Integración con otras herramientas

Se integra perfectamente con interfaces gráficas y notebooks Jupyter, convirtiéndola en una herramienta esencial para cualquier proyecto de visualización de datos.

## Seaborn

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/3db52a2829374e8389c50c44050abad9/optimized/Digital-presentation-bro.svg)

## Seaborn: Elegancia y simplicidad

#### ¿Qué es Seaborn?

Es una librería construida sobre **Matplotlib** que ofrece sintaxis más simple y estética mejorada.

#### Origen y desarrollo

Desarrollada por Michael Waskom para facilitar la exploración y visualización estadística.

#### Ventajas principales

**Seaborn** simplifica la creación de visualizaciones estadísticas complejas con menos código y mejor estética predeterminada.

## Características destacadas de Seaborn

#### Gráficos estadísticos

Facilita la creación de regplots, boxplots, violinplots y gráficos de barras categóricas.

#### Integración con Pandas

Genera visualizaciones directamente desde DataFrames con mínimo código.

#### Visualizaciones complejas

Simplifica la creación de heatmaps y pairplots para análisis multivariable.

#### Estilo profesional

Aplica automáticamente paletas de colores coherentes y etiquetas legibles.

## Plotly

---

![](https://cdn.gamma.app/5k42ay5jcl12uau/e2523359e64c4ce18e726abde29b1abf/optimized/Analytics-bro.svg)

## Plotly: Visualización interactiva

#### ¿Qué ofrece Plotly?

Permite al usuario hacer zoom, desplazar y explorar los datos.

#### Aplicaciones en el entorno profesional

Ideal para mostrar resultados a clientes sin conocimientos técnicos.

#### Integración con plataformas de desarrollo

Funciona perfectamente con Google Colab y Jupyter Notebooks.

![](https://cdn.gamma.app/5k42ay5jcl12uau/bd07e2d4ca10405680064befbd1cfb40/optimized/Financial-data-bro.svg)

## Capacidades de Plotly

#### Gráficos básicos interactivos

Líneas, barras y dispersión con información al pasar el cursor.

#### Visualizaciones avanzadas

Gráficos 3D y mapas geográficos para análisis complejos.

#### Integración web

Exporta gráficos en HTML para incluirlos en páginas web.

## Análisis exploratorio

---

## Análisis exploratorio de datos (EDA)

#### Descubrimiento

Identificación de patrones y relaciones entre variables

#### Exploración

Análisis de distribuciones y correlaciones

#### Detección

Identificación de anomalías y valores atípicos

#### Validación

Verificación de la calidad de los datos

![](https://cdn.gamma.app/5k42ay5jcl12uau/31ac1fa118e944a783f92fda0c8fdab9/optimized/Information-tab-bro.svg)

## Componentes del EDA

#### Estadísticas descriptivas

Cálculo de media, mediana y desviación estándar para entender variables.

#### Visualizaciones básicas

Creación de histogramas, diagramas de caja y gráficos de dispersión.

#### Análisis de correlación

Uso de mapas de calor para identificar relaciones entre variables.

#### Detección de outliers

Identificación de valores atípicos que pueden afectar el análisis.

## Mejores prácticas en EDA

1

#### Comenzar con preguntas claras

Definir objetivos específicos antes de iniciar la exploración de datos.

2

#### Visualizar temprano y con frecuencia

Crear gráficos desde el inicio para detectar patrones no evidentes.

3

#### Documentar hallazgos

Registrar observaciones, decisiones y transformaciones realizadas.

4

#### Iterar y profundizar

Refinar el análisis basándose en descubrimientos iniciales.

## Limpieza de datos

---

## Limpieza de datos

#### Identificación

Detectar problemas como valores nulos, duplicados o incorrectos.

#### Eliminación

Quitar registros irrelevantes o duplicados que afectan el análisis.

#### Transformación

Convertir formatos y tipos de datos para asegurar consistencia.

#### Imputación

Reemplazar valores faltantes con estimaciones razonables.

![](https://cdn.gamma.app/5k42ay5jcl12uau/8cef824f0700417f8f5281b63a436678/optimized/Analyze-bro.svg)

## Problemas comunes en datos reales

#### Valores nulos

Campos vacíos que requieren imputación o eliminación según su importancia.

#### Inconsistencias

Formatos diferentes para el mismo tipo de información (fechas, nombres).

#### Duplicados

Registros repetidos que pueden distorsionar análisis y resultados.

#### Outliers

Valores extremos que pueden representar errores o casos especiales.

![](https://cdn.gamma.app/5k42ay5jcl12uau/c0439c60935f40d1a3c2136e546bb7d1/optimized/Development-bro.svg)

## Estrategias de limpieza

#### Filtrado

Eliminar registros problemáticos.

#### Imputación

Reemplazar con media, mediana o moda.

#### Transformación

Convertir tipos y formatos de datos.

#### Validación

Verificar resultados tras la limpieza.

## Consolidación de datos

---

## Consolidación de datos

#### Identificación de fuentes

Localizar todos los orígenes de datos relevantes para el análisis.

#### Homogeneización

Unificar formatos, nombres de columnas y estructuras entre fuentes.

#### Integración

Combinar datos de múltiples fuentes en un único conjunto coherente.

#### Verificación

Comprobar la integridad y consistencia del conjunto consolidado.

![](https://cdn.gamma.app/5k42ay5jcl12uau/9b8e1d60e2ac4a9ab665a6c7b808cbb0/optimized/Consulting-bro.svg)

## Beneficios de la consolidación

#### Visión unificada

Una única "versión de la verdad" para todos los análisis.

#### Eficiencia

Reducción del tiempo de procesamiento y análisis.

#### Consistencia

Eliminación de contradicciones entre fuentes de datos.

#### Calidad

Mejora en la fiabilidad de los resultados analíticos.

![](https://cdn.gamma.app/5k42ay5jcl12uau/0f767fc3ac2b45639f0a3ca5e4babd07/optimized/Report-bro.svg)

## Análisis de correlación

#### Correlaciones fuertes

El gasto en marketing y el tráfico de clientes muestran alta correlación positiva con las ventas.

#### Correlaciones moderadas

La estacionalidad tiene un impacto medio en las ventas de ciertos productos.

#### Correlaciones débiles

El precio muestra correlación negativa débil con el volumen de ventas en algunas categorías.

## Optimización del flujo de trabajo

#### Importación

Carga eficiente de datos desde múltiples fuentes.

#### Limpieza

Corrección de problemas y estandarización.

#### Exploración

Análisis visual y estadístico para entender patrones.

#### Transformación

Creación de nuevas variables y preparación para análisis.

![](https://cdn.gamma.app/5k42ay5jcl12uau/1db8d6a07d2b47f0ac5af1f0577f22e8/optimized/Thinking-face-bro.svg)

## Preguntas para reflexionar

---

1

#### Análisis exploratorio de datos (EDA)

¿Por qué creés que el EDA es una etapa crítica antes de aplicar modelos de Machine Learning?

2

#### Consolidación de datos

¿Qué riesgos podrías enfrentar si trabajás con datos que no han sido correctamente limpiados o consolidados?

3

#### Pandas

¿Qué beneficios aporta Pandas al flujo de trabajo cuando se combinan tareas de análisis y visualización de datos?

## ⚙️Ejercicios prácticos

---

## ⚙️Trabajamos con datos en TechLab.

---

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5k42ay5jcl12uau/182eb66a70df424e999467dee4fd3441/original/AD_4nXcegXnZssE1ECwile7liJPouQGIUQC1u_0OCHf-5pKZUANALICslAxY5sc_w9tFYsvWwZ9mWIIOsrQ6Hre4jhpuDyaM7aSIZ60hHl806hqLxDV40_jz7zE7_IZpRMw2EgPQxHiRVKEM3KeAjPHStDo.png)

**Talento Lab** ya ha comenzado a revisar el dataset enviado por el cliente del sector retail y Silvia ha pedido un informe preliminar para la próxima reunión. Matías y Luis necesitan que cada integrante del equipo contribuya realizando un análisis exploratorio y una limpieza básica de los datos.

Tu tarea es la siguiente:

## Ejercicio práctico

```
Obligatorio
```

---

1

#### Carga de datos

Usa Pandas para importar un dataset de Kaggle o uno que tengas disponible.

2

#### Análisis exploratorio

Inspecciona la estructura, tipos de datos y busca valores nulos o duplicados.

3

#### Visualización

Crea al menos dos visualizaciones: una de distribución y otra de relación entre variables.

4

#### Documentación

Registra tus hallazgos, problemas detectados y posibles transformaciones necesarias.

![](https://imgproxy.gamma.app/resize/quality:80/resizing_type:fit/width:2000/https://cdn.gamma.app/5yq1ea3085dnxt6/8068a888885a47b69a684f5c6d17c2bd/original/advertencia.png)

## 📄¡Nuevo cuestionario en campus!

> [!note] Note
> No olvides que los cuestionarios son de carácter obligatorio para poder avanzar con la cursada.

ML - CLASE 02