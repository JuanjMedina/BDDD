from tkinter import *
import sqlite3

MiConexion = sqlite3.connect("ProyectoU")
MiCursor = MiConexion.cursor()



raiz = Tk()
raiz.title("interfaz 1")
raiz.config(height=250,width=250)
escribir = StringVar()

frame= Frame(raiz, width=500, height=500)
frame.pack()


Materia= Entry(frame,textvariable=escribir, fg="red",state="readonly")
Materia.grid(row=0,column=1,pady=5,padx=5,sticky="w")

Nota= Entry(frame)
Nota.grid(row=1,column=1,padx=5,pady=5)

Fecha = Entry (frame)
Fecha.grid(row=2,column=1,padx=5,pady=5)

Contra= Entry(frame,justify="center")
Contra.grid(row=3,column=1,padx=5,pady=5)
Contra.config(fg="green",show="*", justify="center")


texto1= Text(frame,width=15,height=10)
texto1.grid(row=4,column=1)

barradeScroll = Scrollbar(frame,command=texto1.yview)
barradeScroll.grid(row=4,column=2, sticky="nswe")
    
texto1.config(yscrollcommand=barradeScroll.set)


def codigoboton():
    escribir.set("Pedro")


class boton():
    boton1 = Button(frame,text="Agregar",command=codigoboton)
    boton1.grid(row=6,column=1,padx=5,pady=10)




class label():
    MateriaLabel= Label(frame,text="Nombre:")
    MateriaLabel.grid(row=0,column=0,padx=5,pady=5,sticky="w")

    NotaLabel= Label(frame,text="Nota:")
    NotaLabel.grid(row=1,column=0,padx=5,pady=5,sticky="w")

    FechaLabel= Label(frame,text="Fecha:")
    FechaLabel.grid(row=2,column=0,padx=5,pady=5,sticky="w")

    ContraLabel = Label(frame,text="contraseña:")
    ContraLabel.grid(row=3,column=0,pady=5,padx=5,sticky="w")

    comentarioLabel = Label(frame, text="Comentarios:")
    comentarioLabel.grid(row=4,column=0)

raiz.mainloop()

MiConexion.commit()


MiConexion.close()