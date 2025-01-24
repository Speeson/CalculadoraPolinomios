"""
Algoritmo para la resolución de operaciones entre 2 polinomios
"""

# Importamos la librería SymPy para usar variables simbólicas (x, y)
import sympy


# Definimos los símbolos
sympy.init_printing()
x, y = sympy.symbols('x y')

# Declaramos una función para obtener los polinomios
def obtener_polinomios():
    P1 = input("Primer Polinomio (Formato: a*x**n(orden) + b*x**n-1(orden-1) etc): ")
    P2 = input("Segundo Polinomio (Formato: a*x**n(orden) + b*x**n-1(orden-1) etc): ")
    # Luego almacenamos en variables los dos polinomios procesados por la función Poly de sympy
    Poly1 = sympy.Poly(P1)
    Poly2 = sympy.Poly(P2)
    return Poly1, Poly2

# Declaramos una función para cada operación
def mult(p1, p2):
    return p1 * p2

def suma(p1, p2):
    return p1 + p2

def res(p1, p2):
    return p1 - p2

def div(p1, p2):
    return p1 / p2

# Menú para elegir la operación
def operaciones_polinomio():
    print("Elige una operación:")
    print("1. Multiplicar")
    print("2. Sumar")
    print("3. Restar")
    print("4. Dividir")
    print("0. Salir")

    while True:
        try:
            opcion = int(input("Introduce el número de la operación (0-4): "))
            if opcion == 0:
                print("Saliendo del programa. ¡Adiós!")
                break
            elif opcion in range(1, 5):
                # Obtener polinomios
                Poly1, Poly2 = obtener_polinomios()
                if opcion == 1:
                    resultado = mult(Poly1, Poly2)
                    print("------------------------------------------")
                    print("Resultado de la multiplicación:", resultado)
                    print("------------------------------------------")
                elif opcion == 2:
                    resultado = suma(Poly1, Poly2)
                    print("------------------------------------------")
                    print("Resultado de la suma:", resultado)
                    print("------------------------------------------")
                elif opcion == 3:
                    resultado = res(Poly1, Poly2)
                    print("------------------------------------------")
                    print("Resultado de la resta:", resultado)
                    print("------------------------------------------")
                elif opcion == 4:
                    resultado = div(Poly1, Poly2)
                    print("------------------------------------------")
                    print("Resultado de la división:", resultado)
                    print("------------------------------------------")
                break
            else:
                print("Por favor, elige una opción válida (0-4).")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
        except ZeroDivisionError:
            print("Error: División por cero no permitida.")

# Este bloque asegura que no se ejecute nada al importar
if __name__ == "__main__":
    operaciones_polinomio()