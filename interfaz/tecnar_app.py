import tkinter as tk

from tkinter import messagebox

# Función para mostrar los datos ingresados en un Messagebox
def registrar_datos():
    nombre = cnombre.get()
    apellido = capellido.get()
    edad = cedad.get()
    direccion = cdirrecion.get()
    telefono = ctelefono.get()
    sexo = var_sexo.get()
    ciudad = lista_ciudades.get(lista_ciudades.curselection())
    info = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nCiudad: {ciudad}"
    messagebox.showinfo("Datos Registrados", info)
    
    
ventana = tk.Tk()

ventana.title("Tecnar App")

ventana.geometry("800x600")

ventana.resizable(True, True)

lnombre= tk.Label(ventana,text= "Nombre:")
lnombre.place(x=5,y=10)
cnombre= tk.Entry(ventana, width=30)
cnombre.place(x=80,y=10)

lapellido= tk.Label(ventana,text="Apellido:")
lapellido.place(x=5,y=40)
capellido= tk.Entry(ventana, width=30)
capellido.place(x=80,y=40)

ledad= tk.Label(ventana,text="Edad:")
ledad.place(x=5,y=70)
cedad= tk.Entry(ventana, width=30)
cedad.place(x=80,y=70)

ldirrecion= tk.Label(ventana,text="Dirrecion:")
ldirrecion.place(x=5,y=100)
cdirrecion= tk.Entry(ventana, width=30)
cdirrecion.place(x=80,y=100)

ltelefono= tk.Label(ventana,text="Telefono:")
ltelefono.place(x=5,y=130)
ctelefono= tk.Entry(ventana, width=30)
ctelefono.place(x=80,y=130)

lciudad = tk.Label(ventana, text="Ciudad:")
lciudad.place(x=5, y=190)
lista_ciudades = tk.Listbox(ventana, height=3)
lista_ciudades.insert(1, "Cartagena")
lista_ciudades.insert(2, "Bogotá")
lista_ciudades.insert(3, "Medellín")
lista_ciudades.place(x=80, y=190)

var_sexo = tk.StringVar()
var_sexo.set("Otro")
lsexo = tk.Label(ventana, text="Sexo:")
lsexo.place(x=5, y=160)
r1 = tk.Radiobutton(ventana, text="Masculino", variable=var_sexo, value="Masculino")
r1.place(x=80, y=160)
r2 = tk.Radiobutton(ventana, text="Femenino", variable=var_sexo, value="Femenino")
r2.place(x=180, y=160)

frame = tk.Frame(ventana, width=300, height=100, relief="raised", bd=1)
frame.place(x=70, y=310)

bregistrar = tk.Button(ventana, text="Registrar", command=registrar_datos)
bregistrar.place(x=80, y=280)

ventana.mainloop()