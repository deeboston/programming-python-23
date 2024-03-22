#1.Declarar una lista vacia
lista_victores = []

#2.Declarar una lista con mas de 5 elementos
lista_mas_de_5 = [1, 2, 3, 4, 5, 6, 7]

#3.Encuentre la longitud de as dos listas creadas anteriormente.
longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_de_5 = len(lista_mas_de_5)

#4.Obtener el primer elemento,el elemento central y el ultimo elemento de la lista.
primer_elemento = lista_mas_de_5[0]
elemento_central = longitud_lista_mas_de_5[len(longitud_lista_mas_de_5) // 2]
ultimo_elemento = lista_mas_de_5[-1]

#5.Crear una lista llamada Datos_personales que contenga(nombre,edad,altura,estado civil,direccion), y agrega datos utilizando la funcion append()
Datos_personales = []
Datos_personales.append("D'Andre")
Datos_personales.append(25)
Datos_personales.append(1.80)
Datos_personales.append("soltero")
Datos_personales.append("Parque Heredia Conjunto Candil")

#6.Crea una lista llamada it_companies y asignele los valores inciales Facebook,Google,Microsoft,Apple,IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7.Añadir una empresa  a la lista it_companies utilizando la funcion insert().
it_companies utilizando la función insert().
it_companies.insert(2, "Twitter")

#8.Comprobar si na determinada empresas exisite en la lista it_companies.
empresa = "Google"
if empresa in it_companies:
    print(f"{empresa} exisite en la lista it_companies.")
else:
    print(f"{empresa} no exisite en la lista it_companies.")
    
#9.Ordene la lista con el metodo sort()
it_companies.sort()

#10.Invierte la lista en orden descendenre utilizando el metodo reverse()
it_companies.reverse()

#11.Elimine la primera empresa informatica de la lista utilizando el metodo pop y delete.
primer_empresa = it_companies.pop(0)
# Alternativamente, se puede usar del para eliminar por índice:
# del it_companies[0]

#12.Eliminar todas las empresas de la lista it_companies
it_companies
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

print("Todos las tareas se han realizado correctamente.")
