from tkinter import *
from tkinter import ttk
import tkinter
import os
import cv2
import imutils

from click import command


def Entrenar():
    os.system('python entrenandoRF.py')


def Run():
    os.system('python ReconocimientoFacial.py')


def Registrarse():
    global entry
    global personName
    personName = entry.get()
    label.configure(text='Bienvenido '+personName)


personName = ''


def Capturar():

    # Cambia a la ruta donde hayas almacenado Data
    dataPath = 'C:/Users/diego.mendez/Desktop/ReconocimientoFacial/Data'
    personPath = dataPath + '/' + personName

    if not os.path.exists(personPath):
        print('Carpeta creada: ', personPath)
        os.makedirs(personPath)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #cap = cv2.VideoCapture('Video.mp4')

    faceClassif = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:

        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv2.flip(frame, 1)
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (150, 150),
                                interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count), rostro)
            count = count + 1
        cv2.imshow('Capturando Rostro', frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= 250:
            break

    cap.release()
    cv2.destroyAllWindows()
# Aca terminan las funciones


# Crear Ventana
ventana = tkinter.Tk()
# Dimensionar Ventana
ventana.geometry("600x600")
# Imagen de fondo
bg = PhotoImage(file="bkgr.png")
# Crear Canvas
canvas1 = Canvas(ventana, width=600,
                 height=600)
# Asociar la imagen de fondo al Canvas
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")
canvas1.pack(fill="both", expand=True)
# Crear Botones
btnRegis = ttk.Button(ventana, text="Registrarse", width=20,
                      command=Registrarse)
btnCapt = ttk.Button(ventana, text="Capturar", width=20,
                     command=Capturar)
btnEntrenar = ttk.Button(ventana, text="Entrenar", width=20,
                         command=Entrenar)
btnRun = ttk.Button(ventana, text="Reconocer", width=20,
                    command=Run)

label = Label(ventana, text="Inicio", font=("Courier 22 bold"))
label_canvas = canvas1.create_window(300, 30, anchor="center", window=label)

# Create an Entry widget to accept User Input
entry = Entry(ventana, width=30, justify='center')
entry.focus_set()
entry_canvas = canvas1.create_window(200, 70, anchor='nw', window=entry)

button1_canvas = canvas1.create_window(230, 100,
                                       anchor="nw",
                                       window=btnRegis)
button1_canvas = canvas1.create_window(230, 130,
                                       anchor="nw",
                                       window=btnCapt)
button1_canvas = canvas1.create_window(230, 160,
                                       anchor="nw",
                                       window=btnEntrenar)
button1_canvas = canvas1.create_window(230, 190,
                                       anchor="nw",
                                       window=btnRun)


ventana.mainloop()
