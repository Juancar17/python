
def tabla():
    tablero = [["⬜"] * 8 for _ in range(8)]
    return tablero

def mostrar_tablero(tablero):
    print("\n")
    for fila in tablero:
        print(fila)


def generar_comecocos(tablero):
    import random
    posicionX = random.randint(0,7)
    posicionY = random.randint(0,7)
    tablero[posicionX][posicionY] = "😊"
    return tablero


def generar_comida(tablero):
    import random
    
    for _ in range(5):
        posicionX = random.randint(0,7)
        posicionY = random.randint(0,7)
        tablero[posicionX][posicionY] = "🍎" 
    return tablero


tablero = tabla()
tablero = generar_comecocos(tablero)
tablero = generar_comida(tablero)

for i in range(7):
    mostrar_tablero(tablero)