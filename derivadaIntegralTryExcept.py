import matplotlib.pyplot as plt 
from sympy import symbols, diff, integrate, sympify

def derivadaIntegral():
    try:
        # Definir la variable simbólica
        x = symbols('x')

        # Pedir al usuario que introduzca el polinomio
        polinomio_str = input("Introduce el polinomio en términos de x (ejemplo: x**3 - 6*x**2 + 11*x - 6): ")
        p = sympify(polinomio_str)  # Convierte la cadena en un objeto simbólico
        
        # Verificar que la entrada es un polinomio
        if not p.is_polynomial(x):
            raise ValueError("La expresión introducida no es un polinomio válido.")

        # Mostrar el polinomio original
        print(f"\nPolinomio original: {p}")

        # Calcular la derivada del polinomio
        derivada = diff(p, x)
        print(f"Derivada del polinomio: {derivada}")

        # Calcular la integral del polinomio
        integral = integrate(p, x)
        print(f"Integral del polinomio (indefinida): {integral} + C")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    derivadaIntegral()