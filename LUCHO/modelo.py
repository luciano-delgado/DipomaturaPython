from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import mysql.connector   


class clase_validacion():

    """ Clase destinada a validar caracteres alfanumericos mediante una cadena regex"""

    def validar(a):

        patron = "^[A-Za-z0-9]+(?:[ _-][A-Za-z]+)*$"
        
        if (re.match(patron,a)):
            return True
        else:
            return False

class clase_abmc(clase_validacion):

    """ Clase destinada a comunicarse con la base de datos y gestionar ABMC de registros, heredando el metodo validar de su clase
    padre clase_validacion 

    """

    def mostrar(self):

        """ Metodo que muestra registros existentes en base de datos """
        try:
            # limpieza de tabla 
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)

            # Consiguiendo datos
            sql_select='SELECT * FROM producto ORDER BY id ASC'
            mibase = mysql.connector.connect(host="localhost", user="root", passwd="" ,database = "base_luciano3")
            micursor = mibase.cursor()     
            micursor.execute(sql_select)
            resultado = micursor.fetchall()

            for fila in resultado:
                self.tree.insert('', 0, text = fila[0], values = (fila[1],fila[2]))
        except:
            messagebox._show(message="Aún no se ha creado una bd")

    def alta(self):    

        """ Metodo que realiza el alta de los registros que ingreso en los entrys, validando los campos previamente"""

        cadena1=self.a_val.get() 
        cadena2=self.b_val.get() 

        if(clase_validacion.validar(cadena1))==True:
            if (clase_validacion.validar(cadena2))==True:
               
                mibase = mysql.connector.connect(host="localhost", user="root", passwd="" ,database = "base_luciano3")
                micursor = mibase.cursor()
                sql_insert = "INSERT INTO producto (titulo, descripcion) VALUES (%s, %s)"
                datos = (self.a_val.get(), self.b_val.get())
                micursor.execute(sql_insert, datos)
                mibase.commit()
                messagebox._show(message="Alta exitosa --> Datos validados")
        else:
            messagebox.showerror(message= "Error! Escriba caracteres Alfanumericos!")  
        #Consulta
        clase_abmc.mostrar(self)

    def crearbd(self,):

        """ Metodo que crea la base de datos "base_luciano3" si esta misma no existe previamente"""

        try:
            mibase = mysql.connector.connect(host="localhost", user="root", passwd="" )
            micursor = mibase.cursor()
            micursor.execute("CREATE DATABASE base_luciano3")
            mibase = mysql.connector.connect(host="localhost", user="root",passwd="",database="base_luciano3")
            micursor = mibase.cursor()
            micursor.execute("CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
            
            messagebox._show(message= "Base de datos creada")
            
        except:
            messagebox.showerror(message= "Ya existe la base de datos")

    def baja(self,):

        """ Metodo para borrar registros seleccionados"""

        try:
            mibase = mysql.connector.connect(host="localhost", user="root", passwd="" ,database = "base_luciano3")
            micursor = mibase.cursor()
            micursor.execute("USE base_luciano3")

            elemento= self.tree.focus()  #sfunciono item de la lista ("hago foco/click")
            elemento_dicc = self.tree.item(elemento) # atributo item: me devuelve un dicc con la info del item
            id_valor = elemento_dicc["text"] # tomo el valor de la columna 1, es decir el ID 
            id_valor = str(id_valor)
            sql_delete= "DELETE FROM producto WHERE id = " + id_valor
            micursor.execute(sql_delete)
            mibase.commit()
            
            sql_select = "SELECT * FROM base_luciano3.producto"
            micursor.execute(sql_select)
            mibase2 = self.micursor.fetchall()
            self.tree.delete(*tree.get_children())
            for row in mibase2:
                self.tree.insert("", "end", text=row[0],values=(row[1], row[2]))

        except:
            messagebox.showinfo(message = "Confirma que desea borrar el registro?")

        #Consulta
        clase_abmc.mostrar(self)

    def modificar(self):

        """Metodo para modificar registros existentes previamente seleccionados"""
        try:
            item = self.tree.focus()
            dicc_item=self.tree.item(item)
            id_valor=int(dicc_item["text"])
            self.tree.delete(item) 
            mibase = mysql.connector.connect(host="localhost", user="root", passwd="" ,database = "base_luciano3")
            micursor = mibase.cursor()
            micursor.execute("USE base_luciano3")
            sql_update = "UPDATE producto SET titulo =%s WHERE id=%s"
            datos=(self.a_val.get(),id_valor)
            sql_update2 = "UPDATE producto SET descripcion =%s WHERE id=%s"
            datos2=(self.b_val.get(),id_valor)
            micursor.execute(sql_update,datos)
            micursor.execute(sql_update2,datos2)
            mibase.commit()
            self.tree.insert("", "end", text=str(id_valor), values=(str(self.a_val.get()),str(self.b_val.get())))
        except:
            messagebox.showinfo(message = "Seleccione registro a modificar")

    # Limpio y muestro datos con la mofificacion            
    
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        mibase = mysql.connector.connect(host="localhost", user="root", passwd="" ,database = "base_luciano3")
        micursor = mibase.cursor()
        micursor.execute("USE base_luciano3")
        sql_select = "SELECT * FROM base_luciano3.producto ORDER BY id DESC"
        micursor.execute(sql_select)
        registros_base = micursor.fetchall()    
        for fila in registros_base:
            self.tree.insert('', 0, text = fila[0], values = (fila[1],fila[2]))

        #Consulta
        clase_abmc.mostrar(self)



class clase_tema():

    def funcion_tema(self, tema, window):

        self.tema = str(tema)
        self.root = window


        if "Tema1" == self.tema:
            self.root.configure(background="green")


        elif "Tema2" == self.tema:
            self.root.configure(background="black")


        elif "Tema3" == self.tema:
            self.root.configure(background="blue")
        else:pass

        return self.tema, self.root   