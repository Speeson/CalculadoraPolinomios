import unittest
from sympy import symbols, diff, integrate, sympify, simplify, S

#Definimos la variable simbólica x para trabajar con expresiones algebraicas
x = symbols('x')

class TestDerivadaIntegral(unittest.TestCase):
    
    def test_basico(self):
        polinomio = "x**3 - 6*x**2 + 11*x - 6"  # Polinomio de prueba
        p = sympify(polinomio) # Convertimos la cadena en una expresión simbólica

        #Comprobamos que la derivada es correcta
        self.assertEqual(diff(p, x), 3*x**2 - 12*x + 11)

        #Definimos la integral esperada, evitando problemas de precisión con flotantes
        integral_esperada = S(1)/4 * x**4 - 2*x**3 + S(11)/2 * x**2 - 6*x
        #Verificamos que la integral calculada es algebraicamente equivalente a la esperada
        self.assertEqual(simplify(integrate(p, x) - integral_esperada), 0)  

    def test_valores_limite(self):
        #Prueba con una expresión mal formada (debería lanzar una excepción)
        with self.assertRaises(Exception):  
            sympify("x**3 + 2*/x", evaluate=False)  # `evaluate=False` evita interpretación automática
        
        #Prueba con una expresión que no es un polinomio en una sola variable
        resultado = sympify("xyz", evaluate=False)  #Se interpreta como x * y * z

        #Verificamos que la expresión contiene más de una variable (no es un polinomio en x)
        self.assertNotEqual(resultado.free_symbols, {x})  

    def test_datos_masivos(self):
        #Creamos un polinomio con términos desde x^1 hasta x^99
        polinomio = " + ".join([f"{i}*x**{i}" for i in range(1, 100)])  # Polinomio de alto grado
        p = sympify(polinomio)  #Convertimos la cadena en una expresión simbólica
        # Calculamos la derivada e integral del polinomio
        derivada = diff(p, x) 
        integral = integrate(p, x)
        self.assertIsInstance(derivada, type(p))  # Verificar que la derivada es válida
        self.assertIsInstance(integral, type(p))  # Verificar que la integral es válida

if __name__ == "__main__":
    unittest.main()