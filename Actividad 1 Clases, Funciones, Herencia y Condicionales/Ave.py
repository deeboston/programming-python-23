from animal import animal  # Asegúrate de importar la clase animal correctamente

class Ave(animal):  # La clase Ave hereda de animal
    def __init__(self, nombre, peso, nacimiento, propietario):
        super().__init__(nombre, peso)  # Llamar al constructor de la clase padre
        self.nacimiento = nacimiento
        self.propietario = propietario
        
    def calcular_edad(self):
        from datetime import datetime  # Importa datetime para calcular la edad
        año_actual = datetime.now().year
        edad = año_actual - self.nacimiento
        if edad > 5:
            print(f"{self.nombre} es MAYOR DE EDAD")
        else:
            print(f"{self.nombre} es MENOR DE EDAD")
    
    def imprimir_nombre(self):
        self.printnombre()  # Usar el método printnombre de la clase padre

ave1 = Ave('Boss', 3, 2005, 'Tecnar')
ave1.calcular_edad()
ave1.imprimir_nombre()