import csv

def leer_csv(archivo): #se define la función para leer el archivo CSV
    try:
        #se definen las variables solicitadas 
        balance_final = 0
        transaccion_mayor = {'id':None,'monto':0}
        conteo = {'Crédito':0,'Débito':0}

        #se abre y lee el archivo CSV 
        with open (archivo, mode ='r',encoding='utf-8') as archivo_abierto:
            lector = list(csv.DictReader(archivo_abierto)) #al usar list, aseguramos que el archivo siga abierto y evitamos un mensaje de error
        
        #se inicia con el bucle donde se lee el monto y tipo de transacción
        for fila in lector:
            monto = float(fila['monto'])
            tipo = fila['tipo']

            #se hacen las validaciones para poder asignar valores al monto. conteo de tipo de transacción y ubicar la transacción mayor
            if tipo == 'Crédito':
                balance_final += monto
                conteo['Crédito'] += 1
            elif tipo == 'Débito':
                balance_final -= monto
                conteo['Débito'] += 1
            if monto>transaccion_mayor['monto']:
                transaccion_mayor={'id':fila['id'],'monto':monto}
        
        #se imprimen los datos obtenidos
        print("Reporte de Transacciones: ")
        print("-----------------------")
        print(f"Balance Final: {balance_final:.2f}")
        print(f"Transacción de Mayor Monto: ID {transaccion_mayor['id']} - {transaccion_mayor['monto']:.2f}")
        print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

    #se asignan los mensajes de error.
    except FileNotFoundError:
        print("No se encontró el archivo")
    except Exception as e:
        print(f"No se puede leer el archivo: {e}")   

#se da datos del archivo a leer
test_file = "transacciones.csv"
leer_csv(test_file)

