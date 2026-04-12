import datetime
import re
import os

# 1. Tu fecha de inicio (Año, Mes, Día)
start_date = datetime.date(2023, 6, 3) 
current_date = datetime.date.today()

# 2. Cálculo de años
years = current_date.year - start_date.year
if (current_date.month, current_date.day) < (start_date.month, start_date.day):
    years -= 1

# 3. Leer el README
if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # 4. Regex segura: Busca las etiquetas exactas y atrapa los números en el medio
    pattern = r'(\s*)(\d+)(\s*)'
    
    # Reemplaza usando los grupos exactos (\g<1> es la primera etiqueta, \g<3> es la última)
    replacement = r'\g<1>' + str(years) + r'\g<3>'
    
    new_content = re.sub(pattern, replacement, content)

    # 5. Guardar solo si hay cambios
    if new_content != content:
        with open('README.md', 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Actualizado exitosamente a {years} años.")
    else:
        print("No se requirieron cambios. Los años están actualizados.")
else:
    print("Error: No se encontró el archivo README.md")
