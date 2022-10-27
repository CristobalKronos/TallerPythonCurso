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
from functions import Mensajes

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
    print("Iniciando lectura de archivos.")



    print("Fin de la lectura.")

#ESCRITURA DE ARCHIVOS
def Escritura():
    print("Iniciando la escritura de archivos.")



    print("Fin de la escritura de archivos.")

#GLOBAL VARIABLES
respWhile = 0



#MAIN
os.system("cls")
while respWhile != "0":
    resp = menu()


print("Gracias por trabajar con nosotros.")