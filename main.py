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
     for i in product:
          if i["name"] == name:
               print(i)

def update_product():
     products = view_products()

     found = False

     id = int(input("please enter your ID number: "))
     for i in products:
          if id == i["id"]:
               found = True
               print("ID found")
               print(i)
               print("""which section do you want to change?
                         1. name
                         2. category
                         3. price
                         4. stock
                         5. salir""")
               while True:
                    option = int(input("option: "))
                    if option == 1:
                         i["name"] = input("new name: ")
                         print("Name successfully changed")
                    elif option == 2:
                         i["category"] = input("new category: ")
                         print("Category successfully changed")
                    elif option == 3:
                         i["price"] = input("new price: ")
                         print("Price successully changed")
                    elif option == 4:
                         i["stock"] = input("new stock: ")
                         print("Stock successfully changed")
                    elif option == 5:
                         print("see ya")
                         break
                    else:
                         print("invalid option")
               save_products(products)
     if not found:
          print("product not found")

          

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
