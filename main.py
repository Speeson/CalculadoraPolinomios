# from TaylorPolinomioV2 import PolTaylor # También se puede importar la función directamente y no será necesario llamarla con el nombre del módulo
from TaylorPolinomioV3Numpy import PolTaylor
from Raices import raices
from factorizar_polinomiosV2 import factorizar_polinomio
from operaciones_polinomiosv3 import operaciones_polinomio


def mostrar_menu():
    print("\n---- Herramientas de Gestión Polinómicas ----")
    print("\n---- Menu Principal ----")
    print("1. Generar Polinomio de Taylor")
    print("2. Hallar raíces de un polinomio")
    print("3. Evaluar un polinomio en un punto (x)")
    print("4. Factorizar un polinomio")
    print("5. Operaciones con polinomios")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":    
            PolTaylor() # Llamar directamente a la función que gestiona todo en el módulo TaylorPolinomioV2
        elif opcion == "2":
            raices() #Llama directamente a la funcion que gestiona todo en el modulo de raices y soluciones.
        elif opcion == "3":
            print("Opción 3 aqui tu funcion marotooo (aún no implementada).")
        elif opcion == "4":
            factorizar_polinomio() #Llama directamente a la funcion que gestiona todo en el modulo de factorizar_polinomiosV2
        elif opcion == "5":
            operaciones_polinomio() #Llama directamente a la funcion que gestiona todo en el modulo de operaciones_polinomiosv3
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    main()

