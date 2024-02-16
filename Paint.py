from tkinter import *
from tkinter import colorchooser

import cv2
import numpy as np
from PIL import ImageTk

ventana = Tk()
ventana.title('Paint')
ventana.geometry('1100x600')

# ---------------- Variables --------------------
#Eleccion de acciones
selectActions = ''

# Valor de color
strokeColor = StringVar()
strokeColor.set('black')

# Variables para el lapiz
initialPoint = [0,0]
finalPoint = [0,0]

#Valor grosor
strokeSize = IntVar()
strokeSize.set(1)
options = [1,2,3,5,10]

# ---------------- Funciones --------------------
def pencil():
    global selectActions
    strokeColor.set('black')
    selectActions = 'lapiz'
def eraser():
    global selectActions
    strokeColor.set('white')
    canvas["cursor"] = DOTBOX
    selectActions = 'borrador'
def selectColor():
    selectedColor =  colorchooser.askcolor('red', title='Seleccionar Color')

    if selectedColor[1] == None:
        strokeColor.set('black')
    else:
        strokeColor.set(selectedColor[1])
def line():
    global selectActions
    selectActions = "trazo"


def circle():
    global selectActions
    selectActions = "circulo"
def rectangle():
    global selectActions
    selectActions = "rectangulo"
def paint(e):
    global initialPoint,finalPoint,selectActions
    if selectActions == 'lapiz' or selectActions == 'borrador':
        x = e.x
        y = e.y
        finalPoint = [x,y]

        if initialPoint != [0 , 0] :
            canvas.create_line( initialPoint[0] , initialPoint[1] , finalPoint[0] , finalPoint[1] ,
                                fill=strokeColor.get() , width=strokeSize.get() )
            print( 'Dibujando' )
        initialPoint = finalPoint

        if e.type == '5' :
            initialPoint = [0 , 0]

    elif selectActions == 'trazo':
        finalPoint.append([e.x,e.y])
        initialPoint = finalPoint[2]
        if e.type == '5':
            finalPoint = finalPoint[-1]
            canvas.create_line(initialPoint[0], initialPoint[1], finalPoint[0], finalPoint[1], width=strokeSize.get(), tags="final_line", fill=strokeColor.get())
            print( 'Dibujando linea' )
            initialPoint = [0, 0]
            finalPoint = [0, 0]
        canvas.delete( "temp_line" )
        canvas.create_line( initialPoint[0] , initialPoint[1] , finalPoint[-1][0] , finalPoint[-1][1] ,
                            width=strokeSize.get() , tags="temp_line", fill=strokeColor.get() )

    elif selectActions == 'circulo':
        finalPoint.append( [e.x , e.y] )
        initialPoint = finalPoint[2]
        if e.type == '5':
            finalPoint = finalPoint[-1]
            canvas.create_oval(initialPoint[0], initialPoint[1], finalPoint[0], finalPoint[1],
                               width=strokeSize.get(), outline=strokeColor.get(), tags="final_circle")
            print( 'Dibujando circulo' )
            initialPoint = [0,0]
            finalPoint = [0,0]
        canvas.delete( "temp_circle" )
        canvas.create_oval( initialPoint[0] , initialPoint[1] , finalPoint[-1][0] , finalPoint[-1][1] ,
                            width=strokeSize.get() , outline=strokeColor.get() , tags="temp_circle" )

    elif selectActions== "rectangulo":
        finalPoint.append([e.x, e.y])
        initialPoint = finalPoint[2]
        if e.type == "5":
            # initialPoint = finalPoint[2]
            finalPoint = finalPoint[-1]
            canvas.create_rectangle(initialPoint[0], initialPoint[1], finalPoint[0], finalPoint[1],
                               width=strokeSize.get(), outline=strokeColor.get(), tags="final_rect")
            print( 'Dibujando rectangulo' )
            initialPoint = [0, 0]
            finalPoint = [0, 0]
        canvas.delete("temp_rect")
        canvas.create_rectangle(initialPoint[0], initialPoint[1], finalPoint[-1][0], finalPoint[-1][1],
                           width=strokeSize.get(), outline=strokeColor.get(), tags="temp_rect")

    elif selectActions == "rectangulo":
        finalPoint.append([e.x, e.y])
        initialPoint = finalPoint[2]
        if e.type == "5":
            # initialPoint = finalPoint[2]
            finalPoint = finalPoint[-1]
            canvas.create_rectangle(initialPoint[0], initialPoint[1], finalPoint[0], finalPoint[1],
                                    width=strokeSize.get(), outline=strokeColor.get(), tags="final_rect")
            print( 'Dibujando rectangulo' )
            initialPoint = [0, 0]
            finalPoint = [0, 0]

        canvas.delete("temp_rect")
        canvas.create_rectangle(initialPoint[0], initialPoint[1], finalPoint[-1][0], finalPoint[-1][1],
                                width=strokeSize.get(), outline=strokeColor.get(), tags="temp_rect")

# ---------------- Interfas --------------------
# Section 1 - Tools
section1 = Frame(ventana, height=100, width=1100)
section1.grid(row=0,column=0,sticky=NW)

# Frame - Herramientas
toolsFrame = Frame(section1, height=100, width=100, relief=SUNKEN, borderwidth=3)
toolsFrame.grid(row=0,column=0)

pencilButton = Button(toolsFrame, text="Lapiz", width=10, command=pencil)
pencilButton.grid(row=0,column=0)

eraserButton = Button(toolsFrame, text="Borrador", width=10,  command=eraser)
eraserButton.grid(row=1,column=0)

toolsLabel = Label(toolsFrame, text="Herramientas", width=10)
toolsLabel.grid(row=3,column=0)

# Frame - Tamaños
sizeFrame = Frame(section1, height=100, width=100, relief=SUNKEN, borderwidth=3)
sizeFrame.grid(row=0,column=1)

defaultButton = Button(sizeFrame, text='Default', width=10, command=pencil)
defaultButton.grid(row=0,column=0)

sizeList = OptionMenu(sizeFrame, strokeSize, *options)
sizeList.grid(row=1, column=0)

sizeLabel = Label(sizeFrame, text="Tamaño", width=10)
sizeLabel.grid(row=2,column=0)

# Frame - Colores
colorFrame = Frame(section1, height=100, width=100, relief=SUNKEN, borderwidth=3)
colorFrame.grid(row=0, column=2)

colorBoxButton = Button(colorFrame, text='Seleccionar Color', width=15, command=selectColor)
colorBoxButton.grid(row=0, column=0)

# Frame - Colores Destacados
colorsFrame = Frame(section1, height=100, width=100, relief=SUNKEN, borderwidth=3)
colorsFrame.grid(row=0, column=3)

redButton = Button(colorsFrame, text='Rojo', bg='red', fg='white', command=lambda: strokeColor.set('red'), width=10)
redButton.grid(row=0, column=0)
blueButton = Button(colorsFrame, text='Azul', bg='blue', fg='white', command=lambda: strokeColor.set('blue'), width=10)
blueButton.grid(row=1, column=0)
greenButton = Button(colorsFrame, text='Verde', bg='green', fg='white', command=lambda: strokeColor.set('green'), width=10)
greenButton.grid(row=2, column=0)

#Frame - Figuras
shapeFrame = Frame(section1, height=100,width=100, relief=SUNKEN, borderwidth=3)
shapeFrame.grid(row=0, column=4)

lineButton = Button(shapeFrame, text='Linea', width=15, command=line)
lineButton.grid(row=0, column=0)
circleButton = Button(shapeFrame, text='Circulo', width=15, command=circle)
circleButton.grid(row=1, column=0)
rectangleButton = Button(shapeFrame, text='Rectangulo', width=15, command=rectangle)
rectangleButton.grid(row=2, column=0)

# Section 2 - Canvas
section2 = Frame(ventana,height=500,width=1100,bg="yellow")
section2.grid(row=1,column=0)

canvas = Canvas(section2, height=500,width=1100, bg="white")
canvas.grid(row=0,column=0)



canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
ventana.resizable(False,False)
ventana.mainloop()

'''
    canvas.create_oval(100,100,120,120,fill='black') //Crear el circulo relleno
    canvas.create_line(100,100,120,120,fill='black') //Crear una linea rellena 
    canvas.create_oval( x , y , x+5 , y+5 , fill="black" )
    canvas.create_rectangle(100,100,120,120,fill='black') //Crea un rectangulo relleno
'''