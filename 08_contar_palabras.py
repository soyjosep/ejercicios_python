""" 
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
  lo resuelvan automáticamente.
"""

def limpiar_palabra(palabra):
    """
    Elimina signos de puntuación de una palabra y la convierte a minúsculas.

    Parámetros:
    palabra (str): La palabra a limpiar.

    Retorna:
    str: La palabra sin signos de puntuación y en minúsculas.
    """
    palabra_limpia = ""
    for char in palabra:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            palabra_limpia += char.lower()
    return palabra_limpia

def contar_palabras(texto):
    """
    Cuenta cuántas veces se repite cada palabra en el texto.

    Parámetros:
    texto (str): El texto en el que contar las palabras.

    Retorna:
    dict: Un diccionario con las palabras como claves y sus recuentos como valores.
    """
    palabras_contadas = {}
    palabra_actual = ""
    
    for char in texto:
        if char == " ":
            if palabra_actual:
                palabra_limpia = limpiar_palabra(palabra_actual)
                if palabra_limpia in palabras_contadas:
                    palabras_contadas[palabra_limpia] += 1
                else:
                    palabras_contadas[palabra_limpia] = 1
                palabra_actual = ""
        else:
            palabra_actual += char

    # Añadir la última palabra si no hay un espacio al final
    if palabra_actual:
        palabra_limpia = limpiar_palabra(palabra_actual)
        if palabra_limpia in palabras_contadas:
            palabras_contadas[palabra_limpia] += 1
        else:
            palabras_contadas[palabra_limpia] = 1

    return palabras_contadas

def main():
    texto = input("Ingrese el texto a analizar: ")
    recuento_palabras = contar_palabras(texto)
    print("\nRecuento de palabras:")
    for palabra, cuenta in recuento_palabras.items():
        print(f"{palabra}: {cuenta}")

if __name__ == "__main__":
    main()