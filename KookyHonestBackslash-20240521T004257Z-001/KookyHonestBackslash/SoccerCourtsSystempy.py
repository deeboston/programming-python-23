import os
import tkinter as tk
from tkinter import Label, Button, Listbox, Scrollbar, messagebox
from tkinter import Button, Entry, Label, Listbox, PhotoImage, Scrollbar, Tk, messagebox

from clientes_manager import ClientsManager
from courts_manager import CourtsManager
from invoices_manager import InvoicesManager
from reservations_manager import ReservationsManager

DATA_FOLDER = "data"

VALID_CREDENTIALS = {
    "jayz": "valencia",
    "user2": "password2",
    "user3": "password3"
}

def create_data_folder(self):
        pass 
    
class SoccerCourtsSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Soccer Courts System")

        self.background_image = tk.PhotoImage(file="C:\\Users\\Monitor.Saber\\Music\\KookyHonestBackslash-20240521T004257Z-001\\KookyHonestBackslash\\logo")

        
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.clients_manager = ClientsManager()
        self.courts_manager = CourtsManager()
        self.reservations_manager = ReservationsManager()
        self.invoices_manager = InvoicesManager()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Welcome to Soccer Courts System")
        self.label.pack(pady=50)

        self.username_label = Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        self.password_label = Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=50)

    def create_data_folder(self):
        pass 
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in VALID_CREDENTIALS and password == VALID_CREDENTIALS[username]:
            messagebox.showinfo("Login", "Login Successful!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


    def show_main_menu(self):
        self.clear_screen()

        self.clients_button = Button(self.root, text="Manage Clients", command=self.manage_clients, font=("Helvetica", 18))
        self.clients_button.pack(anchor="center")

        self.courts_button = Button(self.root, text="Manage Courts", command=self.manage_courts, font=("Helvetica", 18))
        self.courts_button.pack(anchor="center")

        self.reservations_button = Button(self.root, text="Manage Reservations", command=self.manage_reservations, font=("Helvetica", 18))
        self.reservations_button.pack(anchor="center")

        self.invoices_button = Button(self.root, text="Manage Invoices", command=self.manage_invoices, font=("Helvetica", 18))
        self.invoices_button.pack(anchor="center")
        

    def manage_reservations(self):
        self.clear_screen()

        heading_label = Label(self.root, text="Manage Reservations")
        heading_label.pack()

        add_reservation_button = Button(self.root, text="Add Reservation", command=self.add_reservation)
        add_reservation_button.pack()

        self.reservations_listbox = Listbox(self.root, width=50, height=10)
        self.reservations_listbox.pack()

        for reservation in self.reservations_manager.get_reservations():
            self.reservations_listbox.insert("end", f"Date: {reservation['date']}, Time: {reservation['time']}, Court: {reservation['court']}")

        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side="right", fill="y")
        self.reservations_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.reservations_listbox.yview)

        delete_reservation_button = Button(self.root, text="Delete Reservation", command=self.delete_reservation)
        delete_reservation_button.pack()

        update_reservation_button = Button(self.root, text="Update Reservation", command=self.update_reservation)
        update_reservation_button.pack()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()


        
    def add_reservation(self):
        self.clear_screen()

        heading_label = Label(self.root, text="Add Reservation")
        heading_label.pack()

        date_label = Label(self.root, text="Date (YYYY-MM-DD):")
        date_label.pack()
        self.date_entry = Entry(self.root)
        self.date_entry.pack()

        time_label = Label(self.root, text="Time (HH:MM):")
        time_label.pack()
        self.time_entry = Entry(self.root)
        self.time_entry.pack()

        court_label = Label(self.root, text="Court:")
        court_label.pack()
        self.court_entry = Entry(self.root)
        self.court_entry.pack()

        save_button = Button(self.root, text="Save Reservation", command=self.save_reservation)
        save_button.pack()
        
        
        
    def delete_reservation(self):
            index = self.reservations_listbox.curselection()
            if index:
                reservation_index = int(index[0])
                reservation = self.reservations_manager.get_reservations()[reservation_index]
                self.reservations_manager.delete_reservation(reservation_index)
                messagebox.showinfo("Success", f"Reservation deleted successfully: {reservation}")
                self.manage_reservations()
            else:
                messagebox.showwarning("Warning", "Please select a reservation to delete.")
                
            back_button = Button(self.root, text="Back", command=self.show_main_menu)
            back_button.pack()    
                
    def save_reservation(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        court = self.court_entry.get()

        self.reservations_manager.add_reservation(date, time, court)
        messagebox.showinfo("Success", "Reservation added successfully!")
        self.manage_reservations()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()
        
    def update_reservation(self):
            index = self.reservations_listbox.curselection()
            if index:
                reservation_index = int(index[0])
                reservation = self.reservations_manager.get_reservations()[reservation_index]
                new_date = input(f"Enter new date for reservation {reservation['date']} (YYYY-MM-DD): ")
                new_time = input(f"Enter new time for reservation {reservation['time']} (HH:MM): ")
                new_court = input(f"Enter new court for reservation {reservation['court']}: ")
                self.reservations_manager.update_reservation(reservation_index, new_date, new_time, new_court)
                messagebox.showinfo("Success", "Reservation updated successfully!")
                self.manage_reservations()
            else:
                messagebox.showwarning("Warning", "Please select a reservation to update.")
        
        
            back_button = Button(self.root, text="Back", command=self.show_main_menu)
            back_button.pack()
    
        
    def manage_invoices(self):
        self.clear_screen()

        heading_label = Label(self.root, text="Manage Invoices")
        heading_label.pack()

        add_invoice_button = Button(self.root, text="Add Invoice", command=self.add_invoice)
        add_invoice_button.pack()

        self.invoices_listbox = Listbox(self.root, width=50, height=10)
        self.invoices_listbox.pack()

        for invoice in self.invoices_manager.get_invoices():


            self.invoices_listbox.insert("end", f"Client: {invoice['client']}, Amount: {invoice['amount']}, Date: {invoice['date']}")

        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side="right", fill="y")
        self.invoices_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.invoices_listbox.yview)

        delete_invoice_button = Button(self.root, text="Delete Invoice", command=self.delete_invoice)
        delete_invoice_button.pack()

        update_invoice_button = Button(self.root, text="Update Invoice", command=self.update_invoice)
        update_invoice_button.pack()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()
    
    def add_invoice(self):
        self.clear_screen()

        heading_label = Label(self.root, text="Add Invoice")
        heading_label.pack()

        client_name_label = Label(self.root, text="Client Name:")
        client_name_label.pack()
        self.client_name_entry = Entry(self.root)
        self.client_name_entry.pack()

        amount_label = Label(self.root, text="Amount:")
        amount_label.pack()
        self.amount_entry = Entry(self.root)
        self.amount_entry.pack()

        date_label = Label(self.root, text="Date (YYYY-MM-DD):")
        date_label.pack()
        self.date_entry = Entry(self.root)
        self.date_entry.pack()

        save_button = Button(self.root, text="Save Invoice", command=self.save_invoice)
        save_button.pack()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()
        
    def save_invoice(self):
        client_name = self.client_name_entry.get()
        amount = float(self.amount_entry.get())
        date = self.date_entry.get()

        self.invoices_manager.add_invoice(client_name, amount, date)
        messagebox.showinfo("Success", "Invoice added successfully!")
        self.manage_invoices()
    
        save_button = Button(self.root, text="Save Invoice", command=lambda: self.save_invoice(client_name_entry.get(), float(amount_entry.get()), date_entry.get())) # type: ignore
        save_button.pack()
        
        
        

    def delete_invoice(self):
        index = self.invoices_listbox.curselection()
        if index:
            invoice_index = int(index[0])
            invoice = self.invoices_manager.get_invoices()[invoice_index]
            self.invoices_manager.delete_invoice(invoice_index)
            messagebox.showinfo("Success", f"Invoice deleted successfully: {invoice}")
            self.manage_invoices()
        else:
            messagebox.showwarning("Warning", "Please select an invoice to delete.")
            
        
    def update_invoice(self):
        index = self.invoices_listbox.curselection()
        if index:
            invoice_index = int(index[0])
            invoice = self.invoices_manager.get_invoices()[invoice_index]
            new_client_name = input(f"Enter new client name for invoice {invoice['client']}: ")
            new_amount = float(input(f"Enter new amount for invoice {invoice['amount']}: "))
            new_date = input(f"Enter new date for invoice {invoice['date']} (YYYY-MM-DD): ")
            self.invoices_manager.update_invoice(invoice_index, new_client_name, new_amount, new_date)
            messagebox.showinfo("Success", "Invoice updated successfully!")
            self.manage_invoices()
        else:
            messagebox.showwarning("Warning", "Please select an invoice to update.")
            
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()


    def manage_clients(self):
        self.clear_screen()
        
        heading_label = tk.Label(self.root, text="Manage Clients")
        heading_label.pack()

        add_client_button = tk.Button(self.root, text="Add Client", command=self.add_client)
        add_client_button.pack()

        self.clients_listbox = tk.Listbox(self.root, width=50, height=10)
        self.clients_listbox.pack()

        for client in self.clients_manager.get_clients():
            client_info = f"Name: {client.get('name', '')}, Email: {client.get('email', '')}, Phone: {client.get('phone', '')}"
            self.clients_listbox.insert("end", client_info)

        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side="right", fill="y")
        self.clients_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.clients_listbox.yview)

        delete_client_button = tk.Button(self.root, text="Delete Client", command=self.delete_client)
        delete_client_button.pack()

        update_client_button = tk.Button(self.root, text="Update Client", command=self.update_client)
        update_client_button.pack()
        
        back_button = tk.Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    
    def add_client(self):
        self.clear_screen()

        heading_label = Label(self.root, text="Add New Client")
        heading_label.pack()

        name_label = Label(self.root, text="Name:")
        name_label.pack()
        name_entry = Entry(self.root)
        name_entry.pack()

        email_label = Label(self.root, text="Email:")
        email_label.pack()
        email_entry = Entry(self.root)
        email_entry.pack()

        phone_label = Label(self.root, text="Phone:")
        phone_label.pack()
        phone_entry = Entry(self.root)
        phone_entry.pack()

        save_button = Button(self.root, text="Save", command=lambda: self.save_client(name_entry.get(), email_entry.get(), phone_entry.get()))
        save_button.pack()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    def save_client(self, name, email, phone):
        self.clients_manager.add_client(name, email, phone)
        messagebox.showinfo("Success", "Client added successfully!")
        self.manage_clients()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    def delete_client(self):
        selected_index = self.clients_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.clients_manager.delete_client(index)
            messagebox.showinfo("Success", "Client deleted successfully!")
            self.manage_clients()
        else:
            messagebox.showwarning("Warning", "Please select a client to delete.")
            
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    def update_client(self):
        selected_index = self.clients_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            client = self.clients_manager.get_client(index)
            self.clear_screen()

            heading_label = Label(self.root, text="Update Client")
            heading_label.pack()

            name_label = Label(self.root, text="Name:")
            name_label.pack()
            name_entry = Entry(self.root)
            name_entry.insert(0, client["name"])
            name_entry.pack()

            email_label = Label(self.root, text="Email:")
            email_label.pack()
            email_entry = Entry(self.root)
            email_entry.insert(0, client["email"])
            email_entry.pack()

            phone_label = Label(self.root, text="Phone:")
            phone_label.pack()
            phone_entry = Entry(self.root)
            phone_entry.insert(0, client["phone"])
            phone_entry.pack()

            save_button= Button(self.root, text="Save", command=lambda: self.save_updated_client(index, name_entry.get(), email_entry.get(), phone_entry.get()))
            save_button.pack()
        else:
            messagebox.showwarning("Warning", "Please select a client to update.")
            
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    def save_updated_client(self, index, name, email, phone):
        self.clients_manager.update_client(index, name, email, phone)
        messagebox.showinfo("Success", "Client updated successfully!")
        self.manage_clients()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    def manage_courts(self):
        self.clear_screen()

        heading_label = Label(self.root, text="Manage Courts")
        heading_label.pack()

        add_court_button = Button(self.root, text="Add Court", command=self.add_court)
        add_court_button.pack()

        self.courts_listbox = Listbox(self.root, width=50, height=10)
        self.courts_listbox.pack()

        for court in self.courts_manager.get_courts():
            self.courts_listbox.insert("end", f"Name: {court['name']}, Location: {court['location']}")

        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side="right", fill="y")
        self.courts_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.courts_listbox.yview)

        delete_court_button = Button(self.root, text="Delete Court", command=self.delete_court)
        delete_court_button.pack()

        update_court_button = Button(self.root, text="Update Court", command=self.update_court)
        update_court_button.pack()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    def add_court(self):
        self.clear_screen()

        heading_label = Label(self.root, text="Add New Court")
        heading_label.pack()

        name_label = Label(self.root, text="Name:")
        name_label.pack()
        name_entry = Entry(self.root)
        name_entry.pack()

        location_label = Label(self.root, text="Location:")
        location_label.pack()
        location_entry = Entry(self.root)
        location_entry.pack()

        save_button = Button(self.root, text="Save", command=lambda: self.save_court(name_entry.get(), location_entry.get()))
        save_button.pack()

        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()
        
    def save_court(self, name, location):
        self.courts_manager.add_court(name, location)
        messagebox.showinfo("Success", "Court added successfully!")
        self.manage_courts()
        
        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()

    def delete_court(self):
        selected_index = self.courts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.courts_manager.delete_court(index)
            messagebox.showinfo("Success", "Court deleted successfully!")
            self.manage_courts()
        else:
            messagebox.showwarning("Warning", "Please select a court to delete.")

        back_button = Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack()
        
    def update_court(self):
        selected_index = self.courts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            court = self.courts_manager.get_court(index)
            self.clear_screen()

            heading_label = Label(self.root, text="Update Court")
            heading_label.pack()

            name_label = Label(self.root, text="Name:")
            name_label.pack()
            name_entry = Entry(self.root)
            name_entry.insert(0, court["name"])
            name_entry.pack()

            location_label = Label(self.root, text="Location:")
            location_label.pack()
            location_entry = Entry(self.root)
            location_entry.insert(0, court["location"])
            location_entry.pack()

            save_button = Button(self.root, text="Save", command=lambda: self.save_updated_court(index, name_entry.get(), location_entry.get()))
            save_button.pack()
        else:
            messagebox.showwarning("Warning", "Please select a court to update.")

    def save_updated_court(self, index, name, location):
        self.courts_manager.update_court(index, name, location)
        messagebox.showinfo("Success", "Court updated successfully!")
        self.manage_courts()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

root = Tk()
root.configure(background="Grey")  
app = SoccerCourtsSystem(root)
root.mainloop()