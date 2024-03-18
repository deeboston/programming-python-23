import time

class Menu:
    def __init__(self):
        self.opciones = ["Personas", "Vehiculos", "Universidades", "Notas", "Salir"]

    def mostrar_menu(self):
        print("Opciones del Menu:")
        for idx, opcion in enumerate(self.opciones, start=1):
            print(f"{idx}. {opcion}")

    def obtener_opcion_usuario(self):
        while True:
            eleccion = input("Por favor, elige una opcion: ")
            if eleccion.isdigit():
                eleccion = int(eleccion)
                if 1 <= eleccion <= len(self.opciones):
                    if eleccion == len(self.opciones):
                        print("¡Adiós! Gracias por usar el programa.")
                        exit()
                    else:
                        print(f"Hola, has presionado la opción '{self.opciones[eleccion - 1]}'.")
                        return eleccion
            print("Opción inválida. Por favor, elige nuevamente.")
            self.mostrar_menu()

menu = Menu()
menu.mostrar_menu()
while True:
    opcion_elegida = menu.obtener_opcion_usuario()
    choice = input("¿Desea elegir otra opción (Sí/No)? ").lower()
    if choice == "no":
        print("¡Adiós! Gracias por usar el programa.")
        break
    elif choice == "sí" or choice == "si":
        continue
    else:
        print("Opción inválida. Saliendo del programa.")
        break
