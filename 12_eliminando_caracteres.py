""" 
Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""

def diferencias_cadenas(str1, str2):
    # Caracteres únicos de str1 que no están en str2
    out1 = ''.join([char for char in str1 if char not in str2])
    # Caracteres únicos de str2 que no están en str1
    out2 = ''.join([char for char in str2 if char not in str1])
    
    print(f"Out1: {out1}")
    print(f"Out2: {out2}")

# Ejemplo de uso
cadena1 = "abcdef"
cadena2 = "bdfgh"
diferencias_cadenas(cadena1, cadena2)