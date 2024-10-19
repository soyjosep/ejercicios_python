"""
Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Url de ejemplo:
  https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
  imagen de 1920*1080px.
"""

import requests
from PIL import Image
from io import BytesIO
import math

# URL de la imagen
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Descargar la imagen desde la URL
respuesta = requests.get(url)
imagen = Image.open(BytesIO(respuesta.content))

# Obtener las dimensiones de la imagen
ancho, alto = imagen.size

# Calcular el máximo común divisor
mcd = math.gcd(ancho, alto)

# Simplificar las dimensiones
aspect_ratio_ancho = ancho // mcd
aspect_ratio_alto = alto // mcd

# Imprimir el aspect ratio
print(f"El aspect ratio es {aspect_ratio_ancho}:{aspect_ratio_alto}")