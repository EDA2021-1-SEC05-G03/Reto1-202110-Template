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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def initcatalog (estructuradedatos):
    if estructuradedatos == "ARRAY_LIST":
      r={"videos": lt.newList('ARRAY_LIST')}
    elif estructuradedatos == "LINKED_LIST":
      r={"videos": lt.newList('LINKED_LIST')}
    return r
def addvideo (catalog, video):
    lt.addLast(catalog["videos"],video)
def initcategory (estructuradedatos):
    if estructuradedatos == "ARRAY_LIST":
       r={"categorias": lt.newList('ARRAY_LIST')}
    elif estructuradedatos == "LINKED_LIST":
       r={"categorias": lt.newList('LINKED_LIST')}
    return r
def addcategory (category,categorias):
    lt.addLast(category["categorias"],categorias)
def compareviews(video1, video2):
    return (float(video1['views']) < float(video2['views']))
def sortvideos(catalog, Numerodeelementos,algoritmo):
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

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento