"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    # Inicializar un diccionario para sumar los valores de la segunda columna por cada letra
    sums = {}

    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la primera columna (la letra)
            letter = columns[0]
            # Obtener el valor de la segunda columna y convertirlo a entero
            value = int(columns[1])
            # Sumar el valor en el diccionario
            if letter in sums:
                sums[letter] += value
            else:
                sums[letter] = value
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    result = sorted(sums.items())
    
    return result


#print(pregunta_03())
