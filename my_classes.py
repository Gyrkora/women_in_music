from tkinter import Label
import sqlite3

class Utilities():
    def __init__(self, tree):
        self.tree = tree
    
    def update_treeview_GUI(self):
       for item in self.tree.get_children():
          self.tree.delete(item)

    def capitalized_doubled(artists_name):
        name_split = artists_name.split()
        if len(name_split) >= 2:
                name_split[0] = name_split[0].capitalize()
                name_split[1] = name_split[1].capitalize()
                name_capitalized = ' '.join(name_split)
                return name_capitalized
        else:
            return artists_name.capitalize()
        

    
    def advertencia(texto, colorfg, colorbg, row, col, root):
        global type_error
        type_error = Label(root, text=texto, fg=colorfg, bg=colorbg)
        type_error.grid(row=row, column=col)
        root.after(2000, lambda:type_error.destroy())  


    def clear_entries(val1, val2, val3, val4):
        entries = [val1, val2, val3, val4]
        for entry in entries:
            entry.delete(0, 'end')



class MyDataBase():
    def __init__(self):
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect('mydatabase.db')
            self.conn.execute("PRAGMA encoding = 'UTF-8'")
            print("Conectado")
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("the error ==> ", e)


    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS mujeres_en_la_musica
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(20) NOT NULL,
                país varchar(20) NOT NULL, 
                género varchar(20) NOT NULL,
                descripción TEXT NOT NULL
                )"""
        self.cursor.execute(sql)
        self.conn.commit()
    