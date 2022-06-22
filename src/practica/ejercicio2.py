"""Ejercicio 2"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def calcular_estadistica(secuencia):
    """Esta función calcula una estadística de una secuencia.
    El máximo, el mínimo y el promedio.
    """
    limite = len(secuencia)
    posicion = 0
    maximo = secuencia[posicion]
    minimo = secuencia[posicion]
    contador = 0
    promedio = 0
    while contador != limite:
        if secuencia[posicion] < minimo:
            minimo = secuencia[posicion]
        if secuencia[posicion] > maximo:
            maximo = secuencia[posicion]
        promedio = promedio + secuencia[posicion]
        posicion = posicion + 1
        contador = contador + 1
    promedio = promedio / limite
    resultado = (minimo, maximo, promedio)
    return resultado
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    limite = int(input("¿Cuántos números desea ingresar? "))
    contador = 0
    secuencia = []
    while contador != limite:
        numero = int(input("Ingrese un número: "))
        contador = contador + 1
        secuencia.append(numero)
    respuesta = calcular_estadistica(secuencia)
    print(respuesta)
if __name__ == "__main__":
    principal()
