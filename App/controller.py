"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt
import time
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def initcatalog (estructuradedatos):
    catalog = model.newCatalog(estructuradedatos)
    return catalog
def cargardatos(catalog):
    vfile = cf.data_dir + 'videos/videos-small.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for video in input_file:
        model.addvideo(catalog, video)
def cargardatoss(category):
    cfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(cfile, encoding='utf-8'))
    for categorias in input_file:
        model.addcategory(category,categorias)
def compareviews(video1, video2):
    return (float(video1['views']) < float(video2['views']))
def sortvideos(catalog, Numerodeelementos, algoritmo):
    sub_list = lt.subList(catalog['videos'], 0, Numerodeelementos)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if algoritmo ==  "shell":
       sorted_list = sa.sort(sub_list, compareviews)
    elif  algoritmo ==  "insertion":
      sorted_list = ins.sort(sub_list, compareviews)
    elif  algoritmo ==  "selection":
      sorted_list = sel.sort(sub_list, compareviews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
    
# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
