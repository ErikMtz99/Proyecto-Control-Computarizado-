import numpy as np
from scipy.ndimage.interpolation import shift
from matplotlib import pyplot as plt

ARRAY_SIZE = 20
T = 5                      #Tiempo de muestreo

y = np.zeros(ARRAY_SIZE)
u = np.zeros(ARRAY_SIZE)


M = 3                       #Magnitud de escalón
Pe = 2                      #Magnitud ruido entrada
Ps = 5                      #Magnitud ruido salida

a1 = 0.7
a2 = 0.2
a3 = 0
a4 = 0


b0 = 0
b1 = 0.1
b2 = 0.5
b3 = 0.3
b4 = 10

d = 5
 
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
    
