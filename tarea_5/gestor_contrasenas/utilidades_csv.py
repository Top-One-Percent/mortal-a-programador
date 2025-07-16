import csv
from utilidades_lista_entradas import agregar_entrada, obtener_lista_entradas

def convertir_fila_a_dict(fila: list[str]):
    return {'url': fila[0], 'usuario': fila[1], 'contrasena': fila[2]}

def leer_csv(nombre_csv='tarea_5/gestor_contrasenas/bd.csv'):
    try:
        with open(nombre_csv, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                dict_entrada = convertir_fila_a_dict(fila)
                agregar_entrada(dict_entrada)
        print(f'Archivo {nombre_csv} leído correctamente.')
    except Exception as e:
        print(f'Ocurrió un error al leer el CSV: {e}')

def actualizar_csv(nombre_csv='tarea_5/gestor_contrasenas/bd.csv'):
    try:
        with open(nombre_csv, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows([list(entrada.values()) for entrada in obtener_lista_entradas()])
            print('CSV actualizado exitosamente.')
    except Exception as e:
        print(f'Ocurrió un error al actualizar el CSV: {e}')