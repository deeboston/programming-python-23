from tkinter import *
from tkinter import messagebox

def signin():
    usuario = user.get()
    contraseña = code.get()
    if usuario == 'admin' and contraseña == '1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        Label(screen, text='Welcome to Automate TechSolutions', bg='#ADD8E6', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#ADD8E6")  # Modified color value
root.resizable(False, False)

img = PhotoImage(file='C:\\Users\\iBblioteca.DESUF3898Y1-10\\Desktop\\Sign up')

Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Automate Tech Solutions', fg='#57alf8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Usuario')

frame_line1 = Frame(frame, width=295, height=2, bg='black')
frame_line1.place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == "":
        code.insert(0, 'Contraseña')

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Contraseña')

frame_line2 = Frame(frame, width=295, height=2, bg='black')
frame_line2.place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()
