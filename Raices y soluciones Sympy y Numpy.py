from sympy import symbols, solve
import numpy as np
def raices():
# Raíces y soluciones simbólicas con SymPy

# Define la variable simbólica
x = symbols('x')

# Define el polinomio
polinomio = x**3 - 6*x**2 + 11*x - 6

# Encuentra las raíces del polinomio
raices = solve(polinomio, x)

# Muestra las raíces
print(f"Polinomio: {polinomio}")
print(f"Raíces: {raices}")

#Aproximación numérica (por ejemplo, para polinomios con raíces
#complejas o con coeficientes decimales), usando NumPy:

# Coeficientes del polinomio (en orden descendente)
coeficientes = [1, -6, 11, -6]  # x^3 - 6x^2 + 11x - 6

# Encuentra las raíces del polinomio
raices2 = np.roots(coeficientes)

# Muestra las raíces
print(f"Raíces: {raices2}")
if _name_ == "_main_":
    raices()