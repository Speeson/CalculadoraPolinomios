import TaylorPolinomioV2 # Importar el módulo que contiene la función que genera el polinomio de Taylor
# from TaylorPolinomioV2 import PolTaylor # También se puede importar la función directamente y no será necesario llamarla con el nombre del módulo

def mostrar_menu():
    print("\n---- Herramientas de Gestión Polinómicas ----")
    print("\n---- Menu Principal ----")
    print("1. Generar Polinomio de Taylor")
    print("2. Opción 2 (christian)")
    print("3. Opción 3 (gonzalo")
    print("4. Opción 4 (natalia)")
    print("5. Opción 5 (carol)")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":    
            TaylorPolinomioV2.PolTaylor() # Llamar directamente a la función que gestiona todo en el módulo TaylorPolinomioV2
        elif opcion == "2":
            print("Opción 2 aqui tu funcion chrissszzz (aún no implementada).")
        elif opcion == "3":
            print("Opción 3 aqui tu funcion marotooo (aún no implementada).")
        elif opcion == "4":
            print("Opción 4 aqui tu funcion nataliaaa (aún no implementada).")
        elif opcion == "5":
            print("Opción 5 aqui tu funcion carooool (aún no implementada).")
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    main()

