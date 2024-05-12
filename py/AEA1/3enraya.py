
import random

def dibujar_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)


def comprobar(tablero, simbolo):
    # Comprobar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == simbolo:
            return True

    # Comprobar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == simbolo:
            return True

    # Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
        return True

    # Si no hay ganador
    return False
        
tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
            
jugadores = ["X", "O"]
turno_actual = random.choice(jugadores)
            
while True:
    print(" Turno del jugador actual: ", turno_actual)
    tirada_fila = random.randint(0, 2)
    tirada_columna = random.randint(0, 2)
    
    if tablero[tirada_fila][tirada_columna] == " ":
        tablero[tirada_fila][tirada_columna] = turno_actual
    else:
        print(" Esta casilla está ocupada, intentando en otra...")
        continue
    
    dibujar_tablero(tablero)
            
    if comprobar(tablero, turno_actual):
        print("¡El jugador", turno_actual, "ha ganado!")
        break
    
    turno_actual = jugadores[(jugadores.index(turno_actual) + 1) % len(jugadores)]
    
    if all(all(celda != " " for celda in fila) for fila in tablero):
        print("¡Empate!")
        break


