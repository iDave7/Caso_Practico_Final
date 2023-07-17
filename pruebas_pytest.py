import pytest
from matriz_sumas import generar_matriz, calcular_sumas

def test_generar_matriz():
    matriz = generar_matriz(3)
    assert len(matriz) == 3
    for fila in matriz:
        assert len(fila) == 3

def test_calcular_sumas():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    filas_suma, columnas_suma = calcular_sumas(matriz)
    assert filas_suma == [6, 15, 24]
    assert columnas_suma == [12, 15, 18]

def test_calcular_sumas_matriz_vacia():
    matriz = []
    filas_suma, columnas_suma = calcular_sumas(matriz)
    assert filas_suma == []
    assert columnas_suma == []

def test_calcular_sumas_matriz_unica_celda():
    matriz = [[7]]
    filas_suma, columnas_suma = calcular_sumas(matriz)
    assert filas_suma == [7]
    assert columnas_suma == [7]

def test_calcular_sumas_matriz_cuadrada_random():
    matriz = generar_matriz(5)
    filas_suma, columnas_suma = calcular_sumas(matriz)
    for suma in filas_suma:
        assert len(matriz) == suma
    for suma in columnas_suma:
        assert suma <= 45

if __name__ == "__main__":
    pytest.main()
