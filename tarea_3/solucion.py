# Constantes
# PIN del usuario
PIN = 1234

# Fondos del usuario en su cuenta
fondos = 0


# Funciones de control del flujo
# Manejan la lógica principal del programa, validación y navegación
def validar_pin():
    input_pin = int(input('Ingresa tu PIN: '))
    if input_pin != PIN:
        print('PIN incorrecto, cerrando sesión...')
        exit(1)


def mostrar_menu_opciones() -> int:
    print('-------------------EASY ATM--------------------------')
    print('Elige una opción:')
    print('0: Salir\n1: Mostrar saldo actual\n2: Retirar dinero\n3: Depositar dinero')
    print('-----------------------------------------------------')

    try:
        opcion = int(input(': '))
        print('------------------------------------------------------\n')
        return opcion
    except: 
        print('La opcion seleccionada no es válida')
        return 0


# Funciones de operaciones bancarias
# Realizan las acciones específicas del cajero automático
def salir():
    print('Cerrando sesión...')
    exit(0)


def mostrar_fondos():
    print(f'Tienes ${fondos}\n')


def retirar_fondos():
    global fondos
    try:
        cantidad_retiro = int(input('Cuánto quieres retirar? '))
        if cantidad_retiro > fondos:
            print('No tienes suficientes fondos, intenta con una cantidad menor')
        else:
            fondos -= cantidad_retiro
            print(f'Has retirado ${cantidad_retiro}, te quedan ${fondos} en la cuenta')
    except:
        print('La cantidad ingresada, no es válida')


def depositar_fondos():
    global fondos
    try:
        cantidad_deposito = int(input('Cuánto quieres depositar? '))
        fondos += cantidad_deposito
        print(f'Has depositado ${cantidad_deposito}, ahora tienes ${fondos} en la cuenta')
    except:
        print('La cantidad ingresada, no es válida')


def ejecutar_funcion(opcion_elegida: int):
    match(opcion_elegida):
            case 0:
                salir()
            case 1:
                mostrar_fondos()
            case 2:
                retirar_fondos()
            case 3:
                depositar_fondos()
            case _:
                print('La opcion seleccionada no es válida')


def main():
    validar_pin()
    while True:
        opcion_elegida = mostrar_menu_opciones()
        ejecutar_funcion(opcion_elegida=opcion_elegida)



if __name__ == '__main__':
    main()