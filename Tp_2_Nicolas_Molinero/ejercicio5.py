productos = []

def cargar_producto():
    while True:
        nombre = input("ingrese el nombre del producto o fin para salir: ")
        if nombre.lower() == "fin":
            break
        else:
            precio = float(input("ingrese el precio del producto: "))
            productos.append({"nombre": nombre, "precio": precio})
    return productos
def sumar_precios(productos):
    subtotal = 0
    for p in productos:
            subtotal += p["precio"]
    return subtotal

def calcular_descuento(subtotal, cantidad_productos, es_club):
    descuento = 0
    if es_club == "s":
        descuento = subtotal * 0.05
    if cantidad_productos > 5:
        descuento +=  1000
    if subtotal > 50000:
            descuento = subtotal * 0.15
    elif subtotal > 20000:
            descuento = subtotal * 0.10
    elif subtotal > 10000:
            descuento =  subtotal * 0.05
    return descuento
def mostrar_resumen(productos, subtotal, descuento, total):
    print(f"{productos}")
    cantidad_productos = len(productos)
    if es_club == "s":
        print("5% de descuento por ser miembro del club")
    if cantidad_productos > 5:
        print("$1000 de descuento por tener mas de 5 productos")
    if subtotal > 50000:
        print("15% de descuento porque el total es mayor a $50000")
    elif subtotal > 20000:
        print("10% de descuento porque el total es mayor a $20000")
    elif subtotal > 10000:
        print("5% de descuento porque el total es mayor a $10000")
    print(f"Descuento a aplicar: {descuento}")
    print(f"Total: {total}")


while True:
    es_club = input("¿Es miembro del club de clientes? (s/n): ")
    if es_club == "s" or es_club == "n":
        break
    else:
        print("Opción inválida. Por favor, ingrese 's' o 'n'.")
producto = cargar_producto()
cantidad_productos = len(productos)
if cantidad_productos > 0:
    subtotal = sumar_precios(productos)
    descuento = calcular_descuento(subtotal, cantidad_productos, es_club)
    total = subtotal - descuento
    mostrar_resumen(productos, subtotal, descuento, total)
else:
    print("no hay productos cargados")
