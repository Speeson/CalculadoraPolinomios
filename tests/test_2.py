# archivo: tests/test_operaciones.py
import unittest
from sympy import Poly, symbols
from operaciones_polinomiosv3_try import div, suma, mult, res

# Definimos las variables simbólicas
x, y = symbols('x y')

class TestErroresOperacionesPolinomios(unittest.TestCase):

    def test_division_polinomio_por_cero(self):
        x = symbols('x')
        p1 = Poly(x**2 + 1)
        p2 = Poly(0, x)
        resultado = div(p1, p2)
        self.assertEqual(resultado, "Error: División por cero")
        #with self.assertRaises(ZeroDivisionError):
            #div(p1, p2)

    def test_division_numero_por_cero(self):
        resultado = div(5, 0)
        self.assertEqual(resultado, "Error: División por cero")

    def test_tipo_dato_invalido(self):
        resultado = div("x + 1", Poly(x + 1))
        self.assertEqual(resultado, "Error: Tipo de dato no válido")

    def test_suma_con_polinomio_invalido(self):
        with self.assertRaises(Exception):  # Esperamos que lance una excepción
            p1 = Poly(x**2 + 1)
            p2 = Poly("x**2 ++ 1")  # Sintaxis inválida
            suma(p1, p2)

if __name__ == '__main__':
    unittest.main()