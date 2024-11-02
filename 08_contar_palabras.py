""" 
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
  lo resuelvan automáticamente.
"""

def contar_palabras(texto):
    # Convertir el texto a minúsculas y eliminar signos de puntuación manualmente
    texto = texto.lower()
    caracteres_no_deseados = ".,;:!?"
    texto_sin_puntuacion = ""
    
    for caracter in texto:
        if caracter not in caracteres_no_deseados:
            texto_sin_puntuacion += caracter
    
    # Separar palabras manualmente
    palabras = []
    palabra_actual = ""
    
    for caracter in texto_sin_puntuacion:
        if caracter == " ":
            if palabra_actual:  # Añadir palabra completa a la lista si no está vacía
                palabras.append(palabra_actual)
                palabra_actual = ""
        else:
            palabra_actual += caracter
    
    if palabra_actual:  # Añadir la última palabra si existe
        palabras.append(palabra_actual)
    
    # Contar palabras manualmente
    recuento = {}
    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1
    
    # Mostrar el recuento de palabras
    for palabra, cantidad in recuento.items():
        print(f"'{palabra}': {cantidad}")

# Ejemplo de uso
texto = "Hola mundo, hola universo. ¡Hola a todos en el mundo!"
contar_palabras(texto)