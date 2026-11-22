**Objetivo:** Utilizar aprendizaje no supervisado para agrupar canciones según sus características sonoras, simulando el motor de recomendación detrás de las playlists automáticas de Spotify.

### **Parte 1: Análisis Exploratorio (EDA)**

1. Cargar el dataset de canciones usando Pandas.  
2. Explorar las distribuciones: ¿La mayoría de las canciones son alegres (*valence* alto) o tristes? ¿Cómo se distribuye el *tempo*?  
3. Crear al menos dos gráficos de dispersión (scatter plots) cruzando variables que sospechen que tienen relación (ej. **`energy` vs `acousticness`**).

### **Parte 2: Preprocesamiento y el problema de las escalas**

1. Observar los rangos de las variables. Mientras que `danceability` va de 0 a 1, `tempo` puede ir de 60 a 200 BPM.  
2. Responder: ¿Qué pasaría con el algoritmo K-Means si calculamos las distancias sin igualar las escalas?  
3. Aplicar **`StandardScaler` o `MinMaxScaler`** de Scikit-Learn a las características numéricas de las canciones.

### **Parte 3: Encontrando la cantidad de "Vibras" (K óptimo)**

1. Aplicar el **Método del Codo (Inercia)** probando valores de *k* entre 2 y 10\. Graficar la curva.  
2. Calcular el **Índice de Silhouette** para esos mismos valores y graficarlo.  
3. **Decisión:** En base a ambas métricas, ¿cuántos grupos (clusters) distintos de canciones existen en nuestro dataset? Justificar la elección del *k*.

### **Parte 4: Entrenamiento y Asignación**

1. Instanciar el modelo `KMeans` con el valor de *k* elegido y entrenarlo sobre los datos escalados.  
2. Agregar una nueva columna al DataFrame original llamada `Cluster` con la etiqueta que el algoritmo le asignó a cada canción.

### **Parte 5: Análisis de los Centroides y Bautismo**

1. Calcular el promedio de las variables de audio para cada cluster (mirar los centroides).  
2. Armar un gráfico (puede ser un gráfico de barras agrupadas o un radar chart) para comparar el perfil de cada cluster.  
3. **El toque final:** En base a las características de cada grupo, "bautizar" a cada cluster con un nombre comercial para una playlist. (Ejemplo: *Cluster 0 \= "Para entrenar a full" (alta energía, alto tempo), Cluster 1 \= "Domingo de lluvia" (alta acústica, bajo tempo, baja valencia)*).

