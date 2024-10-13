"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos(limite):
    for num in range(1, limite + 1):
        if es_primo(num):
            print(num)

# Imprimir números primos entre 1 y 100
imprimir_primos(100)