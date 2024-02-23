class Estudiante:
    def __init__(self, cedula, nombre, apellido, correo, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def obtener_nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def obtener_cedula(self):
        return self.cedula

    def obtener_correo(self):
        return self.correo

    def obtener_telefono(self):
        return self.telefono

# Example usage:
if __name__ == "__main__":
    estudiante1 = Estudiante("11228804", "D'Andre", "Boston", "dandreboston707@gmail.com", "321-570-0940")
    print("Nombre completo:", estudiante1.obtener_nombre_completo())
    print("Cédula:", estudiante1.obtener_cedula())
    print("Correo electrónico:", estudiante1.obtener_correo())
    print("Teléfono:", estudiante1.obtener_telefono())
