import numpy as np
from matplotlib import pyplot as plt
from tkinter import Tk, Label, Entry, Button
import tkinter as tk
import math

root = Tk()
root.title('Proyecto Control Computarizado')
root.geometry("800x620")
root.configure(background='#ADD8E6')

ARRAY_SIZE = 100

#--------------- T I T U L O S -----------------
titulo = tk.Label(root, 
		 text="Control Computarizado",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 20 bold italic",
         anchor = "center")

t_manual = tk.Label(root, 
		 text="Seleccione el modelo a utilizar",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 12 bold italic",
         anchor = "center")

t_planta = tk.Label(root, 
		 text="Simulación de Planta",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 20 bold italic",
         anchor = "center") 

t_orden1 = tk.Label(root, 
		 text="Simulación de Modelo 1er Orden",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 20 bold italic",
         anchor = "center")  

t_orden2 = tk.Label(root, 
		 text="Simulación de Modelo 2ndo Orden",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 20 bold italic",
         anchor = "center")  

t_PID = tk.Label(root, 
		 text="Control PID",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 20 bold italic",
         anchor = "center")  

t_constantes = tk.Label(root, 
		 text="Constantes PID",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 14 bold italic",
         anchor = "center")

titulo.grid(row=0,column=1,pady=10)

#--------------- E T I Q U E T A S -----------------
l1 = Label(text="M. Escalón", width=10)
l2 =Label(text="M. Ruido E", width=10)
l3 =Label(text="M. Ruido S", width=10)
l4 =Label(text="a1", width=10)
l5 =Label(text="a2", width=10)
l6 =Label(text="a3", width=10)
l7 =Label(text="a4", width=10)

l8 =Label(text="b0", width=10)
l9 =Label(text="b1", width=10)
l10 =Label(text="b2", width=10)
l11 =Label(text="b3", width=10)
l12 =Label(text="b4", width=10)
l13 =Label(text="d", width=10)
l14 =Label(text="T", width=10) 

l15 =Label(text="Ganancia K", width=10)
l16 =Label(text="Tau", width=10)
l17 =Label(text="T. muerto", width=10)
l18 =Label(text="Int. Muestreo", width=10)
l19 =Label(text="M. Escalón", width=10)
 
l20 =Label(text="Amort. Zeta", width=10)
l21 =Label(text="Freq wn", width=10)

l22 =Label(text="Kc", width=10)
l23 =Label(text="Tau i", width=8)
l24 =Label(text="Tau d", width=10)
lerror = Label(root, 
		 text="Error, zeta entre 0 y 1",
		 fg = "red",
		 font = "Verdana 14 bold italic",
         anchor = "center") 
#----------- Manual ARX ------------------------   
inputs_lista = []
#0 1 2 3 4 5 6
for x in range(7):
    inputs = Entry(root)
    inputs_lista.append(inputs)
#0 1 2 3 4 5
for x in range(7): 
    inputs = Entry(root)
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
e14 = inputs_lista[13]   #Intervalo de Muestreo

#----------- Manual 1er orden ------------------------ 
k1 = Entry(root)
tau1 = Entry(root)
teta_prima1 = Entry(root)

#----------- Manual 2ndo orden ------------------------ 
zeta = Entry(root)
wn = Entry(root)

#----------- PID ------------------------ 
kc = Entry(root)
tau_i = Entry(root)
tau_d = Entry(root)

#---------------------------------------------------------
#******************F U N C I O N E S**********************
#---------------------------------------------------------
def func_inicio():
    titulo.grid(row=0,column=1,pady=10)
    b_man.grid(row=1,column=1,pady=10)
    b_auto.grid(row=1,column=2,pady=10)

    t_manual.grid_forget()
    t_planta.grid_forget()
    t_orden1.grid_forget()
    t_orden2.grid_forget()
    t_constantes.grid_forget()
    t_PID.grid_forget()
    
    b_ARX.grid_forget()
    b_orden1.grid_forget()
    b_orden2.grid_forget()
    

    b_sim1.grid_forget() 
    b_sim2.grid_forget()
    b_sim3.grid_forget()
    b_sim4.grid_forget()
    
    for x in range(7):
        inputs_lista[x].grid_forget()
    #0 1 2 3 4 5
    for x in range(7): 
        inputs_lista[x+7].grid_forget()
        
    k1.grid_forget()
    tau1.grid_forget()
    teta_prima1.grid_forget()
    zeta.grid_forget()
    wn.grid_forget()
    #e14.grid_forget()
    #1.grid_forget()
    
    kc.grid_forget()
    tau_i.grid_forget()
    tau_d.grid_forget()
    
    reg1.grid_forget()

    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l5.grid_forget()
    l6.grid_forget()     
    l7.grid_forget()
    l8.grid_forget()
    l9.grid_forget()
    l10.grid_forget()
    l11.grid_forget()
    l12.grid_forget()
    l13.grid_forget()    
    l14.grid_forget()    
    l15.grid_forget()
    l16.grid_forget()
    l17.grid_forget()
    l18.grid_forget()
    l19.grid_forget()
    l20.grid_forget()
    l21.grid_forget()    
    l22.grid_forget()
    l23.grid_forget()
    l24.grid_forget()
    lerror.grid_forget()
    
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)
    e7.delete(0, tk.END)
    e8.delete(0, tk.END)
    e9.delete(0, tk.END)
    e10.delete(0, tk.END)
    e11.delete(0, tk.END)
    e12.delete(0, tk.END)
    e13.delete(0, tk.END)
    e14.delete(0, tk.END)
    k1.delete(0, tk.END)
    tau1.delete(0, tk.END)
    teta_prima1.delete(0, tk.END)    
    zeta.delete(0, tk.END) 
    wn.delete(0, tk.END) 
    kc.delete(0, tk.END) 
    tau_i.delete(0, tk.END) 
    tau_d.delete(0, tk.END) 
    
def func_manual():
    titulo.grid_forget()
    b_man.grid_forget()
    b_auto.grid_forget()
      

    t_manual.grid(row=0,column=0,pady=0,columnspan=4)
    b_ARX.grid(row=1,column=2,pady=10)
    b_orden1.grid(row=3,column=2,pady=10)
    b_orden2.grid(row=5,column=2,pady=10)
    
    reg1.grid(row=11, column = 1, pady=10)
    
    
#****************** A R X **********************
#-----------------------------------------------
def func_ARX():
    t_manual.grid_forget()
    b_ARX.grid_forget()
    b_orden1.grid_forget()
    b_orden2.grid_forget()
    
    t_planta.grid(row=0,column=0,pady=0,columnspan=4)
    b_sim1.grid(row=10,column=0,pady=10)
    reg1.grid(row=11, column = 1, pady=10)    
    
    for x in range(7):
        inputs_lista[x].grid(row=x+1, column=1, pady=10, padx=3)
    #0 1 2 3 4 5
    for x in range(7): 
        inputs_lista[x+7].grid(row=x+1, column=8, pady=10, padx=3)

    l1.grid(row=1, column=0)
    l2.grid(row=2, column=0)
    l3.grid(row=3, column=0)
    l4.grid(row=4, column=0)
    l5.grid(row=5, column=0)
    l6.grid(row=6, column=0)
    l7.grid(row=7, column=0)

    l8.grid(row=1, column=4)
    l9.grid(row=2, column=4)
    l10.grid(row=3, column=4)
    l11.grid(row=4, column=4)
    l12.grid(row=5, column=4)
    l13.grid(row=6, column=4)
    l14.grid(row=7, column=4)
    
    e1.insert(0, "2")
    e2.insert(0, "0")
    e3.insert(0, "0")
    e4.insert(0,"0.7")
    e5.insert(0,"0.2")
    e6.insert(0,"0")
    e7.insert(0,"0")
    e8.insert(0,"0")
    e9.insert(0,"1")
    e10.insert(0,"0.3")
    e11.insert(0,"0")
    e12.insert(0,"0")
    e13.insert(0,"0")
    e14.insert(0,"1")


    



def func_ARX_2():
    
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
    plt.plot(x,y_interval,'.') 
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
        
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
    plt.show()    

            
#************** 1ER O R D E N ******************
#-----------------------------------------------    
   
def func_orden1():
    t_manual.grid_forget()
    b_ARX.grid_forget()
    b_orden1.grid_forget()
    b_orden2.grid_forget()
    
    t_orden1.grid(row=0,column=0,pady=0,columnspan=4)
    b_sim2.grid(row=10,column=0,pady=10)
    
    k1.grid(row=1, column=1, pady=10, padx=3)
    tau1.grid(row=2, column=1, pady=10, padx=3)
    teta_prima1.grid(row=3, column=1, pady=10, padx=3) 
    e14.grid(row=4, column=1, pady=10, padx=3)
    e1.grid(row=5, column=1, pady=10, padx=3)
    e2.grid(row=6, column=1, pady=10, padx=3)
    e3.grid(row=7, column=1, pady=10, padx=3)
    
    k1.insert(0, "1") 
    tau1.insert(0, "2.7")
    teta_prima1.insert(0, "1.9")
    e14.insert(0,"1")
    e1.insert(0,"2")
    e2.insert(0, "0")
    e3.insert(0, "0")
    
    l15.grid(row=1, column=0)
    l16.grid(row=2, column=0)
    l17.grid(row=3, column=0)
    l18.grid(row=4, column=0)
    l19.grid(row=5, column=0)
    l2.grid(row=6, column=0)
    l3.grid(row=7, column=0)
    

def func_orden1_2():
    
    M = float(e1.get())           #Magnitud de escalón 
    K1 = float(k1.get())           
    Tau1 = float(tau1.get())          
    Teta_prima1 = float(teta_prima1.get())           
    T = float(e14.get())           
    Pe = float(e2.get())          #Magnitud ruido entrada 
    Ps = float(e3.get())          #Magnitud ruido salida 
    d = math.floor(Teta_prima1/T)            #Retraso
    teta1 = Teta_prima1 - (d*T)  
    m1 = 1 - (teta1/T)   
                
    a1 = math.exp(-T/Tau1)                     
    a2 = 0                      
    a3 = 0                       
    a4 = 0                      
    
                                      # b's
    b0 = 0                      
    b1 = K1*(1 - (math.exp((-m1*T)/(Tau1))))                     
    b2 = K1*((math.exp((-m1*T)/(Tau1))) - math.exp(-T/Tau1))                       
    b3 = 0                       
    b4 = 0       
    
    
    
    
    y = np.zeros(ARRAY_SIZE)      #Lista valores de salida
    y_interval = np.zeros(ARRAY_SIZE)
    x = np.zeros(ARRAY_SIZE)      #Lista de intervalos kT
    u = np.zeros(ARRAY_SIZE)      #Lista valores de escalón entrada
        
    #intervalo_muestreo = int(ARRAY_SIZE / T)
    #--------------CALCULO DE VALORES------------------
    for k in range(ARRAY_SIZE):
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
    plt.plot(x,y_interval,'.') 
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
        
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
    plt.show()   
    

#************** 2NDO O R D E N ******************
#-----------------------------------------------    
   
def func_orden2():
    t_manual.grid_forget()
    b_ARX.grid_forget()
    b_orden1.grid_forget()
    b_orden2.grid_forget()
    
    t_orden2.grid(row=0,column=0,pady=0,columnspan=4)
    b_sim3.grid(row=10,column=0,pady=10)
    
    k1.grid(row=1, column=1, pady=10, padx=3)
    zeta.grid(row=2, column=1, pady=10, padx=3)
    wn.grid(row=3, column=1, pady=10, padx=3)
    teta_prima1.grid(row=4, column=1, pady=10, padx=3) 
    e14.grid(row=5, column=1, pady=10, padx=3)
    e1.grid(row=6, column=1, pady=10, padx=3)
    e2.grid(row=7, column=1, pady=10, padx=3)
    e3.grid(row=8, column=1, pady=10, padx=3)
    
    k1.insert(0, "1") 
    zeta.insert(0, "0.5")
    wn.insert(0, "2.7")
    teta_prima1.insert(0, "1.9")
    e14.insert(0,"1")
    e1.insert(0,"2")
    e2.insert(0, "0")
    e3.insert(0, "0")
    
    l15.grid(row=1, column=0)
    l20.grid(row=2, column=0)
    l21.grid(row=3, column=0)
    l17.grid(row=4, column=0)
    l18.grid(row=5, column=0)
    l19.grid(row=6, column=0)
    l2.grid(row=7, column=0)
    l3.grid(row=8, column=0)

def func_orden2_2():

    M = float(e1.get()) 
    Pe = float(e2.get())          #Magnitud ruido entrada 
    Ps = float(e3.get())          #Magnitud ruido salida           
    K1 = float(k1.get())           
    Zeta = float(zeta.get()) 
    
    if (Zeta < 0) or (Zeta > 1):
        lerror.grid(row=2, column=2)
    else:
        lerror.grid_forget()
        
    Wn = float(wn.get())         
    Teta_prima1 = float(teta_prima1.get())           
    T = float(e14.get())           
    
    d = math.floor(Teta_prima1/T)            
    a = Wn*Zeta
    b = Wn*(math.sqrt(1 - (Zeta*Zeta)))
                
    a1 = 2*(math.exp(-a*T))*math.cos(b*T)                  
    a2 = -(math.exp(-2*a*T))                     
    a3 = 0                       
    a4 = 0                      
     
                                      
    b0 = 0                      
    b1 = K1*( 1 - math.exp(-a*T)*math.cos(b*T) - (a/b)*math.exp(-a*T)*math.sin(b*T))                   
    b2 = K1*(math.exp(-2*a*T) - math.exp(-a*T)*math.cos(b*T) + (a/b)*math.exp(-a*T)*math.sin(b*T))                        
    b3 = 0                        
    b4 = 0        
    
    
    
    
    y = np.zeros(ARRAY_SIZE)      #Lista valores de salida
    y_interval = np.zeros(ARRAY_SIZE)
    x = np.zeros(ARRAY_SIZE)      #Lista de intervalos kT
    u = np.zeros(ARRAY_SIZE)      #Lista valores de escalón entrada
        
    #intervalo_muestreo = int(ARRAY_SIZE / T)
    #--------------CALCULO DE VALORES------------------
    for k in range(ARRAY_SIZE):
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
    plt.plot(x,y_interval,'.') 
    plt.title('Salida de la Planta')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo (s)')
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    
    plt.subplot(2, 1, 2)
    plt.plot(u, '-')
    plt.title('Escalón de entrada')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo (s)')
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
        
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
    plt.show()
#---------------------------------------------------------------------------------


def func_auto():
    titulo.grid_forget()
    b_man.grid_forget()
    b_auto.grid_forget()
    
    t_PID.grid(row=0,column=0,pady=0,columnspan=4)
    b_sim4.grid(row=12,column=0,pady=10)
    
    k1.grid(row=1, column=1, pady=10, padx=3)
    tau1.grid(row=2, column=1, pady=10, padx=3)
    teta_prima1.grid(row=3, column=1, pady=10, padx=3) 
    e14.grid(row=4, column=1, pady=10, padx=3)
    e1.grid(row=5, column=1, pady=10, padx=3)
    e2.grid(row=6, column=1, pady=10, padx=3)
    e3.grid(row=7, column=1, pady=10, padx=3)
    
    t_constantes.grid(row=8, column=0)
    
    kc.grid(row=9, column=1, pady=10, padx=3)
    tau_i.grid(row=10, column=1, pady=10, padx=3)
    tau_d.grid(row=11, column=1, pady=10, padx=3)     

    reg1.grid(row=13, column = 1, pady=10)

    l15.grid(row=1, column=0)
    l16.grid(row=2, column=0)
    l17.grid(row=3, column=0)
    l18.grid(row=4, column=0)
    l19.grid(row=5, column=0)
    
    l2.grid(row=6, column=0)
    l3.grid(row=7, column=0)
    
    l22.grid(row=9, column=0)
    l23.grid(row=10, column=0)
    l24.grid(row=11, column=0)
    
    k1.insert(0, "1") 
    tau1.insert(0, "2.7")
    teta_prima1.insert(0, "1.9")
    e14.insert(0,"1")
    e1.insert(0,"2")
    kc.insert(0, "1.3") 
    tau_i.insert(0, "3.89")
    tau_d.insert(0, "0.59")
    e2.insert(0, "0")
    e3.insert(0, "0")
    


def func_auto_2():
    
    M = float(e1.get())           #Magnitud de escalón 
    Pe = float(e2.get())          #Magnitud ruido entrada 
    Ps = float(e3.get())          #Magnitud ruido salida 
    K1 = float(k1.get())           
    Tau1 = float(tau1.get())          
    Teta_prima1 = float(teta_prima1.get())           
    T = float(e14.get())           
    
    Kc = float(kc.get())
    Tau_i = float(tau_i.get())
    Tau_d = float(tau_d.get())
    
    d = math.floor(Teta_prima1/T)            #Retraso
    teta1 = Teta_prima1 - (d*T)  
    m1 = 1 - (teta1/T)   
                
    a1 = math.exp(-T/Tau1)                     
    a2 = 0                      
    a3 = 0                       
    a4 = 0                      
    
                                      # b's
    b0 = 0                      
    b1 = K1*(1 - (math.exp((-m1*T)/(Tau1))))                     
    b2 = K1*((math.exp((-m1*T)/(Tau1))) - math.exp(-T/Tau1))                       
    b3 = 0                       
    b4 = 0       
    
    beta0 = Kc*(1 + (T/Tau_i) + (Tau_d/T))
    beta1 = Kc*(-1 - (2*Tau_d/T))
    beta2 = Kc*(Tau_d/T)
        
    y = np.zeros(ARRAY_SIZE)      #Lista valores de salida
    y_interval = np.zeros(ARRAY_SIZE)
    m_interval = np.zeros(ARRAY_SIZE)
    x = np.zeros(ARRAY_SIZE)      #Lista de intervalos kT
    u = np.zeros(ARRAY_SIZE)      #Lista valores de escalón entrada
    m = np.zeros(ARRAY_SIZE)      #Lista valores de controlador entrada
        
    #intervalo_muestreo = int(ARRAY_SIZE / T)
    
    #--------------CALCULO DE VALORES------------------
    for k in range(ARRAY_SIZE):
        y[0] = a1*y[1] + a2*y[2] + a3*y[3] + a4*y[4] + b0*m[d] + b1*m[d+1] + b2*m[d+2] + b3*m[d+3] + b4*m[d+4]

        #Suma de perturbación de entrada a la entrada
        u[0] = M + Pe 
        
        m[0] = m[1] + beta0*(u[0] - y[0]) + beta1*(u[1] - y[1]) + beta2*(u[2] - y[2])
        
        #Suma de perturbación de salida a la salida
        y[0] = y[0] + Ps
        

        
        #Creación de vector de intervalos kT 
        x[k] = k*T
            
        #shifts de los arrays
        y = np.roll(y,1)
        u = np.roll(u,1)
        m = np.roll(m,1)
    
    #se añade el retraso (0's) en la gráfica del escalón para visualización    
    for i in range(d+1): 
        u[i] = 0
          
    #Se voltea el array de salida para poder graficar los valores   
    y_flip = np.flip(y) 
    m_flip = np.flip(m)        
            
    #Para que funcione el intervalo de muestreo T (PUROS ENTEROS HASTA EL MOMENTO)
    for i in range(ARRAY_SIZE):
        if(x[i] < ARRAY_SIZE):
            y_interval[i] = y_flip[int(x[i])]
            m_interval[i] = m_flip[int(x[i])]
    
    #GRAFICA DE SALIDA DE LA PLANTA
    plt.subplot(2, 1, 1)
    plt.plot(x,y_interval,'-') 
    plt.plot(x,u,'-') 
    plt.title('Control PID de la planta')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo (s)')
    
    plt.subplot(2, 1, 2)
    plt.plot(x, m_interval, '-')
    plt.title('Salida del Controlador')
    plt.xlim([0, ARRAY_SIZE-4])  
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo (s)')
        
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
    plt.show()   
b_man = Button(root, text="Manual", command=func_manual, height=2, width=20, bg='#567', fg='White', font = "Verdana 10 bold italic")   
b_man.grid(row=1,column=1,pady=10)

b_auto = Button(root, text="Automatico", command=func_auto, height=2, width=20, bg='#567', fg='White', font = "Verdana 10 bold italic")   
b_auto.grid(row=1,column=2,pady=10)

b_ARX = Button(root, text="Modelo General ARX", command=func_ARX, height=2, width=20, bg='#567', fg='White', font = "Verdana 10 bold italic")   
b_orden1 = Button(root, text="Modelo 1er Orden", command=func_orden1, height=2, width=20, bg='#567', fg='White', font = "Verdana 10 bold italic")   
b_orden2 = Button(root, text="Modelo 2ndo Orden", command=func_orden2, height=2, width=20, bg='#567', fg='White', font = "Verdana 10 bold italic")   
b_sim1 = Button(root, text="Empezar simulación", command=func_ARX_2, bg='#567', fg='White', font = "Verdana 8 bold italic")
b_sim2 = Button(root, text="Empezar simulación", command=func_orden1_2, bg='#567', fg='White', font = "Verdana 8 bold italic")
b_sim3 = Button(root, text="Empezar simulación", command=func_orden2_2, bg='#567', fg='White', font = "Verdana 8 bold italic")
b_sim4 = Button(root, text="Empezar simulación", command=func_auto_2, bg='#567', fg='White', font = "Verdana 8 bold italic")

reg1 = Button(root, text="Regresar", command=func_inicio, bg='#567', fg='White', font = "Verdana 8 bold italic")

root.mainloop()


 


    
