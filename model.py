from tkinter import Button
from peewee import *
# import sqlite3
# import re
from my_classes import Utilities, MyDataBase

db = SqliteDatabase("mi_base.db")


class BaseModel(Model):
    class Meta:
        database = db


class Musica(BaseModel):
    nombre = CharField(unique=True)
    genero = CharField()
    pais = CharField()
    descripcion = CharField()

db.connect()
db.create_tables(Musica)

##--Modelo--##

class Model():
    def __init__(self, tree):
        self.tree = tree
        self.type_error = None
        self.guardar_cambios_btn = None
        self.my_utilities = Utilities(tree)
        self.db = MyDataBase()
        self.db.create_table()


    # def enter_event(self, var_search):
    #     self.buscar_item(self.tree, var_search)


    """ CRUD """

    # def guardar(self, name, country, gender, description, entry_name, entry_country, entry_gender, entry_description, root):
    #     if not all((name, country, gender, description)):
    #         Utilities.advertencia("se deben rellenar todas las entradas", "red", "white", 4, 1, root)
    #         return
    #     patron = "^[a-zA-Z0-9 ]*$"
    #     if re.match(patron, name):
    #         name_capitalized = Utilities.capitalized_doubled(name)
    #         data = (name_capitalized, country.capitalize(), gender.capitalize(), description.capitalize())
    #         sql = "INSERT INTO mujeres_en_la_musica(nombre, país, género, descripción) VALUES(?, ?, ?, ?)"
    #         self.db.cursor.execute(sql, data)
    #         self.db.conn.commit()
    #         self.my_utilities.update_treeview_GUI()
    #         self.insert_treeview()
    #         Utilities.clear_entries(entry_name, entry_country, entry_gender, entry_description)
    #         Utilities.advertencia("cantante guardada con éxito 😁", "green", "white", 4, 1, root)
    #     else:
    #         Utilities.advertencia("Sólo se aceptan números o letras", "red", "white", 1, 1, root)

    # def eliminar_item(self):
    #     items_seleccionados = self.tree.selection() 
    #     for item in items_seleccionados:
    #         id_item = self.tree.item(item, "text")
    #         print(id_item)
    #         mi_id = id_item
    #         print(type(mi_id))
    #         data = (mi_id,)
    #         sql = "DELETE FROM mujeres_en_la_musica WHERE id = ?"
    #         self.db.cursor.execute(sql, data)
    #         self.db.conn.commit()
    #         self.tree.delete(item)


    # def insert_treeview(self):
    #     sql = "SELECT * FROM mujeres_en_la_musica ORDER BY id ASC"
    #     datos = self.db.cursor.execute(sql)
    #     datos_db = datos.fetchall()
    #     for row in datos_db:
    #         self.tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4]))

    # def buscar_item(self, tree, var_search):
    #     self.my_utilities.update_treeview_GUI()
    #     sql = "SELECT * FROM mujeres_en_la_musica ORDER BY id ASC"
    #     datos = self.db.cursor.execute(sql)
    #     search_value = var_search.get().lower()  
    #     datos_db = datos.fetchall()
    #     for dato in datos_db:
    #         if any(search_value in str(value).lower() for value in dato):
    #             tree.insert("", 0, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4]))

    # def editar_item(self, root, var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description):
    #     global guardar_cambios_btn
    #     selected_item = self.tree.selection()
    #     if selected_item:
    #         selected_id = self.tree.item(selected_item, "text") 
    #         sql_selection = "SELECT * FROM mujeres_en_la_musica WHERE id=?"
    #         self.db.cursor.execute(sql_selection, (selected_id,))
    #         row = self.db.cursor.fetchone()
    #         if row:
    #             var_name.set(row[1])
    #             var_country.set(row[2])
    #             var_gender.set(row[3])
    #             var_description.set(row[4])
    #             guardar_cambios_btn = Button(root, text="Guardar Cambios", command=lambda:self.guardar_cambios(var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description))
    #             guardar_cambios_btn.grid(row=4, column=1, pady=15)

    # def guardar_cambios(self, var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description):
    #     selected_item = self.tree.selection()
    #     selected_id = self.tree.item(selected_item, "text")
    #     name_capitalized = Utilities.capitalized_doubled(var_name.get())
    #     var_name  = name_capitalized
    #     self.db.cursor.execute("UPDATE mujeres_en_la_musica SET nombre=?, país=?, género=?, descripción=? WHERE id=?", (
    #         name_capitalized, var_country.get().capitalize(), var_gender.get().capitalize(), var_description.get().capitalize(), selected_id))
    #     self.db.conn.commit()
    #     Utilities.clear_entries(entry_name, entry_country, entry_gender, entry_description)
    #     self.my_utilities.update_treeview_GUI()
    #     self.insert_treeview()
    #     guardar_cambios_btn.destroy()
