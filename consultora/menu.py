#apertura de archivo:
#trabajadores=[]
#with open("trabajadores.dat", "a") as trabajadores:
# t=trabajador.replace("\n","")
# t=t.split(",")
# trabajadores.append(t)

# trabajadores.close()


while True:
    print(f'''
        Menu:
        [1] Gestion de Trabajadores
        [2] Reportes
        [3] Cambiar status trabajador
        [0] Salir
        ''')

    opcion = int(input("Ingrese una opcion: "))
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
            # while True:
                # nombre=input("Nombre('x' para salir): ")
                # if nombre == 'x':
                #     break
                # edad = int(input("Edad: "))
                # profesion = input("Porofesion: ")
                # activo = input("Esta trabajando? (s/n): ")
                # if activo == "s" or activo =="S": 
                #     activo = True
                # else:
                #     activo = False
                # trabajador = (nombre, edad, profesion, activo)
                # trabajadores.append(trabajador)
        elif (opcion == 2):
            print('Modificar dato de trabajador (file.writelines())')
            #acciones para modificar trabajador
                #encontrar un trabajador
                #modificarlo
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
            # for trabajador in trabajadores:
            #     if trabajador[5] == True:
            #         print(trabajador)
        elif (opcion == 2):
            print('Mostrar trabajadores desocupados')
            # for trabajador in trabajadores:
            #     if trabajador[5] == False:
            #         print(trabajador)
        elif (opcion == 3):
            print('Mostrar desocupados en un rango de edad')
            # desde = int(input("Ingrese rango de inicio: "))
            # hasta = int(input("Ingrese rango de fin: "))
            # for trabajor in trabajadores:
            #     if ((trabajor[5] == False) in range(desde, hasta + 1)):
            #         print(trabajor)
        elif (opcion == 4):
            print('Mostrar trabajadores segun la profesion')
            # profesion = input("Elegir profesion: ")
            # profesionEncontrada = False
            # for trabajador in trabajadores:
            #     if trabajador[4].lower() == profesion.lower():
            #         print(trabajador)
            # profesionEncontrada = True
            # if not profesionEncontrada:
            #     print("Profesión no existente")   

    elif (opcion == 3):
        print('Cambiar status trabajador: ')
    else:
        print('Ingresa una opcion valida')



