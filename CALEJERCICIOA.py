from tkinter import*

root = Tk()
root.geometry("330x300")
root.title("CALCULADORA")

framePrincipal = Frame(root, bg="#a0a0a0")
framePrincipal.pack(fill="both", expand=1)

valorA= IntVar()
valorB= IntVar()
suma=IntVar()
multiplicacion=IntVar()
resta=IntVar()
division=IntVar()

def sumando():
    r=valorA.get()+valorB.get()
    respuesta.config(text=r)

def multi():
    r=valorA.get()*valorB.get()
    respuesta.config(text=r)
    
def div():
    r=valorA.get()/valorB.get()
    respuesta.config(text=r)
    
def res():
    r=valorA.get()-valorB.get()
    respuesta.config(text=r)
  
def clc():
    valorA.set("0")
    valorB.set("0")


#salidas o mensajes
titulo = Label(framePrincipal, text="CALCULADORA", bg="#a0a0a0", font=("Roboto", 20, "bold")).pack()
numeroA = Label (framePrincipal, text="NÚMERO A", bg="#a0a0a0").place(x=50, y=60)
numeroB = Label (framePrincipal, text="NÚMERO B", bg="#a0a0a0").place(x=50, y=90)
resx = Label (framePrincipal,text="RESULTADO", bg="#a0a0a0").place(x=50, y=120)
respuesta = Label (framePrincipal,text="" )
respuesta.place(x=130, y=120)


#entradas
A = Entry(framePrincipal, textvariable=valorA)
A.place(x=130, y=60)
B = Entry(framePrincipal, textvariable=valorB)
B.place(x=130, y=90)

#Botones
botonsuma=Button(framePrincipal, text="SUMA", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=sumando).place(x=25, y=180)
botonmultiplicacion=Button(framePrincipal, text="MULT", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=multi).place(x=120, y=180)
botonresta=Button(framePrincipal, text="RESTA", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=res).place(x=215, y=180)
botondivision=Button(framePrincipal, text="DIVISIÓN", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=div).place(x=25, y=230)
botonc=Button(framePrincipal, text="C", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2, command=clc).place(x=120, y=230)

botonigual=Button(framePrincipal, text="=", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10, height=2).place(x=215, y=230)

root.mainloop()