"""
Ejercicio 6: Crear un diccionario que almacene como clave el
nombre de un país y como valor un set de ciudades de ese país.
Añadir después una nueva ciudad a uno de los países y mostrar 
el diccionario actualizado.

"""
def  crea_dicc():
    paises = [" España", " Francia"," Alemania"]
    ciudades = ["Madrid","París","Berlín"]
    
    paises_ciudades = {}
    
    for pais, ciudad in zip(paises, ciudades):
        paises_ciudades[pais] = ciudad 
    
    print("\n" , paises_ciudades)
    
    ciudadesNuevas = ["Barcelona" , "Marsella" , "Munich"]
  
    for pais, ciudad in zip (paises, ciudadesNuevas):
        paises_ciudades.update({pais : {paises_ciudades[pais], ciudad}})
        
    print(paises_ciudades)
    
crea_dicc()
