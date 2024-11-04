""" 
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario  # Agregar el residuo al inicio de la cadena
        numero = numero // 2  # Actualizar el número dividiéndolo por 2
    
    return binario

# Ejemplo de uso
numero_decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es: {binario}")