import datetime
import os

# 1. Tu fecha de inicio (Año, Mes, Día)
start_date = datetime.date(2021, 5, 1) 
current_date = datetime.date.today()

# 2. Cálculo de años
years = current_date.year - start_date.year
if (current_date.month, current_date.day) < (start_date.month, start_date.day):
    years -= 1

# 3. Leer el README
if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # 4. Método de Partición de Texto (SIN REGEX)
    start_marker = ""
    end_marker = ""

    # Verificamos que los marcadores existan en el archivo
    if start_marker in content and end_marker in content:
        
        # Cortamos el texto exactamente donde están los marcadores
        texto_antes = content.split(start_marker)[0]
        texto_despues = content.split(end_marker)[1]
        
        # Ensamblamos el archivo de nuevo poniendo los años exactos en el medio
        new_content = f"{texto_antes}{start_marker}{years}{end_marker}{texto_despues}"

        # 5. Guardar solo si hay cambios
        if new_content != content:
            with open('README.md', 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Actualizado exitosamente a {years} años de experiencia.")
        else:
            print("Los años ya estaban actualizados. No se hicieron cambios.")
            
    else:
        print("Error: No se encontraron los marcadores y en el README.")
else:
    print("Error: No se encontró el archivo README.md")
