""" 
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto.
"""

def es_numero_armstrong(numero):
    # Convertir el número a cadena para separa sus dígitos
    digitos = list(map(int, str(numero)))
    # Calcular la longitud de los dígitos
    potencia = len(digitos)
    # Sumar cada dígito elevado a la potencia
    suma = sum(digito ** potencia for digito in digitos)
    # Verificar si la suma es igual al número original
    return suma == numero

# Ejemplo de uso
numero = int(input("Ingresa un número: "))
if es_numero_armstrong(numero):
    print(f"{numero} es un número de Armstrong.")
else:
    print(f"{numero} no es un número de Armstrong.")