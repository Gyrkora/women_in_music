""" 

clases_secundarias.py: 

Módulo que tiene como objetivo entregar clases y métodos que ayuden a organizar mejor las clases importantes de las complementarias

"""


from tkinter import Label
import sqlite3
import re
import datetime

# import sys
# import os

class Utilidades():

    """
    
    Clase con diferentes métodos utilitarios que ayudan al funcionamiento global de la aplicación
    
    """
    def __init__(self, tree):
        self.tree = tree
    
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
    def __init__(self, option):
        self.option = option

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            fcn_retornada = func(*args, **kwargs)
            date_time = datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')

            with open('log.txt', 'a') as file:  
                if self.option == 'option1':
                    print("nuevo registro")
                    file.write(f"el dia {date_time}.\n")
                elif self.option == 'option2':
                    print("Se ha eliminado un registro")
                    file.write(f"registro eliminado con id: {fcn_retornada} el dia {date_time}.\n")
                    return fcn_retornada
                elif self.option == 'option3':
                    print("Se ha actualizado un registro")
                    file.write(f"registro actualizado con id: {fcn_retornada} el dia {date_time}.\n")
                    return fcn_retornada
        

        return wrapper


theproc = ""

import subprocess
import threading
import sys
import os
from pathlib import Path
import socket

theproc = None

class Servidor():

    def __init__(self) -> None:
        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz, 'src', 'servidor.py')

    def iniciar_conexion(self):
        global theproc
        if theproc is not None:
            self.apagar_servidor()
        threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
            
    def lanzar_servidor(self, var):
        global theproc
        the_path = self.ruta_server
        if var == True:
            theproc = subprocess.Popen([sys.executable, the_path])
            print('Servidor iniciado desde ventanita')
            theproc.communicate()

    def apagar_servidor(self):
        global theproc
        if theproc is not None:  
            try:
                theproc.kill()  
                theproc = None  
                print("Servidor apagado")
            except Exception as e:
                print(f"Error al intentar apagar el servidor: {e}")


    def conexion_cliente(nuevo_registro, server_host='127.0.0.1', server_port=65432):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_host, server_port))
            with open('log.txt', 'a') as file:  
                file.write(f"nuevo registro con nombre =  {nuevo_registro}  ")
            s.sendall(b"Hola, servidor. Soy el cliente.")
            data = s.recv(1024)
            print(f"Mensaje recibido del servidor: {data.decode('utf-8')}")
