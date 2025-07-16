

def main():
    numero_secreto = 7
    intento = None # El intento inicial es None o Nulo, o sea que no tiene valor

    while intento != numero_secreto:
        # El usuario ingresa un número
        intento = int(input("Adivina el número (entre 1 y 10): "))

        # Si el número ingresado es igual al número secreto, se imprime un mensaje de éxito y se sale del bucle
        if intento == numero_secreto:
            print("¡Correcto!")
            break # Se sale del bucle
        else:
            # Si el número ingresado es diferente al número secreto, se le da una pista al usuario y se repite el bucle
            pista = 'mayor' if intento < numero_secreto else 'menor'
            print(f"Ese no es el número secreto... prueba con un número {pista}.")


if __name__ == "__main__":
    main()