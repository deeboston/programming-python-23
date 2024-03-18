# Crear el diccionario de tipo Vuelo
vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino": "MDE",
    "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
}

# Imprimir los valores del diccionario
print("Valores del diccionario de tipo Vuelo:")
for key, value in vuelo.items():
    print(f"{key}: {value}")

# Imprimir los valores de tipo de maleta
print("\nValores de tipo de maleta:")
for maleta in vuelo["Tipo_Maleta"]:
    print(maleta)
