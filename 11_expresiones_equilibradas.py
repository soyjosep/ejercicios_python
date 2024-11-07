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

def esta_equilibrado(expresion):
    # Diccionario para los pares de apertura y cierre
    pares = {'(': ')', '{': '}', '[': ']'}
    # Pila para almacenar los caracteres de apertura
    pila = []

    for caracter in expresion:
        # Si el caracter es de apertura, lo añadimos a la pila
        if caracter in pares:
            pila.append(caracter)
        # Si es un caracter de cierre, comprobamos si corresponde al último en la pila
        elif caracter in pares.values():
            if not pila or pares[pila.pop()] != caracter:
                return False
    
    # Al final, la pila debe estar vacía si esta equilibrada
    return len(pila) == 0

# Ejemplo de uso
expresion1 = "{ [ a * ( c + d ) ] - 5 }"
expresion2 = "{ a * ( c + d ) ] - 5 }"

print(f"Expresión 1 está equilibrada: {esta_equilibrado(expresion1)}")
print(f"Expresión 2 está equilibrada: {esta_equilibrado(expresion2)}")