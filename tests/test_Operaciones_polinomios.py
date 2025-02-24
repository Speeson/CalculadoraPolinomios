# archivo: tests/test_operaciones.py
import unittest
from operaciones_polinomiosv3_try import div
class TestOperaciones(unittest.TestCase):

    def test_division_basica(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(9, 3), 3)

    def test_division_extremos(self):
        self.assertEqual(div(0, 10), 0)
        self.assertEqual(div(1000000, 2), 500000)

    def test_division_masiva(self):
        i = 1
        while i <= 100:
            self.assertEqual(div(i * 2, 2), i)
            i += 1

    def test_excepciones(self):
        self.assertEqual(div(10, 0), "Error: División por cero")
        self.assertEqual(div("a", 2), "Error: Tipo de dato no válido")
if __name__ == '__main__':
 unittest.main()
