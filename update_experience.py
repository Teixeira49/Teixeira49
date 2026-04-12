import datetime
import re

# 1. Configura tu fecha de inicio (Año, Mes, Día)
start_date = datetime.date(2023, 6, 4) # ¡Cambia esto por tu fecha!
current_date = datetime.date.today()

# 2. Calcular años de experiencia reales
years_of_experience = current_date.year - start_date.year
if (current_date.month, current_date.day) < (start_date.month, start_date.day):
    years_of_experience -= 1

# 3. Leer el README actual
with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

# 4. Reemplazar el número entre los marcadores invisibles usando Regex
new_content = re.sub(
    \s*(\d+)\s*,
    f'{years_of_experience}',
    readme_content
)

# 5. Guardar los cambios
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(new_content)
    
print(f"Experiencia actualizada a {years_of_experience} años.")
