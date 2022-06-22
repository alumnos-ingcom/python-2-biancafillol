"""Ejercicio 1"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def par_o_impar(numero):


    """Esta función determina si un número es par o impar
    """
    numero = abs(numero)
    limite = numero
    contador = 0
    while contador != limite:
        while numero > 0:
            numero = numero - 2
        contador = contador + 1
    resultado = numero == 0
    return resultado
def principal():


    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número: "))
    respuesta = par_o_impar(numero)
    print(respuesta)
if __name__ == "__main__":


    principal()
