#programa pystock

import json

directory = "data.json"


def view_products():
    try:
        with open("data.json", "r") as f:
              return json.load(f)
    except FileNotFoundError:
         with open("data.json", "w") as f:
              json.dump([], f, indent=4)
              print("File succesfully created.")
              return []
    except json.JSONDecodeError:
         with open("data.json", "w") as f:
              json.dump([], f, indent=4)
              print("The file was corrupted, so a new one was created")
              return []



print("""========================
        PyStock
========================

1. Ver productos
2. Añadir producto
3. Buscar producto
4. Modificar producto
5. Eliminar producto
6. Estadísticas
7. Salir

Selecciona una opción::""")
