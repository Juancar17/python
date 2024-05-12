"""
Enunciado:
Crea un programa en Python que tome una lista de palabras y mezcle aleatoriamente 
los caracteres de cada palabra,
excepto el primero y el último carácter. Por ejemplo, la palabra "Python" podría 
transformarse en "Pytnoh" o "Pyhotn",
mientras que "Hola" podría ser "Hloa" o "Halo".


import random
def mezclaPalabras(palabra):
    if len(palabra) <=3:
        return palabra
    
    listaPalabra = list(palabra)

    caracteres = listaPalabra[1:-1]
    random.shuffle(caracteres)

    palabra_mezclada = listaPalabra[0] + ' '.join(caracteres) + listaPalabra[-1]

    return palabra_mezclada

lista_palabras = ["Programación"]
for palabra in lista_palabras:
    print(mezclaPalabras(palabra))  
    
"""







"""


Requisitos:
- La lista de palabras debe estar predefinida en el programa con al menos 5 palabras distintas.
- Utiliza los módulos 'random' y 'string' para realizar las mezclas.
- Asegúrate de que el primer y el último carácter de cada palabra permanezcan en su lugar.
"""



"""
Enunciado:
Crea un programa en Python que simule el lanzamiento de un dado. 
El usuario debe poder especificar el número de caras del dado (por ejemplo, 
6 para un dado tradicional, 20 para un dado de rol, etc.). 
Después de especificar el número de caras, el programa debe generar y mostrar un resultado aleatorio
entre 1 y el número de caras del dado.

Requisitos:
- Pide al usuario que introduzca el número de caras del dado.
- Utiliza el módulo 'random' para generar el resultado aleatorio.
- Asegúrate de validar que el número de caras es un número válido mayor que 1.


import random

def lanzar_dado(num_caras):
    resultado = random.randint(1, num_caras)
    return resultado

# Pedir al usuario que ingrese el número de caras del dado
num_caras = int(input("Ingrese el número de caras del dado: "))

# Lanzar el dado y mostrar el resultado
resultado = lanzar_dado(num_caras)
print("El resultado del lanzamiento del dado de", num_caras, "caras es:", resultado)
"""


   




"""
Enunciado:
Crea un programa en Python que genere un número aleatorio entre 1 y 10 y permita al usuario adivinarlo.
El programa debe indicar si el intento del usuario es demasiado alto, demasiado bajo, 
o correcto. Después de adivinar correctamente, el programa debe preguntar al usuario si 
quiere jugar de nuevo.

Requisitos:
- Utiliza el módulo 'random' para generar el número aleatorio.
- El programa debe seguir ejecutándose hasta que el usuario decida no jugar más.
- Asegúrate de capturar y manejar los errores, como entradas no numéricas.

import random
def adivinaza(numero):
    numero = random.randint(1, 10)
    while True:
            jugador = int(input( " Adivina el numero del 1 al 10 \n" ))
            if jugador > 10:
                print(" el numero debe introducido debe ser menor a 10 ") 
                continue
            if jugador < numero:
                  print("Tu intento fue muy alto")
            elif jugador > numero:  
                print(" Tu intento fue muy alto")
                  
            else :
                if jugador == numero:
                  print("Felicidades, has ganado!, el resultado era: " , numero)
              
adivinaza(0)
"""



           

"""
Enunciado:
Crea un programa en Python que simule un sorteo. Dada una lista de nombres de participantes,
el programa debe seleccionar un ganador al azar y luego removerlo de la lista para evitar
que sea seleccionado nuevamente. Repite el proceso para seleccionar un segundo y tercer ganador,
asegurándote de que no se repitan los ganadores.

Requisitos:
- Utiliza una lista predefinida de nombres de participantes.
- Utiliza el módulo 'random' para seleccionar los ganadores.
- Asegúrate de que cada ganador sea único y muestre los nombres de los ganadores al final.

import random
def  juego_sorteo():
    #Lista de participantes
    participantes = ["Juan", "María", "Pedro", "Luis", "Ana", "Carlos"]
    ganadores = []
    print("Los participantes son: ",participantes)
    
    while len(ganadores) < 3:
        ganador = random.choice(participantes)
        
        if ganador not in ganadores:
            ganadores.append(ganador)
            participantes.remove(ganador)
            print("quedan: ", participantes)
    
    print("¡Los ganadores son:" , ganadores)

juego_sorteo()
"""


    
   

"""
Enunciado:
Crea un programa en Python que genere nombres de usuario aleatorios para 
una lista de nombres de personas. El nombre de usuario debe ser una 
combinación de una cadena aleatoria de tres letras (pueden ser mayúsculas o minúsculas)
seguido de un número aleatorio entre 100 y 999.

Requisitos:
- Utiliza una lista predefinida de nombres completos de personas.
- Utiliza los módulos 'random' y 'string' para generar las partes del nombre de usuario.
- Genera un nombre de usuario para cada persona en la lista



"""

import random
import string

# Lista de nombres completos de personas
nombres_completos = ["Juan Pérez", "María García", "Pedro Rodríguez", "Luis López", "Ana Martínez", "Carlos Sánchez"]

# Función para generar un nombre de usuario aleatorio
def generar_nombre_usuario(nombre_completo):
    # Obtener las iniciales del nombre completo
    iniciales = ''.join(word[0] for word in nombre_completo.split())
    # Generar una cadena aleatoria de tres letras
    letras_aleatorias = ''.join(random.choices(string.ascii_letters, k=3))
    # Generar un número aleatorio entre 100 y 999
    numero_aleatorio = random.randint(100, 999)
    # Combinar las partes para formar el nombre de usuario
    nombre_usuario = iniciales + letras_aleatorias + str(numero_aleatorio)
    return nombre_usuario

# Generar un nombre de usuario para cada persona en la lista
for nombre_completo in nombres_completos:
    nombre_usuario = generar_nombre_usuario(nombre_completo)
    print(f"{nombre_completo}: {nombre_usuario}")