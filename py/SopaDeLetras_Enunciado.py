'''
La siguiente lista de listas simula una sopa de letras.
Se quiere realizar una función que diga la coordenada de origen de la palabra y la dirección hacia la que se ha encontrado la palabra
Recuerda que hay 8 direcciones:
    1-hacia arriba
    2-hacia abajo
    3-hacia derecha
    4-hacia izquierda
    5-diagonal a la derecha y hacia arriba
    6-diagonal a la derecha y hacia abajo
    7-diagonal a la izquierda y hacia arriba
    8-diagonal a la izquierda y hacia abajo
    
    
La solución ES la siguiente:
    -La palabra PYTHON comienza en la coordenada X y va en la dirección Y
    -La palabra PAPA comienza en la coordenada X y va en la dirección Y
    -La palabra DATOS comienza en la coordenada X y va en la dirección Y
    -La palabra COCHAZO comienza en la coordenada X y va en la dirección Y
    -La palabra TROPECIENTOS no se encuentra en la sopa de letras
Obviamente hay que sustituir la X por la coordenada de la primera letra y la Y por la dirección hacia donde está la palabra
'''



sopaLetras = [
    ['P', 'Y', 'T', 'H', 'O', 'N', 'A', 'C', 'W', 'Q'],
    ['I', 'T', 'E', 'X', 'U', 'S', 'O', 'B', 'V', 'R'],
    ['N', 'U', 'H', 'N', 'J', 'O', 'I', 'O', 'W', 'L'],
    ['T', 'G', 'C', 'M', 'K', 'T', 'Z', 'L', 'P', 'K'],
    ['E', 'I', 'D', 'O', 'F', 'A', 'G', 'K', 'X', 'J'],
    ['L', 'A', 'T', 'O', 'H', 'D', 'M', 'F', 'Y', 'Z'],
    ['I', 'N', 'G', 'C', 'E', 'O', 'N', 'Z', 'T', 'U'],
    ['G', 'J', 'O', 'C', 'Y', 'U', 'W', 'R', 'E', 'S'],
    ['E', 'C', 'O', 'P', 'R', 'E', 'Q', 'K', 'F', 'I'],
    ['N', 'C', 'A', 'A', 'P', 'A', 'P', 'Ñ', 'H', 'A'],
]
# Palabras a buscar
palabras = ["PYTHON", "PAPA", "DATOS","COCHAZO","TROPECIENTOS"]

'''
sopaLetras = [
  ['Y', 'W', 'D', 'E', 'N', 'V', 'U', 'D', 'M', 'R'],
  ['A', 'Q', 'C', 'V', 'U', 'J', 'Y', 'O', 'A', 'D'],
  ['O', 'L', 'W', 'T', 'N', 'M', 'G', 'M', 'Z', 'J'],
  ['W', 'E', 'G', 'T', 'G', 'I', 'A', 'P', 'R', 'V'],
  ['F', 'G', 'N', 'U', 'D', 'R', 'X', 'L', 'L', 'B'],
  ['Q', 'J', 'B', 'O', 'R', 'K', 'W', 'X', 'N', 'R'],
  ['K', 'E', 'C', 'O', 'B', 'I', 'I', 'U', 'A', 'I'],
  ['D', 'F', 'R', 'S', 'O', 'L', 'T', 'W', 'W', 'I'],
  ['B', 'P', 'S', 'V', 'P', 'L', 'J', 'M', 'U', 'G'],
  ['K', 'T', 'S', 'V', 'Z', 'O', 'C', 'H', 'O', 'D']]
# Palabras a buscar
palabras = ['PROGRAMAR', 'ALGORITMO', 'DEBUG', 'CODIGO']
'''