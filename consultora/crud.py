import json
from excepcion import correccionErrores

# funciones de gestion de datos:

# abrir un archivo
def abrirArchivo(archivo, modo):
    trabajadores = open(archivo, modo)
    return trabajadores

# crear listado de archivo:
def listado(archivo):
    listado = []
    # devuelve lista ["Ingrid","14","47845231", "Estudiante", "False\n"]
    trabajadores = open(archivo, "r")
    for renglon in trabajadores.readlines():
        var = renglon.split(",")
        trabajador = {"Nombre": var[0], "Edad": int(var[1]), "Dni": int(var[2]), "Profesion": var[3], "Activo": (
            var[4].rstrip())}  # o replace("\n", "") -rstrip: metodo string: elimina caracter fantasmas (\n, \t...)
        listado.append(trabajador)
        trabajadores.close()
    return listado

# crear trabajador:
def agregarTrabajador():
    while True:
        nombre = input("Nombre('x' para salir): ")
        if nombre == 'x':
            break
        edad = input("Edad: ")
        dni = input("Dni: ")
        profesion = input("Profesion: ")
        activo = input("Esta trabajando? (s/n): ")
        if activo == "s" or activo == "S":
            activo = True
        else:
            activo = False
        trabajadores = open("trabajadores.dat", "a")
        trabajadores.write(f'''{nombre},{edad},{dni},{profesion},{activo}\n''')
        trabajadores.close()
    return print(">>>Trabajador ingresado")

# cambiar dato:
def cambiarDato(dic, dato):
    nuevoDato = input(f'''{dato}: ''')
    dic[dato] = nuevoDato
    print(dic)
    # a = open(archivo, "w")
    # a.writelines(
    #     f'''{lista[dic]["Nombre"]}, {str(lista[dic]["Edad"])}, {str(lista[dic]["Dni"])}, {lista[dic]["Profesion"]}, {lista[dic]["Activo"]}\n''')
    # a.close()

# modificar datos de un trabajador
def modificar(archivo):
    lista = listado(archivo)
    print(lista)
    referencia = correccionErrores("Dni: ")
    for elemento in lista:
        if elemento["Dni"] == referencia:
            print(elemento)

            while True:
                print(f'''
                    Que desea modificar:
                    [1] Nombre
                    [2] Edad
                    [3] Dni
                    [4] Profesion
                    [5] Activo
                    [0] Salir
                ''')

                opcion = correccionErrores()

                if (opcion == 0):
                    break
                elif (opcion == 1):
                    cambiarDato(elemento, "Nombre", "trabajadores.dat")
                elif (opcion == 2):
                    cambiarDato(elemento, "Edad", "trabajadores.dat")
                elif (opcion == 3):
                    cambiarDato(elemento, "Dni", "trabajadores.dat")
                elif (opcion == 4):
                    cambiarDato(elemento, "Profesion", "trabajadores.dat")
                elif (opcion == 5):
                    cambiarDato(elemento, "Activo", "trabajadores.dat")


# eliminar trabajador de archivo

# imprimir listado de base de datos:
def imprimirLista(lista):
    print(json.dumps(lista, sort_keys=False, indent=4))

# Reportes
def armarReporte(archivo, key, value):
    lista = listado(archivo)
    reporte = []
    for trabajador in lista:
        estado = trabajador[key]
        if estado == value:
            reporte.append(trabajador)
    return imprimirLista(reporte)

def armarReporteEdad(archivo, key1, value, key2):
    lista = listado(archivo)
    reporte = []
    desde = correccionErrores('Edad desde: ')
    hasta = correccionErrores('Edad hasta: ')
    for trabajador in lista:
        estado = trabajador[key1]
        edad = trabajador[key2]    
        if estado == value and edad in range(desde, hasta+1):
            reporte.append(trabajador)
    return imprimirLista(reporte)

def armarReporteProfesion(archivo, key):
    lista = listado(archivo)
    reporte = []
    profesion = input(f'''Elegir {key}: ''')
    profesionEncontrada = False
    for trabajador in lista:
        estado = trabajador[key]
        if estado.lower() == profesion.lower():
            reporte.append(trabajador)
            profesionEncontrada = True
    if not profesionEncontrada:
        print("Profesión no existente")
    return imprimirLista(reporte)