from excepcion import correccionNumeros, correcionPalabras, correccionDni
from decoracion import decorarSalto, noIngresado, itemMenu, menu, imprimirLista, imprimirElemento

# funciones de gestion de datos:
# abrir un archivo
def abrirArchivo(archivo, modo = "r"):
    trabajadores = open(archivo, modo, encoding="utf-8")
    return trabajadores

# crear listado de archivo:
def listado(archivo):
    listado = []
    trabajadores = abrirArchivo(archivo)
    for renglon in trabajadores.readlines():
        var = renglon.split(",")
        trabajador = {"Nombre": var[0], "Edad": int(var[1]), "Dni": int(var[2]), "Profesion": var[3], "Activo": (
            var[4].rstrip())}  # o replace("\n", "") -rstrip: metodo string: elimina caracter fantasmas (\n, \t...)
        listado.append(trabajador)
        trabajadores.close()
    return listado

# crear trabajador:
def agregarTrabajador(archivo):
    while True:
        lista = listado("trabajadores.dat")
        dni = correccionDni("Dni: ")
        for elemento in lista:
            encontrado = False
            if(elemento["Dni"] == dni):
                encontrado == True
                dni = correccionDni("Este dni ya se encuentra registrado, ingrese otro: ")
            else:
                encontrado = False
        nombre = correcionPalabras("Nombre ('x' para salir): ")
        if nombre == 'X':
            break
        edad = correccionNumeros("Edad: ")
        profesion = correcionPalabras("Profesion: ")
        if profesion == "":
            noIngresado()
            break
        activo = correcionPalabras("Esta trabajando? (s/n): ")
        if activo == "":
            noIngresado()
            break
        if activo == "s" or activo == "S":
            activo = "Activo"
        else:
            activo = "Inactivo"

        if (encontrado == False):
            trabajadores = abrirArchivo(archivo, "a")
            trabajadores.write(f'''{nombre},{edad},{dni},{profesion},{activo}\n''')
            trabajadores.close()
            itemMenu(">>> Trabajador ingresado <<<")

# cambiar dato:
def cambiarDato(dic, dato, archivo, lista):
    nuevoDato = input(f'''{dato}: ''')
    dic[dato] = nuevoDato
    nuevaLista = []
    for dic in lista:
        if dic["Activo"] == "s" or dic["Activo"] == "S":
            dic["Activo"] = "Activo"
        else:
            dic["Activo"] = "Inactivo"
        nuevoRenglon = f'''{dic["Nombre"].capitalize()},{str(dic["Edad"])},{str(dic["Dni"])},{dic["Profesion"].capitalize()},{dic["Activo"].capitalize()}\n'''
        nuevaLista.append(nuevoRenglon)
    imprimirElemento(nuevoRenglon.replace("\n", ""))

    a = open(archivo,"w",encoding="utf-8")
    a.writelines(nuevaLista)
    a.close()

# modificar datos de un trabajador
def modificar(archivo):
    lista = listado(archivo)
    imprimirLista(lista)
    referencia = correccionNumeros("Dni: ")
    for elemento in lista:
        if elemento["Dni"] == referencia:
            imprimirElemento(elemento)

            while True:
                menu(f'''
                    Que desea modificar:
                    [1] Nombre
                    [2] Edad
                    [3] Dni
                    [4] Profesion
                    [5] Activo (s/n)
                    [0] Salir
                ''')

                opcion = correccionNumeros()

                if (opcion == 0):
                    break
                elif (opcion == 1):
                    cambiarDato(elemento,"Nombre", "trabajadores.dat",lista)
                elif (opcion == 2):
                    cambiarDato(elemento,"Edad", "trabajadores.dat",lista)
                elif (opcion == 3):
                    cambiarDato(elemento,"Dni", "trabajadores.dat",lista)
                elif (opcion == 4):
                    cambiarDato(elemento,"Profesion", "trabajadores.dat",lista)
                elif (opcion == 5):
                    cambiarDato(elemento,"Activo", "trabajadores.dat",lista)
        
    if elemento["Dni"] != referencia:
        print("Dni no encontrado")
        decorarSalto()

# eliminar trabajador de archivo
def eliminarTrabajador(archivo):
    lista = listado(archivo)
    nuevaLista = []
    imprimirLista(lista)
    referencia = correccionNumeros("Dni: ")
    for elemento in lista:
        if elemento["Dni"] == referencia:
            lista.remove(elemento)        
    for dic in lista:
        nuevoRenglon = f'''{dic["Nombre"]},{str(dic["Edad"])},{str(dic["Dni"])},{dic["Profesion"]},{dic["Activo"]}\n'''
        nuevaLista.append(nuevoRenglon)
    imprimirLista(nuevaLista)

    a = open(archivo, "w", encoding="utf-8")
    a.writelines(nuevaLista)
    a.close()

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
    desde = correccionNumeros('Edad desde: ')
    hasta = correccionNumeros('Edad hasta: ')
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
        print(">>> Profesión no existente <<<")
    return imprimirLista(reporte)

def cambiarStatus(archivo):
    lista = listado(archivo)
    imprimirLista(lista)
    referencia = correccionNumeros("Dni: ")
    for elemento in lista:
        if elemento["Dni"] == referencia:
            imprimirElemento(elemento)
    cambiarDato(elemento,"Activo",archivo, lista)

def imprimirIntegrantes(archivo):
    print(f'''>>> Grupo C: <<<''')
    integrantes = abrirArchivo(archivo)
    listado = []
    for renglon in integrantes.readlines():
        var = renglon.split(",")
        integrante = {"Nombre": var[0], "Apellido": var[1].replace("\n", "")} 
        listado.append(integrante)
        integrantes.close()
    return imprimirLista(listado)

