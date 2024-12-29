"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    counts = {}

    with open('files\\input\\data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            # Obtener la columna 5 y dividirla en claves y valores
            if len(columns) > 4:  # Asegurarse de que la columna 5 existe
                entries = columns[4].split(',')
                for entry in entries:
                    key = entry.split(':')[0]
                    # Contar cada clave
                    if key in counts:
                        counts[key] += 1
                    else:
                        counts[key] = 1

    result = [key for key in sorted(counts.items())]
    result = dict(result)
    return result


#print(pregunta_09())