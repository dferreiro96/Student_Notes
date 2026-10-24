
def pedir_estudiante(mensaje):
    estudiante = input(mensaje).title().strip()
    return estudiante


def pedir_notas(mensaje):
    while True:
        try:
            notas = float(input(mensaje))
            if notas < 0 or notas > 100:
                print("Introduzca un valor válido de notas.")
                continue
            return notas
        except ValueError:
            print("Introduzca un valor válido de notas.")