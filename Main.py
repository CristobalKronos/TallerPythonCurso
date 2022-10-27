""" Documents
    Nombre: Cristóbal Osses Obreque

    Enunciado:
        a

Elementos evaluados:
    Lectura de archivos (txt o csv)
    Estructuras de almacenamiento
    Graficos de la información otorgada, mínimo 2 gráficos
"""

#IMPORT's
import numpy as np
import os
from functions import mensajes

""" FUNCTIONS

"""
#MENU
def menu():
    print("Hola Mundo")
    print("0|Finalizar")
    temp = input("Inserte respuesta: ")
    return temp

#LECTURA DE ARCHIVOS    
def lectura():
    mensajes.lecturaArchivoInicio()
    archivo = open("./recursos/enunciado.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        parteA=partes[0].upper()
        parteB=partes[1].upper()
        print(parteA,parteB)
        linea = archivo.readline().strip()
    archivo.close()


    mensajes.lecturaArchivosFin()

#ESCRITURA DE ARCHIVOS
def escritura():
    mensajes.escrituraArchivosInicio() 


    mensajes.escrituraArchivosFin()

#GLOBAL VARIABLES
respWhile = 0



#MAIN
os.system("cls")
mensajes.saludo()
lectura()
while respWhile != "0":
    respWhile = menu()

escritura()
mensajes.despedida()