# archivo: tests/test_operaciones.py
import unittest
from sympy import Poly, symbols
from operaciones_polinomiosv3_try import div, suma, mult, res

# Definimos las variables simbólicas
x, y = symbols('x y')

class TestErroresOperacionesPolinomios(unittest.TestCase):

    def test_division_polinomio_por_cero(self):
        x = symbols('x')
        p1 = Poly(x**2 + 1, x)  # Polinomio 1: x**2 + 1
        p2 = Poly(0, x)  # Polinomio 2: 0 (divisor)

        # Usamos assertRaises para verificar que se lanza ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):  # Captura la excepción de división por cero
            div(p1, p2)  # Intentamos dividir por 0

    def test_division_numero_por_cero(self):
        # Usamos assertRaises para verificar que se lanza ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):  # Captura la excepción de división por cero
            div(5, 0)  # Intentamos dividir por 0
            
    def test_suma_con_polinomio_invalido(self):
        x = symbols('x')  # Definir el símbolo 'x'
        with self.assertRaises(Exception):  # Esperamos que lance una excepción
            p1 = Poly(x**2 + 1)
            p2 = "x**2 ++ 1"  # Sintaxis inválida, pasamos la cadena directamente
            suma(p1, p2)  # Debería lanzar una excepción debido a la sintaxis incorrecta
if __name__ == '__main__':
    unittest.main()