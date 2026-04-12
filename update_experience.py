import re
from datetime import datetime

README_PATH = 'README.md'  # Cambia esto si tu archivo se llama distinto
START_DATE = datetime(2023, 6, 3)  # Tu fecha de inicio en experiencia laboral (cámbialo si es necesario)

def calcular_anios_experiencia():
    hoy = datetime.now()
    anios = hoy.year - START_DATE.year - ((hoy.month, hoy.day) < (START_DATE.month, START_DATE.day))
    return anios

def actualizar_readme(path):
    with open(path, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Regex para encontrar la línea de experiencia
    pattern = r'(💻 Poco mas de )\d+ (Años de experiencia laboral completados)'
    anios = calcular_anios_experiencia()
    nuevo_texto = f'💻 Poco mas de {anios} Años de experiencia laboral completados'

    nuevo_contenido, n = re.subn(pattern, nuevo_texto, contenido)
    if n == 0:
        print("No se encontró la línea a modificar.")
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(nuevo_contenido)
        print(f'Readme actualizado con {anios} años de experiencia laboral.')

if __name__ == '__main__':
    actualizar_readme(README_PATH)
