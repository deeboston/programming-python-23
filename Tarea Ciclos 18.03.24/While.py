def print_menu():
    print("Menu de opciones:")
    print("1. Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")

def get_option():
    while True:
        try:
            option = int(input("Seleccione una opción (1-5): "))
            if option < 1 or option > 5:
                raise ValueError
            return option
        except ValueError:
            print("Por favor, ingrese un número válido del 1 al 5.")

def handle_option(option):
    if option == 1:
        print("Hola, has presionado la opción Personas.")
    elif option == 2:
        print("Hola, has presionado la opción Vehiculos.")
    elif option == 3:
        print("Hola, has presionado la opción Universidades.")
    elif option == 4:
        print("Hola, has presionado la opción Notas.")
    elif option == 5:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida.")

def main():
    while True:
        print_menu()
        option = get_option()
        handle_option(option)

if __name__ == "__main__":
    main()
