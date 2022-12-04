import os
import pandas as pd
import json
from tabulate import tabulate

# funciones para decorar menu:
def decorar(caracter="*", cantidad=50):
    os.system("cls")
    print(caracter*cantidad)
    print(caracter*cantidad)
    return ""

def decorar2(caracter="*", cantidad=50):
    print(caracter*cantidad)
    print(caracter*cantidad)
    return ""

def decorarSalto():
    print(f'''\t''')
    return ""

def noIngresado():
    decorarSalto()
    print(">>> Trabajador no Ingresado <<<")
    decorarSalto()
    return ""

def itemMenu(mensaje):
    decorar2()
    print(mensaje)
    decorarSalto()
    return ""

def menu(menu):
    decorar2()
    print(menu)
    decorar2()
    return ""

# imprimir listado de base de datos:
def imprimirLista(lista):
    df = pd.DataFrame(lista)
    df = print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid'))
    decorarSalto()
    return df

def imprimirElemento(elemento):
    trabajador = print(json.dumps(elemento, indent=2))
    decorarSalto()
    return trabajador



