from decoracion import decorarSalto

def correccionNumeros(mensaje="Ingrese una opción: ", msjError="Ingrese un numero entero"):
    while True:
        try:
            decorarSalto()
            entero = int(input(mensaje))
            decorarSalto()
            break
        except ValueError:
            decorarSalto()
            print(msjError)
            decorarSalto()
    return entero


def correcionPalabras(mensaje="Ingrese dato solicitado: ", msjError="No puede ingresar numeros"):
    while True:
        try:
            decorarSalto()
            string = input(mensaje).capitalize()
            decorarSalto()
            break
        except ValueError:
            decorarSalto()
            print(msjError)
            decorarSalto()
    return string     

def correccionDni(mensaje="Ingrese una opción: ", msjError="Ingrese un numero entero"):
    while True:
        try:
            decorarSalto()
            entero = int(input(mensaje))
            decorarSalto()
            while len(str(entero)) < 8:
                entero = input("Ingrese dni de 8 digitos, si posee menos complete con 0 a la izquierda: ")
            break
        except ValueError:
            decorarSalto()
            print(msjError)
            decorarSalto()
    return entero



