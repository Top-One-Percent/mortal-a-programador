from cryptography.fernet import Fernet
import base64

def generar_llave_cifrado():
    llave = Fernet.generate_key()
    with open('llave_secreta.key', 'wb') as archivo_llave:
        archivo_llave.write(llave)

def cargar_llave_cifrado():
    with open('tarea_5/gestor_contrasenas/llave_secreta.key', 'rb') as archivo_llave:
        llave = archivo_llave.read()
    return llave

# Cargar la llave de cifrado almacenada en el archivo
llave = cargar_llave_cifrado()

# Instancia de Fernet
f = Fernet(llave)

def cifrar_contrasena(contrasena: str):
    cifrado = f.encrypt(contrasena.encode())
    cifrado_en_b64 = base64.b64encode(cifrado).decode()
    return cifrado_en_b64

def descifrar_contrasena(contrasena_cifrada: str):
    cifrado = base64.b64decode(contrasena_cifrada.encode())
    return f.decrypt(cifrado).decode()