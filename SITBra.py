from guizero import App, Box, Text, TextBox, PushButton, Picture
from datetime import datetime
from playsound import playsound
import os

flag = 0
indice = 0
fila = 3
columna = 2
Letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', ' ', 'u', 'v', 'w', 'x', 'y', 'z', 'ñ', 'á', 'é', 'í', 'ó', 'ú', 'ü', '!', '?', ',', '.', ';', ':', 'Núm.', '(', ')', 'May.']
Codigos = [1, 12, 14, 145, 15, 124, 1245, 125, 24, 245, 13, 123, 134, 1345, 135, 1234, 12345, 1235, 234, 2345, 0, 136, 1236, 2456, 1346, 13456, 1356, 12456, 12356, 2346, 34, 346, 23456, 1256, 235, 26, 2, 3, 23, 25, 3456, 126, 453, 46]
matrix = [
    [' ', ' '],
    [' ', ' '],
    [' ', ' ']
]
#matrix
'''
1 4
2 5
3 6

0,0 0,1
1,0 1,1
2,0 2,1

'''
#--------------------------------------
def imprimir_archivo(texto, nombre):
    print(texto)
    os.startfile(nombre, "print")
    informacion = "Se ha enviado el archivo", nombre, " a imprimir."
    FrmInicio.info("Info", informacion)
    
#------------------------------
#Guardar
def guardar_archivo():
    fecha = datetime.now()
    d = fecha.strftime("%a")#Wed
    f = fecha.strftime("%d")#31
    m = fecha.strftime("%b")#Dec
    Y = fecha.strftime("%Y")#2023
    H = fecha.strftime("%H")#00-23
    M = fecha.strftime("%M")#00-59 minutos
    S = fecha.strftime("%S")#00-59 segundos
    ms = fecha.strftime("%f")#00-59 micro segundos
            #SITBra012311.txt
    #print(f"SITBra{ms}.txt")
    nombre_archivo = "SITBra" + f + m + ms +".txt"
    texto = str(TxtB_resultado.value)
    archivo = open(nombre_archivo, "w")#crea el archivo
    archivo.write(texto)#escribe en el archivo lo que trae como parámetro
    archivo.close()
    imprimir_archivo(texto, nombre_archivo)
#------------------------------------------------------------------------------

def on_key_press(event):
    #print(event.keycode)
    global flag
    if event.keycode == 13 :#presiono Enter
        if Txt_prefijo.value != "" and flag == 0:
            Txt_simbolo.focus()
            Braille_a_Texto()
            flag = 1

        if Txt_simbolo.value != "" and flag == 1:
            PB_mostrar.focus()
            Braille_a_Texto()
            flag = 2 
      
         
    if event.keycode == 110: #Borrar punto (.)
        limpiar()
        flag = 0
    
#------------------------------------------------------
   
def limpiar():
    limpiar_prefijo()
    limpiar_simbolo()
    Txt_simbolo.clear()
    Txt_prefijo.clear()
    Txt_prefijo.cursor_position = 0
    Txt_prefijo.focus()

#--------------------------
def  limpiar_prefijo():
    vacio1.image = "1.png"
    vacio2.image = "2.png"
    vacio3.image = "3.png"
    vacio4.image = "4.png"
    vacio5.image = "5.png"
    vacio6.image = "6.png"
#----------------------------------------
def limpiar_simbolo():
    v1.image = "vacio.png"
    v2.image = "vacio.png"
    v3.image = "vacio.png"
    v4.image = "vacio.png"
    v5.image = "vacio.png"
    v6.image = "vacio.png"
    
#-----------------------------------------
def Braille_a_Texto():
    global nombre_archivo
    global pref
    simbolo = ""
    prefijo = ""

    if Txt_prefijo.value != "" and flag == 0:
        prefijo = Txt_prefijo.value  #str
        prefijo = int(prefijo)
        if prefijo >= 0:
            for x in Codigos:
                if x == prefijo:
                    indice = Codigos.index(prefijo)
                    pref = Letras[indice]
                    traducir_prefijo(pref)
                    Txt_resultado.value = pref
            if prefijo == 9:
                playsound("9.mp3")
                guardar_archivo()
                FrmInicio.info("Info", "Se ha guardado el archivo.")
                limpiar()
                
    if Txt_simbolo.value != "" and flag == 1:
        simbolo = Txt_simbolo.value  #str
        simbolo = int(simbolo)
        if simbolo>= 0:
            for x in Codigos:
                if x == simbolo:
                    indice = Codigos.index(simbolo)
                    simb = Letras[indice]
                    traducir_simbolo(simb)
                    Txt_resultado.value = simb

    if Txt_simbolo.value != "" and Txt_prefijo.value != "":
        if pref == "Núm.":
            if simb == "a":
                Txt_resultado.value = "1"
                playsound("1.mp3")
            if simb == "b":
                Txt_resultado.value = "2"
                playsound("2.mp3")
            if simb == "c":
                Txt_resultado.value = "3"
                playsound("3.mp3")
            if simb == "d":
                Txt_resultado.value = "4"
                playsound("4.mp3")
            if simb == "e":
                Txt_resultado.value = "5"
                playsound("5.mp3")
            if simb == "f":
                Txt_resultado.value = "6"
                playsound("6.mp3")
            if simb == "g":
                Txt_resultado.value = "7"
                playsound("7.mp3")
            if simb == "h":
                Txt_resultado.value = "8"
                playsound("8.mp3")
            if simb == "i":
                Txt_resultado.value = "9"
                playsound("9.mp3")
            if simb == "j":
                Txt_resultado.value = "0"
                playsound("0.mp3")

        if pref == "May.":
            Txt_resultado.value = simb.upper()
    
    Txt_prefijo.clear
    Txt_simbolo.clear
    

#-----------------------------------    
def mostrar_texto():  
    global flag    
    TxtB_resultado.value += Txt_resultado.value
    limpiar()
    flag = 0
#------------------------------------
def traducir_prefijo(prefijo): #devuelve una matriz de la letra
    if prefijo in Letras:
        i = Letras.index(prefijo)
        codigo = str(Codigos[i])
        limpiar_prefijo()
        for j in codigo:
            if j == "1":
                vacio1.image = "lleno.png"
                playsound("1.mp3")

            if j == "4":
                vacio4.image = "lleno.png"
                playsound("4.mp3")

            if j == "2":
                vacio2.image = "lleno.png"
                playsound("2.mp3")

            if j == "5":
                vacio5.image = "lleno.png"
                playsound("5.mp3")
                
            if j == "3":
                vacio3.image = "lleno.png"
                playsound("3.mp3")

            if j == "6":
                vacio6.image = "lleno.png"
                playsound("6.mp3")
                
            if j == "0":
                playsound("0.mp3")
#-------------------------------
def traducir_simbolo(simbolo): #devuelve una matriz de la letra
    if simbolo in Letras:
        i = Letras.index(simbolo)
        codigo = str(Codigos[i])
        limpiar_simbolo()
        for j in codigo:
            if j == "1":
                v1.image = "lleno.png"
                playsound("1.mp3")

            if j == "4":
                v4.image = "lleno.png"
                playsound("4.mp3")

            if j == "2":
                v2.image = "lleno.png"
                playsound("2.mp3")

            if j == "5":
                v5.image = "lleno.png"
                playsound("5.mp3")

            if j == "3":
                v3.image = "lleno.png"
                playsound("3.mp3")

            if j == "6":
                v6.image = "lleno.png"
                playsound("6.mp3")
                   
#Guizero
#------------------------------------------------
FrmInicio = App(title="SIT Bra - Sistema Informático Traductor de Braille", layout="grid", width=570, bg="white")
   #[x,y]
titulos = Box(FrmInicio, align="top", width="fill",  border=True, grid=[0,0])
prefijo = Text(titulos, text="Prefijo", align="left", width=20)
simbolo = Text(titulos, text="Símbolo", align="left", width=20)
resultado = Text(titulos, text="Resultado", align="left", width=20)

#Contenedor de Prefijo, símbolo y resultado
contenedor = Box(FrmInicio, width="fill", layout="grid", grid=[0,1])
#Box0 ------------------                                      [x,y]
Box_prefijo = Box(contenedor, layout="grid", align="left", grid=[0,0])
vacio1 = Picture(Box_prefijo,  grid=[0,0], width=50, height=50)
vacio4 = Picture(Box_prefijo,  grid=[1,0], width=50, height=50)
vacio2 = Picture(Box_prefijo,  grid=[0,1], width=50, height=50)
vacio5 = Picture(Box_prefijo,  grid=[1,1], width=50, height=50)
vacio3 = Picture(Box_prefijo,  grid=[0,2], width=50, height=50)
vacio6 = Picture(Box_prefijo,  grid=[1,2], width=50, height=50)

espacio = Box(contenedor, width="fill",grid=[2,0])
txt_vacio = Text(espacio, width=5, height=10)

box_simbolo = Box(contenedor, layout="grid", grid=[4,0], align="left")
v1 = Picture(box_simbolo, image="vacio.png", width=50, height=50, grid=[0,0])
v4 = Picture(box_simbolo, image="vacio.png", width=50, height=50, grid=[1,0])
v2 = Picture(box_simbolo, image="vacio.png", width=50, height=50, grid=[0,1])
v5 = Picture(box_simbolo, image="vacio.png", width=50, height=50, grid=[1,1])
v3 = Picture(box_simbolo, image="vacio.png", width=50, height=50, grid=[0,2])
v6 = Picture(box_simbolo, image="vacio.png", width=50, height=50, grid=[1,2])

espacio2 = Box(contenedor, width="fill",grid=[6,0])
txt_vacio = Text(espacio2, width=10, height=10)

box2 = Box(contenedor, width="fill", grid=[8,0])
Txt_resultado = Text(box2, text="A", size=50, width="fill", height="fill")

#Fin Box0-------------

#Contenedor de TextBox Prefijo, Símbolo y TextoResultante
contenedor_pst = Box(FrmInicio,layout="grid", width="fill", grid=[0,2])
lbl_pref = Text(contenedor_pst, text="Prefijo", grid=[0,0], align="left")
Txt_prefijo = TextBox(contenedor_pst, grid=[1,0], width=40)

lbl_simb = Text(contenedor_pst, text="Símbolo", grid=[0,1], align="left")
Txt_simbolo = TextBox(contenedor_pst, grid=[1,1], width=40)

lbl_resul = Text(contenedor_pst, text="Resultado", grid=[0,2], align="left")
TxtB_resultado = Text(contenedor_pst, grid=[1,2], width=40, enabled=False)

#Botones
contenedor_botones = Box(FrmInicio, align="bottom", width="fill", grid=[0,8] )
PB_mostrar = PushButton(contenedor_botones, text="Mostrar", align="right", command=mostrar_texto)
PB_imprimir = PushButton(contenedor_botones, text="Imprimir", align="right", command=guardar_archivo)

texto_informativo= "ACLARACIÓN: Este sistema debe ser utilizado con ayuda de una persona vidente ya que no se controlaron todas las posibilidades para que una persona No vidente pueda hacerlo solo. Se debe utilizar solo el teclado numérico y puede utilizarse las siguientes teclas para las diferentes funciones: Enter: Cambia el foco de prefijo a símbolo y al botón Mostrar. Para guadar la letra generada se debe presionar la Barra espaciadora, lo cual también se mostrará por pantalla para verificar el texto traducido. El punto (.) del teclado numérico se utiliza para borrar el prefijo y el símbolo juntos haciendo foco nuevamente en el texto del prefijo. Presionando el 9 como prefijo, se guarda y manda a imprimir el texto generado."
aclaracion = TextBox(FrmInicio, text=texto_informativo, multiline=True, enabled = False, width=60, height=10,scrollbar=True, align="bottom", grid=[0,9])


FrmInicio.tk.bind("<KeyPress>", on_key_press)

Txt_prefijo.focus()

limpiar_prefijo()

FrmInicio.display()

