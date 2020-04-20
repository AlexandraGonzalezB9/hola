
import scipy.io as sio;
import matplotlib.pyplot as plt;
import numpy as np;
import scipy.signal as signal;
import math;

mat_contents = sio.loadmat('signals.mat');
print("Los campos cargados son: " + str(mat_contents.keys()));

data = np.squeeze(mat_contents['ECG_asRecording']);
print("Variable python: " + str(type(data)));
print("Tipo de variable cargada: " + str(data.dtype));
print("Dimensiones de los datos cargados: " + str(data.shape));
print("Numero de dimensiones: " + str(data.ndim));
print("Tamanio: " + str(data.size));
print("Tamanio en memoria (bytes): " + str(data.nbytes));

data1 = np.squeeze(mat_contents['ECG_filtered']);
print("Variable python: " + str(type(data1)));
print("Tipo de variable cargada: " + str(data1.dtype));
print("Dimensiones de los datos cargados: " + str(data1.shape));
print("Numero de dimensiones: " + str(data1.ndim));
print("Tamanio: " + str(data1.size));
print("Tamanio en memoria (bytes): " + str(data1.nbytes));

data2 = np.squeeze(mat_contents['EMG_asRecording1']);
print("Variable python: " + str(type(data2)));
print("Tipo de variable cargada: " + str(data2.dtype));
print("Dimensiones de los datos cargados: " + str(data2.shape));
print("Numero de dimensiones: " + str(data2.ndim));
print("Tamanio: " + str(data.size));
print("Tamanio en memoria (bytes): " + str(data2.nbytes));

data3 = np.squeeze(mat_contents['EMG_asRecording2']);
print("Variable python: " + str(type(data3)));
print("Tipo de variable cargada: " + str(data3.dtype));
print("Dimensiones de los datos cargados: " + str(data3.shape));
print("Numero de dimensiones: " + str(data3.ndim));
print("Tamanio: " + str(data3.size));
print("Tamanio en memoria (bytes): " + str(data3.nbytes));

data4 = np.squeeze(mat_contents['EMG_filtered1']);
print("Variable python: " + str(type(data4)));
print("Tipo de variable cargada: " + str(data4.dtype));
print("Dimensiones de los datos cargados: " + str(data4.shape));
print("Numero de dimensiones: " + str(data4.ndim));
print("Tamanio: " + str(data4.size));
print("Tamanio en memoria (bytes): " + str(data4.nbytes));

data5 = np.squeeze(mat_contents['EMG_filtered2']);
print("Variable python: " + str(type(data5)));
print("Tipo de variable cargada: " + str(data5.dtype));
print("Dimensiones de los datos cargados: " + str(data5.shape));
print("Numero de dimensiones: " + str(data5.ndim));
print("Tamanio: " + str(data5.size));
print("Tamanio en memoria (bytes): " + str(data5.nbytes));

# 5,1
def rms(x):
    a =np.zeros(len(x))
    for i in range(0,len(x)):
        a[i] = (x[i]**(2))
        b = np.sum(a)
        c = (1/len(x))*b;
        rms = c**(1/2);
    return rms

# 5,2
#5,2,a
N = 30720
t = np.arange(0,(N/1024),(1/1026));
print(t)

#5,2,b
plt.subplot(2,1,1)
plt.plot(t,data)
plt.subplot(2,1,2)
plt.plot(t,data1)
plt.show()

#5,2,c
plt.plot(t[0:840], data[0:840])
plt.show()

sumatoria = np.sum(data[0:840])
totaldatos = (len(data[0:840]))
promedio_data = sumatoria/totaldatos
print('Promedio Señal = ', promedio_data)

rms_data = rms(data)
print('Valor RMS señal =', rms_data )

varianza_data = np.var(data[0:840])
print('Varianza Señal = ', varianza_data)

desviacion_data = np.std(data[0:840])
print('Desviación estandar Señal = ', desviacion_data)

#5,2,d
plt.plot(t[0:840], data1[0:840])
plt.show()

sumatoria1 = np.sum(data1[0:840])
totaldatos1 = (len(data1[0:840]))
promedio_data1 = sumatoria1/totaldatos1
print('Promedio Señal Filtrada = ', promedio_data1)

rms_data1 = rms(data1)
print('Valor RMS Señal filtrada =', rms_data1 )

varianza_data1 = np.var(data1[0:840])
print('Varianza Señal Filtrada = ', varianza_data1)

desviacion_data1 = np.std(data1[0:840])
print('Desviación estandar Señal Filtrada = ', desviacion_data1)

#5,2,e
tiempo_inicial = 0
tiempo_final = 840
data_filtrada = data1[0:840]

for i in np.arange(15):
    tiempo = np.arange(tiempo_inicial,tiempo_final)
    plt.figure()
    plt.plot(tiempo, data_filtrada) 
    plt.show()
    
    varianza_data1 = np.var(data_filtrada)
    print('Varianza = ', varianza_data1)
    desviacion_data1 = np.std(data_filtrada)
    print('Desviacion Estandar = ', desviacion_data1)
    i = i + 1
    tiempo_inicial = tiempo_final + 1
    tiempo_final = tiempo_final + 840
    data_filtrada = data1[tiempo_inicial:tiempo_final]
    
#6.a
M = 30721
t1 = np.arange(0,(M/1024),(1/1024));
print(t1)

#tseñal2 = np.arange(0,(M/1024),(1/1024));
#print(tseñal2)
#
#tseñalfiltrada1 = np.arange(0,(M/1024),(1/1024));
#print(tseñalfiltrada1)
#
#tseñalfiltrada2 = np.arange(0,(M/1024),(1/1024));
#print(tseñalfiltrada2)

#6,b musculo 1
plt.subplot(2,1,1)
plt.plot(t1,data2)
plt.subplot(2,1,2)
plt.plot(t1,data4,'y')
plt.show()

#musculo 2
plt.subplot(2,1,1)
plt.plot(t1,data3,'g')
plt.subplot(2,1,2)
plt.plot(t1,data5,'r')
plt.show()

#6,c 
## musculo 1
plt.plot(t1[0:3070], data4[0:3070])
plt.show()

sumatoria_musculo1 = np.sum(data4[0:3070])
totaldatos_musculo1 = (len(data4[0:3070]))
promedio_data_musculo1 = sumatoria_musculo1/totaldatos_musculo1
print('Promedio Señal Biceps= ', promedio_data_musculo1)

rms_musculo1=rms(data4)
print('Valor RMS Biceps =', rms_musculo1)

varianza_data_musculo1 = np.var(data4[0:3070])
print('Varianza Señal Biceps= ', varianza_data_musculo1)

desviacion_data_musculo1 = np.std(data4[0:3070])
print('Desviación estandar Señal Biceps = ', desviacion_data_musculo1)

#musculo 2 
plt.plot(t1[0:3235], data5[0:3235])
plt.show()

sumatoria_musculo2 = np.sum(data5[0:3235])
totaldatos_musculo2 = (len(data5[0:3235]))
promedio_data_musculo2 = sumatoria_musculo2/totaldatos_musculo2
print('Promedio Señal Triceps= ', promedio_data_musculo2)

rms_musculo2=rms(data5)
print('Valor RMS Triceps =', rms_musculo2)

varianza_data_musculo2 = np.var(data5[0:3235])
print('Varianza Señal Triceps= ', varianza_data_musculo2)

desviacion_data_musculo2 = np.std(data5[0:3235])
print('Desviación estandar Señal Triceps = ', desviacion_data_musculo2)

##6.d
#musculo1
tiempo_inicial_musculo1 = 0
tiempo_final_musculo1 = 3070
data_musculo1 = data4[0:3070]

for i in np.arange(10):
    tiempo_musculo1 = np.arange(tiempo_inicial_musculo1,tiempo_final_musculo1)
    #plt.subplot(15,1,i+1)
    plt.figure()
    plt.plot(tiempo_musculo1, data_musculo1) 
   
    plt.show()
    varianza_data4 = np.var(data_musculo1)
    print('Varianza Bicepss = ', varianza_data4)
    desviacion_data4 = np.std(data_musculo1)
    print('Desviacion Estandar Biceps = ', desviacion_data4)
    i = i + 1
    tiempo_inicial_musculo1 = tiempo_final_musculo1 +1
    tiempo_final_musculo1  = tiempo_final_musculo1 + 3070
    data_musculo1 = data4[tiempo_inicial_musculo1:tiempo_final_musculo1]

#musculo 2
tiempo_inicial_musculo2 = 0
tiempo_final_musculo2 = 3235
data_musculo2 = data5[0:3235]

for i in np.arange(9):
    tiempo_musculo2  = np.arange(tiempo_inicial_musculo2,tiempo_final_musculo2)
    plt.figure()
    plt.plot(tiempo_musculo2, data_musculo2) 
   
    plt.show()
    varianza_data5 = np.var(data_musculo2)
    print('Varianza Triceps = ', varianza_data5)
    desviacion_data5 = np.std(data_musculo2)
    print('Desviacion Estandar triceps = ', desviacion_data5)
    i = i + 1
    tiempo_inicial_musculo2 = tiempo_final_musculo2 + 1
    tiempo_final_musculo2 = tiempo_final_musculo2 + 3235
    data_musculo2 = data5[tiempo_inicial_musculo2:tiempo_final_musculo2]     










        
        
    
