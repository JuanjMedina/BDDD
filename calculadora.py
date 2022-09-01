from tkinter import  *


raiz = Tk()
raiz.title("Calculadora")

frame= Frame(raiz, width=500, height=500, bg="white")
frame.pack()

#linea de vista 
Pantalla = StringVar()
sumatoria = 0
operacion = ""
resultado=0
cambio_pantalla = False

vista1= Entry (frame,textvariable=Pantalla)
vista1.grid(row=1,column=1,pady=10,columnspan=4)
vista1.config(justify="right",bg="black",fg="green", font=("Arial",12))


def funcionalidad(num):
    global cambio_pantalla
    if cambio_pantalla != False:
        Pantalla.set(num)
        cambio_pantalla = False
    else:
        Pantalla.set(Pantalla.get()+num)


def sumas(num):
    global resultado
    global operacion 
    global cambio_pantalla
    resultado += int(num)
    operacion = "suma"
    Pantalla.set(resultado)

    cambio_pantalla= True

contador_resta=0
def restas(num):
    global sumatoria
    global resultado
    global cambio_pantalla
    global operacion
    global contador_resta
    if contador_division==0:
        sumatoria = int(num)
        resultado = sumatoria 

    else:
        if contador_division==1:
            resultado = int(resultado)-int(num)

        else:
            resultado= int (resultado)-int(num)
        Pantalla.set(resultado)
        resultado=Pantalla.get()

    contador_resta +=1
    operacion = "resta"
    cambio_pantalla= True
        


contador_multiplicacion=0
def multiplicacion(num):

    global operacion
    global cambio_pantalla
    global resultado
    global contador_multiplicacion
    global sumatoria

    if contador_multiplicacion == 0:
        sumatoria= int(num)
        resultado = sumatoria

    else:
        if contador_multiplicacion ==1:
            resultado = sumatoria*int(num)

        else:
            resultado = int(resultado)*int(num)

        Pantalla.set(resultado)
        resultado=Pantalla.get()

    contador_multiplicacion +=1
    operacion ="multiplicacion"
    cambio_pantalla= True




numerador = 0
contador_division=0
def divisiones(num):
    
    global operacion
    global contador_division
    global cambio_pantalla
    global resultado
    global numerador
    if contador_division ==0:
        numerador = float(num)   
        resultado = int(num)

    else:
        if contador_division==1:
            try:
                resultado = numerador/float(num)
            except ZeroDivisionError:
                print("division en cero no es posible")
        else: 
            try:
                resultado = resultado/float(num)
            except ZeroDivisionError:
                print("division en cero no es posible")
        Pantalla.set(resultado)
        resultado= float(Pantalla.get())


    contador_division +=1
    cambio_pantalla= True 
    operacion ="division"

contador_potencia=0


def raiz (num):
    pass
def potencia(num):
    global resultado
    global cambio_pantalla
    global sumatoria
    global operacion
    global contador_potencia
    if contador_potencia==0:
        sumatoria=int(num)
        resultado= sumatoria

    else:
        if contador_potencia==1:
            resultado = int(resultado)**int(num)

        else:
            resultado = int(resultado)**int(num)

        Pantalla.set(resultado)
        resultado=Pantalla.get()

    contador_potencia +=1
    cambio_pantalla= True
    operacion="potencia"


def resultadofinal():
    global operacion
    global resultado
    global sumatoria
    global contador_multiplicacion
    global contador_division
    global contador_resta
    global contador_potencia
    if operacion=="suma":
        Pantalla.set(int(resultado)+int(Pantalla.get()))
        resultado=0

    elif operacion=="resta":
        Pantalla.set(int(resultado)-int(Pantalla.get()))
        resultado=0
        contador_resta=0
    
    elif operacion =="division":
        try:
            Pantalla.set(resultado/float(Pantalla.get()))
        except ZeroDivisionError:
            Pantalla.set("Sintax Error")

        finally:
            resultado =0
            contador_division=0
            

    elif operacion=="multiplicacion":
        Pantalla.set(int(resultado)*int(Pantalla.get()))
        resultado= 0
        contador_multiplicacion=0

    elif operacion=="potencia":
        Pantalla.set(int(resultado)**int(Pantalla.get()))
        resultado=0
        contador_potencia=0




#linea 1 
boton1 = Button(frame, text="7", width=3,command=lambda:funcionalidad("7"))
boton1.grid(row=2,column=1)

boton1 = Button(frame, text="8", width=3, command=lambda:funcionalidad("8"))
boton1.grid(row=2,column=2)

boton1 = Button(frame, text="9",width=3,command=lambda:funcionalidad("9"))
boton1.grid(row=2,column=3)

boton1 = Button(frame, text="/", width=3,command=lambda:divisiones(Pantalla.get()))
boton1.grid(row=2,column=4)

#linea2 

boton2 = Button(frame, text="4", width=3,command=lambda:funcionalidad("4"))
boton2.grid(row=3,column=1)

boton2 = Button(frame, text="5", width=3,command=lambda:funcionalidad("5"))
boton2.grid(row=3,column=2)

boton2 = Button(frame, text="6", width=3,command=lambda:funcionalidad("6"))
boton2.grid(row=3,column=3)

boton2 = Button(frame, text="*", width=3,command=lambda:multiplicacion(Pantalla.get()))
boton2.grid(row=3,column=4)

#linea3

boton3= Button(frame, text="1", width=3, command=lambda:funcionalidad("1"))
boton3.grid(row=4,column=1)

boton3 = Button (frame,text="2", width=3, command=lambda:funcionalidad("2"))
boton3.grid(row=4,column=2)

boton3 = Button (frame,text="3", width=3,command=lambda:funcionalidad("3"))
boton3.grid(row=4,column=3)

boton3 = Button (frame,text="+", width=3, command=lambda:sumas(Pantalla.get()))
boton3.grid(row=4,column=4)

#linea4

boton4 = Button(frame, text="0", width=3, command=lambda:funcionalidad("0"))
boton4.grid(row=5,column=1)

boton4 = Button(frame, text=".", width=3, command=lambda:funcionalidad("."))
boton4.grid(row=5,column=2)

boton4 = Button(frame, text="=", width=3, command=lambda:resultadofinal())
boton4.grid(row=5,column=3)

boton4 = Button(frame, text="-", width=3, command=lambda:restas(Pantalla.get()))
boton4.grid(row=5,column=4)

botonEliminar = Button(frame, text="Del ", width=3, command=lambda:elimino())
botonEliminar.grid(row=6,column=3)

BotonClear = Button(frame,text="Clr",command=lambda:limpiar())
BotonClear.grid(row=6,column=4)

Botonpotencia= Button(frame,text="x^n", width=3, command=lambda:potencia(Pantalla.get()))
Botonpotencia.grid(row=6,column=2)

BotonRaiz= Button(frame,text="√", width=3, command=lambda:raiz(Pantalla.get()))
BotonRaiz.grid(row=6,column=1)


def elimino():
    vista1.delete(first=len(vista1.get())-1)

def limpiar():
    global resultado
    global cambio_pantalla
    resultado=0
    Pantalla.set(0)
    cambio_pantalla=True

def borrar():
    global resultado
    global cambio_pantalla
    resultado=0
    Pantalla.set(0)
    cambio_pantalla=True






raiz.mainloop()