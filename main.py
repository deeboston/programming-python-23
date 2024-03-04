class Animal:
  def __init__(self, nombre, num_patas, fecha_vacuna, propietarios):
      self.nombre = nombre
      self.num_patas = num_patas
      self.fecha_vacuna = fecha_vacuna
      self.propietarios = propietarios

  def imprimir_nombre(self):
      print(f"Nombre: {self.nombre}")

  def imprimir_num_patas(self):
      print(f"Número de patas: {self.num_patas}")

  def imprimir_fecha_vacuna(self):
      print(f"Fecha de vacuna: {self.fecha_vacuna}")

  def imprimir_propietarios(self):
      print(f"Propietarios: {', '.join(self.propietarios)}")

# Producto
perro = Animal("Fido", 4, "2023-06-15", ["D'Andre", "Boston"])
perro.imprimir_nombre()
perro.imprimir_num_patas()
perro.imprimir_fecha_vacuna()
perro.imprimir_propietarios()