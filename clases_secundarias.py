""" 

clases_secundarias.py: 

Módulo que tiene como objetivo entregar clases y métodos que ayuden a organizar mejor las clases importantes de las complementarias

"""


from tkinter import Label
import sqlite3
import re
import datetime
from servidor_cliente_sockets import Servidor

class Utilidades():

    """
    
    Clase con diferentes métodos utilitarios que ayudan al funcionamiento global de la aplicación
    
    """
    def __init__(self, tree):
        self.tree = tree
        self.cliente_socket = Servidor()
    
    def actualizar_treeview_GUI(self):
       
       """
       actualiza la interfaz del Treeview

       """

       for item in self.tree.get_children():
          self.tree.delete(item)

    def capitalizar_doble(self, nombre_artista):

        """
        Capitaliza ambos nombres de la artista en el caso de que haya dos

        """

        nombre_split = nombre_artista.split()
        if len(nombre_split) >= 2:
                nombre_split[0] = nombre_split[0].capitalize()
                nombre_split[1] = nombre_split[1].capitalize()
                nombre_capitalizado = ' '.join(nombre_split)
                return nombre_capitalizado
        else:
            return nombre_artista.capitalize()
        

    
    def advertencia(self, texto, colorfg, colorbg, row, col, root):

        """
        
        Crea una ventana de advertencia con un texto y colores
        
        """
        global type_error
        type_error = Label(root, text=texto, fg=colorfg, bg=colorbg)
        type_error.grid(row=row, column=col)
        root.after(2000, lambda:type_error.destroy())  


    def limpiar_entradas(self, val1, val2, val3, val4):

        """
        Limpia las entradas de la interfaz del Treeview
        
        """
        entradas = [val1, val2, val3, val4]
        for entry in entradas:
            entry.delete(0, 'end')



class MyDataBase():

    """
    Clase creadora de la base de datos. Acá se crea directamente la base de datos y su respectiva conexión.
    
    """

    def __init__(self):
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect('mydatabase.db')
            self.conn.execute("PRAGMA encoding = 'UTF-8'")
            print("Conectado a la base de datos")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Hubo un error con SQLite", e)
        except Exception as e:
            print("Hubo un error", e)


    def crear_tabla(self):
 
        """
        Método creador de la tabla de la base de datos SQLite3

        """

        try:
            sql = """CREATE TABLE IF NOT EXISTS mujeres_en_la_musica
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre varchar(20) NOT NULL,
                    país varchar(20) NOT NULL, 
                    género varchar(20) NOT NULL,
                    descripción TEXT NOT NULL
                    )"""
            self.cursor.execute(sql)
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error al crear la tabla", e)


class Validar():

    """
    
    Clase cuyos métodos sirven para validar carácteres válidos que se ingresan en las entradas
    
    """


    def __init__(
        self,
    ):
        print("validado")
    
    
    def validar_nombre(self, name):

        """
        Clase que valida que el nombre de la artista comience sólo con números o letras

        """
        patron = "^[a-zA-Z0-9 ]*$"
        if re.match(patron, name):
            return True
        else:
            print("Sólo se aceptan números o letras")






class Decoradores_iea:


    """ 
    Clase decoradora que crea diferentes decoradores para las acciones que sucedan en la app 

    """

    def __init__(self, option):
        self.option = option
        self.cliente_socket = Servidor()


    def __call__(self, func):
        def wrapper(*args, **kwargs):
            fcn_retornada = func(*args, **kwargs)
            date_time = datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')

            with open('log.txt', 'a') as file:  
                    
                if self.option == 'option2':
                    print("Se ha eliminado un registro")
                    file.write(f"registro eliminado con id: {fcn_retornada} el dia {date_time}.\n")
                    
                    return fcn_retornada
                elif self.option == 'option3':
                    print("Se ha actualizado un registro")
                    file.write(f"registro actualizado con id: {fcn_retornada} el dia {date_time}.\n")
                    
                    return fcn_retornada
        

        return wrapper


