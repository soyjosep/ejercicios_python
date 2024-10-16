"""
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

class Triángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

class Rectángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

def calcular_area(poligono):
    if isinstance(poligono, Triángulo):
        return (poligono.base * poligono.altura) / 2
    elif isinstance(poligono, Cuadrado):
        return poligono.lado ** 2
    elif isinstance(poligono, Rectángulo):
        return poligono.base * poligono.altura
    else:
        return None

# Imprimir el cálculo del área de un polígono de cada tipo
triangulo = Triángulo(base=10, altura=5)
cuadrado = Cuadrado(lado=4)
rectangulo = Rectángulo(base=6, altura=3)

print(f"Área del triángulo: {calcular_area(triangulo)}")
print(f"Área del cuadrado: {calcular_area(cuadrado)}")
print(f"Área del rectángulo: {calcular_area(rectangulo)}")

