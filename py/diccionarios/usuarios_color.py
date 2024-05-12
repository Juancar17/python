"""

Ejercicio 4: Dado un diccionario que almacena las preferencias
de color de los usuarios, actualizar el diccionario agregando un 
conjunto de usuarios que prefieren el mismo color.
"""

def agregar_preferencia (preferencia_original, nuevo_conjunto):
    for color, usuario in nuevo_conjunto.items():
        if color in preferencia_original:
            preferencia_original[color].update(usuario)
        else:
            preferencia_original[color] = usuario
            
preferencia_original = {'azul': {'Juan', 'María'}, 'rojo': {'Pedro', 'Ana'}}
    
nuevo_conjunto = nuevo_conjunto = {'azul': {'Carlos', 'Laura'},'verde': {'Pablo', 'Sofía'}}
    
agregar_preferencia(preferencia_original, nuevo_conjunto)
    
print("Preferencias actualizadas:")
print(preferencia_original) 
        
