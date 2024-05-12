class cuentaBancaria():
    base_datos = {}
    
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        cuentaBancaria.base_datos[numeroCuenta] = self
    
    @classmethod
    def crearUsusario(self):
        titular=input("Introduce el nombre del nuevo usuario: ")
        numeroCuenta= int(input(" Introduzca su numero de cuenta"))
        
        if numeroCuenta in self.base_datos:
            print(" El numero de cuenta ya existe")
            return None
        saldoInicial = float(input("Introduce el saldo inicial de la cuenta: "))
        nuevaCuenta = self(titular, numeroCuenta, saldoInicial)
        return nuevaCuenta
        
    def retirar_fondos(self):
    
        while True:
            
            cantidad = int(input("Introduzca la cantidad que desea retirar"))
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Se ha retirado ${cantidad:.2f}. Saldo restante: ${self.saldo:.2f}")
            else:
                print("Saldo insuficiente. No se puede realizar el retiro.")
                continue

nuevaCuenta = cuentaBancaria.crearUsusario()
if nuevaCuenta:
    print(f"Titular: {nuevaCuenta.titular}, Número de Cuenta: {nuevaCuenta.numeroCuenta}, Saldo: ${nuevaCuenta.saldo:.2f}")

    # Retirar fondos de la cuenta
    nuevaCuenta.retirar_fondos()
