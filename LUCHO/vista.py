from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import modelo
	
class clase_vista():

    def __init__(self,window):

        """Clase destinada a ser el Constructor de la ventana de la interfaz tklinter"""

    	# Ventana principal

        self.root = window       
        self.root.geometry("600x500")
        self.root.title("Tarea POO")
        self.root.resizable(width=False, height=False)

        # Entry
        
        self.a_val, self.b_val = StringVar(), StringVar()           
        self.e1 = Entry(self.root, textvariable = self.a_val, width = 20).grid(row = 1, column = 1)
        self.e2 = Entry(self.root, textvariable = self.b_val, width = 20).grid(row = 2, column = 1)
        
        #Labels

        self.labelt = Label(self.root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        self.labelt.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
        self.label1 = Label(self.root, text="Título")
        self.label1.grid(row=1, column=0, sticky=W)
        self.label2 =Label(self.root, text="Descripción")
        self.label2.grid(row=2, column=0, sticky=W)
        self.labelradios = Label(self.root, text="Temas", height=1, width=70, fg="red", bg="black",borderwidth="5", relief="groove")
        self.labelradios.grid(row = 7, columnspan = 4, sticky = W + E) 
            

        # Botones ABMC 
        self.b_mostrar = Button(self.root, text = 'Mostrar registros existentes',command=lambda:modelo.clase_abmc.mostrar(self))
        self.b_mostrar.grid( row = 3, columnspan = 3, sticky = W + E)
        self.b_crearbd = Button(self.root,  text="Crear bd", anchor = E ,command=lambda:modelo.clase_abmc.crearbd(self))
        self.b_crearbd.grid(row=1, column=2,sticky = W)
        self.b_alta = Button(self.root, text="Alta", command=lambda:modelo.clase_abmc.alta(self))
        self.b_alta.grid(row=4, column=1)
        self.b_modificar = Button(self.root, text="Modificar", command=lambda:modelo.clase_abmc.modificar(self))
        self.b_modificar.grid(row=4, column=2)
        self.b_baja= Button(self.root, text="Baja", command=lambda:modelo.clase_abmc.baja(self))
        self.b_baja.grid(row=4, column=0)


        #Treeview
        self.tree = ttk.Treeview(height = 10, columns = 3)
        self.tree["columns"]=("one","three")
        self.tree.grid(row = 5, column = 0, columnspan = 3)

        #Titulos de columnas de Treeview
        self.tree.heading("#0",text="ID",anchor=CENTER)
        self.tree.heading("one", text = 'Título', anchor = CENTER)
        self.tree.heading("three", text = 'Descripción', anchor = CENTER) 

        # RadioBotones
        self.tema1 = str("Tema1")
        self.tema2 = str("Tema2")
        self.tema3 = str("Tema3")
        self.v_radios = IntVar()
        self.radiob1 = Radiobutton(self.root,text="Tema 1",variable=self.v_radios, value=1, padx=50, pady=10, fg="red", bg="black",command=lambda:modelo.clase_tema.funcion_tema(self,self.tema1, self.root))
        self.radiob1.grid(column=0, row=9,columnspan ="3")
        self.radiob2 =Radiobutton(self.root, text="Tema 2",variable=self.v_radios, value=2,padx=50, pady=10, fg="red", bg="black",command=lambda:modelo.clase_tema.funcion_tema(self,self.tema2,self.root))
        self.radiob2.grid(column=0, row=10,columnspan ="3")
        self.radiob3 =Radiobutton(self.root, text="Tema 3",variable=self.v_radios, value=3,  padx=50, pady=10, fg="red", bg="black",command=lambda:modelo.clase_tema.funcion_tema(self,self.tema3,self.root))
        self.radiob3.grid(column=0, row=11,columnspan ="3")

