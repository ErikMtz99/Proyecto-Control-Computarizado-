import numpy as np
from scipy.ndimage.interpolation import shift
from matplotlib import pyplot as plt
from tkinter import *
import tkinter as tk

root = Tk()
root.title('Proyecto Control Computarizado')
root.geometry("700x500")

tk.Label(root, 
		 text="Simulación de Planta",
		 fg = "blue",
		 font = "Helvetica 16 bold italic").grid(row=0,column=1,pady=10)

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
e2.insert(0, "0")
e3.insert(0, "0")
e4.insert(0,"0.7")
e5.insert(0,"0.2")
e6.insert(0,"0")
e7.insert(0,"0")
e8.insert(0,"0")
e9.insert(0,"0.1")
e10.insert(0,"0.5")
e11.insert(0,"0.3")
e12.insert(0,"0")
e13.insert(0,"0")
e14.insert(0,"1")

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
Label(text="d", width=10).grid(row=6, column=4)
Label(text="T", width=10).grid(row=7, column=4)

def Click():
    M = float(e1.get())           #Magnitud de escalón 
    Pe = float(e2.get())          #Magnitud ruido entrada 
    Ps = float(e3.get())          #Magnitud ruido salida 
                                  # a's
    a1 = float(e4.get())                       
    a2 = float(e5.get())                       
    a3 = float(e6.get())                       
    a4 = float(e7.get())                       

                                  # b's
    b0 = float(e8.get())                      
    b1 = float(e9.get())                      
    b2 = float(e10.get())                      
    b3 = float(e11.get())                       
    b4 = float(e12.get())       

    d = int(e13.get())            #Retraso
    T = float(e14.get())          #Intervalo de Muestreo
    
    ARRAY_SIZE = 50
    y = np.zeros(ARRAY_SIZE)      #Lista valores de salida
    y_interval = np.zeros(ARRAY_SIZE)
    x = np.zeros(ARRAY_SIZE)      #Lista de intervalos kT
    u = np.zeros(ARRAY_SIZE)      #Lista valores de escalón entrada
    
    #intervalo_muestreo = int(ARRAY_SIZE / T)
    #--------------CALCULO DE VALORES------------------
    for k in range(ARRAY_SIZE):
        #Estructura ARX
        y[0] = a1*y[1] + a2*y[2] + a3*y[3] + a4*y[4] + b0*u[d] + b1*u[d+1] + b2*u[d+2] + b3*u[d+3] + b4*u[d+4]
        
        #Suma de perturbación de salida a la salida
        y[0] = y[0] + Ps 
        
        #Suma de perturbación de entrada a la entrada
        u[0] = M + Pe    
        
        #Creación de vector de intervalos kT 
        x[k] = k*T
        
        #shifts de los arrays
        y = np.roll(y,1)
        u = np.roll(u,1)

    #se añade el retraso (0's) en la gráfica del escalón para visualización    
    for i in range(d+1): 
        u[i] = 0
      
    #Se voltea el array de salida para poder graficar los valores   
    y_flip = np.flip(y) 
        
        
    #Para que funcione el intervalo de muestreo T (PUROS ENTEROS HASTA EL MOMENTO)
    for i in range(ARRAY_SIZE):
        if(x[i] < ARRAY_SIZE):
            y_interval[i] = y_flip[int(x[i])]
    
    #GRAFICA DE SALIDA DE LA PLANTA
    plt.subplot(2, 1, 1)
    plt.plot(x,y_interval,'*') 
    plt.title('Salida de la Planta')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo (s)')

    plt.subplot(2, 1, 2)
    plt.plot(u, '-')
    plt.title('Escalón de entrada')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo (s)')
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
    plt.show()

boton = Button(root, text="Empezar simulación", command=Click)   
boton.grid(row=0,column=0,pady=10)
 
root.mainloop()





    
