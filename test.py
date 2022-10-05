import tkinter
import os

from click import command

ventana = tkinter.Tk()
ventana.geometry("400x400")


def Capturar():
    os.system('python capturandoRostros.py')


def Entrenar():
    os.system('python entrenandoRF.py')


def Run():
    os.system('python ReconocimientoFacial.py')


botonCapturar = tkinter.Button(ventana, text="Capturar Rostro",
                               activebackground='blue', activeforeground='red', bg='green', command=Capturar)
botonEntrenar = tkinter.Button(ventana, text="Entrenar",
                               activebackground='blue', activeforeground='red', bg='green', command=Entrenar)
botonRun = tkinter.Button(ventana, text="Alto ahí!!! Reconocimiento facial",
                          activebackground='blue', activeforeground='red', bg='green', command=Run)
botonCapturar.pack(side='top')
botonEntrenar.pack(side='top')
botonRun.pack(side='top')

#boton1.place(x=130, y=40)

ventana.mainloop()
