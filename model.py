from tkinter import Button
from peewee import *
# import sqlite3
import re
from my_classes import Utilities

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
db.create_tables([Musica])

##--Modelo--##

class Model():
    def __init__(self, tree):
        self.tree = tree
        self.type_error = None
        self.guardar_cambios_btn = None
        self.my_utilities = Utilities(tree)



    # def enter_event(self, e, var_search):
    #     self.buscar_item(self.tree, var_search)


    """ CRUD """



    def guardar(self, name, country, genre, description, entry_name, entry_country, entry_gender, entry_description, root):
        if not all((name, country, genre, description)):
            Utilities.advertencia("se deben rellenar todas las entradas", "red", "white", 4, 1, root)
            return
        patron = "^[a-zA-Z0-9 ]*$"
        if re.match(patron, name):
            name_capitalized = Utilities.capitalized_doubled(name)
            musica=Musica()
            musica.nombre=name_capitalized
            musica.genero=genre.capitalize()
            musica.pais=country.capitalize()
            musica.descripcion=description.capitalize()
            musica.save()
            self.my_utilities.update_treeview_GUI()
            self.insert_treeview()
            Utilities.clear_entries(entry_name, entry_country, entry_gender, entry_description)
            Utilities.advertencia("cantante guardada con éxito 😁", "green", "white", 4, 1, root)
        else:
            Utilities.advertencia("Sólo se aceptan números o letras", "red", "white", 1, 1, root)


    def insert_treeview(self):
        for row in Musica.select():
            self.tree.insert("", 0, text=row.id, values=(row.nombre, row.pais, row.genero, row.descripcion))

    def eliminar_item(self):
        items_seleccionados = self.tree.selection() 
        selected_id = self.tree.item(items_seleccionados)
        borrar=Musica.get(Musica.id==selected_id['text'])
        borrar.delete_instance()
        for item in items_seleccionados:
            self.tree.delete(item)



    def editar_item(self, root, var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description):
        global guardar_cambios_btn
        selected_item = self.tree.selection()
        if selected_item:
            selected_id = self.tree.item(selected_item, "text")
            selected_obj = Musica.get_or_none(id=selected_id)
            if selected_obj:
                var_name.set(selected_obj.nombre)
                var_country.set(selected_obj.pais)
                var_gender.set(selected_obj.genero)
                var_description.set(selected_obj.descripcion)
                guardar_cambios_btn = Button(root, text="Guardar Cambios", command=lambda:self.guardar_cambios(var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description))
                guardar_cambios_btn.grid(row=1, column=2, sticky="w")


    def guardar_cambios(self, var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description):
        selected_item = self.tree.selection()
        selected_id = self.tree.item(selected_item, "text")
        name_capitalized = Utilities.capitalized_doubled(var_name.get())
        var_name  = name_capitalized

        update = Musica.update(nombre = name_capitalized, pais = var_country.get().capitalize() , genero = var_gender.get().capitalize() , descripcion = var_description.get().capitalize()  ).where(Musica.id == selected_id)
        update.execute()
        Utilities.clear_entries(entry_name, entry_country, entry_gender, entry_description)
        self.my_utilities.update_treeview_GUI()
        self.insert_treeview()
        guardar_cambios_btn.destroy()
        

    def buscar_item(self, var_search):
        self.my_utilities.update_treeview_GUI()
        selected_obj = Musica.select()
        search_value = var_search.get().lower()  
        print(selected_obj)
        for record in selected_obj:
            if any(search_value in str(getattr(record, field)).lower() for field in record._meta.fields):
                self.tree.insert("", 0, text=record.id, values=(record.nombre, record.pais, record.genero, record.descripcion))

