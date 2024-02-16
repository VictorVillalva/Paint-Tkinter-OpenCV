from tkinter import colorchooser
from PIL import Image

import customtkinter
app = customtkinter.CTk()
app.title('Paint')
app.geometry('1100x600')

# ---------------- Variables --------------------
#Eleccion de acciones
selectActions = ''

# Valor de color
strokeColor = customtkinter.StringVar()
strokeColor.set('black')

# Variables para el lapiz
initialPoint = [0,0]
finalPoint = [0,0]

#Valor grosor
strokeSize = customtkinter.IntVar()
strokeSize.set(1)
options = [1,2,3,5,10]
def stroke(choice):
    if choice == "1":
        strokeSize.set(1)
    elif choice == "2":
        strokeSize.set(2)
    elif choice == "3":
        strokeSize.set(3)
    elif choice == "5":
        strokeSize.set(5)
    elif choice == "10":
        strokeSize.set(10)

# ---------------- Funciones --------------------
def pencil():
    global selectActions
    strokeColor.set('black')
    selectActions = 'lapiz'
    canvas['cursor'] = 'CROSS'
def eraser():
    global selectActions
    strokeColor.set('white')
    canvas['cursor'] = 'DOTBOX'
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
    canvas['cursor'] = 'CROSS'
    strokeColor.set( 'black' )
def circle():
    global selectActions
    selectActions = "circulo"
    canvas['cursor'] = 'CROSS'
    strokeColor.set( 'black' )
def rectangle():
    global selectActions
    selectActions = "rectangulo"
    canvas['cursor'] = 'CROSS'
    strokeColor.set( 'black' )
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


#-----------------------Interfas-----------------------
# Section 1 - Funcionalidades
section1 = customtkinter.CTkFrame(master=app, width=100, height=1100)
section1.grid(row=0,column=0,sticky='nw')

# Frame - Herramientas
toolsFrame = customtkinter.CTkFrame( master=section1, height=100, width=150, border_width=3 )
toolsFrame.grid(row=0, column=0)

lapiz = customtkinter.CTkImage( light_image=Image.open( "images/lapiz.png" ) , dark_image=Image.open(
    "images/lapiz.png" ) , size=(10, 10) )
pencilButton = customtkinter.CTkButton(master=toolsFrame, text='Lapiz', width=120, height=42, anchor='center', corner_radius=0, command=pencil,fg_color="#272727" ,
                                   hover_color=("#1E1E1E","#222D65"),font=("JetBrains Mono",12), image=lapiz)
pencilButton.grid(row=0, column=0)

borrador = customtkinter.CTkImage( light_image=Image.open( "images/borrador.png" ) , dark_image=Image.open(
    "images/borrador.png" ) , size=(10, 10) )
eraserButton = customtkinter.CTkButton(master=toolsFrame, text='Borrador', width=120, height=42, anchor='center', corner_radius=0, command=eraser, fg_color="#272727" ,
                                   hover_color=("#1E1E1E","#222D65"),font=("JetBrains Mono",12), image=borrador)
eraserButton.grid(row=1, column=0)

# Frame - Tamaños
sizeFrame = customtkinter.CTkFrame( master=section1, height=100, width=150, border_width=3 )
sizeFrame.grid(row=0,column=1)

defaultButton = customtkinter.CTkButton(master=sizeFrame, text='Default', width=120, height=42, anchor='center', corner_radius=0, command=pencil, fg_color="#272727" ,
                                   hover_color=("#1E1E1E","#222D65"),font=("JetBrains Mono",12))
defaultButton.grid(row=0,column=0)

sizeList = customtkinter.CTkOptionMenu(master=sizeFrame,values=["1","2","3","5","10"],command=stroke, corner_radius=0, width=120,  height=42)
sizeList.grid(row=1, column=0)


# Frame - Colores
colorFrame = customtkinter.CTkFrame( master=section1, height=100, width=150, border_width=3)
colorFrame.grid(row=0,column=2)

colorBoxButton =customtkinter.CTkButton( master=colorFrame, text='Color', width=120, height=85, corner_radius=0,  command=selectColor, fg_color="#272727" ,
                                   hover_color=("#1E1E1E","#222D65"),font=("JetBrains Mono",12))
colorBoxButton.grid(row=0,column=0)

# Frame - Figuras
shapeFrame = customtkinter.CTkFrame( master=section1, height=100, width=100, border_width=3)
shapeFrame.grid(row=0,column=3)

lineaimg = customtkinter.CTkImage( light_image=Image.open( "images/linea.png" ) , dark_image=Image.open(
    "images/linea.png" ) , size=(10, 10) )
lineButton = customtkinter.CTkButton(master=shapeFrame, text='Linea', width=120, corner_radius=0, command=line, fg_color="#272727" ,
                                   hover_color=("#1E1E1E","#222D65"),font=("JetBrains Mono",12), image=lineaimg)
lineButton.grid(row=0,column=0)

circuloimg = customtkinter.CTkImage( light_image=Image.open( "images/circulo.png" ) , dark_image=Image.open("images/circulo.png" ) , size=(10, 10) )
circleButton = customtkinter.CTkButton(master=shapeFrame, text='Circulo', width=120, corner_radius=0, command=circle, fg_color="#272727" ,
                                   hover_color=("#1E1E1E","#222D65"),font=("JetBrains Mono",12), image=circuloimg)
circleButton.grid(row=1,column=0)

rectanguloimg = customtkinter.CTkImage( light_image=Image.open( "images/rectangulo.png" ) , dark_image=Image.open(
    "images/rectangulo.png" ) , size=(10, 10) )
rectangleButton = customtkinter.CTkButton(master=shapeFrame, text='Rectangulo', width=120, corner_radius=0, command=rectangle, fg_color="#272727" ,
                                   hover_color=("#1E1E1E","#222D65"),font=("JetBrains Mono",12), image=rectanguloimg)
rectangleButton.grid(row=2,column=0)


# Section 2 - Canvas
section2 = customtkinter.CTkFrame(master=app,height=500,width=1100)
section2.grid(row=1,column=0)

canvas = customtkinter.CTkCanvas(master=section2, height=500,width=1100, bg="white")
canvas.grid(row=0,column=0)



canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
app.resizable(False,False)
app.mainloop()
