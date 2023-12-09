import csv
import os

def cls():
    if  os.name in ('nt','dos'):
        os.system('cls')
    else: 
        os.system('clear')
        

archivos=os.listdir()

diccionario_archivo={}

for archivo in archivos:
    if '.csv' in archivo:
        
        diccionario_archivo[archivo]=[]
    
        with open (archivo, 'r') as file:
            
            diccionario_pruebas={}
            
            csv_reader = csv.reader(file)
            
            contador_rows=0
            for row in csv_reader:
                cantDatos=len(row)
                if contador_rows==0:
                    nombres_lista=row
                    for item in nombres_lista:
                        diccionario_pruebas[item]=[]
                         
                    contador_rows+=1         
                else:
                    cont=0
                    for item in diccionario_pruebas:
                        diccionario_pruebas[item].append(row[cont])
                        cont+=1
                

            
            diccionario_archivo[archivo].append(diccionario_pruebas)            

for item in diccionario_archivo:
    for it in diccionario_archivo[item]:
            
        contIt=len(it['Label'])
        
        for i in range(0,contIt-1,1):
            print('\033[1m','\033[4m',item.replace('.csv',''),'\033[0m')
            print()
            print('Label: '+it['Label'][i])
            print('Samples: '+it['# Samples'][i])
            print('Promedio: '+it['Average'][i])
            print('Maximo: '+it['Max'][i])
            if int(it['Max'][i])>=6000:
                print('\033[41m','Tiempo de espera maximo fuera de parametros aceptables','\033[0m')
            else:
                print('\033[42m','Tiempo de espera maximo aceptable','\033[0m')
            print()
            print('Error(%): '+it['Error %'][i])
            error=it['Error %'][i].replace('%','')
            if float(error)>=10:
                print('\033[41m','Cantidad de errores mayor a los parametros aceptables','\033[0m')
            else:
                print('\033[42m','Cantidad de errores dentro de los parametros aceptables','\033[0m')
            print()
            input('Enter para continuar')
            cls()
print('Gracias por utilizarme!!')
input('Enter para finalizar')