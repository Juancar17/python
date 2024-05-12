from Tablero import Tablero


colocarFicha = int(input(" Coloca la columna "))
tablero1 = Tablero()
while True:
    tablero1.imprimirTablero()
    tablero1.colocarFichas(colocarFicha)
    tablero1.imprimirTablero()  

