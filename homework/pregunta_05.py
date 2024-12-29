"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    min_max_values = {}
    
    # Abrir el archivo y leer línea por línea
    with open('files\input\data.csv', 'r') as file:
   
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la primera columna (letra) y la segunda columna (valor)
            letter = columns[0]
            value = int(columns[1])
            # Actualizar los valores máximo y mínimo para la letra
            if letter in min_max_values:
                min_max_values[letter]['max'] = max(min_max_values[letter]['max'], value)
                min_max_values[letter]['min'] = min(min_max_values[letter]['min'], value)
            else:
                min_max_values[letter] = {'max': value, 'min': value}
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    result = [(letter, values['max'], values['min']) for letter, values in sorted(min_max_values.items())]
    
    return result

#print(pregunta_05())