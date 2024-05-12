
"""""
Se quiere desarrollar el siguiente juego: el bingo.
Para hacer este juego vamos a simular el juego de la vida real poniendo una serie de reglas que deberemos cumplir:

Cada cartón:
o Tiene 2 números de cada rango numérico de 10 en 10, por ejemplo:  [ 1, 6, 12, 17, 21, 27, 35, 39, 46, 49, 50, 56, 62, 64, 71, 72, 82, 90 ]
o Siempre estarán ordenados de forma ascendente.
o Los números se generarán de forma aleatoria.
o Solo hay una excepción.

El número 90 estará dentro del último rango numérico (80-91 ambos incluidos).

Siempre habrá 3 jugadores
o El jugador 1 tendrá siempre 3 cartones diferentes.
o El jugador 2 tendrá siempre 2 cartones diferentes.
o El jugador 3 tendrá siempre 1 cartón.
o Los jugadores y sus cartones se almacenarán obligatoriamente en un diccionario, siendo la clave “JugadorX” y el valor una lista cartones.

La función que vaya sacando número tras número deberá ser una función generadora de iteradores. Esto números deberán salir de forma aleatoria.
La salida por pantalla despues de cada partida deberá tener el siguiente formato (y ajustarse lo máximo posible) :

Lista de jugadores junto con sus cartones.

Jugador que ha ganado y con qué cartón ha ganado.

Lista de números que han ido saliendo en la partida (tanto los ganadores como los que no) y cuantos han salido en total. Estos números no hay que ordenarlos, hay que dejarlos en el orden en el que han ido saliendo.

Posición de los números ganadores en función del carton ganador(aquí hay que fijarse en las comas y poner solo las necesarias).
"""""

import random

def generar_carton():
    carton = []
    for i in range(1, 91, 10):
        numerosCarton = sorted(random.sample(range(i, i+10), 2))
        carton.extend(numerosCarton)
    return carton


def jugadores():
    print("\n¡Bienvenido al juego!")
    cartonJugador1 = [generar_carton() for _ in range(3)]
    cartonJugador2 = [generar_carton() for _ in range(2)]
    cartonJugador3 = generar_carton()
    
    print( "\n El carton del jugador 1 es: " )
    for carton in cartonJugador1:
        print(carton)
    
    print( "\n El carton del jugador 2 es: " )
    for carton in cartonJugador2:
        print(carton)
        
    print( "\n El carton del jugador 3 es: \n", carton )
    
    
    return cartonJugador1, cartonJugador2, cartonJugador3
    
    
def juegoBingo(cartonJugador1, cartonJugador2, cartonJugador3):
    print("\n \t GENERAR BOMBO:")
    bombo_generado = random.sample(range(100), 100)
    print(bombo_generado)
    
    for numeroBombo in bombo_generado:
        if any (numeroBombo in carton for carton in cartonJugador1):
            print("¡El jugador 1 ha ganado")
            break
        elif any(numeroBombo in carton for carton in cartonJugador2):
            print("¡El jugador 2 ha ganado!")
            break
        elif numeroBombo in cartonJugador3:
            print("¡El jugador 3 ha ganado!")
            break
    else:
        print("No ha habido ganador en esta ronda.")
    

juegoBingo(*jugadores())