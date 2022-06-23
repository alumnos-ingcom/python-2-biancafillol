"""
Se quiere testear que la función calcular_estadistica()
funciona correctamente.
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from practica.ejercicio3 import elementos_superpuestos


def test_iguales():
    """
    Cuando los elementos de las listas
    son iguales.
    """
    primera = ["a", "a", "a", "a"]
    segunda = ["a", "a", "a", "a"]
    resultado = elementos_superpuestos(primera, segunda)
    assert isinstance(resultado, tuple),"El resultado debe ser una tupla."
    assert resultado[0] == 4, "No se obtiene el resultado esperado."
    assert resultado[1] == 0, "No se obtiene el resultado esperado."


def test_diferentes():
    """
    Cuando los elementos de las listas
    son diferentes.
    """
    primera = ["a", "a", "a", "a"]
    segunda = ["b", "b", "b", "b"]
    resultado = elementos_superpuestos(primera, segunda)
    assert isinstance(resultado, tuple),"El resultado debe ser una tupla."
    assert resultado[0] == 0, "No se obtiene el resultado esperado."
    assert resultado[1] == "", "No se obtiene el resultado esperado."


def test_iguales_distintos():
    """
    Cuando los elementos de las listas
    son iguales pero de forma diferente.
    """
    primera = ["a", "a", "a", "a"]
    segunda = ["A", "A", "A", "A"]
    resultado = elementos_superpuestos(primera, segunda)
    assert isinstance(resultado, tuple),"El resultado debe ser una tupla."
    assert resultado[0] == 4, "No se obtiene el resultado esperado."
    assert resultado[1] == 0, "No se obtiene el resultado esperado."


def test_vacio():
    """
    Cuando no se ingresan elementos
    """
    primera = []
    segunda = []
    resultado = elementos_superpuestos(primera, segunda)
    assert isinstance(resultado, tuple),"El resultado debe ser una tupla."
    assert resultado[0] == 0, "No se obtiene el resultado esperado."
    assert resultado[1] == "", "No se obtiene el resultado esperado."


def test_caracter_vacio():
    """
    Cuando los elementos de las listas
    son caracteres vacios.
    """
    primera = [""]
    segunda = ["", ""]
    resultado = elementos_superpuestos(primera, segunda)
    assert isinstance(resultado, tuple),"El resultado debe ser una tupla."
    assert resultado[0] == 1, "No se obtiene el resultado esperado."
    assert resultado[1] == 0, "No se obtiene el resultado esperado."
