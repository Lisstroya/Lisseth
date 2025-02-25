def ordenar_fila(matriz, fila):
    for i in range(len(matriz[fila]) - 1):
        for j in range(len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

matriz_ordenacion = [
    [2, 4, 10],
    [6, 3, 5 ],
    [7, 8, 9]
]

print("\nMatriz original:")
for fila in matriz_ordenacion:
    print(fila)

matriz_ordenacion = ordenar_fila(matriz_ordenacion, 1)

print("\nMatriz con la fila 1 ordenada:")
for fila in matriz_ordenacion:
    print(fila)