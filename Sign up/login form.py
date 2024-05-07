from tkinter import *

def ingresar():
    usuario = entry_usuario.get()
    clave = entry_clave.get()
    print("Usuario:", usuario)
    print("Clave:", clave)

# Crear la ventana principal
ventana = Tk()
ventana.title("Formulario de Login")
ventana.geometry("400x200")

# Frame izquierdo para el logo
frame_izquierdo = Frame(ventana, bg="white")
frame_izquierdo.pack(side=LEFT, fill=Y)

# Insertar el logo (puedes reemplazar "logo.png" con el nombre de tu archivo de imagen)
logo = PhotoImage(file="logo.png")
Label(frame_izquierdo, image=logo, bg="white").pack(pady=20)

# Frame derecho para el formulario de login
frame_derecho = Frame(ventana)
frame_derecho.pack(side=RIGHT, fill=Y)

# Título "Inicio de sesión"
Label(frame_derecho, text="Inicio de sesión", font=("Arial", 14)).pack(pady=10)

# Campo de usuario y caja de texto
Label(frame_derecho, text="Usuario:").pack()
entry_usuario = Entry(frame_derecho)
entry_usuario.pack()

# Campo de clave y caja de texto
Label(frame_derecho, text="Clave:").pack()
entry_clave = Entry(frame_derecho, show="*")  # Para ocultar la clave
entry_clave.pack()

# Botón de Ingresar
Button(frame_derecho, text="Ingresar", command=ingresar).pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
