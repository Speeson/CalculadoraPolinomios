import unittest
from sympy import symbols, factor
from factorizar_polinomiosV2 import factorizar_polinomio

class TestFactorizarPolinomio(unittest.TestCase):
    def test_basico(self):
        x = symbols('x')
        polinomio, factorizado = factorizar_polinomio()
        self.assertEqual(factorizado, (x - 1) * (x - 2))

    def test_valores_limite(self):
        with self.assertRaises(ValueError):
            factorizar_polinomio([])
        with self.assertRaises(TypeError):
            factorizar_polinomio()

    def test_datos_masivos(self):
        coeficientes = [1] + [0]*99 + [-1]
        polinomio, factorizado = factorizar_polinomio()
        self.assertIsNotNone(factorizado)
        
if __name__ == "__main__":
    unittest.main()
