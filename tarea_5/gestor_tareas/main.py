from utilidades_proyectos import listar_todos_los_proyectos, crear_proyecto
from utilidades_tareas import listar_todas_las_tareas, listar_tareas_de_hoy, crear_tarea, completar_tarea

def mostrar_menu():
    print('Seleccione una opcion-----')
    print('''
0 - Salir
1 - Listar proyectos
2 - Listar tareas de hoy
3 - Listar todas las tareas
4 - Crear proyecto
5 - Crear tarea
6 - Completar tarea
          ''')

def procesar_opcion_usuario():
    try:
        opcion_elegida = int(input(': '))
        if opcion_elegida < 0 or opcion_elegida > 6:
            raise Exception('Opcion fuera de rango')
    except:
        print('La opcion elegida es invalida')
        return
    
    match(opcion_elegida):
        case 0:
            exit()
        case 1:
            listar_todos_los_proyectos()
        case 2:
            listar_tareas_de_hoy()
        case 3: 
            listar_todas_las_tareas()
        case 4:
            crear_proyecto()
        case 5:
            crear_tarea()
        case 6:
            completar_tarea()

def run():
    while True:
        mostrar_menu()
        procesar_opcion_usuario()


if __name__ == '__main__':
    run()