import unittest

from matriz_sumas import generar_matriz
from matriz_sumas import calcular_sumas



class TestMatrizSumas(unittest.TestCase):

    def test_generar_matriz(self):
        matriz = generar_matriz(3)
        self.assertEqual(len(matriz), 3)
        for fila in matriz:
            self.assertEqual(len(fila), 3)

    def test_calcular_sumas(self):
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        filas_suma, columnas_suma = calcular_sumas(matriz)
        self.assertEqual(filas_suma, [6, 15, 24])
        self.assertEqual(columnas_suma, [12, 15, 18])

    def test_calcular_sumas_matriz_vacia(self):
        matriz = []
        filas_suma, columnas_suma = calcular_sumas(matriz)
        self.assertEqual(filas_suma, [])
        self.assertEqual(columnas_suma, [])

    def test_calcular_sumas_matriz_unica_celda(self):
        matriz = [[7]]
        filas_suma, columnas_suma = calcular_sumas(matriz)
        self.assertEqual(filas_suma, [7])
        self.assertEqual(columnas_suma, [7])

    def test_calcular_sumas_matriz_cuadrada_random(self):
        matriz = generar_matriz(5)
        filas_suma, columnas_suma = calcular_sumas(matriz)
        for suma in filas_suma:
            self.assertEqual(len(matriz), suma)
        for suma in columnas_suma:
            self.assertLessEqual(suma, 45)  # La suma máxima sería 9+9+9+9+9 = 45

if __name__ == "__main__":
    unittest.main()
