from math import e,pi
import numpy as np
from scipy import signal
import wave,audioop
from pydub import AudioSegment
import soundfile as sf
from scipy.io.wavfile import write
import scipy.io.wavfile as waves

def restar(x,h):
    return np.subtract(x,h)

def sumar(x,h):
    return np.add(x,h)

def amplificar(x,constante):
    return np.array(x)*constante

def amplificar_audio(constante):
    with wave.open('audio.wav', 'rb') as wav:
        p = wav.getparams()
        with wave.open('nuevo.wav', 'wb') as audio:
            audio.setparams(p)
            frames = wav.readframes(p.nframes)
            audio.writeframesraw( audioop.mul(frames, p.sampwidth, constante))

def sumar_audio(volumen):
    audio_file = "audio.wav"
    song = AudioSegment.from_mp3(audio_file)
    new = song.low_pass_filter(1000)
    new1 = new.high_pass_filter(1000)
    audio = new1 + int(volumen)
    audio.export("nuevo.wav", "wav")

def reflejo(audio):
    return np.flip(audio)

def reflejo_audio(audio):
    nuevo = np.flip(audio)
    write('nuevo.wav', 44100, nuevo)
    return nuevo

def desplazamiento_secuencias(senal,h):
    nuevo = np.append(np.zeros(h),senal)
    return nuevo

def desplazamiento_audio(h):
    archivo = 'audio.wav'
    muestreo, audio = waves.read(archivo)
    nuevo = np.int16(np.append(np.zeros(h*128),audio))
    write('nuevo.wav', 44100, nuevo)
    return nuevo

def fft(a):
    n = len(a)
    if(n == 1):
        return a
    wn = e**((2*pi*1j)/n)
    w = 1

    a0 = []
    a1 = []
    for i in range(len(a)):
        if i%2==0:
            a0.append(a[i])
        else:
            a1.append(a[i])
    
    y0 = fft(a0)
    y1 = fft(a1)

    y = [0 for i in range(n)]
    for k in range(0,(n//2)):
        y[k] = y0[k] + w*y1[k]
        y[k+(n//2)] = y0[k] - w*y1[k]
        w = w*wn
    return y

def convolucion(a, b):
    Na = len(a)
    Nb = len(b)

    y = [0 for x in range(0,Na+Nb-1)]
    Ny = len(y)

    #Sumatoria de convolución
    for n in range(0,Ny):
        k = n; f = 1;
        while k >= 0:
            if n >= Na:   #Este if es para cuando el vector que va recorriendo se sale del indice de a[k]
                k = Na-f; f += 1;
                
            y[n] += a[k]*b[n-k] #Ecuación de la convolución
            k -= 1
            if (n-k) >= Nb:
                break
    return np.array(y)

def convolucion_audio(audio1,audio2):#para el audio porque el otro algoritmo tarda mucho
    nuevo = signal.convolve(audio1,audio2)
    write('nuevo.wav', 44100, nuevo)
    return nuevo

def diezmacion(audio,n):
    nuevo = []
    for i in range(0,len(audio),n):
        nuevo.append(audio[i])
    aux = np.int16(nuevo)
    return aux

def diezmacion_audio(audio,n):
    nuevo = []
    for i in range(0,len(audio),n):
        nuevo.append(audio[i])
    aux = np.int16(nuevo)
    write('nuevo.wav', 44100, aux)
    return aux

def interpolacion_cero(audio,n):
    nuevo = []
    for i in range(0,len(audio)):
        nuevo.append(audio[i])
        for j in range(0,n-1):
            nuevo.append(0)
    aux = np.int16(nuevo)
    return aux

def interpolacion_escalon(audio,n):
    nuevo = []
    for i in range(0,len(audio)):
        nuevo.append(audio[i])
        for j in range(0,n-1):
            nuevo.append(audio[i])
    aux = np.int16(nuevo)
    return aux
        
def interpolacion_escalon_audio(audio,n):
    nuevo = []
    for i in range(0,len(audio)):
        nuevo.append(audio[i])
        for j in range(0,n-1):
            nuevo.append(audio[i])
    aux = np.int16(nuevo)
    write('nuevo.wav', 44100, aux)
    return aux

def interpolacion_lineal(audio,n):
    nuevo = []
    for i in range(0,len(audio)):
        nuevo.append(audio[i])
        for j in range(0,n-1):
            if i != len(audio)-1:
                nuevo.append((audio[i]+audio[i+1])/2)
    aux = np.array(nuevo)
    return aux

def interpolacion_lineal_audio(audio,n):
    nuevo = []
    for i in range(0,len(audio)):
        nuevo.append(audio[i])
        for j in range(0,n-1):
            if i != len(audio)-1:
                nuevo.append((audio[i]+audio[i+1])//2)
            else:
                nuevo.append(nuevo[i])
    aux = np.int16(nuevo)
    write('nuevo.wav', 44100, aux)
    return aux