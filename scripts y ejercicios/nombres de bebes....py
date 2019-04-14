#!/usr/bin/env python
# coding: utf-8

import argparse

def parsear_argumentos_avanzados():
    parser = argparse.ArgumentParser(
        description = """Este script calcula el número de años desde 2002 que el nombre indicado fue de los más populares en España."""
    )
    parser.add_argument("nombre", help = """ Nombre que queremos analizar.""")
    argumentos = parser.parse_args()
    return argumentos

def cargar_archivo(year):
    with open("D:/datasets/Curso_Mauel_Garrido/data_babys/nomnac{}.csv".format(year)) as fname:
        lineas = fname.readlines()
    nombres_masculinos = []
    nombres_femeninos = []
    for linea_nombres in lineas:
        nombres = linea_nombres.strip("\n").split(",")
        assert len(nombres) == 2
        nombres_masculinos.append(nombres[0])
        nombres_femeninos.append(nombres[1])
    return nombres_masculinos + nombres_femeninos

def calcular_popularidad_por_nombre(nombre_busqueda):
    years_nombre = 0
    for year in  ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]:
        nombres_year = cargar_archivo(year)
        if nombre_busqueda in nombres_year:
            years_nombre += 1
    return years_nombre

def main(argumentos):
    """
    Aquí ponemos la funcionalidad principal de nuestro script.
    """
    nombre = argumentos.nombre.upper()
    years_nombres = calcular_popularidad_por_nombre(nombre)
    print("El nombre {} está entre los mas populares en {} años".format(nombre, years_nombres))

if __name__ == "__main__":
    # Este código solo se ejecutará si ejecutamos este script directamente.
    argumentos = parsear_argumentos_avanzados()
    main(argumentos)



