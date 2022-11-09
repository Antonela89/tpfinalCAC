def correccionErrores(entero):
    while True:
        try:
            entero = int(input("Ingrese {entero}: "))
            break
        except ValueError:
            print("Ingrese un numero entero")
    return entero