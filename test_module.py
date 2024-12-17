import unittest
import matplotlib.pyplot as plt
import numpy as np
from main import draw_plot  # Importa la función draw_plot desde main.py

class LinePlotTestCase(unittest.TestCase):
    
    def test_plot_best_fit_lines(self):
        # Ejecutar la función de graficado
        draw_plot()

        # Obtener el eje actual
        ax = plt.gca()  # gca() obtiene el "current axis" de la figura

        # Obtener todas las líneas (scatter plot y líneas de ajuste)
        lines = ax.get_lines()

        # Verificar que haya 2 líneas de ajuste (y no 3, porque el scatter no cuenta como línea)
        self.assertEqual(len(lines), 2, "Se esperaban 2 líneas de ajuste.")

    def test_plot_data_points(self):
        # Ejecutar la función de graficado
        draw_plot()

        # Obtener los puntos de datos
        ax = plt.gca()
        data_points = []

        # Extraemos los puntos de datos del scatter plot
        scatter_points = ax.collections[0].get_offsets()  # Obtener los puntos del gráfico de dispersión (scatter)
        for point in scatter_points:
            data_points.append((point[0], round(point[1], 6)))  # Redondear los valores de nivel del mar a 6 decimales

        # Definir los puntos esperados (esto depende de los datos de tu CSV)
        expected_points = [
            (1880, 0.0), (1881, 0.220472), (1882, -0.440945), (1883, -0.232283),
            (1884, 0.590551), (1885, 0.531496), (1886, 0.437008), (1887, 0.216535),
            (1888, 0.299213), (1889, 0.362205)
        ]

        # Redondear los puntos esperados a 6 decimales para la comparación
        expected_points = [(year, round(value, 6)) for year, value in expected_points]

        # Comprobar que los puntos de datos generados coinciden con los esperados
        # Usamos `self.assertListEqual()` para comparar listas de tuplas
        self.assertListEqual(data_points[:10], expected_points, "Los puntos de datos no son correctos.")  # Solo los primeros 10 puntos

if __name__ == "__main__":
    unittest.main()
