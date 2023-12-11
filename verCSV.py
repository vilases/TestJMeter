import csv
import os
import subprocess

class Test():
    label=[]
    samples=[]
    average=[]
    timeMin=[]
    timeMax=[]
    std_Dev=[]
    error=[]
    troughtput=[]
    recieved_KB=[]
    sent_KB=[]
    avg_Bytes=[]
    



def cls():
    if  os.name in ('nt','dos'):
        os.system('cls')
    else: 
        os.system('clear')

def pruebasJMX():
    tests=[]
    archivos=os.listdir()
    for archivo in archivos:
        if '.jmx' in archivo:
            tests.append(archivo)
    return tests



def ejecuciones(archivos):
    rutaPruebas=os.getcwd().replace('\\','/')
    print(rutaPruebas)
    rutaJMeter=input('Escriba la ruta donde esta el ejecutable de JMeter: ').replace('\\',"/")
    for archivo in archivos:
        os.system(rutaJMeter+'/jmeter -n -t '+rutaPruebas+'/'+archivo+' -l '+rutaPruebas+'/'+archivo.replace('.jmx','.csv'))        

def archivo():
    tests=[]
    archivos=os.listdir()
    for archivo in archivos:
        if '.csv' in archivo:
           tests.append(archivo)
    return tests

def obtenerDatos(archivo):
    
    with open (archivo, 'r') as file:
            
        pruebas=[]
        datos=[]
        csv_reader = csv.reader(file)
        test=Test()
        for item in csv_reader:
            datos.append(item)
            
        cont=len(datos)
        for i in range(1,cont,1):
            sep=datos[i][0].split(':')
            
            if len(sep)==2:
                test.label.append(sep[1])
            else:
                test.label.append(sep[0])
            test.samples.append(datos[i][1])
            test.average.append(datos[i][2])
            test.timeMin.append(datos[i][3])
            test.timeMax.append(datos[i][4])
            test.std_Dev.append(datos[i][5])
            test.error.append(datos[i][6])
            test.troughtput.append(datos[i][7])
            test.recieved_KB.append(datos[i][8])
            test.sent_KB.append(datos[i][9])
            test.avg_Bytes.append(datos[i][10])
           
    return test
            
            
             
     

def mostrarDatos(data):
    for item in data:
        cont=len(data[item].label)
        for i in range(0,cont,1):
            print()
            print('\033[94m','\033[2m',item,' :','\033[0m')
            print()
            print('\033[4m',data[item].label[i],'\033[0m')
            print()
            print('Muestras: '+data[item].samples[i])
            print('Promedio: '+data[item].average[i])
            print('Minimo: '+data[item].timeMin[i])
            print('Maximo: '+data[item].timeMax[i])
            
            if float(data[item].timeMax[i])>=tiempoMax*1000:
                print('\033[1;31m','Cantidad tiempo mayor al permitido','\033[0m')
            else:
                print('Tiempo dentro de los parametros normales')
            print('Std Dev: '+data[item].std_Dev[i])
            print('Error: '+data[item].error[i])
            
            if float(data[item].error[i].replace('%',''))>=errorMax:
                print('\033[1;31m','Cantidad de errores mayor al permitido','\033[0m')
            else:
                print('Errores dentro de los parametros normales')    
            input()
            cls()
                
# ejecuciones(pruebasJMX())       
     
errorMax=float(input('Ingrese cantidad de errores maximo permitido (%): '))
print()
tiempoMax=float(input('Ingrese tiempo de espera maximo (seg): '))
cls()

archivos=archivo()

diccionario_archivo={}

for archivo in archivos:
    diccionario_archivo[archivo]=[]
    diccionario_archivo[archivo]=obtenerDatos(archivo)            

mostrarDatos(diccionario_archivo)

print('Gracias por utilizarme!!')
input('Enter para finalizar')