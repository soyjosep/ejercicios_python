""" 
- Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
- Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
- NO se tienen en cuenta los espacios, signos de puntuación y tildes.

Ejemplo: Ana lleva al oso la avellana.
"""

import unicodedata

def es_palindromo(texto):
    # Normalizar texto para eliminar tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    # Convertir a minúsculas y eliminar espacios y signos de puntuación
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())

    # Verificar si el texto es igual al reverso
    return texto_limpio == texto_limpio[::-1]
# Ejemoplo de uso
frase = "Ana lleva al oso la avellana."
resultado = es_palindromo(frase)
print(f"¿Es palíndromo? {resultado}")