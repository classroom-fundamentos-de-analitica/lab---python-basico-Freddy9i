"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from csv import reader
from collections import Counter
from operator import itemgetter
datos = []

with open('data.csv', 'r') as archivo:
    datosAux = reader(archivo, delimiter="\t")
    for fila in datosAux:
        datos.append(fila)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    aux = [int(i[1]) for i in datos]
    return sum(aux)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    aux = [i[0] for i in datos]
    respuesta = Counter(aux).items()
    print(respuesta)
    respuesta = list(respuesta)
    respuesta.sort(key=itemgetter(0))
    return respuesta


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    resultado = {}
    for fila in datos:
        if resultado.get(fila[0]) == None:
            resultado[fila[0]] = int(fila[1])
        else:
            resultado[fila[0]] += int(fila[1])

    resultado = list(resultado.items())
    resultado.sort(key=itemgetter(0))
    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    resultado = {}
    for fila in datos:
        mes = fila[2][5:7]
        if resultado.get(mes) == None:
            resultado[mes] = 1
        else:
            resultado[mes] += 1

    resultado = list(resultado.items())
    resultado.sort(key=itemgetter(0))
    return resultado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letras = list(set([i[0] for i in datos]))
    letras = sorted(letras)
    listaAux = []

    for _ in range(len(letras)):
        listaAux.append([])

    for fila in datos:
        listaAux[ord(fila[0]) - ord('A')].append(int(fila[1]))

    respuesta = []
    for index, element in enumerate(listaAux):
        tupla = (letras[index], max(element), min(element))
        respuesta.append(tupla)

    return respuesta


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    auxDiccionario = {}
    for fila in datos:
        aux = fila[4].split(',')
        for i in aux:
            clave = i[0:3]
            valor = int(i[4:])
            if auxDiccionario.get(clave) == None:
                auxDiccionario[clave] = [valor]
            else:
                auxDiccionario[clave] += [valor]
    
    respuesta = []
    for clave, valor in auxDiccionario.items():
        respuesta.append((clave, min(valor), max(valor)))

    respuesta.sort(key=itemgetter(0))
    return respuesta


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    respuesta = {}
    for fila in datos:
        clave = int(fila[1])
        if respuesta.get(clave) == None:
            respuesta[clave] = [fila[0]]
        else:
            respuesta[clave] += [fila[0]]
    
    respuesta = list(respuesta.items())
    respuesta.sort(key=itemgetter(0))
    return respuesta


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    respuesta = {}
    for fila in datos:
        clave = int(fila[1])
        if respuesta.get(clave) == None:
            respuesta[clave] = [fila[0]]
        else:
            respuesta[clave] += [fila[0]]

    for clave in respuesta.keys():
        respuesta[clave] = sorted(list(set(respuesta[clave])))

    respuesta = list(respuesta.items())
    respuesta.sort(key=itemgetter(0))
    return respuesta


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    respuesta = {}
    for fila in datos:
        aux = fila[4].split(',')
        for i in aux:
            clave = i[0:3]
            valor = int(i[4:])
            if respuesta.get(clave) == None:
                respuesta[clave] = 1
            else:
                respuesta[clave] += 1

    return respuesta


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    respuesta = []
    for fila in datos:
        columna4 = fila[3].split(',')
        columna5 = fila[4].split(',')
        respuesta.append((fila[0], len(columna4), len(columna5)))

    return respuesta


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    respuesta = {}
    for fila in datos:
        letrasColumna4 = fila[3].split(',')
        for letra in letrasColumna4:
            if respuesta.get(letra) == None:
                respuesta[letra] = int(fila[1])
            else:
                respuesta[letra] += int(fila[1])
    return respuesta


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    respuesta = {}
    for fila in datos:
        columna5 = fila[4].split(',')
        sumaValores = sum([int(i[4:]) for i in columna5])

        clave = fila[0]
        if respuesta.get(clave) == None:
            respuesta[clave] = sumaValores
        else:
            respuesta[clave] += sumaValores

    return respuesta