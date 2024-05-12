"""
Ejercicio 1: Crear un diccionario que almacene los nombres de estudiantes 
y sus notas finales. 
Luego, agregar funcionalidad para cambiar la nota de un estudiante y 
mostrar la nota modificada.



"""


def clase():
    estudiante = {"juan": 20 , "maria": 10}

    for nombre, nota in estudiante.items():
        print("estudiante: " , nombre, ", nota: ", nota)
    
    
    nombre = input("introduzca el nombre de estudiante que desea modificar la nota ")
    if nombre in estudiante:
        Nuevanota = input("introduzca la nota para: "  + nombre )
        estudiante[nombre] = Nuevanota
        print(" la nota del estudiante: ", nombre ," se ha actualizado a la nueva de nota de: " , Nuevanota)
    else:
        print("no se encontró el estudiante")
            
clase()