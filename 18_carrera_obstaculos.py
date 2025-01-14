""" 
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
- La función recibirá dos parámetros:
    - Un array que sólo puede contener String con las palabras "run" o "jump".
    - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla).
- La función imprimirá cómo ha finalizado la carrera:
    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
      - Si hace "run" en "|" (valla), se variará la pista por "/".
 - La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

def evaluar_carrera(acciones, pista):
    if len(acciones) != len(pista):
        raise ValueError("La longitud de las  acciones y la pista debe ser la misma.")
    
    pista_modificada = list(pista)
    correcta = True

    for i in range(len(pista)):
        if acciones[i] == "run" and pista[i] == "_":
            pass # Acción correcta, no cambia nada
        elif acciones[i] == "jump" and pista[i] == "|":
            pass # Acción correcta, no cambia nada
        elif acciones[i] == "jump" and pista[i] == "_":
            pista_modificada[i] = "x" # Acción incorrecta
            correcta = False
        elif acciones[i] == "run" and pista[i] == "|":
            pista_modificada[i] = "/" # Acción incorrecta
            correcta = False
        else:
            raise ValueError("Acción o pista no válida.")
        
    print("Pista final: " + "".join(pista_modificada))
    return correcta

# Ejemplo de uso
acciones = ["run", "jump", "run", "jump", "run"]
pista = "_|_|_"

resultado = evaluar_carrera(acciones, pista)
if resultado:
    print("El/la atleta ha superado la carrera correctamente.")
else:
    print("El/la atleta no ha superado la carrera.")