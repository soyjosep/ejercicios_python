import random

def generar_pista(longitud):
    """
    Genera una pista aleatoria con "_" (suelo) y "|" (valla).

    Parámetros:
    longitud (int): La longitud de la pista.

    Retorna:
    str: Una pista aleatoria.
    """
    return ''.join(random.choice(["_", "|"]) for _ in range(longitud))

def evaluar_carrera_usuario(pista):
    """
    Permite al usuario tomar decisiones en una carrera de obstáculos.
    Evalúa si las decisiones son correctas y genera el resultado final.

    Parámetros:
    pista (str): La pista generada con "_" (suelo) y "|" (valla).

    Retorna:
    bool: True si el usuario supera la carrera, False en caso contrario.
    """
    pista_modificada = list(pista)
    correcta = True

    print("Pista generada: " + pista)
    print("Instrucciones: Ingresa 'run' para suelo (_) o 'jump' para valla (|).\n")

    for i in range(len(pista)):
        print(f"Obstáculo {i + 1} ({pista[i]}):")
        while True:
            accion = input("¿Qué acción deseas realizar? (run/jump): ").strip().lower()
            if accion in ["run", "jump"]:
                break
            print("Entrada inválida. Ingresa 'run' o 'jump'.")

        if accion == "run" and pista[i] == "_":
            pass  # Acción correcta
        elif accion == "jump" and pista[i] == "|":
            pass  # Acción correcta
        elif accion == "jump" and pista[i] == "_":
            pista_modificada[i] = "x"  # Acción incorrecta
            correcta = False
        elif accion == "run" and pista[i] == "|":
            pista_modificada[i] = "/"  # Acción incorrecta
            correcta = False

    print("\nPista final: " + "".join(pista_modificada))
    return correcta

def main():
    """
    Función principal para ejecutar la carrera de obstáculos.
    """
    print("¡Bienvenido/a a la carrera de obstáculos!")
    while True:
        try:
            longitud = int(input("¿Cuántos obstáculos tendrá la pista? (Número entero): "))
            if longitud <= 0:
                print("La longitud debe ser un número positivo. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    pista = generar_pista(longitud)
    resultado = evaluar_carrera_usuario(pista)

    if resultado:
        print("\n¡Felicidades! Has superado la carrera correctamente.")
    else:
        print("\nNo lograste superar la carrera. ¡Inténtalo de nuevo!")

if __name__ == "__main__":
    main()