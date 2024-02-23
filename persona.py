class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def obtener_nombre(self):
        return f'Mi nombre es: {self.nombre} {self.apellido}'
