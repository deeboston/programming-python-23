import json
import os
from tkinter import messagebox

DATA_FOLDER = "data"

class InvoicesManager:
    def __init__(self):
        self.invoices_file = os.path.join(DATA_FOLDER, "invoices.json")
        self.invoices = []  # Initialize the invoices attribute

        self.create_data_folder()

    def create_data_folder(self):
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)
            # Create an empty invoices file if it doesn't exist
            with open(self.invoices_file, "w") as file:
                pass

    def load_invoices(self):
        if os.path.exists(self.invoices_file):
            with open(self.invoices_file, "r") as file:
                self.invoices = json.load(file)
        else:
            self.invoices = []

    def save_invoices(self):
        with open(self.invoices_file, "w") as file:
            json.dump(self.invoices, file)

    def add_invoice(self, client_name, amount, date):
        new_invoice = {"client": client_name, "amount": amount, "date": date}
        self.invoices.append(new_invoice)
        self.save_invoices()

    def get_invoices(self):
        return self.invoices

    def update_invoice(self, index, client, amount):
        if 0 <= index < len(self.invoices):
            self.invoices[index]["client"] = client
            self.invoices[index]["amount"] = amount
            self.save_invoices()
        else:
            print("Invalid invoice index.")

    def delete_invoice(self, index):
        if 0 <= index < len(self.invoices):
            del self.invoices[index]
            self.save_invoices()
        else:
            print("Invalid invoice index.")
