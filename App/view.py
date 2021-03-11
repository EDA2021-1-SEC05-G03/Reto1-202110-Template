"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
import time
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def printResults(catalog, sample=1):
     size = lt.size(catalog["videos"])
     if(size > sample):
         print("El primer ", sample, "video es:")
         i = 1
         while i <= sample:
             video = lt.getElement(catalog['videos'], i)
             print('Titulo: ' + video['title'] + ' Titulo del canal: ' + 
                 video['channel_title'] + '  Fecha de tendencia: ' + video['trending_date']+ " pais: "+ video["country"] + " visitas: " + video["views"]+ " likes: " + video["likes"]+ " Dislikes: "+ video["dislikes"])
             i+=1
def printreq1(req1):
    elements = req1['elements']
    for video in elements:
        print('  Fecha de tendencia: ' + video['trending_date']+'Titulo: ' + video['title'] + ' Titulo del canal: ' + video['channel_title'] +  " Hora de publicacion: "+ video["publish_time"] + " visitas: " + video["views"]+ " likes: " + video["likes"]+ " Dislikes: "+ video["dislikes"])
             

def printreq2(req2):
    print('Titulo: ' + req2[0]['title'] + ' Titulo del canal: ' + req2[0]['channel_title'] +  " pais: "+ req2[0]["country"] +" Dias: " + str(req2[1]))

def printreq3(req3):
    print('Titulo: ' + req3[0]['title'] + ' Titulo del canal: ' + req3[0]['channel_title'] +  " id de la categoria: "+ req3[0]["category_id"] +" Dias: " + str(req3[1]))

def printreq4(req4):
    elements = req4['elements']
    for v in elements:
        print('Titulo: ' + v['title'] + ' Titulo del canal: ' + v['channel_title'] +  " Tiempo de publicacion: "+ v["publish_time"] +" likes: " + v["likes"]+ " Dislikes: "+ v["dislikes"]+ " tags " + v["tags"])



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")   
    print("2- Videos por categorias y páis")
    print("3- Encontrar video tendencia por país")
    print("4- Video tendencia por categorias")
    print("5- Videos por más likes")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        estructuradedatos="ARRAY_LIST"
        print("Cargando información de los archivos ....")
        catalog = controller.initcatalog(estructuradedatos)
        controller.cargardatos(catalog)
        print ("Se cargó la información del catalogo")
        print ("Se cargaron "+ str(lt.size(catalog["videos"])) +" videos")
        controller.cargardatoss(catalog)
        print ("Se cargó la información del category id")
        print ("Se cargaron "+ str(lt.size(catalog["category"])) +" categorias")
        print(catalog["category"])
        printResults(catalog,1)
    
    elif int(inputs[0]) == 2:
        Nombrecategoria=input(" Digite el nombre de la categoria ")
        Pais=input(" Digite el pais ")
        n=int(input(" Digite el numero de videos que quiere listar "))
        req1=controller.requerimiento1(Nombrecategoria,Pais,n,catalog)
        printreq1(req1)
        print("Se ejecuto requerimiento 1")
   
    elif int(inputs[0]) == 3:
        Pais=input(" Digite el pais ")
        req2=controller.requerimiento2(catalog,Pais)
        printreq2(req2)
        print ("Se ejecuto requerimiento 2")
   
    elif int(inputs[0]) == 4:
        nombrecategoria=input(" Digite el nombre de la categoria ")
        req3=controller.requerimiento3(catalog,nombrecategoria)
        printreq3(req3)
        print ("Se ejecuto requerimiento 3")
    
    elif int(inputs[0]) == 5:
        tagsbuscar=str(input("Digite el nombre del tag: "))
        Pais=str(input("Digite el pais: "))
        n=int(input("Digite el numero de videos que quiere listar: "))
        req4=controller.requerimiento4(catalog, Pais, n, tagsbuscar)
        printreq4(req4)
        print ("Se ejecuto requerimiento 4")

    else:
        sys.exit(0)
sys.exit(0)


