"""
Ejercicio 5: Crear un programa que utilice un diccionario para 
mapear nombres de productos y sus precios. Luego, convertir este 
diccionario en una lista de tuplas, donde cada tupla contenga el 
nombre del producto y su precio.
"""

def tienda():
    cant_productos = int(input(" introduzca la cantidad de articulos que desea agregar "))
    
    productos_tienda = {}
    
    for i in range(cant_productos):
        productos = input("introduzca el producto: ")
        precio = float(input(" introduzca su precio "))

        productos_tienda[productos] = precio
    
    # Convertir el diccionario a una lista de tuplas
    lista_tuplas = list(productos_tienda.items())
    print("Productos en la tienda:")
    for clave, valor in lista_tuplas:
        print(f"Producto: {clave}, Precio: {valor}")
# Llamada a la función
    
 

tienda()