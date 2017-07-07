import tkinter as tk
import FormClass as fc

class BusinessApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("500x500")
        #Setting Up Menus
        self.parentMenu= tk.Menu(self)
        self.fileMenu = tk.Menu(self.parentMenu)
        self.accountsMenu = tk.Menu(self.parentMenu)
        self.parentMenu.add_cascade(label="File", menu=self.fileMenu)
        self.parentMenu.add_cascade(label="Edit Accounts", menu = self.accountsMenu)

        self.fileMenu.add_command(label="New Customer Database", command = self.newFile)
        self.fileMenu.add_command(label="Load Customers", command = self.loadFile)
        self.accountsMenu.add_command(label="Add Student Account", command = self.addStudent)
        self.accountsMenu.add_command(label="Add Faculty Account", command = self.addFaculty)
        self.accountsMenu.add_command(label="Edit Student Account", command = self.editStudent)
        self.accountsMenu.add_command(label="Edit Faculty Account", command = self.editFaculty)
        self.config(menu=self.parentMenu)


        #Setting up Main Window
        self.title("Otsego Coffee Shop Point of Sale 1.0")
        self.introMessage = tk.Label(self, text="Welcome to the point of sale software")
        self.sellCoffee = tk.Button(self, text="Sell Coffee", command=self.renderTransaction)

        self.introMessage.grid(row=0, column = 0)
        self.sellCoffee.grid(row = 1, column = 1)



        #To Do Write Event Function
    def newFile(self):
        pass

    def loadFile(self):
        pass

    def addStudent(self):
        form = fc.AddCustomer(self)
        form.grid(row = 5, column = 0, columnspan = 2)
    def addFaculty(self):
        pass

    def editStudent(self):
        pass

    def editFaculty(self):
        pass

    def renderTransaction(self):
        pass
    
#To Do Make Customer Class
    
mainApp = BusinessApp()
mainApp.mainloop()
