"""Ejercicio 5"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def escanear_corchetes(cadena):
    """Esta función determina si los corchetes de una cadena
    están ordenados y tienen su cierre o apertura. []
    """
    cadena = list(cadena)
    limite = len(cadena)
    posicion = 0
    contador = 0
    corchetes = []
    while contador != limite:
        if cadena[posicion] == "[":
            corchetes.append(cadena[posicion])
        elif cadena[posicion] == "]":
            corchetes.append(cadena[posicion])
        posicion = posicion + 1
        contador = contador + 1
    limite = len(corchetes)
    contador = limite
    if limite > 1:
        while limite != 0:
            if corchetes[0] == "[" and corchetes[-1] == "]":
                corchetes.remove("[")
                corchetes.remove("]")
                contador = contador - 2
            limite = limite - 2
        respuesta = contador == 0
    elif limite == 0:
        respuesta = True
    else:
        respuesta = False
    return respuesta


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese una candena: ")
    resultado = escanear_corchetes(cadena)
    print(resultado)


if __name__ == "__main__":
    principal()
