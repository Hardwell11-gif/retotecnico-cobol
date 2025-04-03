# retotecnico-cobol
Introducción:

  El reto consiste en generar una aplicación de línea de comandos que lea un archivo csv y genere un reporte. Este archivo csv contiene transacciones bancarias (crédito y débito).
  El propósito, es que el reporte incluya el balance final (créditos suman y débitos restan), la transacción de mayor monto (ID de la transacción y el monto) y un conteo de transacciones (cuántos de crédito y          cuántos de débito).
  
Instrucciones de Ejecución:

  En primer lugar se importa el modulo CSV en python (para que se pueda leer y escribir archivos de este tipo). Esto se realiza con el siguiente comando: import csv 
  
Enfoque y Solución:

  En primer lugar, se crea un archivo CSV con el ejemplo que dan en el reto técnico. Como puede haber errores en el archivo se usa try, dentro de ello se definen las variables solicitadas y una función para leer el   archivo csv.
  En caso de que el archivo no se haya leído correctamente, se muestran mensajes de error como: "No se encontró el archivo" o "No se puede leer el archivo" el cual detalla el motivo.
  Si el archivo se pudo leer, se inicia un bucle con for con el cual se recorre el documento csv leyendo los montos y el tipo de transacción que es. Al leer estos datos, se asignan valores al balance final (si es     un crédito se suma el monto, y si es débito se resta el monto) y al conteo del tipo de transacción.
  Por otro lado, también se compara el monto con el monto mayor hasta el momento y se elige el monto mas alto.
  Luego, se imprimen los valores solicitados.

Estructura del Proyecto:

  Se tiene el archivo csv que se va a leer. Y, también se tiene el archivo .py donde se tiene el código con los comandos necesarios para brindar lo solicitado en el reto
  
