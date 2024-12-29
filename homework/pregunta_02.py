"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    # Inicializar un diccionario para contar las ocurrencias de cada letra
    counts = {}
    
    # Abrir el archivo y leer línea por línea
    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la primera columna (la letra)
            letter = columns[0]
            # Contar la ocurrencia de la letra
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    result = sorted(counts.items())
    
    return result

#print(pregunta_02())
