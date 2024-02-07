""" 

modelo.py: 

En este módulo se puede encontrar el funcionamiento de la API, ya que utiliza los métodos guardar, editar, eliminar, crear, además de otros complementarios que ayudan a sus total funcionamiento.

"""


from tkinter import Button
from clases_secundarias import Utilidades, MyDataBase, Validar, Decoradores_iea
from observador import Sujeto


class Abmc(Sujeto):
    def __init__(self, tree):
        self.tree = tree
        self.type_error = None
        self.guardar_cambios_btn = None
        self.mis_utilidades = Utilidades(tree)
        self.db = MyDataBase()
        self.db.crear_tabla()


    def evento_enter(self, var_busqueda):
        try:

            self.buscar_item(self.tree, var_busqueda)
        except TypeError as e:
            print("Este es el error ==>", e)    



    @Decoradores_iea(option="option1")
    def guardar(self, nombre, pais, genero, descripcion, entrada_nombre, entrada_pais, entrada_genero, entrada_descripcion, root):

        """
        método principal que guarda los datos

        """

        validar_nombre = Validar().validar_nombre

        if not all((nombre, pais, genero, descripcion)):
            self.mis_utilidades.advertencia("se deben rellenar todas las entradas", "red", "white", 4, 1, root)
            return
        if validar_nombre(nombre):
            nombre_capitalizado = self.mis_utilidades.capitalizar_doble(nombre)
            data = (nombre_capitalizado, pais.capitalize(), genero.capitalize(), descripcion.capitalize())
            sql = "INSERT INTO mujeres_en_la_musica(nombre, país, género, descripción) VALUES(?, ?, ?, ?)"
            self.db.cursor.execute(sql, data)
            self.db.conn.commit()
            self.mis_utilidades.actualizar_treeview_GUI()
            self.insertar_treeview()
            self.mis_utilidades.limpiar_entradas(entrada_nombre, entrada_pais, entrada_genero, entrada_descripcion)
            self.mis_utilidades.advertencia("cantante guardada con éxito 😁", "green", "white", 4, 1, root)
            self.notificar(nombre, descripcion)
        else:
            self.mis_utilidades.advertencia("Sólo se aceptan números o letras", "red", "white", 1, 1, root)

    @Decoradores_iea(option="option2")
    def eliminar_item(self):

        """
        
        Elimina los datos 
        
        """

        try:
            items_seleccionados = self.tree.selection() 
            for item in items_seleccionados:
                id_item = self.tree.item(item, "text")
                mi_id = id_item
                data = (mi_id,)
                sql = "DELETE FROM mujeres_en_la_musica WHERE id = ?"
                self.db.cursor.execute(sql, data)
                self.db.conn.commit()
                self.tree.delete(item)
                return id_item
        except Exception as e:
            print("El error es el siguiente ==> ", e)



    def insertar_treeview(self):

        """ 
        Se insertan los elementos dentro del Treeview 
        
        """

        sql = "SELECT * FROM mujeres_en_la_musica ORDER BY id ASC"
        datos = self.db.cursor.execute(sql)
        datos_db = datos.fetchall()
        for row in datos_db:
            self.tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4]))

    def buscar_item(self, tree, var_busqueda):


        """
        
        Busca elementos dentro de la base de datos y los muestra en el Treeview
        
        """


        try:
            self.mis_utilidades.actualizar_treeview_GUI()
            sql = "SELECT * FROM mujeres_en_la_musica ORDER BY id ASC"
            datos = self.db.cursor.execute(sql)
            value_busqueda = var_busqueda.get().lower()  
            datos_db = datos.fetchall()
            for dato in datos_db:
                if any(value_busqueda in str(value).lower() for value in dato):
                    tree.insert("", 0, text=dato[0], values=(dato[1], dato[2], dato[3], dato[4]))
        except Exception as e:
            print("Hubo un error al buscar los elementos ==> ", e)
    
    def editar_item(self, root, var_nombre, var_pais, var_genero, var_descripcion, entrada_nombre, entrada_pais, entrada_genero, entrada_descripcion):
       
        
        """
        Modifica los datos desde el treeview hasta la base de datos

        """
       
        global guardar_cambios_btn
        try:
            elementos_seleccionados = self.tree.selection()
            if elementos_seleccionados:
                id_seleccionado = self.tree.item(elementos_seleccionados, "text") 
                seleccion_sql = "SELECT * FROM mujeres_en_la_musica WHERE id=?"
                self.db.cursor.execute(seleccion_sql, (id_seleccionado,))
                row = self.db.cursor.fetchone()
                if row:
                    var_nombre.set(row[1])
                    var_pais.set(row[2])
                    var_genero.set(row[3])
                    var_descripcion.set(row[4])
                    guardar_cambios_btn = Button(root, text="Guardar Cambios", command=lambda:self.guardar_cambios(var_nombre, var_pais, var_genero, var_descripcion, entrada_nombre, entrada_pais, entrada_genero, entrada_descripcion))
                    guardar_cambios_btn.grid(row=1, column=2, sticky="w")
        except Exception as e:
            print("Hubo un error editar los elementos ==>", e)


    @Decoradores_iea(option="option3")
    def guardar_cambios(self, var_nombre, var_pais, var_genero, var_descripcion, entrada_nombre, entrada_pais, entrada_genero, entrada_descripcion):
        
        """
        
        Método complementario de "guardar" que crea un nuevo botón como reemplazo

        """
        
        try:
            elementos_seleccionados = self.tree.selection()
            id_seleccionado = self.tree.item(elementos_seleccionados, "text")
            nombre_capitalizado = self.mis_utilidades.capitalizar_doble(var_nombre.get())
            var_nombre  = nombre_capitalizado
            self.db.cursor.execute("UPDATE mujeres_en_la_musica SET nombre=?, país=?, género=?, descripción=? WHERE id=?", (
                nombre_capitalizado, var_pais.get().capitalize(), var_genero.get().capitalize(), var_descripcion.get().capitalize(), id_seleccionado))
            self.db.conn.commit()
            self.mis_utilidades.limpiar_entradas(entrada_nombre, entrada_pais, entrada_genero, entrada_descripcion)
            self.mis_utilidades.actualizar_treeview_GUI()
            self.insertar_treeview()
            guardar_cambios_btn.destroy()
            return id_seleccionado
        except Exception as e:
            print("Hubo un error al guardar los cambios", e)
        

