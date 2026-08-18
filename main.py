#programa pystock
"""
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

    new_id = products[-1]["id"] + 1 if products else 1

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
                         i["price"] = float(input("new price: "))
                         print("Price successully changed")
                    elif option == 4:
                         i["stock"] = int(input("new stock: "))
                         print("Stock successfully changed")
                    elif option == 5:
                         print("see ya")
                         break
                    else:
                         print("invalid option")
               save_products(products)
     if not found:
          print("product not found")

def delete_product():
     products = view_products()

     found = False

     id = int(input("please enter ID number: "))
     for i in products:
          if id == i["id"]:
               found = True
               print("ID found")
               print(i)
               print("Is this the product you were looking for?")
               while True:
                    option = input("Y/N: ").lower()
                    if option == "y":
                         products.remove(i)
                         print("Product removed")
                         save_products(products)
                         break
                    elif option == "n":
                         print("Operation cancelled")
                         break
                    else:
                         print("invalid option, please try again")
     if not found:
          print("product not found")

def show_statics():
     products = view_products()

     if not products:
          print("there are no products in inventory")
          return

     total_products = len(products)

     total_value = sum(p["price"] * p["stock"] for p in products)

     most_expensive_product = max(products, key=lambda p: p["price"])

     more_stock = max(products, key=lambda p: p["stock"])

     less_stock = min(products, key=lambda p: p["stock"])

     categories = set(p["category"] for p in products)

     average_stock = sum(p["stock"] for p in products) / total_products

     print("\n===INVENTORY STATICS===")
     print(f"Total products:            {total_products}")
     print(f"total_value:               {total_value:.2f}")
     print(f"categories:                {', '.join(categories)}")
     print(f"average_stock:             {average_stock:.1f} units")
     print(f"most_expensive_product:    {most_expensive_product['name']} (${most_expensive_product['price']})")
     print(f"more_stock:                {more_stock['name']} ({more_stock['stock']} units)")
     print(f"less_stock:                {less_stock['name']} ({less_stock['stock']} units)")

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
