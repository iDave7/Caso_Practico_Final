import random

def generar_matriz(N):
    
    # Genera una matriz de tamaño NxN y la rellena con números aleatorios entre 0 y 9 mediante una lista de comprensión.
    
    matriz = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]
    return matriz

def imprimir_matriz(matriz):
    
    # Imprime la matriz generada en pantalla con las cabeceras de filas y columnas.
    
    N = len(matriz)
   
    # Imprime cabecera de columnas
   
    print("   ", end="")
    for i in range(1, N + 1):
        print(f"C{i}", end=" ")
    print()

    # Imprime cabecera de filas y valores de fila

    for i, fila in enumerate(matriz):   
        print(f"F{i+1}", end=" ")
        for num in fila:
            print(f"{num:2}", end=" ")
        print()

def calcular_sumas(matriz):
    
    # Calcula la suma de los elementos de cada fila y columna y las almacena en dos listas.
    
    filas_suma = [sum(fila) for fila in matriz]
    columnas_suma = [sum(columna) for columna in zip(*matriz)]
    return filas_suma, columnas_suma

def imprimir_sumas(filas_suma, columnas_suma):
    
    # Imprime en pantalla la suma de cada fila y columna.
    
    print("\nSuma de cada fila:")
    for i, suma in enumerate(filas_suma):
        print(f"F{i+1}: {suma}")

    print("\nSuma de cada columna:")
    for i, suma in enumerate(columnas_suma):
        print(f"C{i+1}: {suma}")

def main():
    while True:
        try:
            N = input("Ingrese un número entero positivo N para el tamaño de la matriz: ")

            # Comprobación de que N es un número entero positivo
            # e.d.: no carácter, no decimal, no negativo y no cero

            if N.isdigit() and int(N) > 0:
                N = int(N)  # Convierte N a entero después de la comprobación
                break
            else:
                raise ValueError("El número N debe ser un entero positivo válido.")
        except ValueError as e:
            print(f"Error: {e}")

    # Llamado a la función de impresión de matriz

    matriz = generar_matriz(N)
    print("Matriz generada:")
    imprimir_matriz(matriz)

    # Cálculo e impresión de las sumas de filas y columnas.
    
    filas_suma, columnas_suma = calcular_sumas(matriz)
    imprimir_sumas(filas_suma, columnas_suma)

# Ejecutor del programa
if __name__ == "__main__":
    main()
