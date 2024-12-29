"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    # Inicializar un diccionario para almacenar las listas de letras por valor de la columna 2
    associations = {}
    
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener el valor de la columna 2 y la letra de la columna 1
            value = int(columns[1])
            letter = columns[0]
            # Agregar la letra a la lista correspondiente en el diccionario
            if value in associations:
                associations[value].append(letter)
            else:
                associations[value] = [letter]
    
    # Convertir el diccionario en una lista de tuplas y ordenar por el valor de la columna 2
    result = sorted(associations.items())
    
    return result

#print(pregunta_07())
