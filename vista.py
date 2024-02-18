""" 

vista.py: 

En este módulo se puede encontrar la configuración de la interfaz gráfica hecha en Tkinter.

"""


from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import Tk 

from modelo import Abmc
from clases_secundarias import Servidor


class Vista:


    def __init__(self, root) -> None:
        
    
        self.var_nombre = StringVar()
        self.var_pais = StringVar()
        self.var_genero = StringVar()
        self.var_descripcion = StringVar()
        self.var_busqueda = StringVar()

     
        # """ configuración estética de root """

        root.geometry("675x450") 
        root['pady'] = 20
        root['padx'] = 20
        root.title("Mujeres en la Música")
        root.config(background = "black") 


        # """ labels """

        self.nombre = Label(root, text="Nombre", fg="white", bg="black" )
        self.nombre.grid(row=0, column=0, sticky="w")
        self.country = Label(root, text="País", fg="white", bg="black")
        self.country.grid(row=1, column=0, sticky="w")
        self.gender = Label(root, text="Género", fg="white", bg="black")
        self.gender.grid(row=2, column=0, sticky="w")
        self.description = Label(root, text="Descripción", fg="white", bg="black")
        self.description.grid(row=3, column=0, sticky="w")
        self.search = Label(root, text="buscar", fg="white", bg="black")
        self.search.grid(row=4, column=3, sticky="w")


        # """ entradas """

        self.entry_nombre = Entry(root, textvariable=self.var_nombre, width=25)
        self.entry_nombre.grid(row=0, column=1)
        self.entry_pais = Entry(root, textvariable=self.var_pais, width=25)
        self.entry_pais.grid(row=1, column=1)
        self.entry_genero = Entry(root, textvariable=self.var_genero, width=25)
        self.entry_genero.grid(row=2, column=1)
        self.entry_descripcion = Entry(root, textvariable=self.var_descripcion, width=25)
        self.entry_descripcion.grid(row=3, column=1)
        self.entry_busqueda = Entry(root, textvariable=self.var_busqueda, width=15)
        self.entry_busqueda.grid(row=3, column=3, sticky="w")



        # """ treeview """

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

        # instancias de clases importadas
        self.model_class = Abmc(self.tree)
        self.lanzar_servidor = Servidor()

        # """ botones """
        
        btn_editar = Button(root, text="Editar", command=lambda:self.model_class.editar_item(root, self.var_nombre, self.var_pais, self.var_genero, self.var_descripcion, self.entry_nombre, self.entry_pais, self.entry_genero, self.entry_descripcion ))

        btn_editar.grid(row=1, column=3, sticky="w")

        btn_alta = Button(root, text="Guardar", command=lambda:self.model_class.guardar(self.var_nombre.get(), self.var_pais.get(), self.var_genero.get(), self.var_descripcion.get(), self.entry_nombre, self.entry_pais, self.entry_genero, self.entry_descripcion, root)
        )
        btn_alta.grid(row=1, column=2, sticky="w")


        btn_eliminar = Button(root, text="Eliminar", command=lambda:self.model_class.eliminar_item())
        
        btn_eliminar.grid(row=3, column=2,sticky="w")


        btn_buscar = Button(root, text="buscar", command=lambda:self.model_class.buscar_item(self.tree, self.var_busqueda))
        
        btn_buscar.grid(row=4, column=3,sticky="w")

        btn_encender_servidor = Button(root, text="encender servidor", command=lambda:self.lanzar_servidor.iniciar_conexion())
        
        btn_encender_servidor.grid(row=7, column=1,sticky="w")

        btn_apagar_servidor = Button(root, text="apagar servidor", command=lambda:self.lanzar_servidor.apagar_servidor())
        
        btn_apagar_servidor.grid(row=7, column=3,sticky="w")

        
        root.bind('<Return>', lambda event: self.model_class.evento_enter(self.var_busqueda))
    

        self.model_class.insertar_treeview()



if __name__ == "__main__":
    root = Tk()
    app=Vista(root)
    root.mainloop()