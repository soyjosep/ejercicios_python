"""
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
"""

def factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Parámetros:
    n (int): El número del cual se desea calcular el factorial.

    Retorna:
    int: El factorial de n.

    Lanza:
    ValueError: Si el número es negativo.
    """
    # Validación de entrada
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva
    return n * factorial_recursivo(n - 1)

def main():
    """
    Punto de entrada principal para calcular el factorial usando la función recursiva.
    """
    try:
        numero = int(input("Ingrese un número entero no negativo: "))
        if numero < 0:
            raise ValueError("El número debe ser no negativo.")
        resultado = factorial_recursivo(numero)
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError as e:
        print(f"Entrada no válida: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()