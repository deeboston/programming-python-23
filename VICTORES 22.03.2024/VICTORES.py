# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
lista_mas_de_5 = [1, 2, 3, 4, 5, 6, 7]

# 3. Encuentre la longitud de las dos listas creadas anteriormente.
longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_de_5 = len(lista_mas_de_5)

# 4. Obtener el primer elemento, el elemento central y el último elemento de la lista.
primer_elemento = lista_mas_de_5[0]
elemento_central = lista_mas_de_5[len(lista_mas_de_5) // 2]
ultimo_elemento = lista_mas_de_5[-1]

# 5. Crear una lista llamada Datos_personales que contenga (nombre, edad, altura, estado civil, dirección), y agrega datos utilizando la función append().
Datos_personales = []
Datos_personales.append("DAndre")
Datos_personales.append(23)
Datos_personales.append(1.80)
Datos_personales.append("Soltero")
Datos_personales.append("Parque Heredia Cojunto Candil")

# 6. Crea una lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Añadir una empresa  a la lista it_companies utilizando la función insert().
it_companies.insert(2, "Twitter")

# 8. Comprobar si una determinada empresa existe en la lista it_companies.
empresa = "Google"
if empresa in it_companies:
    print(f"{empresa} existe en la lista it_companies.")
else:
    print(f"{empresa} no existe en la lista it_companies.")

# 9. Ordena la lista con el método sort()
it_companies.sort()

# 10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()

# 11. Elimine la primera empresa informática de la lista utilizando el metodo pop y delete.
primer_empresa = it_companies.pop(0)
# Alternativamente, se puede usar del para eliminar por índice:
# del it_companies[0]

# 12. Eliminar todas las empresas de la lista it_companies
it_companies.clear()

# Busqueda

# IN Tree, False
if "Tree" in "IN Tree":
    print("Tree está en 'IN Tree'")
else:
    print("Tree no está en 'IN Tree'")

# C =
C = None

# V in 'Google'
V = "o"
if V in "Google":
    print(f"'{V}' está en 'Google'")
else:
    print(f"'{V}' no está en 'Google'")

# Vindex('Valor')
def Vindex(s):
    for i, char in enumerate(s):
        print(i, end=",")
    print()

Vindex('Valor')

# Print each activity at the end
print("1. Declarar una lista vacía:", lista_vacia)
print("2. Declarar una lista con más de 5 elementos:", lista_mas_de_5)
print("3. Longitud de la lista vacía:", longitud_lista_vacia)
print("   Longitud de la lista con más de 5 elementos:", longitud_lista_mas_de_5)
print("4. Primer elemento de la lista:", primer_elemento)
print("   Elemento central de la lista:", elemento_central)
print("   Último elemento de la lista:", ultimo_elemento)
print("5. Datos personales:", Datos_personales)
print("6. Empresas de TI:", it_companies)
print("7. Empresa añadida:", empresa)
print("8. Lista de empresas de TI ordenada:", it_companies)
print("9. Lista de empresas de TI invertida:", it_companies)
print("10. Primera empresa eliminada:", primer_empresa)
print("11. Lista de empresas de TI vacía:", it_companies)

print("Todas las tareas han sido realizadas correctamente.")