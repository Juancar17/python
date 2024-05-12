'''
Ejercicio 1
Crea un programa que procese una lista de tuplas, donde cada tupla representa una venta y contiene el nombre del producto,
la cantidad vendida y el precio unitario (ejemplo: [("manzana", 30, 0.50), ("banana", 20, 0.75)])
Filtra aquellos datos que tengan pocas unidades(menos de 10).
Quiero saber el total de ingresos de las ventas de estos productos

'''
from functools import reduce

ventas = [("manzana", 30, 0.50), ("banana", 20, 0.75), ("naranja", 5, 1.00), ("pera", 8, 0.60), ("melon", 25, 3.00)]
pocasUnidades = filter(lambda x : x[1] < 10, ventas)
print(list(pocasUnidades))
ingresos = map(lambda venta: venta[1] * venta[2], pocasUnidades)
ingresosTotales = reduce(lambda x, y: x + y, ingresos, 0)
print(f"El total de ingresos de las ventas con menos de 10 unidades es: ${ingresosTotales:.2f}")