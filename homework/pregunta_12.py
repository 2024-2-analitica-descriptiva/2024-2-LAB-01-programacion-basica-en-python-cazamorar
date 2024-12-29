"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    # Inicializar un diccionario para almacenar la suma de los valores de la columna 5 por letra en la columna 1
    sums = {}

    with open('data.csv', 'r') as file:
        for line in file:
            # Separar la línea por tabulación para obtener las columnas
            columns = line.strip().split('\t')
            if len(columns) > 4:
                letter = columns[0]
                # Dividir la columna 5 en entradas
                entries = columns[4].split(',')
                # Sumar los valores en la columna 5
                total_sum = sum(int(entry.split(':')[1]) for entry in entries)
                
                # Sumar al total acumulado para la letra correspondiente
                if letter in sums:
                    sums[letter] += total_sum
                else:
                    sums[letter] = total_sum
    result = [letter for letter in sorted(sums.items())]
    result = dict(result)
    return result


#print(pregunta_12())
