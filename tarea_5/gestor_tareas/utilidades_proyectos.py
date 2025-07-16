# Estructura Proyecto
# {
#     'id': 1,
#     'nombre': 'proyecto1',
#     'fecha_limite': '2025-07-14'
# }

from utilidades_fechas import convertir_fecha_de_str_a_date

proyectos = []

def anadir_proyecto_a_lista(nombre, fecha_limite):
    proximo_id = len(proyectos)
    nuevo_proyecto = {
        'id': proximo_id,
        'nombre': nombre,
        'fecha_limite': fecha_limite
    }
    
    proyectos.append(nuevo_proyecto)
    print('Proyecto añadido exitosamente!')
    
def crear_proyecto():
    print('Ingresa los datos del proyecto a continuacion------')
    nombre = input('Nombre: ')
    fecha_limite = convertir_fecha_de_str_a_date(input('Fecha (eje. 2025-07-14): '))
    
    anadir_proyecto_a_lista(nombre, fecha_limite)
    
def mostrar_proyecto(proyecto: dict):
    print(f'ID: {proyecto.get('id')}')
    print(f'Nombre: {proyecto.get('nombre')}')
    print(f'Fecha limite: {proyecto.get('fecha_limite')}')
    
def obtener_proyecto_con_id(id_proyecto: int):
    for proyecto in proyectos:
        if proyecto.get('id') == id_proyecto:
            return proyecto
    print(f'No se encontro un proyecto con el id {id_proyecto}')
    return
    
def listar_todos_los_proyectos():
    for proyecto in proyectos:
        mostrar_proyecto(proyecto)