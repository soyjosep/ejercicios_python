"""

Reto #1
¿ES UN ANAGRAMA?
Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.

"""

import re

def es_anagrama(palabra1, palabra2):

    # Eliminamos espacios y caracteres especiales utilizando expresiones regulares
    palabra1 = re.sub(r'[^a-zA-Z]', '', palabra1.lower())
    palabra2 = re.sub(r'[^a-zA-Z]', '', palabra2.lower())

    # Si las palabras son iguales, no son anagramas
    if palabra1 == palabra2 or len(palabra1) == 0 or len(palabra2) == 0:
        return False

    # Verificamos si tienen las mismas letras en las mismas cantidades
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso mejorado
print(es_anagrama("Amor", "Roma"))  # True
print(es_anagrama("A more", "Roma!"))  # True (ignora espacios y caracteres especiales)
print(es_anagrama("hola", "adios"))  # False
