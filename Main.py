""" Documents
    Nombre: Cristóbal Osses Obreque

Elementos evaluados:
    Lectura de archivos (txt o csv)
    Estructuras de almacenamiento
    Graficos de la información otorgada, mínimo 2 gráficos
"""

#IMPORT's
import numpy as np
import os
import time
from functions import mensajes


""" FUNCTIONS

"""
#MENU
def menu():
    temp = 1
    while temp != "0":
        os.system("cls")
        print("MENU")
        print("0|Finalizar")
        print("1|Agregar un trabajador")
        print("2|Agregar una sucursal")
        print("3|Agregar un producto")
        print("4|Actualizar un trabajador")
        print("5|Actualizar una sucursal")
        print("6|Actualizar un producto")
        print("7|Actualiar stock")
        temp = input("Inserte respuesta: ")


        if temp == "1":
            addTrabajador()
        elif temp == "2":
            addSucursal()
        elif temp == "3":
            addProducto()
        elif temp == "4":
            setProducto()
        elif temp == "5":
            setSucursal()
        elif temp == "6":
            setProducto()
        elif temp == "7":
            setStock()
        else:
            print("Respuesta invalida, vuelva a intentarlo")
            time.sleep(1)
            
    return temp

#LECTURA DE ARCHIVOS    
def lectura():
    mensajes.lecturaArchivoInicio()

    #Trabajdores
    archivo = open("./recursos/trabajadores.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        for i in partes:
            trabajador.append(i.upper())
        print(trabajador)
        trabajadores.append(trabajador.copy())
        trabajador.clear()
        linea = archivo.readline().strip()
    
    print(trabajadores)
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

#AGREGAR TRABAJADOR
def addTrabajador():
    os.system("cls")
    print("AGREGAR TRABAJADOR:")
    time.sleep(1)

#AGREGAR SUCURSAL
def addSucursal():
    os.system("cls")
    print("AGREGAR SUCURSAL:")

#AGREGAR PRODUCTO
def addProducto():
    os.system("cls")
    print("AGREGAR PRODUCTO:")

#ACTUALIZAR TRABAJADOR
def setTrabajador():
    os.system("cls")
    print("ACTUALIZAR TRABAJADOR:")

#ACTUALIZAR SUCURSAL
def setSucursal():
    os.system("cls")
    print("ACTUALIZAR SUCURSAL:")

#ACTUALIZAR PRODUCTO
def setProducto():
    os.system("cls")
    print("ACTUALIZAR PRODUCTO:")

#ACTUALIZAR STOCK
def setStock():
    os.system("cls")
    print("ACTUALIZAR STOCK:")

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

resp = menu()




escritura()
mensajes.despedida()