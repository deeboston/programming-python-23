# 1. Declarar una lista vacía
lista_vacia = []
print("1. Lista vacía creada:", lista_vacia)

# 2. Declarar una lista con más de 5 elementos
lista_mas_de_5 = [1, 2, 3, 4, 5, 6, 7]
print("2. Lista con más de 5 elementos creada:", lista_mas_de_5)

# 3. Encuentre la longitud de las dos listas creadas anteriormente.
longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_de_5 = len(lista_mas_de_5)
print("3. Longitud de la lista vacía:", longitud_lista_vacia)
print("   Longitud de la lista con más de 5 elementos:", longitud_lista_mas_de_5)

# 4. Obtener el primer elemento, el elemento central y el último elemento de la lista.
primer_elemento = lista_mas_de_5[0]
elemento_central = lista_mas_de_5[len(lista_mas_de_5) // 2]
ultimo_elemento = lista_mas_de_5[-1]
print("4. Primer elemento de la lista:", primer_elemento)
print("   Elemento central de la lista:", elemento_central)
print("   Último elemento de la lista:", ultimo_elemento)

# 5. Crear una lista llamada Datos_personales que contenga (nombre, edad, altura, estado civil, dirección), y agrega datos utilizando la funcion append().
Datos_personales = []
Datos_personales.append("D'Andre")
Datos_personales.append(23)
Datos_personales.append(1.80)
Datos_personales.append("Soltero")
Datos_personales.append("Parque Heredia Conjunto Candil")
print("5. Lista Datos_personales creada y datos agregados:", Datos_personales)

# 6. Crea una lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("6. Lista it_companies creada con valores iniciales:", it_companies)

# 7. Añadir una empresa a la lista it_companies utilizando la funcion insert().
it_companies.insert(2, "Twitter")
print("7. Empresa 'Twitter' añadida a la lista it_companies:", it_companies)

# 8. Comprobar si una determinada empresa existe en la lista it_companies.
empresa = "Google"
if empresa in it_companies:
    print(f"8. {empresa} existe en la lista it_companies.")
else:
    print(f"8. {empresa} no existe en la lista it_companies.")

# 9. Ordena la lista con el método sort()
it_companies.sort()
print("9. Lista it_companies ordenada alfabéticamente:", it_companies)

# 10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()
print("10. Lista it_companies invertida en orden descendente:", it_companies)

# 11. Elimine la primera empresa informática de la lista utilizando el metodo pop y delete.
primer_empresa = it_companies.pop(0)
print("11. Primera empresa eliminada de la lista it_companies:", primer_empresa)

# 12. Eliminar todas las empresas de la lista it_companies
it_companies.clear()
print("12. Todas las empresas eliminadas de la lista it_companies:", it_companies)

# Busqueda

# IN => True,False
if "IN" in "IN => True,False":
    print("IN está en 'IN => True,False'")
else:
    print("IN no está en 'IN => True,False'")

# V in 'Google'
V = "o"
if V in "Google":
    print(f"'{V}' está en 'Google'")
else:
    print(f"'{V}' no está en 'Google'")

# [index(' valor')
print("[index(' valor'): 0,1,2…]")