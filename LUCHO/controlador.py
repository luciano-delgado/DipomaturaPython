from tkinter import *
import vista


class controlador():

	""" Clase controladora que toma la consulta externa y la dirige hacia la vista tkinter junto con las funcionalidades del modelo"""

	def __init__(self,ventana):
		self.ventana = ventana
		vista.clase_vista(self.ventana)

if __name__ == '__main__':	
	""" Desarrollador"""	

	root = Tk()
	app = controlador(root)

	mainloop()

	# Imprimir la informacion de la cadena de documentacion del constructor de la clase vista 
	print(app.__init__.__doc__)

	# ¿¿¿DEBERIA IMPRIMIRME "Clase destinada a ser el Constructor de la ventana de la interfaz tklinter" pero no lo hace???