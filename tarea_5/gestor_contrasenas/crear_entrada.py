from utilidades_lista_entradas import obtener_entrada_con_url, agregar_entrada, eliminar_entrada as utilidad_eliminar_entrada
from utilidades_cifrado import cifrar_contrasena

import random, string

def generar_contrasena_aleatoria(longitud: int):
    caracteres_disponibles = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))
    return contrasena

def obtener_url():
    while True:
        url = input('URL: ')
        if obtener_entrada_con_url(url) == None:
            return url
        else:
            print('Ya existe una entrada con esa URL, usa otra o eliminala')

def obtener_contrasena():
    try:
        tipo_contrasena = int(input('Tipo de contraseña (1-Personalizada, 2-Auto-generada): '))
        if tipo_contrasena < 1 or tipo_contrasena > 2:
            raise Exception('Tipo fuera de rango')
    except:
        print('Tipo de contraseña inválido, debe ser un número entre 1 y 2')
    
    longitud_valida = False
    
    while not longitud_valida:
        if tipo_contrasena == 1:
            contrasena = input('Ingresa la contraseña: ')
            longitud_deseada = len(contrasena)
        else:
            longitud_deseada = int(input('Longitud de la contraseña (debe ser >=8): '))
            
        if longitud_deseada < 8:
            print('La contraseña debe tener minimo 8 caracteres')
        else:
            longitud_valida = True
            
    if tipo_contrasena == 2:
        contrasena = generar_contrasena_aleatoria(longitud_deseada)
        
    return contrasena
           
def crear_entrada():
    print('Ingresa los siguientes datos para crear tu entrada')
    
    url = obtener_url()         
    usuario = input('Usuario: ')
    contrasena = obtener_contrasena()
    
    contrasena_cifrada = cifrar_contrasena(contrasena)
    
    dict_entrada = {'url': url, 'usuario': usuario, 'contrasena': contrasena_cifrada}
    
    agregar_entrada(dict_entrada)
