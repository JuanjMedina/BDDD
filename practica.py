from distutils.cmd import Command
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

Miconexion = sqlite3.connect("ProyectoPersonal")
micursor= Miconexion.cursor()


raiz = Tk()
raiz.title("Base de datos")
barramenu = Menu(raiz)
barramenu = Menu(raiz)
raiz.config(height=250, width=250, menu=barramenu)
Dibujo = Frame(raiz)
Dibujo.config(bg="white")
Dibujo.pack()

minota= StringVar()

mimateria = Label(
Dibujo, width=40, text="Selecciona la materia a implementar la nota", padx=4, pady=9, bg="white")
mimateria.config(justify="left")
mimateria.grid(row=1, column=1)

miNota = Label(Dibujo, width=40, text="Tipo de Nota:",background="white", justify="left", pady=9)
miNota.grid(row=2, column=1)

minum= Label(Dibujo,width=40,text="Ponga la nota ",background="white",justify="left")
minum.grid(row=3,column=1)

Entrynota= Entry(Dibujo,width=23,textvariable=minota)
Entrynota.grid(row=3,column=2)

Observacion = Label(Dibujo, width=40, text="Observacion:",background="white", justify="left")
Observacion.grid(row=4, column=1)


Miobservacion = Text(Dibujo, width=15, height=8, pady=15, padx=10)
Miobservacion.grid(row=4, column=2)

Materias = ttk.Combobox(Dibujo, state="readonly", values=["Calculo", "Algebra", "Mecanica", "Programacion"])
Materias.grid(row=1, column=2)

Notas = ttk.Combobox(Dibujo, state="readonly", values=["Parciales", "Talleres", "Quices", "Informes"])
Notas.grid(row=2, column=2)

#micursor.execute("CREATE TABLE NOTAS(Materia VarChar (15), Tipo_Nota Varchar (20), Nota Float(3), Observacion Text)")

def agregar():

    global minota
    global Materias
    global Notas
    global Miobservacion
    Materia=Materias.get()
    Tipo_nota=Notas.get()
    Nota=minota.get()
    Observaciones= Miobservacion.get("1.0",END)
    minota.set("")
    Miobservacion.delete("1.0",END)
    micursor.execute("INSERT INTO NOTAS VALUES('"+Materia+"','"+Tipo_nota+"','"+Nota+"','"+Observaciones+"')")
    
    
    print(Materia,Tipo_nota,Nota,Observaciones)


def mostrarinfo():
    micursor.execute("SELECT * FROM NOTAS")
    informacion= micursor.fetchall()
    print(informacion)
    pass

Boton = Button(Dibujo, text="Agregar", padx=20,command=lambda:agregar())
Boton.grid(row=6, column=2, pady=10)

mirarinfo =Button(Dibujo,text="informacion",pady=4,command=lambda:mostrarinfo())
mirarinfo.grid(row=6,column=1 )

archivomenu = Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Nuevo")
archivomenu.add_command(label="Guardar")
archivomenu.add_separator()
archivomenu.add_command(label="Salir")

Editar = Menu(barramenu, tearoff=0)
Editar.add_cascade(label="copiar")
Editar.add_cascade(label="cortar")
Editar.add_cascade(label="pegar")
Editar.add_separator()
Editar.add_cascade(label="buscar")

barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Editar", menu=Editar)
raiz.mainloop()

Miconexion.commit()
Miconexion.close()