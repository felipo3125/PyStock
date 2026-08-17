#programa pystock
"""
add product
search_product
update_product
delete_product
show_statics
"""




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

def save_products(products):
     with open(directory, "w") as f:
          json.dump(products, f, indent=4)

def add_product(name, category, price, stock):
    products = view_products()

    new_id = products[-1]["id"] + 1

    product = {
        "id": new_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    products.append(product)
    save_products(products)

def search_product(name):
     product = view_products()
     product["name"] = name

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
