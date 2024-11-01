""" 
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_cadena(cadena):
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida

# Ejemplo de uso
texto = "Hola mundo"
texto_invertido = invertir_cadena(texto)
print(texto_invertido)