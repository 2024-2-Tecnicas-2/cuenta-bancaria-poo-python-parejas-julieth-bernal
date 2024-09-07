from cuenta_bancaria import CuentaBancaria

def main():
    print("Bienvenido al banco")
    titular = input("Ingresa tu nombre: ")
    numero_cuenta = input("Ingresa tu número de cuenta: ")
    saldo = float(input("Ingresa tu saldo inicial: "))

    mi_cuenta = CuentaBancaria(titular, numero_cuenta, saldo)

    # Mostrar saldo
    print("Tu saldo actual es:", mi_cuenta.get_saldo())

    # Ingresar dinero
    cantidad_ingresar = float(input("¿Cuánto dinero quieres ingresar? "))
    mi_cuenta.ingresar(cantidad_ingresar)
    print("Tu nuevo saldo es:", mi_cuenta.get_saldo())

    # Retirar dinero
    cantidad_retirar = float(input("¿Cuánto dinero quieres retirar? "))
    mi_cuenta.retirar(cantidad_retirar)
    print("Tu nuevo saldo es:", mi_cuenta.get_saldo())

    # Calcular saldo con interés
    saldo_con_interes = mi_cuenta.calcular_interes()
    print("Tu saldo con el interés aplicado es:", saldo_con_interes)

if __name__ == "__main__":
    main()