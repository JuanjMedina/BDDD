from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class proyecto():
    raiz = Tk()

    raiz.title("Base de datos")
    barramenu=Menu(raiz)
    barramenu= Menu(raiz)
    raiz.config(height=250,width=250,menu=barramenu)
    Dibujo= Frame(raiz)
    Dibujo.config(bg="white")
    Dibujo.pack()


    minombre=Label(Dibujo,width=40,text="introduce tu nombre:",background="white",pady=9)
    minombre.config(justify="left")
    minombre.grid(row=1,column=1)

    mimateria = Label(Dibujo , width=40, text="Selecciona la materia a implementar la nota",padx=4,pady=9,bg="white")
    mimateria.config(justify="left")
    mimateria.grid(row=2,column=1)

    miNota=Label(Dibujo,width=40,text="Tipo de Nota:",background="white",justify="left",pady=9)
    miNota.grid(row=3,column=1)

    Observacion=Label(Dibujo,width=40,text="Observacion:",background="white",justify="left")
    Observacion.grid(row=4,column=1)

    Entrynombre= Entry(Dibujo,width=20)
    Entrynombre.grid(row=1,column=2)
    
    Miobservacion = Text(Dibujo,width=15,height=8,pady=15,padx=10)
    Miobservacion.grid(row=4,column=2)


    Materias = ttk.Combobox(Dibujo,state="readonly",values=["Calculo","Algebra","Mecanica","Programacion"])
    Materias.grid(row=2,column=2)

    Notas = ttk.Combobox(Dibujo,state="readonly",values=["Parciales","Talleres","Quices","Informes"])
    Notas.grid(row=3,column=2)


    Boton=Button(Dibujo,text="Agregar",padx=20)
    Boton.grid(row=6,column=2,pady=10)
    
    
    archivomenu= Menu(barramenu,tearoff=0)
    archivomenu.add_command(label="Nuevo")
    archivomenu.add_command(label="Guardar")
    archivomenu.add_separator()
    archivomenu.add_command(label="Salir")

    Editar= Menu(barramenu,tearoff=0)
    Editar.add_cascade(label="copiar")
    Editar.add_cascade(label="cortar")
    Editar.add_cascade(label="pegar")
    Editar.add_separator()
    Editar.add_cascade(label="buscar")

    barramenu.add_cascade(label="Archivo",menu=archivomenu)
    barramenu.add_cascade(label="Editar",menu=Editar)
    raiz.mainloop()