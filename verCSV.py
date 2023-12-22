import csv
import os
import subprocess


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

    
def archivoCSV():
    tests=[]
    archivos=os.listdir()
    for archivo in archivos:
        if '.csv' in archivo:
           tests.append(archivo)
    return tests

def archivoJMX():
    tests=[]
    archivos=os.listdir()
    for archivo in archivos:
        if '.jmx' in archivo:
           tests.append(archivo)
    return tests


def obtenerDatosCMD(archivo):
    with open (archivo,'r') as file:
        datos=[]
        prueba={}
        csv_reader=csv.reader(file)
        cont=1
        for item in csv_reader:
            if cont==1:
                cont+=1
            else:
                datos.append(item)
        for timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bites,sentBytes,grpThreads,allThreads,url,latency,idleTime,connect in datos:
            if label in prueba:
                prueba[label][0].append(timeStamp)
                prueba[label][1].append(elapsed)
                prueba[label][2].append(responseCode)
                prueba[label][3].append(responseMessage)
                prueba[label][4].append(dataType)
                prueba[label][5].append(success)
                prueba[label][6].append(failureMessage)
                prueba[label][7].append(bites)
                prueba[label][8].append(sentBytes)
                prueba[label][9].append(grpThreads)
                prueba[label][10].append(allThreads)
                prueba[label][12].append(latency)
                prueba[label][13].append(idleTime)
                prueba[label][14].append(connect)
            else:
                prueba[label]=[[timeStamp],[elapsed],[responseCode],[responseMessage],[dataType],[success],[failureMessage],[bites],[sentBytes],[grpThreads],[allThreads],[url],[latency],[idleTime],[connect]]      
          
        
        for item in prueba:
            print('\33[3;32m'+item+'\33[0m')
            print()
            sum=0
            print('\33[4m'+'Latency values:'+'\033[0m ',end='')
            for num in prueba[item][12]:
                print(num, end=' ')
                sum+=float(num)
            print()
            print()
            print('\33[4m'+'Latency average:'+'\033[0m ',sum/len(prueba[item][12]))
            print()
            sum=0
            print('\33[4m'+'Elapsed values:'+'\033[0m ', end='')
            for num in prueba[item][1]:
                print(num, end=' ')
                sum+=float(num)
            print()
            print()
            print('\33[4m'+'Elapsed average:'+'\033[0m ',sum/len(prueba[item][1]))
            
            input()
        input()

archivos=archivoJMX()          
print(archivos)
ejecuciones(archivos)

archivos=archivoCSV()
for archivo in archivos:
    print('\33[2;31m'+archivo+'\033[0m')
    print()
    obtenerDatosCMD(archivo)       
    cls()