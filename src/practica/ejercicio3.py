"""Ejercicio 3"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def elementos_superpuestos(primera, segunda):
    """Esta función determina cuántos elementos
    de dos listas se superponen entre sí.
    Ejercicio extra: imprimir el número de
    posición de cuándo empieza la superposición.
    """
    primer_limite = len(primera)
    segundo_limite = len(segunda)
    if primer_limite > segundo_limite:
        limite = primer_limite
        menor = segundo_limite
        lista = segunda
    else:
        limite = segundo_limite
        menor = primer_limite
        lista = primera
    agregar = limite - menor
    contador = 0
    elemento = "ø"
    while contador != agregar:
        lista.append(elemento)
        contador = contador + 1
    posicion = 0
    elementos = 0
    superpuestos = []
    while posicion != limite:
        if primera[posicion] == segunda[posicion]:
            elementos = elementos + 1
            superpuestos.append(posicion)
        posicion = posicion + 1
    ejercicio_extra = superpuestos[0]
    return elementos, ejercicio_extra


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    contador = 0
    primera = []
    segunda = []
    limite = 0
    limite = int(input("¿Cuantos elementos desea ingresar? "))
    while contador != limite:
        elemento = input("Ingrese un elemento: ")
        verificar = isinstance(elemento, str)
        if verificar:
            elemento = elemento.lower()
        contador = contador + 1
        primera.append(elemento)
    contador = 0
    limite = 0
    limite = int(input("¿Cuántos elementos desea ingresar? "))
    while contador != limite:
        elemento = input("Ingrese un elemento: ")
        verificar = isinstance(elemento, str)
        if verificar:
            elemento = elemento.lower()
        contador = contador + 1
        segunda.append(elemento)
    respuesta = elementos_superpuestos(primera, segunda)
    print(f"Se superponen {respuesta[0]} elementos.")
    print(f"La superposición comienza desde la posición N°{respuesta[1]}.")


if __name__ == "__main__":
    principal()
