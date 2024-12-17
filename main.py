import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

def draw_plot():
    # Cargar los datos del archivo CSV
    data = pd.read_csv('epa-sea-level.csv')

    # Crear la figura y el eje
    fig, ax = plt.subplots()

    # Graficar los puntos de datos
    ax.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Ajustar la línea de regresión para todo el conjunto de datos (1880-2018)
    years_full_range = np.arange(1880, 2019)
    p_full = np.polyfit(data['Year'], data['CSIRO Adjusted Sea Level'], 1)
    ax.plot(years_full_range, np.polyval(p_full, years_full_range), label='Best fit line (1880-2018)', color='red')

    # Ajustar la línea de regresión para el conjunto de datos (1880-2000)
    data_2000 = data[data['Year'] <= 2000]
    p_2000 = np.polyfit(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'], 1)
    ax.plot(years_full_range, np.polyval(p_2000, years_full_range), label='Best fit line (1880-2000)', color='green')

    # Añadir etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Mostrar la leyenda
    ax.legend()

    # Establecer la escala en el eje y para que las marcas sean visibles
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # Guardar la imagen
    plt.savefig('sea_level_plot.png')

    # Mostrar el gráfico
    plt.show()

if __name__ == '__main__':
    print("Ejecutando el script...")
    draw_plot()
    print("Gráfico guardado como 'sea_level_plot.png'.")
