El script verCSV.py ejecuta los TC de JMeter que estan en el mismo directorio. 
Es necesario tener JMeter instalado (y por tanto JAVA) en el dispositivo asi como python.
El script primero pedira la ruta absoluta al ejecutable de JMeter (el que se encuentra en la carpeta \apache-jmeter-5.6.2\bin. Ejemplo: C:\apache-jmeter-5.6.2\bin).
Luego ejecuta todos los archivos .jmx que esten en la carpeta (TCs de JMeter) y crea sus correspondientes .csv en la misma con el mismo nombre de archivo.
Una vez creados los .csv el script los lee y toma todos los datos agrupandolos por TC y por pagina visitada en cada TC y los muestra por consola.
Hasta el momento a modo de prueba solo muestra el nombre del TC, pagina, Latency, Latency average, Elapsed y Elapsed Average. No obstate toma todos los datos como para
poder hacer lo que se requiera con ellos dentro del script.


