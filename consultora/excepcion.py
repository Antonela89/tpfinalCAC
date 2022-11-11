def correccionErrores(mensaje):
    while True:
        try:
            entero = int(input(mensaje))
            break
        except ValueError:
            print("Ingrese un numero entero")
    return entero
