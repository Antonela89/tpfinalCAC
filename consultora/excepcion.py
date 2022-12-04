from decoracion import decorarSalto

def correccionErrores(mensaje="Ingrese una opción: ", msjError="Ingrese un numero entero"):
    while True:
        try:
            entero = int(input(mensaje))
            decorarSalto()
            break
        except ValueError:
            print(msjError)
            decorarSalto()
    return entero


    
