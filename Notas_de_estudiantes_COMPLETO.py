"""
Ejercicio 5. Notas de estudiantes con funciones.
- Pedir nombres y notas.
- Mostrar promedio, mejor, peor nota.
- Funciones: pedir_estudiante, calcular_promedio, mostrar_resultados.
"""


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


def calcular_promedio(datos_de_estudiantes):
    suma = 0
    for est in datos_de_estudiantes:
        suma += est["Nota"]
    return suma / len(datos_de_estudiantes)


def calcular_max(datos_de_estudiantes):
    mayor = float('-inf')
    for est in datos_de_estudiantes:
        mayor = max(mayor, est["Nota"])
    return mayor       
    



def calcular_min(datos_de_estudiantes):
    menor = float('inf')
    for est in datos_de_estudiantes:
       menor = min(menor, est["Nota"])
    return menor
           


def mostrar_resultados(datos_de_estudiantes):
    for i, estudiante in enumerate(datos_de_estudiantes, start=1):
        print(f"{i}. {estudiante["Nombre"]}: {estudiante["Nota"]}")


def menu():
    print("\n____MENU____")
    print("1. Añadir datos de estudiante.")
    print("2. Mostrar relación de estudiantes con sus notas.")
    print("3. Ordenar y mostrar relación de estudiantes.")
    print("4. Calcular promedio, mejor y menor nota; mostrar.")
    print("5. Salir.")


def escoer_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje)
        if opcion not in opciones:
            print("\nCaracter inálido")
            continue
        else:
            return opcion


def jugar():
    print("""\nEjercicio 5. Notas de estudiantes con funciones.
- Pedir nombres y notas.
- Mostrar promedio, mejor, peor nota.
- Funciones: pedir_estudiante, calcular_promedio, mostrar_resultados.""")
    datos_de_estudiantes = []
    while True:
        menu()
        opcion = escoer_opcion("\nTeclee una opción: ", ["1", "2", "3", "4", "5"])
        if opcion == "1":
            estudiante = pedir_estudiante("\nIntroduzca el nombre del estudiante: ")
            if not estudiante.replace(" ", "").isalpha():
                print("\nEl nombre solo puede contener letras y espacios.")
                continue
            existe = False
            for tupla_clave_valor in datos_de_estudiantes:
                if tupla_clave_valor["Nombre"] == estudiante:
                    existe = True
                    break
            if existe:
                print("Ya el estudiante se encuentra registrado.")
                continue
            else:
                print(f"\nSe ha añadido el estudiante {estudiante}.")
                notas = pedir_notas(f"\nIntroduzca la nota de {estudiante}: ")
                datos_de_estudiantes.append({"Nombre": estudiante, "Nota": notas})
                print(f"\nSe ha añadido la nota de {estudiante} correctamente.")

        elif opcion == "2":
            if not datos_de_estudiantes:
                print("No se ha introducido ningún dato.")
            else:
                mostrar_resultados(
                    datos_de_estudiantes
                )
        elif opcion == "3":
            if not datos_de_estudiantes:
                print("No se ha introducido ningún dato.")
                continue
            else:
                print("\n___Orden___")
                print("1. Nombre.")
                print("2. Notas")

                ordenar_por = escoer_opcion(
                    "\nCómo desea ordenar la muestra?: ", ["1", "2"]
                )
                if ordenar_por == "1":
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nombre"])
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes["Nombre"]}: {estudiantes["Nota"]}")

                elif ordenar_por == "2":
                    ordenados = sorted(datos_de_estudiantes, key=lambda x: x["Nota"])
                    for i, estudiantes in enumerate(ordenados, start=1):
                        print(f"{i}. {estudiantes["Nombre"]}: {estudiantes["Nota"]}")

        elif opcion == "4":
            if not datos_de_estudiantes:
                print("No se ha introducido ningún dato.")
                continue
            else:
                promedio = calcular_promedio(datos_de_estudiantes)
                maximo = calcular_max(datos_de_estudiantes)
                minimo = calcular_min(datos_de_estudiantes)
                print(
                    f"El promedio es {promedio:.2f}. La mejor y peor notas son {maximo} y {minimo} respectivamente."
                )

        else:
            return


def main():
    jugar()
    print("\nHa salido satisfactoriamente.\n")


if __name__ == "__main__":
    main()

