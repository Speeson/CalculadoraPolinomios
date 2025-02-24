import sympy  # Importamos la librería SymPy para usar variables simbólicas (x, y)
from sympy import Poly, SympifyError, sympify
sympy.init_printing()  # Definimos los símbolos
x, y = sympy.symbols('x y')

def obtener_polinomios():  # Declaramos una función para obtener los polinomios
    try:
        P1 = input("Primer Polinomio (Formato: a*x**n + b*x**(n-1) + ...): ")
        P2 = input("Segundo Polinomio (Formato: a*x**n + b*x**(n-1) + ...): ")
        Poly1 = sympy.Poly(P1)  # Procesamos los polinomios
        Poly2 = sympy.Poly(P2)
        return Poly1, Poly2
    except (sympy.SympifyError, SyntaxError):
        print("Error: El formato del polinomio no es válido. Por favor, inténtalo de nuevo.")
        return obtener_polinomios()

# Declaramos una función para cada operación
def mult(p1, p2):
    return p1 * p2

def validar_polinomio(p):
    """Función para validar si una entrada es un polinomio correcto."""
    try:
        # Usamos sympify para intentar interpretar la cadena como una expresión matemática
        if isinstance(p, str):
            p = sympify(p)  # Esto intenta convertir la cadena en una expresión válida
        if not isinstance(p, Poly):
            raise TypeError("El polinomio no es válido.")
        return p
    except (SympifyError, TypeError) as e:
        raise Exception(f"Error al procesar el polinomio: {e}")

def suma(p1, p2):
    """Función para sumar dos polinomios."""
    try:
        # Validar si los polinomios son válidos
        p1 = validar_polinomio(p1)
        p2 = validar_polinomio(p2)

        # Realizar la suma de los polinomios si son válidos
        return p1 + p2
    except Exception as e:
        raise Exception(f"Error al sumar los polinomios: {e}")
    
def res(p1, p2):
    return p1 - p2

def div(p1, p2):
    # Si p2 es un polinomio y es cero
    if isinstance(p2, Poly) and p2.is_zero:  # Verificamos si p2 es un polinomio cero
        raise ZeroDivisionError("División por cero no permitida.")
    
    # Si p2 es un número entero o flotante
    elif isinstance(p2, (int, float)):
        if p2 == 0:  # Verificamos si p2 es cero
            raise ZeroDivisionError("División por cero no permitida.")
        return p1 / p2  # Realizamos la división

    # Si no es un polinomio ni un número, lanzamos un error
    raise TypeError("Tipo de dato no válido para la división.")

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
        except (sympy.SympifyError, SyntaxError):
            print("Error: Formato de polinomio incorrecto. Inténtalo de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Este bloque asegura que no se ejecute nada al importar
if __name__ == "__main__":
    operaciones_polinomio()