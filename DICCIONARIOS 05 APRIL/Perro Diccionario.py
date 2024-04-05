# 1. Crea un diccionario vacío llamado perro
perro = {}
print("Diccionario perro creado:", perro, "\n")

# 2. Añade nombre, color, raza, patas y edad al diccionario perro
perro['nombre'] = 'Max'
perro['color'] = 'marrón'
perro['raza'] = 'Labrador'
perro['patas'] = 4
perro['edad'] = 3
print("Diccionario perro actualizado:", perro, "\n")

# 3. Crea un diccionario de estudiante y añade nombre, apellido, sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves del diccionario
estudiante = {
    'nombre': 'DAndre Ryan',
    'apellido': 'Boston',
    'sexo': 'masculino',
    'edad': 24,
    'estado civil': 'soltero',
    'habilidades': ['programación', 'diseño gráfico'],
    'país': 'Colombia',
    'ciudad': 'Medllin',
    'dirección': 'Calle 123 N MEGA'
}
print("Diccionario estudiante creado:", estudiante, "\n")

# 4. Obtén la longitud del diccionario del alumno
longitud_estudiante = len(estudiante)
print("Longitud del diccionario estudiante:", longitud_estudiante, "\n")

habilidades = estudiante['habilidades']
tipo_habilidades = type(habilidades)
print("Valor de habilidades:", habilidades)
print("Tipo de datos de habilidades:", tipo_habilidades, "\n")

estudiante['habilidades'].extend(['redacción', 'idiomas', 'comer', 'bailar'])
print("Habilidades actualizadas:", estudiante['habilidades'], "\n")

claves_estudiante = list(estudiante.keys())
print("Claves del diccionario estudiante:", claves_estudiante, "\n")

valores_estudiante = list(estudiante.values())
print("Valores del diccionario estudiante:", valores_estudiante, "\n")

# 9. Cambie el diccionario a una lista de tuplas utilizando el método items()
tuplas_estudiante = list(estudiante.items())
print("Diccionario estudiante convertido a lista de tuplas:", tuplas_estudiante, "\n")

# 10. Eliminar uno de los elementos del diccionario
del estudiante['dirección']
print("Elemento 'dirección' eliminado del diccionario estudiante:", estudiante, "\n")

# 11. Borrar uno de los diccionarios
del perro
print("Diccionario perro borrado")