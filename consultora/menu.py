from excepcion import correccionNumeros
import crud
from decoracion import itemMenu, menu

while True:
    menu(f'''
        Menu Principal:
        [1] Gestion de Trabajadores
        [2] Reportes
        [3] Cambiar status trabajador
        [0] Salir\n
        ''')

    opcion = correccionNumeros()

    if (opcion == 0):
        break
    elif (opcion == 1):

        while True:
            menu(f'''
            Gestion de Trabajadores:
            [1] Ingresar nuevo Trabajador
            [2] Modificar datos de un trabajador
            [3] Eliminar Trabajador
            [0] Salir\n
            ''')

            opcion = correccionNumeros()

            if (opcion == 0):
                break
            elif (opcion == 1):
                itemMenu('Complete los datos para ingresar nuevo Trabajador:')
                crud.agregarTrabajador("trabajadores.dat")
            elif (opcion == 2):
                itemMenu('Modificar trabajador:')
                crud.modificar("trabajadores.dat")
            elif (opcion == 3):
                itemMenu('Eliminar Trabajador:')
                crud.eliminarTrabajador("trabajadores.dat")

    elif (opcion == 2):
        while True:
            menu(f'''
                Reportes:
                [1] Mostrar trabajadores Activos
                [2] Mostrar trabajadores desocupados
                [3] Mostrar desocupados en un rango de edad
                [4] Mostrar trabajadores segun la profesion
                [0] Salir\n
            ''')

            opcion = correccionNumeros()

            if (opcion == 0):
                break
            elif (opcion == 1):
                itemMenu('Mostrar trabajadores Activos')
                crud.armarReporte('trabajadores.dat', 'Activo', 'True')
            elif (opcion == 2):
                itemMenu("'Mostrar trabajadores desocupados'")
                crud.armarReporte('trabajadores.dat','Activo', 'False')
            elif (opcion == 3):
                itemMenu('Mostrar desocupados en un rango de edad')
                crud.armarReporteEdad('trabajadores.dat','Activo', 'False', 'Edad')
            elif (opcion == 4):
                itemMenu('Mostrar trabajadores segun la profesion')
                crud.armarReporteProfesion('trabajadores.dat','Profesion',)
            else:
                itemMenu('Ingresa una opcion valida')
    
    elif (opcion == 3):
        itemMenu('Cambiar status trabajador: ')
        crud.cambiarStatus('trabajadores.dat')
    else:
        itemMenu('Ingresa una opcion valida')

print(crud.imprimirIntegrantes("integrantes.dat"))
itemMenu("Fin del Programa")