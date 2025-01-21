import TaylorPolinomioV2

def opcion_taylor():
    print("\nGenerador de Polinomios de Taylor")
    
    # Solicitar al usuario los datos necesarios
    func_str = input('Introduzca la función (en términos de x - Ej. ln(x), cos(x), exp(x)): ')
    a = float(input('Introduzca el valor en torno a qué punto desea el polinomio (Eje X): '))
    n = int(input('Introduzca el orden del polinomio de Taylor: '))

    # Llamar a la función desde el módulo TaylorPolinomioV2
    TaylorPolinomioV2.PolTaylor(a, n, func_str)

def mostrar_menu():
    print("\nMenu Principal")
    print("1. Generar Polinomio de Taylor")
    print("2. Opción 2 (Christian.py)")
    print("3. Opción 3 (gonzalo.py)")
    print("4. Opción 4 (natalia.py)")
    print("5. Opción 5 (carol.py)")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            opcion_taylor() # Función de Esteban
        elif opcion == "2":
            print("Opción 2 christian.py (aún no implementada).")
        elif opcion == "3":
            print("Opción 3 gonzalo.py (aún no implementada).")
        elif opcion == "4":
            print("Opción 4 natalia.py (aún no implementada).")
        elif opcion == "5":
            print("Opción 5 carol.py (aún no implementada).")
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    main()