from tkinter import *
import os

#FUENTES 
let1=("Arial", 20)
let2=("Arial", 13)
let3=("Times New Roman", 18)
let4=("Times New Roman", 12)
let5=("Helvetica", 7)


#COLORES
rojo="#FF0400"
magentaOscuro="#610039"
magentaMedio="#CF007A"
magentaClaro="#E48CC0"
hadeOscuro="#0B7456"
hadeMedio="#00A979"
hadeClaro="#40FFC8"
GrisOscuro="#3F4C48"
GrisClaro="#A3A6A5"
AmarilloClaro="#FAFFA8"
AmarilloMedio="#E7E71D"
AmarilloOscuro="#D7C400"
AzulClaro="#679FFF"
AzulMedio="#144FE0"
AzulOscuro="#0D3889"


#--------RAIZ DE LA VENTANA-------------
root=Tk()
root.config(bg="White")
root.title("Registro de Gastos")

ruta = r"D:\\NUEVO PORTATAIL\\PROGRAMACIÓN\\PYTHON\\EJERCICIO 17 Interface gráficas"
name = "billete.ico"
ruta_completa = os.path.join(ruta,name)
root.iconbitmap(ruta_completa)



#-------------------------FRAME PRINCIPALES-----------------------------
frameIzq=Frame(root, bg="White")
frameIzq.pack(fill="both", expand="True", side="left", padx=15, pady=15)

frameDer=Frame(root, bg="White")
frameDer.pack(fill="both", expand="True", side="right", padx=15, pady=15)

#frameDer1=Frame(frameDer, bg="White")
#frameDer1.pack(fill="both", expand="True", side="top", anchor="n", padx=15, pady=15)

#frameDer2=Frame(frameDer, bg="White")
#frameDer2.pack(fill="both", expand="True", side="bottom", padx=15, pady=15)



#--------------------------Frame Izquierda------------------------------
labelIngresar=Label(frameIzq,text="Ingresar registro", font=let1, bg="White", fg=hadeOscuro)
labelIngresar.grid(row=0, columnspan=2)

labelDescripcion=Label(frameIzq,text="DESCRIPCIÓN: ", font=let2, bg="White", fg=hadeOscuro)
labelDescripcion.grid(row=1, column=0, sticky="w", pady=5)

labelMonto=Label(frameIzq,text="MONTO: ", font=let2, bg="White", fg=hadeOscuro)
labelMonto.grid(row=2, column=0, sticky="w", pady=5)

labelCategoria=Label(frameIzq,text="CATEGORÍA: ", font=let2, bg="White", fg=hadeOscuro)
labelCategoria.grid(row=3, column=0, sticky="w", pady=5)

labelFecha=Label(frameIzq,text="FECHA: ", font=let2, bg="White", fg=hadeOscuro)
labelFecha.grid(row=4, column=0, sticky="w", pady=5)


textDesc=StringVar()
textMonto=IntVar()
textCateg=StringVar()
textFecha=StringVar()

entryDescripcion=Entry(frameIzq, width=30, bg=AmarilloClaro, fg=magentaMedio, textvariable=textDesc)
entryDescripcion.grid(row=1, column=1)

entryMonto=Entry(frameIzq, width=30, bg=AmarilloClaro, fg=magentaMedio, textvariable=textMonto)
entryMonto.grid(row=2, column=1)

entryCategoria=Entry(frameIzq, width=30, bg=AmarilloClaro, fg=magentaMedio, textvariable=textCateg)
entryCategoria.grid(row=3, column=1)

entryFecha=Entry(frameIzq, width=30, bg=AmarilloClaro, fg=magentaMedio, textvariable=textFecha)
entryFecha.grid(row=4, column=1)



#------------------CONSTRUCCIÓN DE TABLA DE REGISTROS---------------------------------------
global d1, d2, d3, d4, filas, datos, iden
datos={}
iden=0
def recogeDatos():
    global d1, d2, d3, d4, datos, iden
    iden+=1
    d1=entryDescripcion.get()
    d2=entryMonto.get()
    d3=entryCategoria.get()
    d4=entryFecha.get()
    datos[iden]=(d1,d2,d3,d4)

    print(datos)


#def leeFila(fila):
#    lectura=datos[fila]
#    return lectura

#def borrar(fila):
#    del datos[fila]

filas=1
def construyeFilas():

    global d1, d2, d3, d4, filas
    filas+=1
    
    columna1=Label(frameDer,text=d1, highlightthickness=1, font=let4, bg="White", width=30, anchor="w", fg=GrisOscuro)
    columna1.grid(row=filas, column=0)

    columna2=Label(frameDer,text=d2, highlightthickness=1, font=let4, bg="White", width=15, anchor="w", fg=GrisOscuro)
    columna2.grid(row=filas, column=1)

    columna3=Label(frameDer,text=d3, highlightthickness=1, font=let4, bg="White", width=20, anchor="w", fg=GrisOscuro)
    columna3.grid(row=filas, column=2)

    columna4=Label(frameDer,text=d4, highlightthickness=1, font=let4, bg="White", width=10, anchor="w", fg=GrisOscuro)
    columna4.grid(row=filas, column=3)

#    botonBorrar=Button(frameDer2,text="Borrar", font=let5, fg="white", bg=rojo, width=5, command=lambda: borrar(filas))
#    botonBorrar.grid(row=filas, column=4)

#    botonCambiar=Button(frameDer2,text="Cambiar", font=let5, fg="white", bg=AzulMedio, width=5)
#    botonCambiar.grid(row=filas, column=5)
#    print(filas)


def limpiaCampos():
    entryDescripcion.delete(0, END)
    entryMonto.delete(0, END)
    entryCategoria.delete(0, END)
    entryFecha.delete(0, END)

def pulsaAgregar():
    recogeDatos()
    construyeFilas()
    limpiaCampos()


botonAgregar=Button(frameIzq,text="Agregar", font=let2, bg=AzulClaro, command=pulsaAgregar)
botonAgregar.grid(row=5, columnspan=2)



#----------------------Frame Derecha------------------------------------
labelNuevoRegistro=Label(frameDer, text="Nuevo registro", font=let3, bg="White", fg=magentaMedio)
labelNuevoRegistro.grid(row=0, column=0, sticky="w", pady=5)



def creaTabla():
    codigo=1

    try:
        with open("consecutivo.txt", "r") as serial:
            codigo=int(serial.read())
    except:
        codigo=1


    ruta = r"D:\\NUEVO PORTATAIL\\PROGRAMACIÓN\\PYTHON\\EJERCICIO 17 Interface gráficas"
    nombre = "Registro No." + str(codigo)+".txt"
    ruta_completa = os.path.join(ruta,nombre)
    archivo = open(ruta_completa, "w")


    archivo.write("{:<15} {:<30} {:<15} {:<15} {:<15}".format("ID", "DESCRIPCIÓN", "MONTO", "CATEGORÍA","FECHA"))
    archivo.write("\n")
    for identificador, registro in datos.items():
        desc, monto, cat, fecha = registro
        archivo.write("{:<15} {:<30} {:<15} {:<15} {:15}".format(identificador, desc, monto, cat, fecha))
        archivo.write("\n")
    archivo.close()
    codigo+=1

    with open("consecutivo.txt", "w") as serial:
        serial.write(str(codigo))   
    serial.close()




botonGuardar=Button(frameDer,text="Guardar", bg=AzulClaro, font=let4, width=15, anchor="center", command=creaTabla)
botonGuardar.grid(row=0, column=1, sticky="w")

tituloDescripcion=Label(frameDer,text="DESCRIPCIÓN", highlightthickness=1, font=let4, bg="White", width=30, anchor="w", fg=magentaMedio)
tituloDescripcion.grid(row=1, column=0)

tituloMonto=Label(frameDer,text="MONTO", highlightthickness=1, font=let4, bg="White", width=15, anchor="w", fg=magentaMedio)
tituloMonto.grid(row=1, column=1)

tituloCategoria=Label(frameDer,text="CATEGORÍA", highlightthickness=1, font=let4, bg="White", width=20, anchor="w", fg=magentaMedio)
tituloCategoria.grid(row=1, column=2)

tituloFecha=Label(frameDer,text="FECHA", highlightthickness=1, font=let4, bg="White", width=10, anchor="w", fg=magentaMedio)
tituloFecha.grid(row=1, column=3)





root.mainloop()