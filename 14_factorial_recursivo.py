"""
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
"""
def factorial_recursivo(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # LLamada recursiva
    return n * factorial_recursivo(n-1)

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
resultado = factorial_recursivo(numero)
print(f"El factorial de {numero} es: {resultado}")