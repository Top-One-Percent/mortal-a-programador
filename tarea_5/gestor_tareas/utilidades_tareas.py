# Estructura Tarea
# {
#     'id': 1,
#     'nombre': 'tarea1',
#     'fecha': '2025-07-14',
#     'dificultad': 2,
#     'proyecto': 1,
#     'esta_completada': False,
# }

from datetime import date
from utilidades_fechas import convertir_fecha_de_str_a_date
from utilidades_proyectos import obtener_proyecto_con_id, mostrar_proyecto

tareas = []

def anadir_tarea_a_lista(nombre, fecha, dificultad, proyecto):
    proximo_id = len(tareas)
    nueva_tarea = {
        'id': proximo_id,
        'nombre': nombre,
        'fecha': fecha,
        'dificultad': dificultad,
        'proyecto': proyecto,
        'esta_completada': False
    }
    
    tareas.append(nueva_tarea)
    print('Tarea añadida exitosamente!')
    
def crear_tarea():
    print('Ingresa los datos de la tarea a continuacion------')
    
    nombre = input('Nombre: ')
    fecha = convertir_fecha_de_str_a_date(input('Fecha (eje. 2025-07-14): '))
    
    try:
        dificultad = int(input('Dificultad (1-3): '))
        if dificultad < 1 or dificultad > 3:
            raise Exception('Dificultad fuera de rango')
    except:
        print('Dificultad invalida, asignando 1 por defecto')
        dificultad = 1
        
    proyecto = int(input('ID del proyecto: '))
    
    if obtener_proyecto_con_id(proyecto) == None:
        print('Se guardara la tarea como independiente')
        proyecto = None
    
    anadir_tarea_a_lista(nombre, fecha, dificultad, proyecto)
    
def mostrar_tarea(tarea: dict):
    print(f'ID: {tarea.get('id')}')
    print(f'Nombre: {tarea.get('nombre')}')
    print(f'Fecha: {tarea.get('fecha')}')
    print(f'Dificultad: {tarea.get('dificultad')}')
    if tarea.get('proyecto') != None:
        print(f'Proyecto: \n{mostrar_proyecto(obtener_proyecto_con_id(tarea.get('proyecto')))}')
    print(f'Completada: {tarea.get('esta_completada')}')
    
    
def listar_todas_las_tareas():
    for tarea in tareas:
        mostrar_tarea(tarea)
        
def listar_tareas_de_hoy():
    fecha_hoy = date.today()
    
    for tarea in tareas:
        if tarea.get('fecha') == fecha_hoy:
            mostrar_tarea(tarea)
            
def completar_tarea():
    id_tarea = int(input('ID de la tarea: '))
    for tarea in tareas:
        if tarea.get('id') == id_tarea:
            tarea['esta_completada'] = True
            return
    print('No se encontro una tarea con ese ID')