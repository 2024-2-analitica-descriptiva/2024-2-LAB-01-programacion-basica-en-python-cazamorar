"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    month_counts = {}
    

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la fecha de la tercera columna
            date = columns[2]
            # Extraer el mes de la fecha (YYYY-MM-DD)
            month = date.split('-')[1]
            # Contar la ocurrencia del mes
            if month in month_counts:
                month_counts[month] += 1
            else:
                month_counts[month] = 1
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por el mes
    result = sorted(month_counts.items())
    
    return result


#print(pregunta_04())
