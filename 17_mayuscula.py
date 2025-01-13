""" 
Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
"""

def capitalizar_palabras(texto):
    resultado = ""
    nueva_palabra = True  # Indicador de inicio de palabra
    
    for caracter in texto:
        if caracter.isalpha() and nueva_palabra:
            resultado += caracter.upper()  # Convertir a mayúscula
            nueva_palabra = False
        else:
            resultado += caracter
        
        # Verificar si el carácter actual es un espacio o separador
        if not caracter.isalpha() and not caracter.isdigit():
            nueva_palabra = True
    
    return resultado

# Ejemplo de uso
texto = input("Escribe un texto: ")
resultado = capitalizar_palabras(texto)
print(resultado)
