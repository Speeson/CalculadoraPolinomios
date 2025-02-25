import matplotlib.pyplot as plt  
from sympy import symbols, diff, integrate, sympify

def derivadaIntegral():
    # Definir la variable simbólica
    x = symbols('x')
    
    try:
        # Pedir al usuario que introduzca el polinomio
        polinomio_str = input("Introduce el polinomio en términos de x (ejemplo: x**3 - 6*x**2 + 11*x - 6): ")
        p = sympify(polinomio_str)  # Convierte la cadena en un objeto simbólico

        # Mostrar el polinomio original
        print(f"\nPolinomio original: {p}")
    
        try:
            # Calcular la derivada del polinomio
            derivada = diff(p, x)
            print(f"Derivada del polinomio: {derivada}")

            # Calcular la integral del polinomio
            integral = integrate(p, x)
            print(f"Integral del polinomio (indefinida): {integral} + C")
        except Exception as e:
            print(f"Error al calcular derivada/integral: {e}")
    
    except Exception as e:  # Captura cualquier error en la entrada o procesamiento del polinomio
        print(f"Error: Entrada no válida. Asegúrese de ingresar un polinomio correctamente. ({e})")