# Practica 1: Cajero Automático

# Opciones del cajero
def consultar(saldo):
    print(f"💰 Su saldo actual es: {saldo}")
    return saldo

def retirar(saldo):
    monto = float(input("Ingrese cantidad a retirar: "))
    if monto <= 0:
        print("⚠️ El monto debe ser mayor a 0.")
    elif monto > saldo:
        print("❌ No hay suficiente dinero.")
    else:
        saldo -= monto
        print(f"✅ Retiro exitoso. Saldo restante: {saldo}")
    return saldo

def depositar(saldo):
    monto = float(input("Ingrese cantidad a depositar: "))
    if monto <= 0:
        print("⚠️ El monto debe ser mayor a 0.")
    else:
        saldo += monto
        print(f"✅ Depósito exitoso. Nuevo saldo: {saldo}")
    return saldo

# Programa principal
def cajero():
    PIN_CORRECTO = "4809"
    saldo = 1000
    intentos = 3

    # El PIN
    while intentos > 0:
        pin = input("Ingrese su PIN: ")
        if pin == PIN_CORRECTO:
            print("\n🎉 Bienvenido\n")
            break
        else:
            intentos -= 1
            if intentos == 0:
                print("🚫 Cuenta bloqueada.")
                return
            print(f"❌ PIN incorrecto. Intentos restantes: {intentos}")

    # Menú principal
    opcion = 0
    while opcion != 4:
        print("\n--- Menú ---")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            saldo = consultar(saldo)
        elif opcion == 2:
            saldo = retirar(saldo)
        elif opcion == 3:
            saldo = depositar(saldo)
        elif opcion == 4:
            print("👋 Adios.")
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

cajero()
