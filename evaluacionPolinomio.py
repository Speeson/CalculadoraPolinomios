import sympy

# Función para pedir al usuario que introduzca un polinomio
def pedir_polinomio():
    polinomio_str = input("Introduce el polinomio en términos de x (por ejemplo, 2*x**2 + 3*x - 5): ")
    x = sympy.symbols('x')
    polinomio = sympy.sympify(polinomio_str)  # Convierte la cadena en un objeto polinómico
    return polinomio

# Función para evaluar el polinomio en un valor específico de x
def evaluar_polinomio(polinomio, valor_x):
    return polinomio.subs('x', valor_x)

# Función para realizar la funcionalidad 3 del menú principal
def evalPolinomio():
    polinomio = pedir_polinomio()  # Pedimos el polinomio al usuario
    valor_x = float(input("Introduce el valor de x para evaluar el polinomio: "))  # Pedimos el valor de x
    resultado = evaluar_polinomio(polinomio, valor_x)
    print(f"El valor del polinomio para x = {valor_x} es: {resultado}")

# Este bloque asegura que no se ejecute nada al importar
if __name__ == "__main__":
    evalPolinomio()