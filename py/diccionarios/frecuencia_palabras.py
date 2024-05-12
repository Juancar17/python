"""
Ejercicio 3: Crear un programa que cuente la frecuencia de las
palabras de una frase dada por el usuario y almacene los resultados
en un diccionario.
"""

def contar_palabras():

    frase_usuario = "El éxito es el resultado de la perseverancia, la perseverancia es la clave del éxito. Con esfuerzo y dedicación, se pueden lograr grandes cosas en la vida"

    palabras = frase_usuario.split()
    
    frecuencia_palabras = {}
    
    for palabra in palabras:
        
        palabra = palabra.lower()
        
        palabra = palabra.strip(",.;:!?\"\'")
        
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"'{palabra}':{frecuencia}")


contar_palabras() 
