from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import Tk 

from model import Model


class View:
    
    def __init__(self, root) -> None:
        
    
        self.var_name = StringVar()
        self.var_country = StringVar()
        self.var_gender = StringVar()
        self.var_description = StringVar()
        self.var_search = StringVar()

       

        """ configuración estética de root """

        root.geometry("675x450") 
        root['pady'] = 20
        root['padx'] = 20
        root.title("Mujeres en la Música")
        root.config(background = "black") 

        """ labels """

        self.name = Label(root, text="Nombre", fg="white", bg="black" )
        self.name.grid(row=0, column=0, sticky="w")
        self.country = Label(root, text="País", fg="white", bg="black")
        self.country.grid(row=1, column=0, sticky="w")
        self.gender = Label(root, text="Género", fg="white", bg="black")
        self.gender.grid(row=2, column=0, sticky="w")
        self.description = Label(root, text="Descripción", fg="white", bg="black")
        self.description.grid(row=3, column=0, sticky="w")
        self.search = Label(root, text="buscar", fg="white", bg="black")
        self.search.grid(row=4, column=3, sticky="w")



        """ entries """

        self.entry_name = Entry(root, textvariable=self.var_name, width=25)
        self.entry_name.grid(row=0, column=1)
        self.entry_country = Entry(root, textvariable=self.var_country, width=25)
        self.entry_country.grid(row=1, column=1)
        self.entry_gender = Entry(root, textvariable=self.var_gender, width=25)
        self.entry_gender.grid(row=2, column=1)
        self.entry_description = Entry(root, textvariable=self.var_description, width=25)
        self.entry_description.grid(row=3, column=1)
        self.entry_search = Entry(root, textvariable=self.var_search, width=15)
        self.entry_search.grid(row=3, column=3, sticky="w")



        """ treeview """
        self.tree = ttk.Treeview(root)
        self.tree["columns"]=("col1", "col2", "col3", "col4")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=80, minwidth=80)
        self.tree.column("col2", width=80, minwidth=80)
        self.tree.column("col3", width=80, minwidth=80)
        self.tree.column("col4", width=300, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="País")
        self.tree.heading("col3", text="Género")
        self.tree.heading("col4", text="Descripción")
        self.tree.grid(row=6, column=0, columnspan=4, pady=20)

        self.model_class = Model(self.tree)

        """ buttons """

        # edit_btn = Button(root, text="Editar", command=lambda:self.model_class.editar_item(root, self.var_name, self.var_country, self.var_gender, self.var_description, self.entry_name, self.entry_country, self.entry_gender, self.entry_description ))

        # edit_btn.grid(row=1, column=3, sticky="w")

        # btn_alta = Button(root, text="Guardar", command=lambda:self.model_class.guardar(self.var_name.get(), self.var_country.get(), self.var_gender.get(), self.var_description.get(), self.entry_name, self.entry_country, self.entry_gender, self.entry_description, root)
        # )
        # btn_alta.grid(row=1, column=2, sticky="w")


        # delete_btn = Button(root, text="Eliminar", command=lambda:self.model_class.eliminar_item())
        
        # delete_btn.grid(row=3, column=2,sticky="w")

        
        # root.bind('<Return>', lambda event: self.model_class.enter_event(self.var_search))
    

        # self.model_class.insert_treeview()



if __name__ == "__main__":
    root = Tk()
    app=View(root)
    root.mainloop()