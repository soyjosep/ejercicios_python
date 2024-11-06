""" 
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
  la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
  o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
  https://es.wikipedia.org/wiki/Código_morse.
"""

# Diccionario de traducción Morse
morse_a_texto = {
    'A': '· —', 'B': '— · · ·', 'C': '— · — ·', 'D': '— · ·', 'E': '·',
    'F': '· · — ·', 'G': '— — ·', 'H': '· · · ·', 'I': '· ·', 'J': '· — — —',
    'K': '— · —', 'L': '· — · ·', 'M': '— —', 'N': '— ·', 'O': '— — —',
    'P': '· — — ·', 'Q': '— — · —', 'R': '· — ·', 'S': '· · ·', 'T': '—',
    'U': '· · —', 'V': '· · · —', 'W': '· — —', 'X': '— · · —', 'Y': '— · — —',
    'Z': '— — · ·', '1': '· — — — —', '2': '· · — — —', '3': '· · · — —',
    '4': '· · · · —', '5': '· · · · ·', '6': '— · · · ·', '7': '— — · · ·',
    '8': '— — — · ·', '9': '— — — — ·', '0': '— — — — —'
}

# Crear el diccionario inverso para traducir de Morse a texto
texto_a_morse = {v: k for k, v in morse_a_texto.items()}

def es_morse(texto):
    """Función para detectar si el texto es Morse (si contiene solo '.', '—' y espacios)"""
    return all(c in "·— " for c in texto)

def texto_a_morse_fn(texto):
    """Convertir texto natural a código Morse"""
    morse = []
    for letra in texto.upper():
        if letra in morse_a_texto:
            morse.append(morse_a_texto[letra])
    return "   ".join(morse)  # Usar tres espacios para separar palabras

def morse_a_texto_fn(morse):
    """Convertir código Morse a texto natural"""
    palabras = morse.split("   ")  # Separar palabras usando tres espacios
    texto = []
    for palabra in palabras:
        letras = palabra.split(" ")  # Separar letras usando un solo espacio
        palabra_traducida = "".join(texto_a_morse.get(letra, '') for letra in letras)
        texto.append(palabra_traducida)
    return " ".join(texto)

def convertir(texto):
    """Detecta el tipo de texto y realiza la conversión adecuada"""
    if es_morse(texto):
        return morse_a_texto_fn(texto)
    else:
        return texto_a_morse_fn(texto)

# Ejemplo de uso
texto = input("Ingresa el texto o código Morse a convertir: ")
resultado = convertir(texto)
print("Resultado:", resultado)