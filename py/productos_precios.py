"""
Ejercicio 7: Dado un diccionario de productos y precios,
escribir un programa que convierta los precios a otra moneda
(por ejemplo, de euros a dólares) utilizando un tipo de cambio 
fijo, y guarde los resultados en un nuevo diccionario.
"""

def conversorPrecio(diccionario, tipoCambio):
    nuevoDiccionario = {}
    for producto, precio in diccionario.items():
        nuevoPrecio = precio * tipoCambio
        nuevoDiccionario[producto] = nuevoPrecio
    return nuevoDiccionario
    




def tienda():
    
    cant_productos = int(input(" introduzca la cantidad de productos que desea añadir "))
    
    productos_tienda = {}
    
    for i in range(cant_productos):
        
        productos = input("introduzca el producto ")
        precios =   float(input("introduzca el precio "))
        productos_tienda[productos] = precios
    
    for producto, precio in productos_tienda.items():
        print(f"{producto}: {precio}" , "euros")
        
    tipo_cambio = 1.14
    
    productos_tienda_dolares = conversorPrecio(productos_tienda, tipo_cambio)
    
    print("\nProductos en la tienda (en dólares):")
    for producto, precio in productos_tienda_dolares.items():
        print(f"{producto}: {precio:.2f} dólares")
    
tienda()