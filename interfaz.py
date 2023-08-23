import tkinter as tk
from tkinter import ttk
#crear la ventana
ventana = tk.Tk()
ventana.title("Busqueda de error")

titulo = ttk.Label(ventana, text="Ingresa el codigo", font="Calibri 24")
titulo.pack(padx=10, pady=10)

entrada_texto = ttk.Entry(ventana)
entrada_texto.pack(padx=10, pady=10)

btn_buscar = ttk.Button(ventana, text="Buscar codigo")
btn_buscar.pack(padx=10, pady=10)

descripcion = ttk.Label(ventana,text="")
descripcion.pack(padx=10, pady=10)

ventana.mainloop() #va al final