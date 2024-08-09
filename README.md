# Objetivo
- Predecir futuras ventas del material.
# Pasos seguidos
#### Identificación del problema
El problema es uno de predicción basado en datos dependientes del tiempo, más conocido en inglés como *time series forecasting*.
#### Preparación de datos
- Como el .txt proporcionado tenía un *formatting* poco usual quité las tabulaciones y espacios innecesarios y borré las columnas irrelevantes. 
- Para facilitar el trabajo también renombré las columnas para que el código fuera más legible.
- Ordené los datos por fecha y creé un .csv únicamente con las ventas por día 
- Observé que los datos son inconsistentes y hay muchos días que faltan, no es por festivos ni fines de semana.
- No hay duplicados.
- Aprender sobre diferentes métodos de *forecasting* de utilizando ML y DL
#### Machine learning/Estadística
##### Regresión lineal
- Para tener una visualización inicial de los datos creé un gráfica de regresión lineal donde la variable independiente es el tiempo y el variable dependiente el número de ventas.
- Como material complementario también creé la gráfica de residuos que permite observar mejor el error (distancia vertical) de las observaciones reales frente a la recta de regresión.
Como se esperaba, no se ajusta a una regresión lineal, pero quería tener una visualización inicial de los datos. El error es muy grande. Se puede ya concluir que predecir el futuro con datos tan inconsistentes resultará complicado y los resultados no serán muy fiables.
#### Deep learning
Uso de LSTM: Long Short-Term Memory (LSTM) is **a type of artificial recurrent neural network (RNN) architecture used in the field of deep learning**

Ajustar diferentes parámetros:
- Días de *lookback* => 7
- Batch size => 32
- Learning rate => 0.001
- Número de *epochs* => 50
- Ajustar modelo con más capas (hidden layers) => 4

He realizado dos versiones diferentes, pero adjunto la que mejor funciona. 

Fuentes para el desarrollo del ejercicio:
Teoría sobre diferentes técnicas que podría emplear estadísticas y de ML/DL:
https://hastie.su.domains/ISLP/ISLP_website.pdf.download.html
https://medium.com/analytics-vidhya/rnn-vs-gru-vs-lstm-863b0b7b1573
https://colah.github.io/posts/2015-08-Understanding-LSTMs/
https://www.uber.com/en-ES/blog/m4-forecasting-competition/

Fuentes de código para la realización del ejercicio usando PyTorch:
https://www.youtube.com/watch?v=q_HS4s1L8UI
https://www.youtube.com/watch?v=8A6TEjG2DNw&list=PLzJ0cKlK0v0PvIOQ5bRd4lhTzbdh6_Y8W
https://pytorch.org/docs/stable/index.html
