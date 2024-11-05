""" 
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def decimal_a_binario(numero):
    """ 
    Convierte un número decimal a su representación en binario.

    Parámetros:
    numero (int): El número decimal a convertir.

    Retorna:
    str: La representación binaria del número.
    """
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    return binario

def main ():
    try:
        numero = int(input("Ingrese un número decimal para convertir a binario: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
        else:
            binario = decimal_a_binario(numero)
            print(f"Lan respresentación binaria de {numero} es: {binario}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
    main()