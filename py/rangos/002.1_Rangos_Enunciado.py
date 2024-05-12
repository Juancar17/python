"""
Ejercicio 1: Creación de un Rango Simple
Define un rango que vaya desde 0 hasta 5 (inclusive).
Imprime el rango creado.


def rango():
    for n in range(0, 6):
        print(n)

rango()

"""




"""
Ejercicio 2: Creación de un Rango con Inicio y Fin Específicos
Define un rango que vaya desde 5 hasta 10 (inclusive).
Imprime el rango creado.

def rango():
    for i in range(5, 11):
        print(i)

rango()
"""


"""
Ejercicio 3: Creación de un Rango con Incremento Específico
Define un rango que vaya desde 1 hasta 10 (inclusive) con incremento de 2.
Imprime el rango creado.

def rango():
    for i in range(1, 11, 2):
        print(i +1)

rango()

"""



"""
Ejercicio 4: Iteración sobre un Rango Simple
Itera sobre un rango que vaya desde 0 hasta 3 (inclusive).
Imprime cada valor del rango en una línea separada.


"""

"""
Ejercicio 5: Iteración sobre un Rango con Incremento Específico
Itera sobre un rango que vaya desde 0 hasta 10 (inclusive) con incremento de 2.
Imprime cada valor del rango en una línea separada.
"""

"""
Ejercicio 6: Uso de Rangos en Funciones de Control de Flujo
Itera sobre un rango que vaya desde 10 hasta 1 (inclusive) con decremento de 1.
Imprime cada valor del rango en una línea separada.
"""

"""
Ejercicio 7: Uso de Rangos en Condicionales
Verifica si un número ingresado por el usuario está dentro de un rango predefinido.
"""

"""
Ejercicio 8: Uso de Rangos para Generar Secuencias de Números
Genera una lista de números pares en el rango de 0 a 10 (inclusive).
Imprime la lista resultante.
"""

"""
Ejercicio 9: Uso de Rangos para Sumar Elementos
Calcula la suma de todos los números en el rango de 1 a 100 (inclusive).
Imprime el resultado de la suma.
"""

"""
Ejercicio 10: Uso de Rangos para Contar Elementos
Cuenta cuántos números pares hay en el rango de 1 a 50 (inclusive).
Imprime el total de números pares.
"""

"""
Ejercicio 11: Uso de Rangos en una Función
Define una función llamada `imprimir_rango` que reciba un parámetro `limite`.
La función debe imprimir todos los números desde 0 hasta el `limite` (inclusive) utilizando un rango.
"""

"""
Ejercicio 12: Uso de Rangos en una Función con Paso Personalizado
Define una función llamada `imprimir_rango_paso` que reciba tres parámetros: `inicio`, `fin` y `paso`.
La función debe imprimir todos los números desde `inicio` hasta `fin` (inclusive) utilizando un rango con el paso especificado.
"""

"""
Ejercicio 13: Uso de Rangos para Generar Secuencias de Caracteres
Genera una lista de letras del alfabeto inglés (minúsculas) utilizando un rango.
Imprime la lista resultante.

import string

alfabeto = string.ascii_lowercase
listaAlfabeto = list(alfabeto)
print(listaAlfabeto)

"""





"""
Ejercicio 14: Uso de Rangos para Generar Patrones
Genera un patrón numérico en forma de triángulo utilizando un rango y la función `join()`.
Imprime el patrón resultante.

def imprimir_triangulo(n):
    for i in range (1, n +1):
        numeros = [str(num) for num in range (1, i + 1)]
        print(' '.join(numeros))
        
n = int(input("introduzca el valor de n"))
imprimir_triangulo(n)
"""





"""
Ejercicio 15: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón numérico en forma de triángulo invertido utilizando un bucle for.
Imprime el patrón resultante.


def triangulo(n):
    for i in range (n, 0, -1):
        print(" " * (n - i), end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
n = int(input("introduzca el valor de n"))
triangulo(n)
"""



"""
Ejercicio 16: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de asteriscos en forma de pirámide utilizando un bucle for.
Imprime el patrón resultante.
"""

"""
Ejercicio 17: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de números en forma de diamante utilizando un bucle for.
Imprime el patrón resultante.
"""

"""
Ejercicio 18: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de pirámide utilizando un bucle for.
Imprime el patrón resultante.
"""

"""
Ejercicio 19: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de pirámide invertida utilizando un bucle for.
Imprime el patrón resultante.


def imprimir_piramide_invertida(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = 5

# Llamar a la función para imprimir la pirámide invertida
imprimir_piramide_invertida(n)
"""





"""
Ejercicio 20: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de diamante utilizando un bucle for.
Imprime el patrón resultante.

def triangulo(n):
    for i in range(n):
        print(" "  * (n - i - 1), "*" * (2 * i + 1))
    
  
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

n= 5

triangulo(n)
"""
