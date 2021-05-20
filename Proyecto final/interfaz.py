from grabar_audio import grabar
from tkinter import *
from tkinter import messagebox
import numpy as np
from numpy.core.defchararray import title
from operaciones import *
import tkinter.messagebox
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from pydub.playback import play

#cosas comunes de secuencias
def mostrar_resultado(r):
    v1 = tkinter.Tk()
    v1.title('Resultado')
    v1.configure(background='black')
    res = Label(v1, text='El resultado de la operación es: '+' '.join(map(str, r)) )
    res.grid(row=0)
    res.configure(fg="white",background='black',font=("Verdana",11))
    plt.plot(r)
    plt.title('Resultado')
    plt.show()

def mostrar_2(r1,r2):
    v1 = tkinter.Tk()
    v1.title('Resultado')
    v1.configure(background='black')
    res = Label(v1, text='El resultado de la operación es: '+' '.join(map(str, r2)) )
    res.grid(row=0)
    res.configure(fg="white",background='black',font=("Verdana",11))
    fig, axs = plt.subplots(2)
    axs[0].plot(r1)
    axs[1].plot(r2)
    plt.show()

def mostrar_3(r1,r2,r3):
    v1 = tkinter.Tk()
    v1.title('Resultado')
    v1.configure(background='black')
    res = Label(v1, text='El resultado de la operación es: '+' '.join(map(str, r3)) )
    res.grid(row=0)
    res.configure(fg="white",background='black',font=("Verdana",11))
    fig, axs = plt.subplots(2,2)
    axs[0,0].plot(r1)
    axs[0,1].plot(r2)
    axs[1,0].plot(r3)
    plt.show()

def aceptar_x_h(e1,e2,aux):
    x = list(map(int, e1.get().split(' '))) 
    h = list(map(int, e2.get().split(' ')))
    if(len(aux)==0):
        aux.append(x)
        aux.append(h)
    else:
        aux[0] = x
        aux[1] = h

def aceptar_x(e1,aux):
    x = list(map(int, e1.get().split(' '))) 
    if(len(aux)==0):
        aux.append(x)
    else:
        aux[0] = x

#cosas comunes de audio
def mostrar():
    archivo = 'audio.wav'
    muestreo, audio = waves.read(archivo)
    archivo = 'nuevo.wav'
    muestreo, nuevo = waves.read(archivo)
    fig, axs = plt.subplots(2)
    axs[0].plot(audio)
    axs[1].plot(nuevo)
    plt.show()


def reproducir(nombre_archivo):
    song = AudioSegment.from_wav(nombre_archivo)
    play(song)

def obtener_audio(nombre):
    archivo = 'audio.wav'
    muestreo, audio = waves.read(archivo)
    return audio

#botones de 
def boton_sumar_secuencias():
    v1 = tkinter.Tk()
    v1.geometry('500x200')
    v1.title('Suma de secuencias')
    v1.configure(background='black')
    #tit = Label(v1, text="\nSumar secuencias\n")
    #tit.pack(anchor=CENTER) 
    #tit.configure(fg="white",background='black',font=("Verdana",16))
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    #instruccion = Label(v1, text="\nOprima el boton para grabar audio\n")
    #instruccion.configure(fg="white",background='black',font=("Verdana",11))
    inst = Label(v1, text='Escriba las secuencias separadas por espacios')
    inst.grid(row=0) 
    x = Label(v1, text='x(n)')
    x.grid(row=1) 
    h = Label(v1, text='h(n)')
    h.grid(row=2)
    espacio1.grid(row=3) 
    e1 = Entry(v1) 
    e2 = Entry(v1) 
    e1.grid(row=1, column=1) 
    e2.grid(row=2, column=1)
    aux = []
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x_h(e1,e2,aux),
        mostrar_3(aux[0],aux[1],sumar(aux[0],aux[1]))
    ) )
    acep.grid()
    inst.configure(fg="white",background='black',font=("Verdana",11))
    x.configure(fg="white",background='black',font=("Verdana",11))
    h.configure(fg="white",background='black',font=("Verdana",11))
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

def boton_restar_secuencias():
    v1 = tkinter.Tk()
    v1.geometry('500x200')
    v1.title('Resta de secuencias')
    v1.configure(background='black')
    inst = Label(v1, text='Escriba las secuencias separadas por espacios')
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    inst.grid(row=0) 
    x = Label(v1, text='x(n)')
    x.grid(row=1) 
    h = Label(v1, text='h(n)')
    h.grid(row=2)
    espacio1.grid(row=3) 
    e1 = Entry(v1) 
    e2 = Entry(v1) 
    e1.grid(row=1, column=1) 
    e2.grid(row=2, column=1)
    aux = []
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x_h(e1,e2,aux),
        mostrar_3(aux[0],aux[1],restar(aux[0],aux[1]))
    ) )
    acep.grid()
    inst.configure(fg="white",background='black',font=("Verdana",11))
    x.configure(fg="white",background='black',font=("Verdana",11))
    h.configure(fg="white",background='black',font=("Verdana",11))
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

def subir_bajar_volumen():
    v2 = tkinter.Tk()
    v2.geometry('600x200')
    v2.title('Suma/Resta de audio')
    v2.configure(background='black')
    inst = Label(v2, text='Ingrese cuanto desea subir o bajar el volumen del audio') 
    inst.grid(row=0)
    espacio1 = Label(v2, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    e1 = Entry(v2) 
    e1.grid(row=0, column=1) 
    acep = Button(v2, text='Aceptar', width=25, command=lambda:(
        sumar_audio(int(e1.get())),
        reproducir('nuevo.wav'),
        mostrar(),
        v2.destroy()
    ) )
    espacio1.grid(row=1) 
    acep.grid(row=2)
    inst.configure(fg="white",background='black',font=("Verdana",11))
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

def boton_amp_frecuencias():
    v1 = tkinter.Tk()
    v1.geometry('500x200')
    v1.title('Amplificar/Atenuar')
    v1.configure(background='black')
    inst = Label(v1, text='Escriba la secuencia separadas por espacios')
    inst.grid(row=0) 
    x = Label(v1, text='x(n)')
    x.grid(row=1) 
    const = Label(v1, text='Constante')
    const.grid(row=3) 
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=4)
    e1 = Entry(v1) 
    e3 = Entry(v1) 
    e1.grid(row=1, column=1) 
    e3.grid(row=3, column=1)
    aux = []
    aux1 = [1]
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        aux1.insert(0,float(e3.get())),
        mostrar_resultado(amplificar(aux[0],aux1[0]))
    ) )
    acep.grid()
    inst.configure(fg="white",background='black',font=("Verdana",11))
    x.configure(fg="white",background='black',font=("Verdana",11))
    const.configure(fg="white",background='black',font=("Verdana",11))
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

def audio_amplificar():
    v2 = tkinter.Tk()
    v2.geometry('550x200')
    v2.title('Amplificar/Atenuar audio de audio')
    v2.configure(background='black')
    inst = Label(v2, text='Ingrese cuanto desea amplificar o atenuar el audio') 
    inst.grid(row=0) 
    e1 = Entry(v2) 
    e1.grid(row=1, column=0)
    espacio1 = Label(v2, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=2) 
    inst2 = Label(v2, text='Presione para grabar audio') 
    inst2.grid(row=3)

    acep = Button(v2, text='Aceptar', width=25, command=lambda:(
        grabar(),
        reproducir('audio.wav'),
        amplificar_audio(float(e1.get())),
        reproducir('nuevo.wav'),
        mostrar(),
        v2.destroy()
    ) )
    acep.grid(row=4)
    inst.configure(fg="white",background='black',font=("Verdana",11))
    inst2.configure(fg="white",background='black',font=("Verdana",11))   
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold")) 

def reflejar_sequencias():
    v1 = tkinter.Tk()
    v1.geometry('500x200')
    v1.title('Amplificar/Atenuar')
    v1.configure(background='black')
    inst = Label(v1, text='Escriba la secuencia separadas por espacios')
    inst.grid(row=0) 
    x = Label(v1, text='x(n)')
    x.grid(row=1) 
    e1 = Entry(v1) 
    e1.grid(row=1, column=1)
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=2)  
    aux = []
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        mostrar_2(aux[0],reflejo(aux[0]))
    ) )
    acep.grid()
    inst.configure(fg="white",background='black',font=("Verdana",11))
    x.configure(fg="white",background='black',font=("Verdana",11))
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold")) 

def audio_reflejo():
    grabar()
    reproducir('audio.wav')
    archivo = 'audio.wav'
    muestreo, audio = waves.read(archivo)
    nuevo = reflejo_audio(audio)
    reproducir('nuevo.wav')
    mostrar_2(audio,nuevo)

def desplazar_sequencias():
    v1 = tkinter.Tk()
    v1.geometry('700x400')
    v1.configure(background='black')
    l1 = Label(v1, text='Los valores deben estar separados por espacios EJEMPLO: 1 2 -4 ...')
    l2 = Label(v1, text='x(n)')
    l3 = Label(v1, text='Constante')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=1)
    l2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2 = Label(v1, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.grid(row=3)
    l3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3 = Label(v1, text="")
    espacio3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3.grid(row=5)
    l1.grid(row=0) 
    l2.grid(row=2)
    l3.grid(row=4) 
    e1 = Entry(v1) 
    e3 = Entry(v1) 
    e1.grid(row=2, column=1) 
    e3.grid(row=4, column=1)
    aux = []
    aux1 = [1]
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        aux1.insert(0,int(e3.get())),
        mostrar_2(aux[0],desplazamiento_secuencias(aux[0],aux1[0]))
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.grid()

def audio_desplazar():
    v2 = tkinter.Tk()
    v2.geometry('700x400')
    v2.title('Desplazar audio')
    v2.configure(background='black')
    l1 = Label(v2, text='Ingrese número positivo o negativo\n(se grabara después de aceptar)')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.pack()
    espacio1 = Label(v2, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.pack()
    e1 = Entry(v2) 
    e1.pack()
    espacio2 = Label(v2, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.pack()
    acep = Button(v2, text='Aceptar', width=25, command=lambda:(
        grabar(),
        reproducir('audio.wav'),
        desplazamiento_audio(int(e1.get())),
        reproducir('nuevo.wav'),
        mostrar(),
        v2.destroy()
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.pack()

def boton_diezmar_secuencia():
    v1 = tkinter.Tk()
    v1.geometry('700x400')
    v1.configure(background='black')
    l1 = Label(v1, text='Los valores deben estar separados por espacios EJEMPLO: 1 2 -4 ...')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.grid(row=0) 
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=1)
    l2 = Label(v1, text='x(n)')
    l2.configure(fg="white",background='black',font=("Verdana",11))
    l2.grid(row=2) 
    espacio2 = Label(v1, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.grid(row=3)
    l3 = Label(v1, text='Constante')
    l3.configure(fg="white",background='black',font=("Verdana",11))
    l3.grid(row=4) 
    espacio3 = Label(v1, text="")
    espacio3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3.grid(row=5)
    e1 = Entry(v1) 
    e3 = Entry(v1) 
    e1.grid(row=2, column=1) 
    e3.grid(row=4, column=1)
    aux = []
    aux1 = [1]
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        aux1.insert(0,int(e3.get())),
        mostrar_2(aux[0],diezmacion(aux[0],aux1[0]))
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.grid()

def boton_interpolar_secuencia_cero():
    v1 = tkinter.Tk()
    v1.geometry('700x400')
    v1.configure(background='black')
    l1 = Label(v1, text='Los valores deben estar separados por espacios EJEMPLO: 1 2 -4 ...')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.grid(row=0) 
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=1)
    l2 = Label(v1, text='x(n)')
    l2.configure(fg="white",background='black',font=("Verdana",11))
    l2.grid(row=2) 
    espacio2 = Label(v1, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.grid(row=3)
    l3 = Label(v1, text='Constante') 
    l3.configure(fg="white",background='black',font=("Verdana",11))
    l3.grid(row=4) 
    espacio3 = Label(v1, text="")
    espacio3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3.grid(row=5)
    e1 = Entry(v1) 
    e3 = Entry(v1) 
    e1.grid(row=2, column=1) 
    e3.grid(row=4, column=1)
    aux = []
    aux1 = [1]
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        aux1.insert(0,int(e3.get())),
        mostrar_2(aux[0],interpolacion_cero(aux[0],aux1[0]))
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.grid()

def boton_interpolar_secuencia_escalon():
    v1 = tkinter.Tk()
    v1.geometry('700x400')
    v1.configure(background='black')
    l1 = Label(v1, text='Los valores deben estar separados por espacios EJEMPLO: 1 2 -4 ...')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.grid(row=0) 
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=1)
    l2 = Label(v1, text='x(n)')
    l2.configure(fg="white",background='black',font=("Verdana",11))
    l2.grid(row=2) 
    espacio2 = Label(v1, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.grid(row=3)
    l3 = Label(v1, text='Constante') 
    l3.configure(fg="white",background='black',font=("Verdana",11))
    l3.grid(row=4) 
    espacio3 = Label(v1, text="")
    espacio3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3.grid(row=5)
    e1 = Entry(v1) 
    e3 = Entry(v1) 
    e1.grid(row=2, column=1) 
    e3.grid(row=4, column=1)
    aux = []
    aux1 = [1]
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        aux1.insert(0,int(e3.get())),
        mostrar_2(aux[0],interpolacion_escalon(aux[0],aux1[0]))
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.grid()

def boton_interpolar_secuencia_lineal():
    v1 = tkinter.Tk()
    v1.geometry('700x400')
    v1.configure(background='black')
    l1 = Label(v1, text='Los valores deben estar separados por espacios EJEMPLO: 1 2 -4 ...')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.grid(row=0) 
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=1)
    l2 = Label(v1, text='x(n)')
    l2.configure(fg="white",background='black',font=("Verdana",11))
    l2.grid(row=2) 
    espacio2 = Label(v1, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.grid(row=3)
    l3 = Label(v1, text='Constante') 
    l3.configure(fg="white",background='black',font=("Verdana",11))
    l3.grid(row=4) 
    espacio3 = Label(v1, text="")
    espacio3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3.grid(row=5)
    e1 = Entry(v1) 
    e3 = Entry(v1) 
    e1.grid(row=2, column=1) 
    e3.grid(row=4, column=1)
    aux = []
    aux1 = [1]
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        aux1.insert(0,int(e3.get())),
        mostrar_2(aux[0],interpolacion_lineal(aux[0],aux1[0]))
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.grid()

def audio_diezmar():
    v2 = tkinter.Tk()
    v2.geometry('700x400')
    v2.title('Diezmar audio')
    v2.configure(background='black')
    l1 = Label(v2, text='Ingrese número positivo o negativo\n(se grabara después de aceptar)')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.pack()
    espacio1 = Label(v2, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.pack()
    e1 = Entry(v2) 
    e1.pack()
    espacio2 = Label(v2, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.pack()
    acep = Button(v2, text='Aceptar', width=25, command=lambda:(
        grabar(),
        reproducir('audio.wav'),
        diezmacion_audio(obtener_audio('audio.wav'),int(e1.get())),
        reproducir('nuevo.wav'),
        mostrar(),
        v2.destroy()
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.pack()


def audio_interpolar_escalon():
    v2 = tkinter.Tk()
    v2.geometry('700x400')
    v2.title('Interpolar audio (Escalon)')
    v2.configure(background='black')
    l1 = Label(v2, text='Ingrese número positivo o negativo\n(se grabara después de aceptar)')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.pack()
    espacio1 = Label(v2, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.pack()
    e1 = Entry(v2) 
    e1.pack()
    espacio2 = Label(v2, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.pack()
    acep = Button(v2, text='Aceptar', width=25, command=lambda:(
        grabar(),
        reproducir('audio.wav'),
        interpolacion_escalon_audio(obtener_audio('audio.wav'),int(e1.get())),
        reproducir('nuevo.wav'),
        mostrar(),
        v2.destroy()
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.pack()

def audio_interpolar_lineal():
    v2 = tkinter.Tk()
    v2.geometry('700x400')
    v2.title('Interpolar audio (lineal)')
    v2.configure(background='black')
    l1 = Label(v2, text='Ingrese número positivo o negativo\n(se grabara después de aceptar)')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    l1.pack()
    espacio1 = Label(v2, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.pack()
    e1 = Entry(v2) 
    e1.pack()
    espacio2 = Label(v2, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.pack()
    acep = Button(v2, text='Aceptar', width=25, command=lambda:(
        grabar(),
        reproducir('audio.wav'),
        interpolacion_lineal_audio(obtener_audio('audio.wav'),int(e1.get())),
        reproducir('nuevo.wav'),
        mostrar(),
        v2.destroy()
    ) )
    acep.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    acep.pack()

def convolucion_finita():
    v1 = tkinter.Tk()
    v1.geometry('700x400')
    v1.configure(background='black')
    l1 = Label(v1, text='Los valores deben estar separados por espacios EJEMPLO: 1 2 -4 ...')
    l2 = Label(v1, text='x(n)')
    l3 = Label(v1, text='Constante')
    l1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1 = Label(v1, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    espacio1.grid(row=1)
    l2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2 = Label(v1, text="")
    espacio2.configure(fg="white",background='black',font=("Verdana",11))
    espacio2.grid(row=3)
    l3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3 = Label(v1, text="")
    espacio3.configure(fg="white",background='black',font=("Verdana",11))
    espacio3.grid(row=5)
    l1.grid(row=0) 
    l2.grid(row=2)
    l3.grid(row=4) 
    e1 = Entry(v1) 
    e3 = Entry(v1) 
    e1.grid(row=2, column=1) 
    e3.grid(row=4, column=1)
    aux = []
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x_h(e1,e3,aux),
        mostrar_3(aux[0],aux[1],convolucion(aux[0],aux[1]))
    ) )
    acep.grid()

def fft_aux(aux):
    r = fft(aux)
    mostrar_resultado(r)

def fft_secuencia():
    v1 = tkinter.Tk()
    v1.geometry('700x400')
    v1.configure(background='black')
    l1 = Label(v1, text='Los valores deben estar separados por espacios EJEMPLO: 1 2 -4 ...')
    l1.grid(row=0) 
    l2 = Label(v1, text='x(n)')
    l2.grid(row=1) 
    e1 = Entry(v1) 
    e1.grid(row=1, column=1) 
    aux = []
    acep = Button(v1, text='Aceptar', width=25, command=lambda:(
        aceptar_x(e1,aux),
        fft_aux(aux[0])
    ) )
    acep.grid()

#botones primer menu
def boton_sumar():
    v = tkinter.Tk()
    v.geometry('700x400')
    v.title('Sumar/Restar')
    v.configure(background='black')
    tit = Label(v, text="\nSuma/Resta\n")
    tit.pack(anchor=CENTER) 
    tit.configure(fg="white",background='black',font=("Verdana",16))
    espacio1 = Label(v, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    instruccion = Label(v, text="\nOprima el boton para grabar audio\n")
    instruccion.configure(fg="white",background='black',font=("Verdana",11))
    sumar_secuencias = Button(v, text='Sumar secuencias x(n), h(n)', width=50, command=boton_sumar_secuencias)
    restar_secuencias = Button(v, text='Restar secuencias x(n), h(n)', width=50, command=boton_restar_secuencias)
    subir_audio = Button(v, text='Sumar/Restar audio', width=50, command=lambda:(
        grabar(),
        reproducir('audio.wav'),
        subir_bajar_volumen()
    ))
    sumar_secuencias.pack()
    espacio1.pack(anchor=CENTER)
    restar_secuencias.pack()
    instruccion.pack(anchor=CENTER) 
    subir_audio.pack()
    sumar_secuencias.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    restar_secuencias.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    subir_audio.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

def boton_amplificar():
    v = tkinter.Tk()
    v.geometry('700x400')
    v.title('Amplificar/Atenuar')
    v.configure(background='black')
    tit = Label(v, text="\nAmplificar/Atenuar\n")
    tit.pack(anchor=CENTER) 
    tit.configure(fg="white",background='black',font=("Verdana",16))
    espacio1 = Label(v, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    instruccion = Label(v, text="\nOprima el boton para grabar audio\n")
    instruccion.configure(fg="white",background='black',font=("Verdana",11))
    ampl_secuencias = Button(v, text='Amplificar/Atenuar secuencia x(n)', width=50, command=boton_amp_frecuencias)
    amp_audio = Button(v, text='Amplificar/Atenuar audio', width=50, command=audio_amplificar)
    ampl_secuencias.pack()
    espacio1.pack(anchor=CENTER)
    amp_audio.pack()
    ampl_secuencias.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    amp_audio.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

def boton_reflejar():
    v = tkinter.Tk()
    v.geometry('700x400')
    v.title('Reflejar')
    v.configure(background='black')
    tit = Label(v, text="\nReflejar\n")
    tit.pack(anchor=CENTER) 
    tit.configure(fg="white",background='black',font=("Verdana",16))
    espacio1 = Label(v, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    instruccion = Label(v, text="\nOprima el boton para grabar audio\n")
    instruccion.configure(fg="white",background='black',font=("Verdana",11))
    ampl_secuencias = Button(v, text='Reflejar secuencia x(n)', width=50, command=reflejar_sequencias)
    amp_audio = Button(v, text='Reflejar audio', width=50, command=audio_reflejo)
    ampl_secuencias.pack()
    instruccion.pack()
    amp_audio.pack()
    ampl_secuencias.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    amp_audio.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

def boton_desplazar():
    v = tkinter.Tk()
    v.geometry('700x400')
    v.title('Desplazar')
    v.configure(background='black')
    tit = Label(v, text="\nDesplazar\n")
    tit.pack(anchor=CENTER) 
    tit.configure(fg="white",background='black',font=("Verdana",16))
    espacio1 = Label(v, text="")
    espacio1.configure(fg="white",background='black',font=("Verdana",11))
    ampl_secuencias = Button(v, text='Desplazar secuencia x(n)', width=50, command=desplazar_sequencias)
    instruccion = Label(v, text="\n(Se grabará después de dar click)\n")
    instruccion.configure(fg="white",background='black',font=("Verdana",11))
    amp_audio = Button(v, text='Desplazar audio', width=50, command=audio_desplazar)
    ampl_secuencias.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    amp_audio.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    ampl_secuencias.pack()
    instruccion.pack()
    amp_audio.pack()

def boton_diezmar():
    v = tkinter.Tk()
    v.geometry('700x400')
    v.title('Diezmar/Interpolar')
    v.configure(background='black')
    tit = Label(v, text="Diezmar/Interpolar\n")
    tit.pack(anchor=CENTER) 
    tit.configure(fg="white",background='black',font=("Verdana",16))
    
    esp0 = Label(v, text="")
    esp0.configure(fg="white",background='black',font=("Verdana",11))
    esp0.pack()
    """
    ampl_secuencias = Button(v, text='Diezmar secuencia x(n)', width=25, command=boton_diezmar_secuencia)
    ampl_secuencias.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    esp1 = Label(v, text="")
    esp1.configure(fg="white",background='black',font=("Verdana",11))
    ampl_secuencias1 = Button(v, text='Interpolar secuencia x(n) cero', width=25, command=boton_interpolar_secuencia_cero)
    ampl_secuencias1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    esp2 = Label(v, text="")
    esp2.configure(fg="white",background='black',font=("Verdana",11))
    ampl_secuencias2 = Button(v, text='Interpolar secuencia x(n) escalon', width=25, command=boton_interpolar_secuencia_escalon)
    ampl_secuencias2.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    esp3 = Label(v, text="")
    esp3.configure(fg="white",background='black',font=("Verdana",11))
    ampl_secuencias3 = Button(v, text='Interpolar secuencia x(n) lineal', width=25, command=boton_interpolar_secuencia_lineal)
    ampl_secuencias3.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    esp4 = Label(v, text="")
    esp4.configure(fg="white",background='black',font=("Verdana",11))
    amp_audio = Button(v, text='Diezmar audio', width=25, command=audio_diezmar)
    amp_audio.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    esp5 = Label(v, text="")
    esp5.configure(fg="white",background='black',font=("Verdana",11))
    """

    amp_audio2 = Button(v, text='Interpolar audio escalon', width=35, command=audio_interpolar_escalon)
    amp_audio2.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    esp6 = Label(v, text="")
    esp6.configure(fg="white",background='black',font=("Verdana",11))
    """
    amp_audio3 = Button(v, text='Interpolar audio lineal', width=25, command=audio_interpolar_lineal)
    amp_audio3.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    """
    """
    ampl_secuencias.pack()
    esp1.pack()
    ampl_secuencias1.pack()
    esp2.pack()
    ampl_secuencias2.pack()
    esp3.pack()
    ampl_secuencias3.pack()
    esp4.pack()
    amp_audio.pack()
    esp5.pack()
    """
    amp_audio2.pack()
    """
    esp6.pack()
    amp_audio3.pack()
    """
def boton_convolucionar():
    v = tkinter.Tk()
    v.geometry('700x400')
    v.title('Convolucionar')
    v.configure(background='black')
    tit = Label(v, text="Convulucionar\n")
    tit.pack(anchor=CENTER) 
    tit.configure(fg="white",background='black',font=("Verdana",16))
    esp = Label(v, text="")
    esp.configure(fg="white",background='black',font=("Verdana",11))
    esp.pack()
    ampl_secuencias = Button(v, text='Convolucionar secuencias x(n) y h(n) finita', width=35, command=convolucion_finita)
    ampl_secuencias.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
    ampl_secuencias.pack()

def boton_fft():
    v = tkinter.Tk()
    v.geometry('500x200')
    v.title('FFT')
    v.configure(background='black')
    ampl_secuencias = Button(v, text='FFT secuencia x(n)', width=70, command=fft_secuencia)
    ampl_secuencias.pack()


ventanaPrincipal = tkinter.Tk()
ventanaPrincipal.title('Proyecto final Teoría de comunicaciones y señales')
ventanaPrincipal.geometry('800x600')
ventanaPrincipal.configure(background='black')
nombres = Label(ventanaPrincipal, text="Proyecto Final Teoría de Comunicaciones y señales\n\n\n3CM5\nMuñoz Primero Elías                                          3CM5\nRamirez Morales Erick Hazel                              3CM5\n\n")
nombres.pack(anchor=CENTER) 
nombres.configure(fg="white",background='black',font=("Verdana",11))
img = tkinter.PhotoImage(file="Images/señal.png")
Label(ventanaPrincipal, image=img, bd=0).pack()
espacio = Label(ventanaPrincipal, text="\n\n\n")
espacio.pack(anchor=CENTER) 
espacio.configure(fg="white",background='black',font=("Verdana",11))
btn_Aceptar = tkinter.Button(ventanaPrincipal,text="Iniciar" ,width=15, height=2,command=ventanaPrincipal.destroy)
btn_Aceptar.pack()
btn_Aceptar.configure(fg="black",background='gray',font=("Verdana",11))
ventanaPrincipal.mainloop()

ventana = tkinter.Tk() 
ventana.title('Proyecto señales')
ventana.geometry('800x600')
ventana.configure(background='black')

frase = Label(ventana, text="\n\nMenu Principal\n\n\n")
frase.pack(anchor=CENTER) 
frase.configure(fg="white",background='black',font=("Verdana",16))
espacio_btn = Label(ventana, text="")
espacio_btn.configure(fg="white",background='black',font=("Verdana",11))
espacio_btn1 = Label(ventana, text="")
espacio_btn1.configure(fg="white",background='black',font=("Verdana",11))
espacio_btn2 = Label(ventana, text="")
espacio_btn2.configure(fg="white",background='black',font=("Verdana",11))
espacio_btn3 = Label(ventana, text="")
espacio_btn3.configure(fg="white",background='black',font=("Verdana",11))
espacio_btn4 = Label(ventana, text="")
espacio_btn4.configure(fg="white",background='black',font=("Verdana",11))
espacio_btn5 = Label(ventana, text="")
espacio_btn5.configure(fg="white",background='black',font=("Verdana",11))
espacio_btn6 = Label(ventana, text="")
espacio_btn6.configure(fg="white",background='black',font=("Verdana",11))
sumar1 = Button(ventana, text='Sumar/Restar', width=25, command=boton_sumar) 
amplificar1 = Button(ventana, text='Amplificar/Atenuar', width=25, command=boton_amplificar) 
reflejar1 = Button(ventana, text='Reflejar', width=25, command=boton_reflejar) 
desplazar1 = Button(ventana, text='Desplazar', width=25, command=boton_desplazar) 
diezmacion_interpolacion1 = Button(ventana, text='Diezmar/Interpolar', width=25, command=boton_diezmar)
convolucion1 = Button(ventana, text='Convolucionar', width=25, command=boton_convolucionar)
fft1 = Button(ventana, text='FFT', width=25, command=boton_fft)

sumar1.pack() 
espacio_btn.pack(anchor=CENTER) 
amplificar1.pack()
espacio_btn1.pack(anchor=CENTER)
reflejar1.pack()
espacio_btn2.pack(anchor=CENTER)
desplazar1.pack()
espacio_btn3.pack(anchor=CENTER)
diezmacion_interpolacion1.pack()
espacio_btn4.pack(anchor=CENTER)
convolucion1.pack()
espacio_btn5.pack(anchor=CENTER)
fft1.pack()

sumar1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
amplificar1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
reflejar1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
desplazar1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
diezmacion_interpolacion1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
convolucion1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))
fft1.configure(fg="black",background='gray',font=("Verdana",11,"bold"))

ventana.mainloop()