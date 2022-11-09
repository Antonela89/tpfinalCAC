while True:
    print(f'''
        Menu:
        [1] Gestion de Trabajadores
        [2] Reportes
        [3] Cambiar status trabajador
        [0] Salir
        ''')


    #while True:
    # try:
    opcion = int(input("Ingrese una opcion: "))
    #     break
    # except ValueError:
    #     print("Ingrese un numero entero")

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

        opcion = int(input("Ingrese una opcion: "))
        if (opcion == 0):
            break
        elif (opcion == 1):

            print('Ingresar nuevo Trabajador')
            while True:
                nombre=input("Nombre('x' para salir): ")
                if nombre == 'x':
                    break
                edad = input("Edad: ")
                dni = input("Dni: ")
                profesion = input("Profesion: ")
                activo = input("Esta trabajando? (s/n): ")
                if activo == "s" or activo =="S": 
                    activo = True
                else:
                    activo = False
                
                trabajadores = open("trabajadores.dat", "a")
                trabajadores.write(f'''{nombre},{edad},{dni},{profesion},{activo}\n''')

                trabajadores.close()

        elif (opcion == 2):
            print('Modificar dato de trabajador (file.writelines())')
            # dato = input("Ingrese dato: ")
            # nuevoDato = input("Ingrese nuevo dato: ")
            # modificar = open("trabajadores.dat", "r+")
            # modificar.writelines([nuevoDato])

            trabajadores.close()
        elif (opcion == 3):
            print('Eliminar Trabajador')
            #acciones para eliminar trabajador
                #encontrar un trabajador
                #eliminarlo

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
            trabajadores = open("trabajadores.dat", "r")
            listado=[]
            for renglon in trabajadores.readlines():
                var=renglon.split(",")
                trabajador={"nombre":var[0], "edad":int(var[1]), "dni":int(var[2]), "profesion":var[3], "activo":(var[4].replace("\n",""))}
                
                estado=trabajador['activo']
                if estado == 'True':
                    listado.append(trabajador)
            print(listado)

            trabajadores.close()
        elif (opcion == 2):
            print('Mostrar trabajadores desocupados')
            trabajadores = open("trabajadores.dat", "r")
            listado=[]
            for renglon in trabajadores.readlines():
                var=renglon.split(",")
                trabajador={"nombre":var[0], "edad":int(var[1]), "dni":int(var[2]), "profesion":var[3], "activo":(var[4].replace("\n",""))}
                
                estado=trabajador['activo']
                if estado == 'False':
                    listado.append(trabajador)
            print(listado)

            trabajadores.close()
        elif (opcion == 3):
            print('Mostrar desocupados en un rango de edad')
            desde = input(int("Ingrese edade desde: "))
            hasta = input(int("Ingrese edade hasta: "))
            
            trabajadores = open("trabajadores.dat", "r")
            listado=[]
            for renglon in trabajadores.readlines():
                var=renglon.split(",")
                trabajador={"nombre":var[0], "edad":int(var[1]), "dni":int(var[2]), "profesion":var[3], "activo":(var[4].replace("\n",""))}
                
                estado=trabajador['activo']
                if estado == 'False' and range(desde, hasta+1):
                    listado.append(trabajador)
            print(listado)

            trabajadores.close()
        elif (opcion == 4):
            print('Mostrar trabajadores segun la profesion')
            profesion = input("Elegir profesion: ")

            trabajadores = open("trabajadores.dat", "r")

            listado=[]
            profesionEncontrada = False

            for renglon in trabajadores.readlines():
                var=renglon.split(",")
                trabajador={"nombre":var[0], "edad":int(var[1]), "dni":int(var[2]), "profesion":var[3], "activo":(var[4].replace("\n",""))}
                
                estado = trabajador['profesion']
                if estado.lower() == profesion.lower():
                    listado.append(trabajador)
                    profesionEncontrada = True
                if not profesionEncontrada:
                    print("Profesión no existente")
            print(listado)

    elif (opcion == 3):
        print('Cambiar status trabajador: ')
    else:
        print('Ingresa una opcion valida')



