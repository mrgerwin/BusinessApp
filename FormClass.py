import tkinter as tk
from CustomerClass import *

class AddCustomer(tk.Frame):
    def __init__(self, rootWindow):
        tk.Frame.__init__(self, rootWindow)
        self.id = tk.StringVar(master=rootWindow)
        self.fnam = tk.StringVar(master=rootWindow)
        self.lnam = tk.StringVar(master=rootWindow)
        self.balance = tk.StringVar(master=rootWindow)
        
        self.idLbl = tk.Label(self, text="Customer ID").grid(row=0, column=0)
        self.fnamLbl = tk.Label(self, text="First Name").grid(row=1, column=0)
        self.lnamLbl = tk.Label(self, text="Last Name").grid(row=2, column=0)
        self.balanceLbl = tk.Label(self, text="Balance").grid(row=3, column=0)

        self.idEntry = tk.Entry(self, textvariable = self.id).grid(row=0, column=1)
        self.fnamEntry = tk.Entry(self, textvariable = self.fnam).grid(row=1, column=1)
        self.lnamEntry = tk.Entry(self, textvariable = self.lnam).grid(row=2, column=1)
        self.balanceEntry= tk.Entry(self, textvariable=self.balance).grid(row=3, column=1)
        self.okButton = tk.Button(self, text="OK", command=self.submit).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.doneButton = tk.Button(self, text="Done", command = self.done).grid(row=4, column=1)
        
    def submit(self):
        self.added = tk.Label(self, text=self.id.get()+" added").grid(row=5, column=0)
        
    def done(self):
        self.destroy()
