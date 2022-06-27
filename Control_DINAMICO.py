import numpy as np
from matplotlib import pyplot as plt
from tkinter import Tk, Label, Entry, Button
import matplotlib.animation as animation
import tkinter as tk
import math
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure

root = Tk()
root.title('Proyecto Control Computarizado')
root.geometry("1000x620")
root.configure(background='#ADD8E6')
global ani

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    global y, u, x, y_flip, m, modo
    global M, Pe, Ps, a1, a2, a3, a4, b0, b1, b2, b3, b4, d, T, Teta_prima1, Tau1, K1, Wn, Zeta, Kc, Tau_i, Tau_d
    x = x + 1
    print(modo)
    if(modo == 0):
        y[0] = a1*y[1] + a2*y[2] + a3*y[3] + a4*y[4] + b0*u[d] + b1*u[d+1] + b2*u[d+2] + b3*u[d+3] + b4*u[d+4]
        y[0] = y[0] + Ps
        u[0] = M + Pe
        #x[0] = T+1
        y_flip = np.flip(y) 
    elif(modo == 1):
        d = math.floor(Teta_prima1/T)            #Retraso
        teta1 = Teta_prima1 - (d*T)  
        m1 = 1 - (teta1/T)   
                    
        a1 = math.exp(-T/Tau1)                      
        a2 = 0                      
        a3 = 0                       
        a4 = 0                      
        
        b0 = 0                      
        b1 = K1*(1 - (math.exp((-m1*T)/(Tau1))))                     
        b2 = K1*((math.exp((-m1*T)/(Tau1))) - math.exp(-T/Tau1))                       
        b3 = 0                       
        b4 = 0
        
        y[0] = a1*y[1] + a2*y[2] + a3*y[3] + a4*y[4] + b0*u[d] + b1*u[d+1] + b2*u[d+2] + b3*u[d+3] + b4*u[d+4]
        y[0] = y[0] + Ps
        u[0] = M + Pe
        #x[0] = T+1
        y_flip = np.flip(y)
    elif(modo == 2):
        
        if (Zeta < 0) or (Zeta >= 1):
            lerror.grid(row=14, column=2)
        else:
            lerror.grid_forget()
            
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
        
        y[0] = a1*y[1] + a2*y[2] + a3*y[3] + a4*y[4] + b0*u[d] + b1*u[d+1] + b2*u[d+2] + b3*u[d+3] + b4*u[d+4]
        y[0] = y[0] + Ps
        u[0] = M + Pe
        #x[0] = T+1
        y_flip = np.flip(y)
    
    elif(modo == 3): 
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
        
        y[0] = a1*y[1] + a2*y[2] + a3*y[3] + a4*y[4] + b0*m[d] + b1*m[d+1] + b2*m[d+2] + b3*m[d+3] + b4*m[d+4]
        u[0] = M + Pe 
        m[0] = m[1] + beta0*(u[0] - y[0]) + beta1*(u[1] - y[1]) + beta2*(u[2] - y[2])
        y[0] = y[0] + Ps
        y_flip = np.flip(y)
        m_flip = np.flip(m)  
        
    # Add x and y to lists
    xs.append(x)
    ys.append(y[0])

    y = np.roll(y,1)
    u = np.roll(u,1)
    m = np.roll(m,1) 
    

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Modelo de la planta')
    plt.grid()



def callback(*args):
        global M, Pe, Ps, a1, a2, a3, a4, b0, b1, b2, b3, b4, d, T, Teta_prima1, Tau1, K1, Wn, Zeta, Kc, Tau_i, Tau_d
        global y, x, u, m,  y_flip, ani, fig, func, modo
        
        try:
            M = float(e1.get())           #Magnitud de escalón 
        except:
            M = 0
        try: 
            Pe = float(e2.get())          #Magnitud ruido entrada 
        except:
            Pe = 0
        try: 
            Ps = float(e3.get())          #Magnitud ruido salida 
        except:
            Ps = 0
        try: 
            a1 = float(e4.get())           
        except:
            a1 = 0
        try: 
            a2 = float(e5.get())           
        except:
            a2 = 0
        try: 
            a3 = float(e6.get())           
        except:
            a3 = 0 
        try: 
            a4 = float(e7.get())           
        except:
            a4 = 0
        try: 
            Ps = float(e3.get())           
        except:
            Ps = 0                                          
   
        try: 
            b0 = float(e8.get())           
        except:
            b0 = 0
        try: 
            b1 = float(e9.get())           
        except:
            b1 = 0
        try: 
            b2 = float(e10.get())           
        except:
            b2 = 0 
        try: 
            b3 = float(e11.get())           
        except:
            b3 = 0
        try: 
            b4 = float(e12.get())           
        except:
            b4 = 0    

        try: 
            d = int(e13.get())           
        except:
            d = 0
        try: 
            T = float(e14.get())           
        except:
            T = 0 
        
        try: 
            K1 = float(k1.get())           
        except:
            K1 = 0
        try: 
            Teta_prima1 = float(teta_prima1.get())           
        except:
            Teta_prima1 = 0
        try: 
            Tau1 = float(tau1.get())           
        except:
            Tau1 = 0
        
            
        try: 
            Wn = float(wn.get())           
        except:
            Wn = 0
        try: 
            Zeta = float(zeta.get())           
        except:
            Zeta = 0
            
        try: 
            Kc = float(kc.get())           
        except:
            Kc = 0
        try: 
            Tau_i = float(tau_i.get())           
        except:
            Tau_i = 0
        try: 
            Tau_d = float(tau_d.get())           
        except:
            Tau_d = 0
            
        try: 
            modo = int(modo_entrada.get())           
        except:
            modo = 0
            
                              
#----------------------------------------
M = 0           #Magnitud de escalón 
Pe = 0          #Magnitud ruido entrada 
Ps = 0          #Magnitud ruido salida 
                                      # a's
a1 = 0                      
a2 = 0                      
a3 = 0                       
a4 = 0                       

                                      # b's
b0 = 0                      
b1 = 0                     
b2 = 0                      
b3 = 0                      
b4 = 0      
    
d = 0            #Retraso
T = 0          #Intervalo de Muestreo

modo = 0

zeta = 0
wn = 0
 
t_planta = tk.Label(root, 
		 text="Simulación de Planta",
		 fg = "black",
         bg="#ADD8E6",
		 font = "Verdana 20 bold italic",
         anchor = "center") 
 
t_planta.grid(row=0,column=0,pady=0,columnspan=4)
inputs_lista = []

v0 = tk.StringVar()
v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()
v5 = tk.StringVar()
v6 = tk.StringVar()
v7 = tk.StringVar()
v8 = tk.StringVar()
v9 = tk.StringVar()
v10 = tk.StringVar()
v11 = tk.StringVar()
v12 = tk.StringVar()
v13 = tk.StringVar()
v14 = tk.StringVar()
v15 = tk.StringVar()
v16 = tk.StringVar()
v17 = tk.StringVar()
v18 = tk.StringVar()

v19 = tk.StringVar()
v20 = tk.StringVar()
v21 = tk.StringVar()

vmodo = tk.StringVar()

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
#lmodo =Label(text="MODO", width=10)
lnum =Label(text="MODO: 0-ARX, 1-1er Orden, 2-2ndo Orden, 3-AUTO", width=50)

for x in range(7):
    inputs = Entry(root, textvariable = "v"+str(x))
    inputs_lista.append(inputs)
#0 1 2 3 4 5
for x in range(7): 
    inputs = Entry(root, textvariable = "v"+str(x+7))
    inputs_lista.append(inputs)

inputs_lista[0] = Entry(root, textvariable=v0) 
inputs_lista[1] = Entry(root, textvariable=v1)
inputs_lista[2] = Entry(root, textvariable=v2)
inputs_lista[3] = Entry(root, textvariable=v3)
inputs_lista[4] = Entry(root, textvariable=v4)
inputs_lista[5] = Entry(root, textvariable=v5)
inputs_lista[6] = Entry(root, textvariable=v6)
inputs_lista[7] = Entry(root, textvariable=v7)
inputs_lista[8] = Entry(root, textvariable=v8)
inputs_lista[9] = Entry(root, textvariable=v9)
inputs_lista[10] = Entry(root, textvariable=v10)
inputs_lista[11] = Entry(root, textvariable=v11)
inputs_lista[12] = Entry(root, textvariable=v12)
inputs_lista[13] = Entry(root, textvariable=v13) 
    
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

modo_entrada = Entry(root, textvariable=vmodo)
k1 = Entry(root, textvariable=v14)
tau1 = Entry(root, textvariable=v15)
teta_prima1 = Entry(root, textvariable=v16)
    
zeta = Entry(root, textvariable=v17)
wn = Entry(root, textvariable=v18)

kc = Entry(root, textvariable=v19)
tau_i = Entry(root, textvariable=v20)
tau_d = Entry(root, textvariable=v21)

for x in range(7):
    inputs_lista[x].grid(row=x+1, column=1, pady=10, padx=3)
    #0 1 2 3 4 5
for x in range(7): 
    inputs_lista[x+7].grid(row=x+1, column=8, pady=10, padx=3)

modo_entrada.grid(row=11, column=4)

k1.grid(row=9, column=1)
tau1.grid(row=10, column=1)
teta_prima1.grid(row=11, column=1)

zeta.grid(row=14, column=1)
wn.grid(row=15, column=1)

kc.grid(row=18, column=1)
tau_i.grid(row=19, column=1)
tau_d.grid(row=20, column=1)

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

l15.grid(row=9, column=0)
l16.grid(row=10, column=0)
l17.grid(row=11, column=0)

l20.grid(row=14, column=0)
l21.grid(row=15, column=0)

l22.grid(row=18, column=0)
l23.grid(row=19, column=0)
l24.grid(row=20, column=0)

#lmodo.grid(row=9, column=4)
lnum.grid(row=10, column=4)

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
k1.insert(0, "10") 
tau1.insert(0, "2.7")
teta_prima1.insert(0, "1.9")
zeta.insert(0, "0.1")
wn.insert(0, "1")
modo_entrada.insert(0, "0")
kc.insert(0, "1.3") 
tau_i.insert(0, "3.89")
tau_d.insert(0, "0.59")
    
modo = int(modo_entrada.get())

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
T = float(e14.get()) #Intervalo de Muestreo

Tau1 = float(tau1.get())          
Teta_prima1 = float(teta_prima1.get())            
K1 = float(k1.get()) 

Zeta = float(zeta.get())  
Wn = float(wn.get())   

Kc = float(kc.get())
Tau_i = float(tau_i.get())
Tau_d = float(tau_d.get())

ARRAY_SIZE = 100
y = np.zeros(ARRAY_SIZE)      #Lista valores de salida
y_interval = np.zeros(ARRAY_SIZE)
#x = np.zeros(ARRAY_SIZE)      #Lista de intervalos kT
u = np.zeros(ARRAY_SIZE)      #Lista valores de escalón entrada
m = np.zeros(ARRAY_SIZE)      #Lista valores de escalón entrada

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = [] 

#fig2 = Figure(figsize = (5, 5),
#                 dpi = 100) 
#canvas = FigureCanvasTkAgg(fig2, master=root)
#canvas.draw() 
#canvas.get_tk_widget().grid(row=8, column=1)
        
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=750)
plt.show()            
v0.trace_add("write", callback)  
v1.trace_add("write", callback)  
v2.trace_add("write", callback)  
v3.trace_add("write", callback)  
v4.trace_add("write", callback)  
v5.trace_add("write", callback)  
v6.trace_add("write", callback)  
v7.trace_add("write", callback)  
v8.trace_add("write", callback)  
v9.trace_add("write", callback)  
v10.trace_add("write", callback)  
v11.trace_add("write", callback)  
v12.trace_add("write", callback)  
v13.trace_add("write", callback)  
v14.trace_add("write", callback)  
v15.trace_add("write", callback)  
v16.trace_add("write", callback)  
v17.trace_add("write", callback) 
v18.trace_add("write", callback) 

v19.trace_add("write", callback)  
v20.trace_add("write", callback) 
v21.trace_add("write", callback) 
vmodo.trace_add("write", callback) 
root.mainloop()
    

