
#           Autor:
#   Armando Augusto Valladares Uc
#   valladaresarmando301@gmail.com  
#   Version 1.01 : 11/03/2025
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pandas as pd

# Datos del ejercicio (Distancia en cm, Temperatura en °C)
distancia = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
temperatura = np.array([250, 220, 180, 150, 140, 125])  # Nota: Usé el valor visible en la imagen: 140°C a 4.0 cm

# Crear interpolaciones
interp_lineal = interp1d(distancia, temperatura, kind='linear')
interp_cuadratica = interp1d(distancia, temperatura, kind='quadratic')
interp_cubica = interp1d(distancia, temperatura, kind='cubic')

# Puntos intermedios (cm) donde estimaremos la temperatura
puntos_intermedios = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
temp_lineal = interp_lineal(puntos_intermedios)
temp_cuadratica = interp_cuadratica(puntos_intermedios)
temp_cubica = interp_cubica(puntos_intermedios)

# Crear DataFrame para comparar métodos
df = pd.DataFrame({
    'Distancia (cm)': puntos_intermedios,
    'Temperatura Lineal (°C)': temp_lineal,
    'Temperatura Cuadrática (°C)': temp_cuadratica,
    'Temperatura Cúbica (°C)': temp_cubica
})

# Guardar en Excel
df.to_excel('comparacion_interpolacion_motor.xlsx', index=False)

# Graficar interpolaciones
x_vals = np.linspace(0, 5, 200)
plt.figure(figsize=(10, 6))
plt.scatter(distancia, temperatura, color='red', label='Datos Originales')
plt.plot(x_vals, interp_lineal(x_vals), '--', label='Lineal', color='blue')
plt.plot(x_vals, interp_cuadratica(x_vals), '-.', label='Cuadrática', color='green')
plt.plot(x_vals, interp_cubica(x_vals), label='Cúbica', color='purple')
plt.xlabel('Distancia (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Interpolación de Temperatura en el Cilindro del Motor')
plt.legend()
plt.grid(True)
plt.savefig('grafico_interpolacion_motor.png')
plt.show()
