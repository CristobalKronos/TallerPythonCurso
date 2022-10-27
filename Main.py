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
    temp = 1
    while temp != "0":
        print("\nMENU")
        print("0|Finalizar")
        temp = input("Inserte respuesta: ")
    return temp

#LECTURA DE ARCHIVOS    
def lectura():
    mensajes.lecturaArchivoInicio()

    #Trabajdores
    archivo = open("./recursos/trabajadores.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        parteA=partes[0].upper()
        parteB=partes[1].upper()
        parteC=partes[2].upper()
        parteD=partes[3].upper()
        print(parteA,parteB,parteC,parteD)
        linea = archivo.readline().strip()
    archivo.close()

    #Sucursales
    archivo = open("./recursos/sucursales.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        parteA=partes[0].upper()
        parteB=partes[1].upper()
        print(parteA,parteB)
        linea = archivo.readline().strip()
    archivo.close()

    #Productos
    archivo = open("./recursos/productos.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        parteA=partes[0].upper()
        parteB=partes[1].upper()
        print(parteA,parteB)
        linea = archivo.readline().strip()
    archivo.close()

    #Stock
    archivo = open("./recursos/stock.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        parteA=partes[0].upper()
        parteB=partes[1].upper()
        parteC=partes[2].upper()
        print(parteA,parteB,parteC)
        linea = archivo.readline().strip()
    archivo.close()


    mensajes.lecturaArchivosFin()

#ESCRITURA DE ARCHIVOS
def escritura():
    mensajes.escrituraArchivosInicio() 


    mensajes.escrituraArchivosFin()

#GLOBAL VARIABLES
trabajadores = []
trabajador = []
sucursales = []
sucursal = []
productos = []
producto = []
stock = []

#MAIN
os.system("cls")
mensajes.saludo()
lectura()

menu()

escritura()
mensajes.despedida()