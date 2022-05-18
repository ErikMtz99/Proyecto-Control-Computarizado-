import numpy as np
from scipy.ndimage.interpolation import shift

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.animation import FuncAnimation

from tkinter import *
import tkinter

root = Tk()
root.title('Proyecto Control Computarizado')
root.geometry("700x500")

ARRAY_SIZE = 50
T = 5                      #Tiempo de muestreo

inputs_lista = []
   
for x in range(7): #0 1 2 3 4 5 6
    inputs = Entry(root)
    inputs.grid(row=x+1, column=1, pady=10, padx=3)
    inputs_lista.append(inputs)
for x in range(7): #0 1 2 3 4 5
    inputs = Entry(root)
    inputs.grid(row=x+1, column=8, pady=10, padx=3)
    inputs_lista.append(inputs)
    

e1 = inputs_lista[0]
e2 = inputs_lista[1]
e3 = inputs_lista[2]
e4 = inputs_lista[3]
e5 = inputs_lista[4]
e6 = inputs_lista[5]
e7 = inputs_lista[6]
e8 = inputs_lista[7]
e9 = inputs_lista[8]
e10 = inputs_lista[9]
e11 = inputs_lista[10]
e12 = inputs_lista[11]
e13 = inputs_lista[12]
e14 = inputs_lista[13]

e1.insert(0, "2")
e2.insert(0, "2")
e3.insert(0, "5")
e4.insert(0,"0.7")
e5.insert(0,"0.2")
e6.insert(0,"0")
e7.insert(0,"0")
e8.insert(0,"0")
e9.insert(0,"0.1")
e10.insert(0,"0.5")
e11.insert(0,"0.3")
e12.insert(0,"10")
e13.insert(0,"Ponerlo en el codigo")
e14.insert(0,"Ponerlo en el codigo")

Label(text="M. Escalón =", width=10).grid(row=1, column=0)
Label(text="M. Ruido E =", width=10).grid(row=2, column=0)
Label(text="M. Ruido S", width=10).grid(row=3, column=0)
Label(text="a1", width=10).grid(row=4, column=0)
Label(text="a2", width=10).grid(row=5, column=0)
Label(text="a3", width=10).grid(row=6, column=0)
Label(text="a4", width=10).grid(row=7, column=0)

Label(text="b0", width=10).grid(row=1, column=4)
Label(text="b1", width=10).grid(row=2, column=4)
Label(text="b2", width=10).grid(row=3, column=4)
Label(text="b3", width=10).grid(row=4, column=4)
Label(text="b4", width=10).grid(row=5, column=4)
Label(text="T", width=10).grid(row=6, column=4)
Label(text="d", width=10).grid(row=7, column=4)

def Click():
    M = float(e1.get())           #Magnitud de escalón 2
    Pe = float(e2.get())          #Magnitud ruido entrada 2
    Ps = float(e3.get())                      #Magnitud ruido salida 5

    a1 = float(e4.get())                       #0.7
    a2 = float(e5.get())                       #0.2
    a3 = float(e6.get())                       #0
    a4 = float(e7.get())                       #0


    b0 = float(e8.get())                       #0
    b1 = float(e9.get())                       #0.1
    b2 = float(e10.get())                       #0.5
    b3 = float(e11.get())                       #0.3
    b4 = float(e12.get())                       #10

    d = 5   
    
    y = np.zeros(ARRAY_SIZE)
    u = np.zeros(ARRAY_SIZE)
    
    #intervalo_muestreo = int(ARRAY_SIZE / T)
    #--------------CALCULO DE VALORES------------------
    for k in range(ARRAY_SIZE):
        #cn  =  a1cn-1 + a2cn-2  + a3cn-3  + a4cn-4  + b0m-d-n + b1mn-d-1  + b2mn-d-2  + b3mn-d-3  + b4mn-d-4
        y[0] = a1*y[1] + a2*y[2] + a3*y[3] + a4*y[4] + b0*u[d] + b1*u[d+1] + b2*u[d+2] + b3*u[d+3] + b4*u[d+4]
        y[0] = y[0] + Ps
        u[0] = M + Pe
        
        y = np.roll(y,1)
        u = np.roll(u,1)

    #se añade el retraso (0's) en la gráfica del escalón para visualización    
    for i in range(d+1): 
        u[i] = 0
 
    y_flip = np.flip(y) 
 
    #--------------GRAFICAS------------------ 
    #x = np.arange(10)
    #y = np.random.random(10)

    #fig = plt.figure()
    #plt.xlim(0, 10)
    #plt.ylim(0, 1)
    #graph, = plt.plot([], [], 'o')

    #def animate(i): 
    #    graph.set_data(x[:i+1], y[:i+1])
    #    return graph

    #ani = FuncAnimation(fig, animate, frames=1, interval=200)
    #plt.show()

    plt.subplot(2, 1, 1)
    plt.plot(y_flip,'.') 
    plt.title('tiempo (s)')
    plt.ylabel('Salida')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo')

    plt.subplot(2, 1, 2)
    plt.plot(u, '-')
    plt.xlabel('tiempo (s)')
    plt.ylabel('Escalón')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo')
    plt.show()

boton = Button(root, text="Empezar simulación", command=Click)   
boton.grid(row=0,column=0,pady=10)
 
root.mainloop()





    
