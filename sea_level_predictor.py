import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leer los datos desde el archivo CSV
    data = pd.read_csv('epa-sea-level.csv')

    # Crear el gráfico de dispersión (scatter plot)
    plt.figure()  # Aseguramos que creamos una nueva figura
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Línea de mejor ajuste para todo el rango de datos (1880 - 2050)
    linreg = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Aseguramos que el rango de años sea de 1880 a 2050
    plt.plot(years_extended, linreg.intercept + linreg.slope * pd.Series(years_extended), label="Best Fit Line (1880 - 2050)")

    # Línea de mejor ajuste para los datos a partir de 2000
    data_recent = data[data['Year'] >= 2000]
    linreg_recent = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, linreg_recent.intercept + linreg_recent.slope * pd.Series(years_extended), label="Best Fit Line (2000 - 2050)", linestyle="--")

    # Imprimir el número de líneas en la gráfica
    lines = plt.gca().get_lines()
    print(f"Number of lines on the plot: {len(lines)}")  # Para asegurarnos de que sean solo 3 líneas

    # Imprimir algunos puntos de datos generados
    data_points = list(zip(data['Year'], data['CSIRO Adjusted Sea Level']))
    print(f"First few data points: {data_points[:10]}")  # Imprimir los primeros 10 puntos

    # Agregar título y etiquetas
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Ajustar las etiquetas del eje X con formato flotante y hasta 2075
    plt.xticks([float(i) for i in range(1850, 2076, 25)])

    # Mostrar la leyenda
    plt.legend()

    # Guardar el gráfico como archivo PNG
    plt.savefig('sea_level_plot.png')

    # Devolver el objeto de la gráfica para poder testearla
    return plt.gca()
