from sympy import symbols, factor

def factorizar_polinomio():
    # Definir la variable simbólica
    x = symbols('x')
try:
    # Solicitar los coeficientes del polinomio al usuario
    print("Vamos a calcular la factorización de un polinomio.")
    print("El polinomio debe estar en la forma a*x**n + b*x**(n-1) + ... + c = 0")

    grado = int(input("Introduce el grado del polinomio (n): "))
    coeficientes = []

    # Pedir los coeficientes del polinomio
    for i in range(grado, -1, -1):
        coef = float(input(f"Introduce el coeficiente de x^{i}: "))
        coeficientes.append(coef)

    # Construir el polinomio a partir de los coeficientes
    polinomio = 0
    for i, coef in enumerate(coeficientes):
        polinomio += coef * x**(grado - i)

    # Factorizar el polinomio
    factores_polinomio = factor(polinomio)

    # Mostrar el polinomio original
    print("\n------------------------------------------")
    print(f"Polinomio original: {polinomio}")
    print("\------------------------------------------")

    # Mostrar la factorización
    print("\n------------------------------------------")
    print(f"Factorización del polinomio: {factores_polinomio}")
    print("\------------------------------------------")
    
except ValueError as e:
    print(f"Error: Entrada no valida {e}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
    
if __name__ == "__main__":
    factorizar_polinomio()