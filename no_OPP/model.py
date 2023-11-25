from tkinter import Label
from tkinter import Button
import sqlite3
import re


##--Modelo--##


""" Base de datos """
def connexión():
    con = sqlite3.connect("women_in_music.db")
    con.execute("PRAGMA encoding = 'UTF-8'")
    return con

con = connexión()
cursor = con.cursor()
type_error = None
guardar_cambios_btn = None

def crear_tabla():
    sql = """CREATE TABLE IF NOT EXISTS mujeres_en_la_musica
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre varchar(20) NOT NULL,
             país varchar(20) NOT NULL, 
             género varchar(20) NOT NULL,
             descripción TEXT NOT NULL
             )"""
    cursor.execute(sql)
    con.commit()

crear_tabla()

""" funciones de utilidad """

def update_treeview_GUI(tree):
   for item in tree.get_children():
      tree.delete(item)

def clear_entries(val1, val2, val3, val4):
    entries = [val1, val2, val3, val4]
    for entry in entries:
        entry.delete(0, 'end')


def enter_event(e, tree, var_search):
    buscar_item(tree, var_search)

def advertencia(texto, colorfg, colorbg, row, col, root):
    global type_error
    type_error = Label(root, text=texto, fg=colorfg, bg=colorbg)
    type_error.grid(row=row, column=col)
    root.after(2000, lambda:type_error.destroy())  

def capitalized_doubled(artists_name):
    name_split = artists_name.split()
    if len(name_split) >= 2:
            name_split[0] = name_split[0].capitalize()
            name_split[1] = name_split[1].capitalize()
            name_capitalized = ' '.join(name_split)
            return name_capitalized
    else:
        return artists_name.capitalize()

""" CRUD """

def guardar(name, country, gender, description, tree, entry_name, entry_country, entry_gender, entry_description, root):
    global type_error
    if not all((name, country, gender, description)):
        print("Error", "Please fill in all mandatory fields.")
        advertencia("se deben rellenar todas las entradas", "red", "white", 4, 1, root)
        return
    patron="^[a-zA-Z0-9 ]*$"
    if(re.match(patron, name)):
        print("entrada válida")
        name_capitalized = capitalized_doubled(name)
        data = (name_capitalized, country.capitalize(), gender.capitalize(), description.capitalize())
        sql = "INSERT INTO mujeres_en_la_musica(nombre, país, género, descripción) VALUES(?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        update_treeview_GUI(tree)
        insert_treeview(tree)
        clear_entries(entry_name, entry_country, entry_gender, entry_description)
        advertencia("cantante guardada con éxito 😁", "green", "white", 4, 1, root)
       
    else:
        advertencia("Sólo se aceptan números o letras", "red", "white", 1, 1, root)


def eliminar_item(tree):
    items_seleccionados = tree.selection() 
    for item in items_seleccionados:
        id_item = tree.item(item, "text")
        print(id_item)
        mi_id = id_item
        print(type(mi_id))
        data = (mi_id,)
        sql = "DELETE FROM mujeres_en_la_musica WHERE id = ?"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(item)


def insert_treeview(tree):

    sql = "SELECT * FROM mujeres_en_la_musica ORDER BY id ASC"
    datos = cursor.execute(sql)

    datos_db = datos.fetchall()
    for row in datos_db:
        tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4]))

def buscar_item(tree, var_search):
    update_treeview_GUI(tree)
    sql = "SELECT * FROM mujeres_en_la_musica ORDER BY id ASC"
    datos = cursor.execute(sql)
    search_value = var_search.get().lower()  
    datos_db = datos.fetchall()
    for dato in datos_db:
        if any(search_value in str(value).lower() for value in dato):
                tree.insert("", 0, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4]))


def editar_item(root, tree, var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description):
    global guardar_cambios_btn
    selected_item = tree.selection()
    if selected_item:
        selected_id = tree.item(selected_item, "text") 
        sql_selection = "SELECT * FROM mujeres_en_la_musica WHERE id=?"
        cursor.execute(sql_selection, (selected_id,))
        row = cursor.fetchone()

        if row:
            var_name.set(row[1])
            var_country.set(row[2])
            var_gender.set(row[3])
            var_description.set(row[4])
            guardar_cambios_btn = Button(root, text="Guardar Cambios", command=lambda:guardar_cambios(tree, var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description))
            guardar_cambios_btn.grid(row=4, column=1, pady=15)


def guardar_cambios(tree, var_name, var_country, var_gender, var_description, entry_name, entry_country, entry_gender, entry_description) :
    selected_item = tree.selection()
    selected_id = tree.item(selected_item, "text")

    cursor.execute("UPDATE mujeres_en_la_musica SET nombre=?, país=?, género=?, descripción=? WHERE id=?", (
        var_name.get(), var_country.get(), var_gender.get(), var_description.get(), selected_id))

    con.commit()
    clear_entries(entry_name, entry_country, entry_gender, entry_description)
    update_treeview_GUI(tree)
    insert_treeview(tree)
    guardar_cambios_btn.destroy()
