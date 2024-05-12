'''
Ejercicio 1
Crea un programa que procese una lista de tuplas, donde cada tupla representa una venta y contiene el nombre del producto,
la cantidad vendida y el precio unitario (ejemplo: [("manzana", 30, 0.50), ("banana", 20, 0.75)])
Filtra aquellos datos que tengan pocas unidades(menos de 10).
Quiero saber el total de ingresos de las ventas de estos productos
'''
from functools import reduce
productos =  [("manzana", 30, 0.50), ("banano", 20, 0.75), ("tomates", 5, 0.42) , ("cebollas" ,8, 0.69)]
filtrado= list(filter(lambda x :x[1] < 10 , productos))
print(f"Productos con menos de 10 unidades: {filtrado}")
ingresos = map(lambda x: x[1] * x[2], filtrado)
totalVentas = reduce(lambda x, y : x + y, ingresos, 0)
print(f"El total de venta de los productos {filtrado} es de {totalVentas}")


""""
Ejercicio 2
Dado un diccionario que contiene el nombre del estudiante y su lista de calificaciones 
(por ejemplo, {"Ana": [4.5, 7.0, 8.0], "Juan": [5.0, 7.5, 6.0]}). Se requiere calcular el promedio de calificaciones de cada estudiante
seleccionando solo aquellos estudiantes con un promedio superior a 6.0.
Además, se quiere determinar el número total de estudiantes que superan este promedio.
"""""
print("------------------------------------------")
calificaciones = {
    "Ana": [4.5, 7.0, 8.0],
    "Juan": [5.0, 7.5, 6.0],
    "Maria": [7.0, 8.5, 9.0],
    "Luis": [5.5, 6.0, 5.0]
}
calificacion = dict(map(lambda item : (item[0], sum(item[1]) / len(item[1])), calificaciones.items()))#Extraigo la lista de calificaciones
print(calificacion)
sobresalietes = dict(filter(lambda item : item[1] > 6.0 , calificacion.items()))
print(sobresalietes)
contar_estudiantes = reduce(lambda x, _: x + 1, sobresalietes.items(), 0)
print(contar_estudiantes)



'''
Ejercicio 3
Considera que tienes una lista de diccionarios, cada uno representando a una persona con claves 
como nombre, edad y ciudad. Se quiere poder filtrar las personas para seleccionar solo las personas que pertenecen a una ciudad específica.
Los datos devueltos tienen que ser la edad promedio de las personas de la ciudad seleccionada.
'''
print("------------------------------------------")

personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Carlos", "edad": 32, "ciudad": "Barcelona"},
    {"nombre": "Marta", "edad": 45, "ciudad": "Madrid"},
    {"nombre": "Pablo", "edad": 22, "ciudad": "Valencia"},
    {"nombre": "Lorena", "edad": 29, "ciudad": "Madrid"},
    {"nombre": "Jordi", "edad": 35, "ciudad": "Barcelona"}
]

ciudad_filtrada = "Madrid"
personas_ciudad = list(filter(lambda p: p["ciudad"] == ciudad_filtrada, personas))
print(f"\nLas personas que viven en  {ciudad_filtrada} son: \n{personas_ciudad}")
filtro_edad = "edad"
filtrado_edad = list(map(lambda edad : edad["edad"], personas_ciudad))
promedoEdad = sum(filtrado_edad) / len(filtrado_edad)
print(f"El promedio de edad para personas de {ciudad_filtrada} es: {promedoEdad} años \n")

'''
Ejercicio 4
Crea un programa que analice una lista de comentarios de usuarios en una red social. 
Cada comentario es un texto que puede contener emociones positivas o negativas. 
El programa debe filtrar los comentarios que contengan al menos una palabra clave negativa, 
analizar el sentimiento general de los comentarios filtrados y calcular el porcentaje de comentarios negativos respecto al total de comentarios analizados.
Crea una lista de palabras con comentarios positivos y comentarios negativos que te ayuden en el filtrado
'''

comentarios = [
    "Me encanta el nuevo diseño de la plataforma!",
    "Es terrible cómo se manejan los bugs aquí.",
    "¡Excelente trabajo con las actualizaciones!",
    "Odio la lentitud del sistema ahora.",
    "No estoy contento con el servicio de atención al cliente.",
    "¡Bravo por los esfuerzos!",
    "El peor cambio que han hecho hasta ahora."
]
print("------------------------------------------")
palabras_positivas = ['encanta', 'excelente', 'bravo', 'bueno', 'genial']
palabras_negativas = ['terrible', 'odio', 'lentitud', 'no estoy contento', 'peor']


palabras = filter(lambda x : x.lower(), palabra in palabras)
print(palabras)