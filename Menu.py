import time

class Menu:
    def __init__(self):
        self.opciones = ["Personas", "Vehiculos", "Universidades", "Notas", "Salir"]
        self.contador_opciones_invalidas = 0

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
    if opcion_elegida != 5:  # Check if the option chosen is not 'Salir'
        menu.contador_opciones_invalidas += 1
        if menu.contador_opciones_invalidas == 3:
            countdown = 10  # Countdown timer in seconds
            print("Has seleccionado 3 opciones inválidas. Iniciando el temporizador...")
            while countdown > 0:
                print(f"Tienes {countdown} segundos para decidir...")
                time.sleep(1)
                countdown -= 1
            menu.contador_opciones_invalidas = 0  # Reset the invalid option counter after the timer ends
    choice = input("¿Desea elegir otra opción (Sí/No)? ").lower()
    if choice == "no":
        print("¡Adiós! Gracias por usar el programa.")
        break
    elif choice == "sí" or choice == "si":
        continue
    else:
        print("Opción inválida. Saliendo del programa.")
        break
