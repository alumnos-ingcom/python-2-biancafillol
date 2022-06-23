"""
Se quiere testear que la función par_o_impar funciona correctamente.
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from practica.ejercicio1 import par_o_impar



def test_par_positivo():
    """
    Cuando el número ingresado es par positivo.
    """
    numero = 4
    resultado = par_o_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un booleano."
    assert resultado is True, "No se obtiene el resultado esperado."


def test_impar_positivo():
    """
    Cuando el número ingresado es impar positivo
    """
    numero = 5
    resultado = par_o_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un booleano."
    assert resultado is False, "No se obtiene el resultado esperado."


def test_par_negativo():
    """
    Cuando el número ingresado es par negativo.
    """
    numero = -16
    resultado = par_o_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un booleano."
    assert resultado is True, "No se obtiene el resultado esperado."


def test_impar_negativo():
    """
    Cuando el número ingresado es impar negativo
    """
    numero = -13
    resultado = par_o_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un booleano."
    assert resultado is False, "No se obtiene el resultado esperado."


def test_neutro():
    """
    Cuando el número ingresado es neutro
    """
    numero = 0
    resultado = par_o_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
