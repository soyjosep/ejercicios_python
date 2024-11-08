""" 
Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran
  en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios.
  No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

def es_equilibrado(expresion):
    """ 
    Verifica si los paréntesis, llasves y corchetes de una expresión están equilibrados.

    Parámetros:
    expresion (str): La expresión a verificar.

    Retorna:
    bool: True si la expresión está equilibrada, False en caso contrario.
    """
    # Diccionario  para los pares de apertura y cierre
    pares = {'(': ')', '{': '}', '[': ']'}
    # Pila para almacenar los delimitadores de apertura
    pila = []

    for char in expresion:
        if char in pares: # Si es un delimitador de apertura
            pila.append(char)
        elif char in pares.values(): # Si es un delimitador de cierre
            if not pila:
                return False # No hay apertura correspondiente
            # Verificar que el último elemento en la pila coincide con el cierre actual
            apertura = pila.pop()
            if pares[apertura] != char:
                return False
    return len(pila) == 0 # La pila debe estar vacía si todo está equilibrado

def main():
    expresion = input("Ingrese la expresión a verificar: ")
    if es_equilibrado(expresion):
        print("La expresión está equilibrada.")
    else:
        print("La expresión no está equilibrada.")

if __name__ == "__main__":
    main()