import random

tablero = [["😊"]*8 for _ in range(8)]
tablero[0][0] = "🌱"

def imprimir_tablero():    
    for fila in tablero:
        print(fila)
    print()
    
    
def mover_fantasma():
    # Coordenadas iniciales
    x, y = 0, 0
    dx, dy = 0, 1  # Dirección inicial: derecha

    for _ in range(64):  # Movimientos para cubrir todo el recuadro (8x8)
        tablero[x][y] = "🌱"
        imprimir_tablero()
        tablero[x][y] = "⬜"  # Vaciar la posición anterior

        # Mover el "🌱👻"
        x += dx
        y += dy

        # Lógica para cambiar de fila o columna cuando alcanza los límites del recuadro
        if y >= 8:
            y = 0
            x += 1
            dx, dy = 0, 1  # Cambiar dirección hacia abajo
        elif y < 0:
            y = 7
            x -= 1
            dx, dy = 0, -1  # Cambiar dirección hacia arriba
    
# Prueba de la función
print("Tablero inicial:")
def generarElementos():
    elementos = ["🥥", "🍇"]
    for elemento in elementos:
        cantidad = 0
        while cantidad < 4:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if tablero[x][y] == "😊":
                tablero[x][y] = elemento
                cantidad =+ 1               

imprimir_tablero()
print("Moviendo el '👻' por todo el recuadro:")
mover_fantasma()



   