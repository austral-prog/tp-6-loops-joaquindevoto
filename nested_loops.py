# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    resultado = []
    for fila in matrix:
        for numero in fila:
            resultado.append(numero)
    return resultado


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    resultado = []
    for fila in matrix:
        suma_fila = 0
        for numero in fila:
            suma_fila += numero
        resultado.append(suma_fila)
    return resultado


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    if not matrix: return []

    num_filas = len(matrix)
    num_cols = len(matrix[0])
    resultado = []

    for c in range(num_cols):
        suma_col = 0
        for f in range(num_filas):
            suma_col += matrix[f][c]
        resultado.append(suma_col)

    return resultado
