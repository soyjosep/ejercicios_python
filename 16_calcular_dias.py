"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
  lanzará una excepción.
"""

from datetime import datetime

def diferencia_dias(fecha1, fecha2):
    try:
        # Convertir las cadenas de texto a objetos de fecha
        formato = "%d/%m/%Y"
        fecha1 = datetime.strptime(fecha1, formato)
        fecha2 = datetime.strptime(fecha2, formato)
        
        # Calcular la diferencia absoluta en días
        diferencia = abs((fecha2 - fecha1).days)
        return diferencia
    except ValueError:
        # Lanzar una excepción si las fechas no son válidas
        raise ValueError("Una o ambas cadenas no representan una fecha válida.")

# Ejemplo de uso
try:
    fecha1 = input("Ingresa la primera fecha (dd/MM/yyyy): ")
    fecha2 = input("Ingresa la segunda fecha (dd/MM/yyyy): ")
    dias = diferencia_dias(fecha1, fecha2)
    print(f"La diferencia en días entre las fechas es: {dias}")
except ValueError as e:
    print(f"Error: {e}")