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
from DISClib.Algorithms.Sorting import quicksort as qu
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.ADT import list as lt
from statistics import mode
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog(estructuradedatos):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category': None,
               'tags': None,
               'video_tags': None}

    catalog['videos'] = lt.newList(estructuradedatos, cmpfunction = comparevideosid)
    catalog['category'] = lt.newList(estructuradedatos, cmpfunction = comparecategoryid)

    return catalog

def addvideo (catalog, video):
    lt.addLast(catalog["videos"],video)
    tags=video['tags'].split('|')

def addcategory (catalog,categorias):
    lt.addLast(catalog["category"],categorias)

def comparevideosid(video1, video2):
    return (video1['video_id']) <= (video2['video_id'])

def comparecategoryid(video1, video2):
    return (float(video1['category_id']) < float(video2['category_id']))

def compareviews(video1, video2):
    return (float(video1['views']) > float(video2['views']))




def idcategoria(catalog,Nombrecategoria):
    categorias=""
    for cate in lt.iterator(catalog["category"]):
        if cate["name"]==Nombrecategoria:
            categorias=cate["id"]
    return categorias

def filtros(catalog,Pais,categorias):
    lista_filtros=lt.newList("ARRAY_LIST")
    for video in lt.iterator(catalog['videos']):
        if video["country"]==Pais and video["category_id"]==categorias :
            lt.addLast(lista_filtros,video)     
    return lista_filtros

def sortvideos(lista_filtros,n):
    qu.sort(lista_filtros, compareviews)
    sub_list = lt.subList(lista_filtros,1,n)
    return sub_list






def sortvideosid(lst, size):
    sub_list = lt.subList(lst, 0, size)
    sub_list = sub_list.copy()
    sorted_list = qu.sort(sub_list, comparevideosid)
    return sorted_list

def videospaises(catalog, Pais):
    lista_paises=lt.newList("ARRAY_LIST")
    for video in lt.iterator(catalog['videos']):
        if video["country"]==Pais :
            lt.addLast(lista_paises,video)  
    videos = sortvideosid(lista_paises, lt.size(lista_paises))
    return videos

def masrepetido(videos):
    i=0
    contador=0
    videoconmasrep=0
    nombre=""
    while i < lt.size(videos):
        video1 =lt.getElement(videos,i)
        video2 =lt.getElement(videos,i+1)
        if video1["video_id"] == video2["video_id"]:
            contador+= 1
        else:
            if contador > videoconmasrep:
               videoconmasrep = contador
               nombre=lt.getElement(videos,i)    
            contador =0
        i+=1
    return (nombre,videoconmasrep)







def sortvideosidcategory(lst, size):
    sub_list = lt.subList(lst, 0, size)
    sub_list = sub_list.copy()
    sorted_list = mg.sort(sub_list, comparecategoryid)
    return sorted_list

def videoscategoryname(catalog, categorias):
    lista_categorias=lt.newList("ARRAY_LIST")
    for video in lt.iterator(catalog['videos']):
        if video["category_id"]==categorias :
            lt.addLast(lista_categorias,video)  
    video = sortvideosidcategory(lista_categorias, lt.size(lista_categorias))
    return video

def masrepetido1(video):
    i=0
    contador=0
    videoconmasrep=0
    nombre=0
    while i < lt.size(video):
        video1 =lt.getElement(video,i)
        video2 =lt.getElement(video,i+1)
        if video1["category_id"] == video2["category_id"]:
           contador+= 1
        else:
            if contador > videoconmasrep:
               videoconmasrep = contador
               nombre=(lt.getElement(video,i))   
            contador =0
        i+=1
    return (nombre,videoconmasrep)
# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento