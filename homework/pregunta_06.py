"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    value_ranges = {}
    
    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la quinta columna (el diccionario codificado)
            encoded_dict = columns[4]
            # Separar las entradas del diccionario
            entries = encoded_dict.split(',')
            for entry in entries:
                key, value = entry.split(':')
                value = int(value)
                if key in value_ranges:
                    value_ranges[key]['min'] = min(value_ranges[key]['min'], value)
                    value_ranges[key]['max'] = max(value_ranges[key]['max'], value)
                else:
                    value_ranges[key] = {'min': value, 'max': value}
    
    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la clave
    result = [(key, values['min'], values['max']) for key, values in sorted(value_ranges.items())]
    
    return result

#print(pregunta_06())

