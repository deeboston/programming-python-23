import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    mensaje = "Seleccionado: " + variable.get()
    messagebox.showinfo("Información", mensaje)

def actualizar_label():
    seleccionados = lista_box.curselection()
    items = [lista_box.get(i) for i in seleccionados]
    texto = ', '.join(items)
    label.config(text="Seleccionados: " + texto)

def verificar_check():
    estado = "Activo" if check_var.get() == 1 else "Inactivo"
    check_label.config(text="Estado: " + estado)

ventana = tk.Tk()
ventana.title("Demostración de Widgets en Tkinter")
ventana.geometry("400x400")

# Frame para agrupar widgets
frame = tk.Frame(ventana)
frame.pack(pady=20)

# Label
label = tk.Label(frame, text="¡Bienvenido a la demostración de Tkinter!")
label.pack()

# Entry
entry = tk.Entry(frame, width=20)
entry.pack()

# Button para actualizar Label basado en Entry
button = tk.Button(frame, text="Actualizar Texto", command=lambda: label.config(text=entry.get()))
button.pack()

# Listbox
lista_box = tk.Listbox(frame, height=4, selectmode='multiple')
lista_box.insert(1, "Elemento 1")
lista_box.insert(2, "Elemento 2")
lista_box.insert(3, "Elemento 3")
lista_box.pack()
lista_box.bind('<<ListboxSelect>>', lambda eff: actualizar_label())

# Checkbutton
check_var = tk.IntVar()
check_button = tk.Checkbutton(frame, text="Activar", variable=check_var, command=verificar_check)
check_button.pack()
check_label = tk.Label(frame, text="Estado: Inactivo")
check_label.pack()

# Radiobutton
variable = tk.StringVar(value="Ninguno")
radios = [("Opción 1", "1"), ("Opción 2", "2"), ("Opción 3", "3")]
for texto, valor in radios:
    r = tk.Radiobutton(frame, text=texto, variable=variable, value=valor, command=mostrar_mensaje)
    r.pack(anchor=tk.W)

ventana.mainloop()
