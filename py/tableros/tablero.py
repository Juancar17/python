# Crear matriz con el "👻" en la posición inicial (0, 0)
matriz = [[" ⬜"]*8 for _ in range(8)]
matriz[0][0] = "👻"

# Función para imprimir la matriz
def imprimir_tablero():
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()  # Salto de línea al final de cada fila
    print()

# Función para mover el "👻" por todo el recuadro
def mover_fantasma():
    # Coordenadas iniciales
    x, y = 0, 0
    dx, dy = 0, 1  # Dirección inicial: derecha

    for _ in range(64):  # Movimientos para cubrir todo el recuadro (8x8)
        matriz[x][y] = "👻"
        imprimir_tablero()
        matriz[x][y] = "🌱"  # Vaciar la posición anterior

        # Mover el "👻"
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
imprimir_tablero()

print("Moviendo el '👻' por todo el recuadro:")
mover_fantasma()

