"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

from typing import List

def es_primo(numero: int) -> bool:
    """Verifica si un número es primo."""
    if numero < 2:
        return False
    if numero == 2:  # 2 es el único número primo par
        return True
    if numero % 2 == 0:  # Elimina todos los pares
        return False
    for i in range(3, int(numero**0.5) + 1, 2):  # Solo verifica números impares
        if numero % i == 0:
            return False
    return True

def obtener_primos(limite: int) -> List[int]:
    """Devuelve una lista de números primos hasta el límite dado."""
    return [num for num in range(2, limite + 1) if es_primo(num)]

def main():
    limite = 100
    primos = obtener_primos(limite)
    print("Números primos entre 1 y 100:", ', '.join(map(str, primos)))

if __name__ == "__main__":
    main()