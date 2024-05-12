from Ficha import Ficha

class Tablero():
    def __init__(self):
        self.tablero = tablero  = [["⬜" for _ in range(9)] for _ in range(8)]

    
    def imprimirTablero(self):
        for fila in self.tablero:
            print(fila)
            
    def comprobarColumnas(self, columna):
        for fila in range(len(self.tablero)):
            if  self.tablero[fila][columna] == "⬜":
                return fila
            else:
                continue
        return -1
    
    def colocarFichas(self, columna):
        fila = self.comprobarColumnas(columna)
        if fila != -1:
            self.tablero[fila][columna]="😊"
            return True
        else:
            return False

    def validarColocacion(self, columna, ficha):
        if self.colocarFichas(columna, ficha):
            print("¡Enhorabuena! Has colocado una ficha en la columna", columna+1,"!\n")
            return True
        else:
            print("\nEsta casilla ya tiene una ficha.\nIntenta otra vez.")
        
        