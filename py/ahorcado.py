import random

def adivinar_letra_por_letra():
    palabras = ["perro", "gato", "casa", "árbol", "sol", "agua", "felicidad", "amor", "libertad", "viaje"]
    palabra_seleccionada = random.choice(palabras)
    longitud_palabra = len(palabra_seleccionada)
    palabra_adivinada = ["_"] * longitud_palabra
    
    print("¡Bienvenido al juego de adivinar la palabra letra por letra!")
    print("La palabra seleccionada tiene {} letras.".format(longitud_palabra))
    
    intentos = 5
    while intentos > 0 and "_" in palabra_adivinada:
        print("Palabra: ", " ".join(palabra_adivinada))
        letra = input("\nIntroduce una letra: ").lower()
        
        if len(letra) == 1 and letra.isalpha():
            if letra in palabra_seleccionada:
                print("¡Correcto! La letra '{}' está en la palabra.".format(letra))
                for i, char in enumerate(palabra_seleccionada):
                    if char == letra:
                        palabra_adivinada[i] = letra
            else:
                print("La letra '{}' no está en la palabra.".format(letra))
                intentos -= 1
                print("Te quedan {} intentos.".format(intentos))
        else:
            print("Entrada no válida. Introduce una sola letra.")

    if "_" not in palabra_adivinada:
        print("¡Felicidades! ¡Has adivinado la palabra correctamente!\n ", palabra_seleccionada.upper())
    else:
        print("¡Lo siento! Te has quedado sin intentos. La palabra correcta era '{}'.".format(palabra_seleccionada))

# Llamamos a la función para jugar
adivinar_letra_por_letra()
        

