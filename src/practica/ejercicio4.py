"""Ejercicio 4"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def sucesion_fibonacci(numero_termino):
    """
    Esta función determina qué termino de la sucesión Fibonacci devolver,
    mediante un número ingresado por el usuario.
    """
    termino_1 = 0
    termino_2 = 0
    suma = 1
    contador = 1
    termino = 1
    while contador <= numero_termino:
        contador = contador + 1
        termino_1 = termino_2
        termino_2 = suma
        suma = termino_1 + termino_2
        termino = termino + 1
    return termino_2


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero_termino = 0
    while numero_termino <= 2:
        numero_termino = int(input("Ingrese un número: "))
        if numero_termino > 2:
            respuesta = sucesion_fibonacci(numero_termino)
            print(f"El término N°{numero_termino}",end="")
            print(f" es el número {respuesta} en la susesión Fibonacci.",end="")
        else:
            respuesta = "\n El término debe ser mayor a 2, intentelo de nuevo.\n"
            print(respuesta)


if __name__ == "__main__":
    principal()
