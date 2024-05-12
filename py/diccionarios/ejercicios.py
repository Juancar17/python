
""""
Escribe un programa que procese una lista de tuplas que representan ventas de productos.
Cada tupla contiene el nombre del producto, la cantidad vendida y el precio unitario. 
El programa debe realizar las siguientes operaciones:

Filtrar aquellas ventas que tengan una cantidad vendida superior a 50 unidades.
Calcular el total de ingresos de las ventas filtradas.
"""
from functools import reduce
class Productos:
    def __init__(self, frutas, precio, unidades):
        self.frutas = frutas
        self.precio = precio
        self.unidades = unidades
        
    def verFrutas(self):
        ventas = [("manzana", 30, 1.2), ("pera", 45, 0.8), ("naranja", 60, 1.5)]
        for frutas, unidades, precio in ventas:
            print(f"Las frutas son: {frutas}, unidades = {unidades} precio:{precio}")
        
        ventas_superior = list(filter(lambda x: x[1] > 50, ventas))
        print(f"Los productos que tienen unidades mayor a 60 son: {ventas_superior}")
        
        calcular_total = reduce(lambda x, y: (y[1]  *  y[2]), ventas_superior, 0)
        print("la suma de cantidades vendidads es: ", calcular_total)
        
# Crear una instancia de la clase Productos
productos = Productos("frutas", "unidades", "precio")

# Llamar al método verFrutas para mostrar las ventas de frutas
productos.verFrutas()

print("----------------------------------------------------------------------------------")
'''
Ejercicio 4
Crea un programa que analice una lista de comentarios de usuarios en una red social. 
Cada comentario es un texto que puede contener emociones positivas o negativas. 
El programa debe filtrar los comentarios que contengan al menos una palabra clave negativa, 
analizar el sentimiento general de los comentarios filtrados y calcular el porcentaje de comentarios negativos respecto al total de comentarios analizados.
Crea una lista de palabras con comentarios positivos y comentarios negativos que te ayuden en el filtrado
'''

# Lista de comentarios de usuarios en una red social
comentarios = [
    "Me encanta el nuevo diseño de la plataforma!",
    "Es terrible cómo se manejan los bugs aquí.",
    "¡Excelente trabajo con las actualizaciones!",
    "Odio la lentitud del sistema ahora.",
    "No estoy contento con el servicio de atención al cliente.",
    "¡Bravo por los esfuerzos!",
    "El peor cambio que han hecho hasta ahora."
]

palabras_positivas = ['encanta', 'excelente', 'bravo', 'bueno', 'genial']
palabras_negativas = ['terrible', 'odio', 'lentitud', 'no estoy contento', 'peor']

def es_negativo(comentario):
    return any(palabra in comentario.lower() for palabra in palabras_positivas)

comentarios_negativos = list(filter(es_negativo, comentarios))
print('Comentarios positivos:\n', '\n'.join(comentarios_negativos))

totalComentarios= len(comentarios)
comentarios_Negativos = len(comentarios_negativos)

porcentaje_comentarios_negativos = (comentarios_Negativos / totalComentarios) * 100
print(f"Porcentaje de comentarios negativos: {porcentaje_comentarios_negativos:2f}%")
print("!--------------------------------------------------------------------------!")
"""
Desarrolla un programa que maneje una lista de reservas de un hotel. 
Cada reserva está representada por un diccionario que incluye información como el nombre del cliente, número de noches reservadas y tipo de habitación.
El objetivo es identificar aquellas reservas que exceden una estancia de 5 noches, procesar la información para calcular el total 
de noches reservadas por esos clientes y determinar el tipo de habitación más demandado entre esas reservas largas.
"""
# Lista de reservas en un hotel
from functools import reduce
reservas = [
    {"nombre": "Carlos", "noches": 4, "tipo_habitacion": "estándar"},
    {"nombre": "María", "noches": 7, "tipo_habitacion": "suite"},
    {"nombre": "Juan", "noches": 5, "tipo_habitacion": "estándar"},
    {"nombre": "Elena", "noches": 9, "tipo_habitacion": "suite"},
    {"nombre": "Pedro", "noches": 6, "tipo_habitacion": "doble"},
    {"nombre": "Lucía", "noches": 3, "tipo_habitacion": "estándar"}
]

def numeroNoches():
    reservas_largas = list(filter(lambda x: x["noches"] > 5, reservas))
    print(reservas_largas)
    
    
    noches_reservadas = list(map(lambda x: x["noches"], reservas_largas,))
    print(" Noches rerservadas:" ,noches_reservadas)
    
    calcularTotal = reduce(lambda x, y: x + y, noches_reservadas, 0)
    print("El total de noches reservadas es:" ,calcularTotal)

    tipo_habitacion = {}
    for habitacion in reservas:
        habitaciones = habitacion["tipo_habitacion"]
        print("Las habitaciones: ", habitaciones)

        if habitaciones in tipo_habitacion:
            tipo_habitacion[habitaciones] =+ 1
        else:
            tipo_habitacion[habitaciones]=1
            
        contador = 0
    
        if habitaciones <= 1:
            contador += 1
        else:
            print("No hay habitaciones disponibles")
    
    print("Total de habitaciones ocupadas: ", habitaciones - contador)
            
    habitaciones_masDemandadas= max(tipo_habitacion, key=tipo_habitacion.get)
    print(f"Las habitaciones mas demandadas son: {habitaciones_masDemandadas}")
    
   
    
numeroNoches()

