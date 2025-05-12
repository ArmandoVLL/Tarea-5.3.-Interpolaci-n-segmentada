
#           Autor:
#   Armando Augusto Valladares Uc
#   valladaresarmando301@gmail.com  
#   Version 1.01 : 11/03/2025
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import pandas as pd

# Datos del ejercicio (Velocidad en km/h, Consumo en L/100km)
velocidad = np.array([40, 60, 80, 100, 120, 140])
consumo = np.array([6.5, 5.8, 5.5, 5.7, 6.2, 7.0])

# Crear interpolaciones
interp_lineal = interp1d(velocidad, consumo, kind='linear')
interp_cuadratica = interp1d(velocidad, consumo, kind='quadratic')
interp_cubica = interp1d(velocidad, consumo, kind='cubic')

# Puntos intermedios donde estimar consumo
vel_intermedia = np.array([50, 70, 90, 110, 130])
cons_lineal = interp_lineal(vel_intermedia)
cons_cuadratica = interp_cuadratica(vel_intermedia)
cons_cubica = interp_cubica(vel_intermedia)

# Crear DataFrame y exportar a Excel
df = pd.DataFrame({
    'Velocidad (km/h)': vel_intermedia,
    'Consumo Lineal (L/100km)': cons_lineal,
    'Consumo Cuadrático (L/100km)': cons_cuadratica,
    'Consumo Cúbico (L/100km)': cons_cubica
})
df.to_excel('comparacion_interpolacion_combustible.xlsx', index=False)

# Graficar interpolaciones
x_vals = np.linspace(40, 140, 300)
plt.figure(figsize=(10, 6))
plt.scatter(velocidad, consumo, color='red', label='Datos Originales')
plt.plot(x_vals, interp_lineal(x_vals), '--', label='Lineal', color='blue')
plt.plot(x_vals, interp_cuadratica(x_vals), '-.', label='Cuadrática', color='green')
plt.plot(x_vals, interp_cubica(x_vals), label='Cúbica', color='purple')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Consumo (L/100km)')
plt.title('Interpolación del Consumo de Combustible')
plt.legend()
plt.grid(True)
plt.savefig('grafico_interpolacion_combustible.png')
plt.show()
