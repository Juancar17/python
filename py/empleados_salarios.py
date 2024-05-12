"""
Ejercicio 2: Dado un diccionario con nombres de empleados y su salario,
calcular el salario medio, el salario más alto y el más bajo.


 
"""

def trabajo():
    
    empleados = {"Juan " :1300, "Maria" : 1540, "Julio" : 1120}
    
    for nombre, salario in empleados.items():
        print(" Trabajadores: \n" , nombre , " salario: " , salario) 
        
    sumasalarios=sum(empleados.values())
    
    mediaSalario = sumasalarios /  len(empleados)
    
    print("la media de salarios es: ", mediaSalario)

    SalarioMax = max(empleados, key=empleados.get)
    print("el salario maximo es el de: ", SalarioMax)
    
    SalarioMin = min(empleados, key=empleados.get)
    print("el salario minimo es el de : ", SalarioMin)

    
    

trabajo()    
