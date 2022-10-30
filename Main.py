""" Documents
    Nombre: Cristóbal Osses Obreque

Elementos evaluados:
    Lectura de archivos (txt o csv)
    Estructuras de almacenamiento
    Graficos de la información otorgada, mínimo 2 gráficos
    colab.research.google.com
"""

#IMPORT's
from pickle import FALSE, TRUE
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
        #print("8|Graficar X")
        #print("9|Graficar Y")
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
        elif temp == "0":
            print("Cerrando el sistema.")
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
        for i in partes:
            sucursal.append(i.upper())
        print(sucursal)
        sucursales.append(sucursal.copy())
        sucursal.clear()
        linea = archivo.readline().strip()
    print(sucursales)
    archivo.close()

    #Productos
    archivo = open("./recursos/productos.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        for i in partes:
            producto.append(i.upper())
        print(producto)
        productos.append(producto.copy())
        producto.clear()
        linea = archivo.readline().strip()
    print(productos)
    archivo.close()

    #Stock
    archivo = open("./recursos/stock.txt","r")
    linea = archivo.readline().strip()
    while(linea != ""):
        partes=linea.split(",")
        for i in partes:
            stock.append(i.upper())
        print(stock)
        linea = archivo.readline().strip()
    archivo.close()


    mensajes.lecturaArchivosFin()

#ESCRITURA DE ARCHIVOS
def escritura():
    mensajes.escrituraArchivosInicio() 
    #Trabajadores
    #FIXME: Lanza error de fuera de rango
    archivo = open("./recursos/trabajadores.txt","a+")
    for i in trabajadores:
        aux = 0
        for j in i:
            archivo.write(j[aux] + ",")
            aux+=1
        archivo.write("\n")
    archivo.close()
    #Productos
    archivo = open("./recursos/productos.txt","a+")

    archivo.close()
    #Sucursales
    archivo = open("./recursos/sucursales.txt","a+")

    archivo.close()
    #Stock
    archivo = open("./recursos/stock.txt","a+")
    
    archivo.close()
    mensajes.escrituraArchivosFin()

#AGREGAR TRABAJADOR
def addTrabajador():
    os.system("cls")
    print("AGREGAR TRABAJADOR:")
    #Solicitar datos del trabajador
    auxNombre = input("Ingrese Nombre del trabajador: ")
    auxRut = input("Ingrese Rut del trabajador: ")
    auxCargo = input("Ingrese Cargo del trabajador: ")
    auxSueldo = input("Ingrese Sueldo del trabajador: ")
    auxSucursal = input("Ingrese ID de Sucursal del trabajador: ")
    #Buscar si ya está el trabajador
    auxBool = 0
    for i in trabajadores:
        if i[1] == auxRut:
            auxBool = 1
    #De estar el trabajador, mandar un aviso y terminar la función
    if auxBool == "1":
        print("Error: El trabajador ya existe")
        return()
    #De no estar el trabajdor, agregarlo al final de la lista
    else:
        auxTrabajador = [auxNombre, auxRut, auxCargo, auxSueldo, auxSucursal]
        print("El trabajador a sido ingresado correctamente")
    #Informar que los cambios están hechos
    time.sleep(1)

#AGREGAR SUCURSAL
def addSucursal():
    os.system("cls")
    print("AGREGAR SUCURSAL:")
    #Solicitar datos de la sucursal
    auxId = input("Ingrese Id de la sucursal: ")
    auxCiudad = input("Inserte Ciudad de la sucursal: ")
    #Buscar si ya está la sucursal
    auxBool = "0"
    for i in sucursales:
        if i[0] == auxId:
            auxBool = "1"
    #De estar la sucursal, mandar un aviso y terminar la función
    if auxBool == "1":
        print("Error: La sucursal ya existe.")
        return()
    #De no estar la sucursal, agregarla al final de la lista
    else:
        auxSucursal = [auxId, auxCiudad]
        print("La sucursal a sido intgresada correctamente")
    #Informar que los cambios están hechos
    time.sleep(1)

#AGREGAR PRODUCTO
def addProducto():
    os.system("cls")
    print("AGREGAR PRODUCTO:")
    #Solicitar datos del producto
    auxId = input("Ingrese Id del producto: ")
    auxNombre = input("Ingrese nombre del producto: ")
    #Buscar si ya está el producto
    auxBool = "0"
    for i in productos:
        if i[0] == auxId:
            auxBool = "1"
    #De estar el producto, mandar un aviso y terminar la función
    if auxBool == "1":
        print("Error: El producto ya existe.")
        return()
    #De no estar el producto, agregarlo al final de la lista
    else:
        auxProducto = [auxId, auxNombre]
        print("El producto a sido ingresado correctamente")
    #Informar que los cambios están hechos
    time.sleep(1)

#ACTUALIZAR TRABAJADOR
def setTrabajador():
    os.system("cls")
    print("ACTUALIZAR TRABAJADOR:")
    #Solicitar datos del trabajador
    #Buscar si ya está el trabajador
    #De no estar el trabajdor, mandar aviso y terminar la función
    #De estar el trabajador, solicitar los nuevos datos
    #Actualizar la información del trabajador
    #Informar que los cambios están hechos

#ACTUALIZAR SUCURSAL
def setSucursal():
    os.system("cls")
    print("ACTUALIZAR SUCURSAL:")
    #Solicitar datos de la sucursal
    #Buscar si ya está la sucursal
    #De no estar la sucursal, mandar aviso y terminar la función
    #De estar la sucursal, solicitar los nuevos datos
    #Actualizar la información de la sucursal
    #Informar que los cambios están hechos

#ACTUALIZAR PRODUCTO
def setProducto():
    os.system("cls")
    print("ACTUALIZAR PRODUCTO:")
    #Solicitar datos del producto
    #Buscar si ya está el producto
    #De no estar el producto, mandar aviso y terminar la función
    #De estar el producto, solicitar los nuevos datos
    #Actualizar la información del producto
    #Informar que los cambios están hechos

#ACTUALIZAR STOCK
def setStock():
    os.system("cls")
    print("ACTUALIZAR STOCK:")
    #Solicitar los cambios a realizar
    #Buscar si ya existe la sucursal y el producto
    #De faltar uno de ellos, mandar aviso y terminar la función
    #De estar los dos, verificar si los cambios son congruentes (No eliminar más de lo que realmente hay)
    #De estar todo en orden, agregar los cambios al final de la lista
    #Informar que los cambios están hechos

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