""" 
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_cadena(cadena):
    """ 
    Invierte el orden de una cadena de texto usando slicing.

    Parámetros:
    cadena (str): La cadena de texto a invertir.

    Retorna:
    str: La cadena invertida.
    """
    return cadena[::-1]

def main():
    texto = input("Ingrese una cadena de texto para invertir: ")
    texto_invertido = invertir_cadena(texto)
    print(f"La cadena invertida es: '{texto_invertido}")

if __name__ == "__main__":
    main()

