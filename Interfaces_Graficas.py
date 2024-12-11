import tkinter.messagebox

#--------------Ventana--------------
ventana = tkinter.Tk()
ventana.title("Test TB")
#Tamaño
ventana.geometry("500x500")
#No queremos que cambie de tamaño
ventana.resizable(0,0)
#-----------Colocando etiqueta--------------
cabecera = tkinter.Label(ventana,text="----------**********__________Bienvenidos a todos__________**********----------").pack()
#-------------Botones---------------
def saludo():
    tkinter.Label(ventana,text="Hola mundo").pack()

def salir():
    ventana.destroy()

boton_saludo = tkinter.Button(ventana,text="Invoca un saludo",command=saludo,fg="red")
boton_saludo.pack()
# boton_saludo.place(x=200,y=200)

boton_salida = tkinter.Button(ventana,text="Salir",command=salir,fg="green")
boton_salida.pack()
# boton_salida.place(x=210,y=300,height=50,width=100)

#-------------------Messagebox----------------------
# tkinter.messagebox.showinfo("Test 1","Mensaje normal")

respuesta = tkinter.messagebox.askquestion("Eres Sub?","¿Ya le diste like a mi programa?")
if respuesta == "yes":
    tkinter.messagebox.showinfo("","Gracias por el apoyo")
else:
    tkinter.messagebox.showinfo("","Que esperas para darle like?")

#Visualizar
ventana.mainloop()