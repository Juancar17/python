import random

def generar_carton():
    carton = []
    for i in range(1, 91, 10):
        numerosCarton = sorted(random.sample(range(i, i+10), 2))
        carton.extend(numerosCarton)
    return carton

def generar_jugadores():
    jugadores = {}
    jugadores['Jugador1'] = [generar_carton() for _ in range(3)]
    jugadores['Jugador2'] = [generar_carton() for _ in range(2)]
    jugadores['Jugador3'] = [generar_carton()]
    return jugadores

def generar_numeros():
    numeros = list(range(1, 91))
    random.shuffle(numeros)
    for numero in numeros:
        yield numero

def verificar_ganador(jugadores, numeros_generados):
    for jugador, cartones in jugadores.items():
        for i, carton in enumerate(cartones):
            if all(numero in numeros_generados for numero in carton):
                return jugador, i + 1
    return None, None

def jugar_bingo():
    jugadores = generar_jugadores()
    numeros_generados = generar_numeros()
    numeros_sacados = []
    while True:
        try:
            numero = next(numeros_generados)
            numeros_sacados.append(numero)
            print(f"Número sacado: {numero}")
            ganador, carton = verificar_ganador(jugadores, numeros_sacados)
            if ganador:
                break
        except StopIteration:
            break
    print("\nLista de jugadores junto con sus cartones:")
    for jugador, cartones in jugadores.items():
        print(f"{jugador}: {cartones}")
    print(f"\nJugador que ha ganado: {ganador} con el cartón número: {carton}")
    print(f"\nLista de números que han ido saliendo en la partida:")
    print(numeros_sacados)
    print(f"\nTotal de números sacados en la partida: {len(numeros_sacados)}")
    print("\nPosición de los números ganadores en función del cartón ganador:")
    if ganador:
        ganador_carton = jugadores[ganador][carton - 1]
        for numero in ganador_carton:
            if numero in numeros_sacados:
                print(ganador_carton.index(numero) + 1, end=", ")
    print("\n")

jugar_bingo()
