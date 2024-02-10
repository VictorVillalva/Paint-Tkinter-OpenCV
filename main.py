from tkinter import *
from tkinter import colorchooser

ventana = Tk()
ventana.title('Paint')
ventana.geometry('1100x600')

# Valor de color
strokeColor = StringVar()
strokeColor.set('black')

# Variables para el lapiz
initialPoint = [0,0]
finalPoint = [0,0]

#Valor grosor
strokeSize = IntVar()
strokeSize.set(1)
options = [1,5,10,15,20]



def pencil():
    strokeColor.set('black')
def eraser():
    strokeColor.set('white')
    canvas["cursor"] = DOTBOX

def selectColor():
    selectedColor =  colorchooser.askcolor('red', title='Seleccionar Color')

    if selectedColor[1] == None:
        strokeColor.set('black')
    else:
        strokeColor.set(selectedColor[1])


def paint(e):
    global initialPoint,finalPoint
    x = e.x
    y = e.y
    finalPoint = [x,y]


    if initialPoint != [0,0] :
        canvas.create_line(initialPoint[0], initialPoint[1], finalPoint[0], finalPoint[1], fill=strokeColor.get(), width=strokeSize.get())

    initialPoint = finalPoint

    if e.type == '5':
        initialPoint = [0,0]



# Section 1 - Tools
section1 = Frame(ventana, height=100, width=1100)
section1.grid(row=0,column=0,sticky=NW)

# Frame - Herramientas
toolsFrame = Frame(section1, height=100, width=100,relief=SUNKEN, borderwidth=3)
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
'''