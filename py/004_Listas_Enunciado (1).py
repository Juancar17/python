"""
Ejercicio 1:
Crear una lista vacía y agregar elementos.
Escribe un programa que cree una lista vacía llamada "mi_lista" y agregue los números del 1 al 5 a esta lista.

def lista():
    lista1 = []
    
    for i in range(1, 6):
        lista1.append(i)
    
    print(lista1)

lista()

"""


"""
Ejercicio 2:
Acceder a elementos de una lista.
Escribe un programa que defina una lista llamada "colores" que contenga los nombres de varios colores y muestre el primer y el último elemento de la lista.




def lista():
    
    colores = ["rojo", "azul", "verde", "amarillo"]
    
    # Accediendo al primer elemento de la lista
    primero = colores[0]
    print("El primer color es ", primero)
    
    # Accediendo al último elemento de la lista
    ultimo = colores[-1]
    print("El último color es ", ultimo)
    
    # Accediendo a un elemento por su índice (posición en la lista)
    tercero = colores[2]
    print("\nEl tercer color es ", tercero)


lista()

"""





"""
Ejercicio 3:
Modificar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y cambie el tercer elemento de la lista por el número 10.
"""


"""
Ejercicio 4:
Eliminar elementos de una lista.
Escribe un programa que tenga una lista de nombres de frutas y elimine el segundo elemento de la lista.
"""

"""
Ejercicio 5:
Contar elementos de una lista.
Escribe un programa que cuente cuántas veces aparece la palabra "perro" en una lista dada.
"""

"""
Ejercicio 6:
Crear una lista a partir de elementos ingresados por el usuario.
Escribe un programa que solicite al usuario ingresar 5 nombres y cree una lista con estos nombres.
"""


"""
Ejercicio 7:
Concatenar dos listas.
Escribe un programa que tenga dos listas de números y las concatene para formar una sola lista.
"""


"""
Ejercicio 8:
Ordenar una lista alfabéticamente.
Escribe un programa que tenga una lista de nombres de países y los ordene alfabéticamente.
"""


"""
Ejercicio 9:
Reemplazar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y reemplace los elementos del segundo al cuarto por el número 0.
"""


"""
Ejercicio 10:
Buscar un elemento en una lista.
Escribe un programa que tenga una lista de números y verifique si el número 5 está presente en la lista.
"""

"""
Ejercicio 11:
Calcular la longitud de una lista.
Escribe un programa que tenga una lista de colores y calcule cuántos elementos tiene la lista.
"""

"""
Ejercicio 12:
Crear una lista de números pares.
Escribe un programa que cree una lista de los primeros 5 números pares a partir de un rango.
Agrega esos números pares a una lista
"""


"""
Ejercicio 13:
Sumar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y sume todos sus elementos.
"""


"""
Ejercicio 14:
Contar elementos mayores que un número dado.
Escribe un programa que tenga una lista de números y cuente cuántos elementos son mayores que 5.
"""


"""
Ejercicio 15:
Eliminar duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine los duplicados de la lista.
"""

"""
Ejercicio 16:
Multiplicar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y multiplique todos sus elementos entre sí.
"""


"""
Ejercicio 17:
Comprobar si una lista está vacía.
Escribe un programa que determine si una lista dada está vacía o no.
"""


"""
Ejercicio 18:
Calcular el promedio de una lista de números.
Escribe un programa que tenga una lista de números y calcule el promedio de esos números.
"""

"""
Ejercicio 19:
Calcular la suma de los elementos pares de una lista.
Escribe un programa que tenga una lista de números y calcule la suma de todos los elementos pares en la lista.
"""


"""
Ejercicio 20:
Reemplazar todos los elementos de una lista con un valor dado.
Escribe un programa que tenga una lista de números y reemplace todos sus elementos por un valor dado.
"""

"""
Ejercicio 21:
Invertir una lista.
Escribe un programa que tenga una lista de números y la invierta, es decir, que el primer elemento se convierta en el último y viceversa.
"""


"""
Ejercicio 22:
Dividir una lista en partes iguales.
Escribe un programa que tenga una lista de números y la divida en partes iguales de longitud especificada por el usuario.
"""


"""
Ejercicio 23:
Ordenar una lista en orden descendente.
Escribe un programa que tenga una lista de números y la ordene en orden descendente.
"""


"""
Ejercicio 24:
Unir dos listas en una sola.
Escribe un programa que tenga dos listas de números y las una en una sola lista.
"""

"""
Ejercicio 25:
Eliminar todos los elementos duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine todos los duplicados, dejando solo una ocurrencia de cada elemento.
"""

'''
Ejercicio 26:
Ordenar una lista de cadenas alfabéticamente sin distinción entre mayúsculas y minúsculas:

Escribe un programa que solicite al usuario ingresar una lista de palabras 
y luego ordene la lista alfabéticamente sin distinguir entre mayúsculas y minúsculas.
Además, el programa debe eliminar cualquier palabra duplicada antes de realizar la ordenación.
'''

'''
Ejercicio 27
Escribe un programa que genere dos listas de números aleatorios entre 1 y 20 
y luego calcule e imprima la intersección de estas dos listas,
es decir, los números que aparecen en ambas listas.
Asegúrate de que no haya duplicados en las listas generadas.
'''


'''
Ejercicio 28
Eliminar elementos repetidos de una lista manteniendo el orden original:

Escribe un programa que reciba una lista de números y elimine los elementos 
repetidos de la lista manteniendo el orden original.
'''
import random

def elminiar():
    numeros = list(range(1, 100)) + [99]  # Lista del 1 al 99, con el 99 añadido varias veces
    print(numeros)
    
elminiar()
'''
Ejercicio 29
Calcular la media de una lista de números:
Escribe un programa que calcule la media de una lista de números ingresada por el usuario.


def media():
    insertar_numeros = int(input(" ingrese la cantidad de numeros a calcular"))
    numeros=[]
    for i in  range (insertar_numeros):
        
        num = float(input("Ingrese el número {}: ".format(i + 1)))
        
        numeros.append(num)
        
    if len(numeros) > 0:
        promedio = sum(numeros) / len(numeros)
        print(" la media de la suma de los numeros ingresados es: " , promedio)
    else:
        print("No se puede realizar la operación.")
        
media()      

'''

  
    




'''
Ejercicio 30
Encontrar el elemento más grande y el más pequeño en una lista:
Escribe un programa que encuentre el elemento más grande y el más pequeño en una lista de números.

import random

def elementos():
    numeros = []
    
    numerosRandoms = random.sample(range(1, 21), 10, ) # Genera 5 números aleatorios entre 1 y 20 sin repeticion
    
    numeros.extend(numerosRandoms)
    print(numeros)
    
    minimo = min(numeros)
    maximo = max(numeros)
    
    print("El elemento más grande es:", maximo)
    print("El elemento más pequeño es:", minimo)
    
elementos()
'''




