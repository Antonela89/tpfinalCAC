import json
# funciones de gestion de datos:

# abrir un archivo


def abrirArchivo(archivo, modo):
    trabajadores = open(archivo, modo)
    return trabajadores

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
        trabajadores = open("trabajadores.dat", "w")
        trabajadores.write(f'''{nombre},{edad},{dni},{profesion},{activo}\n''')
        trabajadores.close()
    return print(">>>Trabajador ingresado")

# modificar datos de un trabajador

# eliminar trabajador de archivo

# imprimir listado de base de datos:


def imprimirLista(lista):
    print(json.dumps(lista, sort_keys=False, indent=4))

# Recorrer base de datos:


def armarReporte(key, value):
    listado = []
    trabajadores = open("trabajadores.dat", "r")
    for renglon in trabajadores.readlines():
        # devuelve lista ["Ingrid","14","47845231", "Estudiante", "False\n"]
        var = renglon.split(",")
        trabajador = {"Nombre": var[0], "Edad": int(var[1]), "Dni": int(var[2]), "Profesion": var[3], "Activo": (
            var[4].rstrip())}  # o replace("\n", "") -rstrip: metodo string: elimina caracter fantasmas (\n, \t...)
        trabajadores.close()
        estado = trabajador[key]
        if estado == value:
            listado.append(trabajador)
    return imprimirLista(listado)

#replace("\n", "")

