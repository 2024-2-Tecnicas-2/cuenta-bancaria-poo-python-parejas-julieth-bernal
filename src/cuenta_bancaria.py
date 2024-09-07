class CuentaBancaria:
    # TODO: Aquí va el código de la clase CuentaBancaria
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.tipo_interes = 1.5  

    def get_saldo(self):
        return self.saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("No tienes suficiente saldo.")

    def calcular_interes(self):
        return self.saldo + (self.saldo * self.tipo_interes / 100)
