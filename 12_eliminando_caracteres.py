""" 
Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""

def diferencias_cadenas(str1, str2):
    """
    Genera dos cadenas de salida:
    - out1: Caracteres en str1 que no están en str2.
    - out2: Caracteres en str2 que no están en str1.

    Parámetros:
    str1 (str): Primera cadena de entrada.
    str2 (str): Segunda cadena de entrada.

    Salidas:
    - Imprime out1: Caracteres únicos de str1.
    - Imprime out2: Caracteres únicos de str2.
    """
    # Validación de entradas
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Ambos parámetros deben ser cadenas de texto.")

    # Generar las cadenas de salida preservando el orden
    out1 = ''.join(char for char in str1 if char not in str2)
    out2 = ''.join(char for char in str2 if char not in str1)

    print(f"Out1: '{out1}'")
    print(f"Out2: '{out2}'")

# Solicitar entrada de datos al usuario
cadena1 = input("Ingrese la primera cadena (str1): ")
cadena2 = input("Ingrese la segunda cadena (str2): ")

# Llamar a la función con las entradas proporcionadas
diferencias_cadenas(cadena1, cadena2)