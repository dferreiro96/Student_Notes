def escoer_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje)
        if opcion not in opciones:
            print("\nCaracter inálido")
            continue
        else:
            return opcion