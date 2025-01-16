""" 
Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
  O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
"""

def analizar_matriz(matriz):
    """
    Analiza una matriz 3x3 de "X", "O" y vacíos para determinar el resultado del juego.

    Parámetros:
    matriz (list of list): Matriz 3x3 con valores "X", "O" o "".

    Retorna:
    str: "X" si ganan las "X", "O" si ganan las "O",
         "Empate" si es empate, "Nulo" si hay inconsistencias.
    """
    # Validar que sea una matriz 3x3
    if len(matriz) != 3 or not all(len(fila) == 3 for fila in matriz):
        return "Nulo"

    # Contar las apariciones de "X" y "O"
    conteo_x = sum(fila.count("X") for fila in matriz)
    conteo_o = sum(fila.count("O") for fila in matriz)
    total_celdas = conteo_x + conteo_o + sum(fila.count("") for fila in matriz)

    # Validar que las proporciones de "X" y "O" sean correctas
    if conteo_x < conteo_o or conteo_x > conteo_o + 1:
        return "Nulo"
    if total_celdas > 9:
        return "Nulo"

    # Función para verificar si hay un ganador
    def hay_ganador(jugador):
        # Comprobar filas, columnas y diagonales
        for i in range(3):
            if all(matriz[i][j] == jugador for j in range(3)):  # Filas
                return True
            if all(matriz[j][i] == jugador for j in range(3)):  # Columnas
                return True
        # Diagonales
        if all(matriz[i][i] == jugador for i in range(3)):
            return True
        if all(matriz[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    # Verificar ganadores
    x_gana = hay_ganador("X")
    o_gana = hay_ganador("O")

    if x_gana and o_gana:  # Si ambos ganan
        return "Nulo"
    if x_gana:
        return "X"
    if o_gana:
        return "O"

    # Si no hay ganadores y todas las celdas están llenas, es empate
    if total_celdas == 9:
        return "Empate"

    # Si ninguna condición se cumple, es un estado de juego válido pero no terminado
    return "Nulo"

# Ejemplo de uso
matriz = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["", "O", "X"]
]
resultado = analizar_matriz(matriz)
print(f"Resultado del análisis: {resultado}")