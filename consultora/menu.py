import excepcion
import crud

while True:
    print(f'''
        Menu:
        [1] Gestion de Trabajadores
        [2] Reportes
        [3] Cambiar status trabajador
        [0] Salir
        ''')

    opcion = excepcion.correccionErrores("Ingrese una opcion: ")

    if (opcion == 0):
        break
    elif (opcion == 1):

        print(f'''
            Gestion de Trabajadores:
            [1] Ingresar nuevo Trabajador
            [2] Modificar dato de trabajador (file.writelines())
            [3] Eliminar Trabajador
            [0] Salir
        ''')

        opcion = excepcion.correccionErrores("Ingrese una opcion: ")
        if (opcion == 0):
            break
        elif (opcion == 1):
            print('Complete los datos para ingresar nuevo Trabajador')
            crud.agregarTrabajador()
        elif (opcion == 2):
            print('Modificar dato de trabajador (file.writelines())')
            trabajadores = open("trabajadores.dat", "r")
            listado = []
            for renglon in trabajadores.readlines():
                var = renglon.split(",")
                trabajador = {"Dni": int(var[2]), "Nombre": var[0], "Edad": int(var[1]),  "Profesion": var[3], "Activo": (var[4].replace("\n", ""))}
                listado.append(trabajador)
            crud.imprimirLista(listado)

            referencia = input("Ingrese dni: ")

            dni = trabajador['Dni']
            print(renglon)

            while True:
                print(f'''
                    Que desea modificar:
                    [1] Dni
                    [2] Nombre
                    [3] Edad
                    [4] Profesion
                    [5] Activo
                    [0] Salir
                ''')

                opcion = excepcion.correccionErrores("Ingrese una opcion: ")
                if (opcion == 0):
                    break
                elif (opcion == 1):
                    nuevoDato = input("Ingrese nuevo Dni: ")
                    for i in var:
                        var[2] = nuevoDato
                    cambio = ",".join([str(elem) for elem in var])
                    print(cambio)
                    trabajadores.writelines(cambio)
                elif (opcion == 2):
                    nuevoDato = input("Ingrese nuevo Nombre: ")
                elif (opcion == 3):
                    nuevoDato = input("Ingrese nueva Edad: ")
                elif (opcion == 4):
                    nuevoDato = input("Ingrese nueva Profesión: ")
                elif (opcion == 5):
                    nuevoDato = input("Ingrese nuevo estado: ")

            trabajadores.close()
        elif (opcion == 3):
            print('Eliminar Trabajador')
            # acciones para eliminar trabajador
            # encontrar un trabajador
            # eliminarlo

    elif (opcion == 2):
        print(f'''
            Reportes:
            [1] Mostrar trabajadores Activos
            [2] Mostrar trabajadores desocupados
            [3] Mostrar desocupados en un rango de edad
            [4] Mostrar trabajadores segun la profesion
            [0] Salir
        ''')

        opcion = int(input("Ingrese una opcion: "))
        if (opcion == 0):
            break
        elif (opcion == 1):
            print('Mostrar trabajadores Activos')
            crud.armarReporte('Activo', 'True')

        elif (opcion == 2):
            print('Mostrar trabajadores desocupados')
            crud.armarReporte('Activo', 'False')

        elif (opcion == 3):
            print('Mostrar desocupados en un rango de edad')
            desde = int(input("Ingrese edad desde: "))
            hasta = int(input("Ingrese edad hasta: "))
            
            listado = []
            trabajadores = open("trabajadores.dat", "r")
            for renglon in trabajadores.readlines():
                var = renglon.split(",")
                trabajador = {"nombre": var[0], "edad": int(var[1]), "dni": int(
                    var[2]), "profesion": var[3], "activo": (var[4].replace("\n", ""))}
                estado = trabajador['activo']
                edad = trabajador['edad']
                if estado == 'False' and edad in range(desde, hasta+1):
                    listado.append(trabajador)
            crud.imprimirLista(listado)

            trabajadores.close()
        elif (opcion == 4):
            print('Mostrar trabajadores segun la profesion')
            profesion = input("Elegir profesion: ")

            trabajadores = open("trabajadores.dat", "r")
            listado = []
            profesionEncontrada = False
            for renglon in trabajadores.readlines():
                var = renglon.split(",")
                trabajador = {"nombre": var[0], "edad": int(var[1]), "dni": int(
                    var[2]), "profesion": var[3], "activo": (var[4].replace("\n", ""))}

                estado = trabajador['profesion']
                if estado.lower() == profesion.lower():
                    listado.append(trabajador)
                    profesionEncontrada = True
            if not profesionEncontrada:
                print("Profesión no existente")
            crud.imprimirLista(listado)
        else:
            print('Ingresa una opcion valida')

    elif (opcion == 3):
        print('Cambiar status trabajador: ')
    else:
        print('Ingresa una opcion valida')
