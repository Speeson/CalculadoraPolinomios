import unittest
from unittest.mock import patch
import numpy as np
from sympy import symbols, solve
from io import StringIO

# Importa la función a probar (asumiendo que está en un archivo llamado raices.py)
from raices import raices

class TestRaices(unittest.TestCase):
    
    @patch("builtins.input", side_effect=[2, 1, -3, 2])  # Polinomio x^2 - 3x + 2
    @patch("sys.stdout", new_callable=StringIO)
    def test_raices_cuadraticas(self, mock_stdout, mock_input):
        raices()
        salida = mock_stdout.getvalue()
        self.assertIn("Raíces simbólicas: [1, 2]", salida)
        self.assertIn("Raíces numéricas (aproximadas): [2. 1.]", salida)
    
    @patch("builtins.input", side_effect=[3, 1, 0, -4, 4])  # Polinomio x^3 - 4x + 4
    @patch("sys.stdout", new_callable=StringIO)
    def test_raices_cubicas(self, mock_stdout, mock_input):
        raices()
        salida = mock_stdout.getvalue()
        self.assertIn("Polinomio: x**3 - 4*x + 4", salida)
        self.assertIn("Raíces simbólicas", salida)  # Verifica que se encuentren raíces
    
    @patch("builtins.input", side_effect=[1, 0, 0])  # Polinomio 0*x + 0 = 0 (error esperado)
    @patch("sys.stdout", new_callable=StringIO)
    def test_error_coeficiente_principal_cero(self, mock_stdout, mock_input):
        raices()
        salida = mock_stdout.getvalue()
        self.assertIn("Error de valor: El coeficiente principal no puede ser cero.", salida)

if __name__ == "__main__":
    unittest.main()