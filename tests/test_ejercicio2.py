"""
Se quiere testear que la función calcular_estadistica()
funciona correctamente.
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from practica.ejercicio2 import calcular_estadistica


def test_positivos():
    """
    Cuando todos los números
    ingresados son positivos
    """
    secuencia = (4, 3, 2, 3)
    resultado = calcular_estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (2, 4, 3.0), "No se obtiene el resultado esperado."


def test_negativos():
    """
    Cuando todos los números
    ingresados son negativos
    """
    secuencia = (-4, -2, -3, -9, -5, -1, -5, -4)
    resultado = calcular_estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (-9, -1, -4.125), "No se obtiene el resultado esperado."


def test_iguales():
    """
    Cuando todos los números
    ingesados son iguales
    """
    secuencia = (3, 3, 3, 3)
    resultado = calcular_estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (3, 3, 3.0), "No se obtiene el resultado esperado."


def test_neutro():
    """
    Cuando todos los números
    ingresados son cero
    """
    secuencia = (0, 0, 0, 0)
    resultado = calcular_estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (0, 0, 0.0), "No se obtiene el resultado esperado."
