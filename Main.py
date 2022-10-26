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


#FUNCTIONS
def menu():
    print("Hola Mundo")
    print("0|Finalizar")
    resp = input("Inserte respuesta: ")
    return resp

#GLOBAL VARIABLES
resp = 0

#MAIN
os.system("cls")
while resp != "0":
    resp = menu()


print("Gracias por trabajar con nosotros.")