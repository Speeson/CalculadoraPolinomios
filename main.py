import TaylorPolinomioV2

def mostrar_menu():
    print("\nMenu Principal")
    print("1. Generar Polinomio de Taylor")
    print("2. Opción 2 (por definir)")
    print("3. Opción 3 (por definir)")
    print("4. Opción 4 (por definir)")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1": # Para evitar que se ejecute la función directamente al importar, se solicitarán los parámetros en el main
            print("\nGenerador de Polinomios de Taylor") 
            func_str = input('Introduzca la función (en términos de x - Ej. ln(x), cos(x), exp(x)): ')
            a = float(input('Introduzca el valor en torno a qué punto desea el polinomio (Eje X): '))
            n = int(input('Introduzca el orden del polinomio de Taylor: '))
            TaylorPolinomioV2.PolTaylor(a, n, func_str)
        elif opcion == "2":
            print("Opción 2 seleccionada (aún no implementada).")
        elif opcion == "3":
            print("Opción 3 seleccionada (aún no implementada).")
        elif opcion == "4":
            print("Opción 4 seleccionada (aún no implementada).")
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
