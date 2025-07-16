from utilidades_csv import leer_csv, actualizar_csv
from utilidades_lista_entradas import listar_entradas, eliminar_entrada, revelar_contrasena_de_entrada
from crear_entrada import crear_entrada
from utilidades_cifrado import generar_llave_cifrado

CONTRASENA_MAESTRA = '1'

def pedir_y_validar_constrasena_maestra():
    contrasena_ingresada = input('Ingresa tu contraseña maestra: ')
    if contrasena_ingresada != CONTRASENA_MAESTRA:
        print('La contraseña ingresada es incorrecta... Acceso DENEGADO\n')
        exit(0)

def procesar_opcion_del_usuario():
    print('''
Bienvenido al Gestor de Contraseñas favorito de los programadores --------
Selecciona una opcion para continuar:
0 - Salir
1 - Mostrar entradas
2 - Revelar contraseña
3 - Crear entrada
4 - Eliminar entrada
          ''')
    try:
        opcion_elegida = int(input(': '))
        print('')
    except:
        print('Opcion inválida, ingresa un número entre 0 y 4')
    
    match(opcion_elegida):
        case 0:
            print('Adios!')
            exit()
        case 1:
            # Mostrar todas las entradas
            listar_entradas()
        case 2:
            revelar_contrasena_de_entrada()
        case 3:
            # Crear una nueva entrada
            crear_entrada()
            actualizar_csv()
        case 4:
            # Eliminar una entrada a partir de su URL
            eliminar_entrada()
            actualizar_csv()


def run():
    generar_llave_cifrado()
    pedir_y_validar_constrasena_maestra()
    leer_csv()
    
    while True:
        procesar_opcion_del_usuario()

if __name__ == '__main__':
    run()