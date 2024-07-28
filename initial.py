import xml.etree.ElementTree as ET

# Abre y analiza el archivo XML
tree = ET.parse('a.xml')

# Obtiene el elemento raíz del archivo XML
root = tree.getroot()

for persona in root.findall('persona'):
    nombre = persona.find('nombre').text
    edad = int(persona.find('edad').text)
    print(f"Nombre: {nombre}, Edad: {edad}")


