def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

matriz = [
    [8, 6, 10],
    [5, 7, 9],
    [4, 3, 2]
]

valor_buscado = 3
resultado = buscar_en_matriz(matriz, valor_buscado)
if resultado:
    print(f"Valor {valor_buscado} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz.")