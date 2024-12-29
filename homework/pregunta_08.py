"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    # Inicializar un diccionario para almacenar las letras únicas por valor de la columna 2
    associations = {}

    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener el valor de la columna 2 y las letras de la columna 1
            value = int(columns[1])
            letters = columns[0]
            # Agregar las letras a la lista correspondiente en el diccionario
            if value in associations:
                associations[value].update(letters)
            else:
                associations[value] = set(letters)
    
    # Convertir el diccionario en una lista de tuplas y ordenar por el valor de la columna 2
    result = [(key, sorted(list(letters))) for key, letters in sorted(associations.items())]
    
    return result

#print(pregunta_08())