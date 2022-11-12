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
                listado.append((renglon).replace("\n",""))
            print(listado)
            trabajadores.close()

            referencia = input("Ingrese dni: ")
            for elemento in listado:
                if referencia in elemento:
                    elemento=elemento.split(",")
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

                        opcion = excepcion.correccionErrores("Ingrese una opcion: ")
                        if (opcion == 0):
                            break
                        elif (opcion == 1):
                            nuevoDato = input("Ingrese nuevo nombre: ")
                            elemento[0] = nuevoDato
                            print(elemento)


                            a = open("trabajadores.dat","w")
                            a.writelines(f'''{elemento[0]},{elemento[1]},{elemento[2]},{elemento[3]},{elemento[4]}\n''')
                            a.close()
                        elif (opcion == 2):
                            nuevoDato = input("Ingrese nueva edad: ")
                            elemento[1] = nuevoDato
                            print(elemento)
                        elif (opcion == 3):
                            nuevoDato = input("Ingrese nuevo dni: ")
                            elemento[2] = nuevoDato
                            print(elemento)
                        elif (opcion == 4):
                            nuevoDato = input("Ingrese nueva profesión: ")
                            elemento[3] = nuevoDato
                            print(elemento)
                        elif (opcion == 5):
                            nuevoDato = input("Ingrese nuevo estado: ")
                            elemento[4] = nuevoDato
                            print(elemento)


        elif (opcion == 3):
            print('Eliminar Trabajador')
            # acciones para eliminar trabajador
            # encontrar un trabajador
            # eliminarlo

    elif (opcion == 2):
        while True:
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
