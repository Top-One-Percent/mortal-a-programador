from utilidades_cifrado import descifrar_contrasena

# Lista de entradas
lista_entradas = []

def agregar_entrada(entrada: dict):
    try:
        lista_entradas.append(entrada)
    except Exception as e:
        print(f'Ocurrio un error al agregar la entrada: {e}')
        
def eliminar_entrada():
    global lista_entradas
    url = input('URL de entrada a eliminar: ')
    longitud_inicial = len(lista_entradas)
    lista_entradas = [entrada for entrada in lista_entradas if entrada.get('url') != url] 
    longitud_final = len(lista_entradas)
    
    if longitud_inicial == longitud_final:
        print('No se encontró ninguna entrada con esa URL, intenta con otra.')
        
def mostrar_entrada(entrada: dict):
    print(f'{entrada.get('url')} | {entrada.get('usuario')} | {entrada.get('contrasena')}')

def revelar_contrasena_de_entrada():
    url = input('URL de la entrada: ')
    entrada = obtener_entrada_con_url(url)
    if entrada == None:
        print('No se encontró ninguna entrada con esa URL, intenta con otra.')
        return
    contrasena_descifrada = descifrar_contrasena(entrada.get('contrasena'))
    print(f'La contraseña es: {contrasena_descifrada}')


def listar_entradas():
    print('URL | Usuario | Contraseña')
    
    for entrada in lista_entradas:
        print('---------------------------------------------------')
        mostrar_entrada(entrada)
        

def obtener_entrada_con_url(url: str):
    for entrada in lista_entradas:
        if entrada.get('url') == url:
            return entrada
        
def obtener_lista_entradas():
    return lista_entradas